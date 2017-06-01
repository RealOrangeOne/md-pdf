from tests import BaseTestCase
import os
from md_pdf.build.pdf import export_pdf, TOC_OPTIONS, DEFAULT_MARGIN_VERTICAL, DEFAULT_MARGIN_HORIZONTAL
from unittest.mock import patch
from md_pdf.build.templates import FILE_NAME_FORMAT
from md_pdf.exceptions import PDFRenderException
import pdfkit


class PDFRendererTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.content = 'test content'
        self.output_file_path = os.path.join(self.BASE_VALID_CONFIG['output_dir'], 'output.pdf')
        self.assertFalse(os.path.isfile(self.output_file_path))
        self.create_fake_templates()

    def tearDown(self):
        super().tearDown()
        self.remove_file(self.output_file_path)

    def test_renders(self):
        export_pdf(self.content, self.BASE_VALID_CONFIG)
        self.assertTrue(os.path.isfile(self.output_file_path))

    def test_title(self):
        context = export_pdf(self.content, self.BASE_VALID_CONFIG)
        self.assertEqual(context['title'], self.BASE_VALID_CONFIG['title'])

    def test_replace_context(self):
        self.BASE_VALID_CONFIG['context'] = {
            '1': 2,
            '2': '1'
        }
        context = export_pdf(self.content, self.BASE_VALID_CONFIG)
        self.assertEqual(context['replace'], [
            ('1', '2'),
            ('2', '1'),
        ])

    def test_default_margins(self):
        context = export_pdf(self.content, self.BASE_VALID_CONFIG)
        self.assertEqual(context['margin-top'], DEFAULT_MARGIN_VERTICAL)
        self.assertEqual(context['margin-bottom'], DEFAULT_MARGIN_VERTICAL)
        self.assertEqual(context['margin-left'], DEFAULT_MARGIN_HORIZONTAL)
        self.assertEqual(context['margin-right'], DEFAULT_MARGIN_HORIZONTAL)

    def test_override_margin(self):
        self.BASE_VALID_CONFIG['context'] = {
            'margin_vertical': '1cm',
            'margin_horizontal': '2cm'
        }
        context = export_pdf(self.content, self.BASE_VALID_CONFIG)
        self.assertEqual(context['margin-top'], '1cm')
        self.assertEqual(context['margin-bottom'], '1cm')
        self.assertEqual(context['margin-left'], '2cm')
        self.assertEqual(context['margin-right'], '2cm')

    @patch.object(pdfkit, 'from_string')
    def test_kit_call(self, pdf_render):
        context = export_pdf(self.content, self.BASE_VALID_CONFIG)
        self.assertTrue(pdf_render.called)
        args, kwargs = self.call_to_args(pdf_render)
        self.assertEqual(args[0], self.content)
        self.assertIn(self.output_file_path, args[1])
        self.assertEqual(kwargs['options'], context)
        self.assertTrue(kwargs['cover_first'])
        self.assertEqual(kwargs['cover'], FILE_NAME_FORMAT.format('cover'))
        self.assertEqual(kwargs['toc'], {})

    @patch.object(pdfkit, 'from_string')
    def test_toc(self, pdf_render):
        self.BASE_VALID_CONFIG['toc'] = True
        export_pdf(self.content, self.BASE_VALID_CONFIG)
        args, kwargs = self.call_to_args(pdf_render)
        self.assertEqual(kwargs['toc'], TOC_OPTIONS)

    def test_fails_if_missing_templates(self):
        self.remove_file(FILE_NAME_FORMAT.format('cover'))
        with self.assertRaises(PDFRenderException):
            export_pdf(self.content, self.BASE_VALID_CONFIG)

    def test_files_exist(self):
        context = export_pdf(self.content, self.BASE_VALID_CONFIG)
        self.assertTrue(os.path.isfile(context['header-html']))
        self.assertTrue(os.path.isfile(context['footer-html']))
        self.assertEqual(context['header-html'], FILE_NAME_FORMAT.format('header'))
        self.assertEqual(context['footer-html'], FILE_NAME_FORMAT.format('footer'))



