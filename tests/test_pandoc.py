from tests import BaseTestCase
from md_pdf.build.pandoc import output_html, build_document
from md_pdf.build.md import read_files
from md_pdf.utils import remove_dir
import os
import glob


class ReadFileTestCase(BaseTestCase):
    file_glob = 'test-files/*.md'

    def test_reads_files(self):
        files = read_files(self.file_glob)
        self.assertNotEqual(files, '')

    def test_contains_all_files(self):
        files = read_files(self.file_glob)
        for file in glob.iglob(self.file_glob):
            with open(file) as f:
                self.assertIn(f.read(), files)


class OutputHTMLTestCase(BaseTestCase):
    output_dir = 'test-output'

    def setUp(self):
        super().setUp()
        os.makedirs(self.output_dir)

    def tearDown(self):
        super().tearDown()
        remove_dir(self.output_dir)

    def test_outputs_file(self):
        self.assertFalse(os.path.isfile(os.path.join(self.output_dir, 'output.html')))
        output_html('test', self.output_dir)
        self.assertTrue(os.path.isfile(os.path.join(self.output_dir, 'output.html')))

    def test_outputs_correct_data(self):
        output_html('test', self.output_dir)
        with open(os.path.join(self.output_dir, 'output.html')) as f:
            self.assertEqual(f.read(), 'test')


class BuildDocumentTestCase(BaseTestCase):
    def test_parses_markdown(self):
        doc = build_document('# test', None)
        self.assertIn('<h1 id="test">test</h1>', doc)

    def converts_nothing_if_plain(self):
        doc = build_document('test', None)
        self.assertIn('test', doc)

    def test_bibliography(self):
        bibliography = {
            'references': 'test-files/bib.yaml',
            'csl': 'chicago-author-date'
        }
        with open('test-files/2-pandoc.md') as f:
            test_content = f.read()
        doc = build_document(test_content, bibliography)
        self.assertIn(
            '<span class="citation">Doe (2005, 2006, 30; see also Doe and Roe 2007)</span> says blah.',
            doc
        )
        self.assertIn('Doe, John. 2005.', doc)

