from tests import BaseTestCase
from md_pdf.build.pandoc import output_html, build_document
from md_pdf.utils import remove_dir
import os

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

