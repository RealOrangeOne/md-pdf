import unittest
import os
from md_pdf.consts import TEMPLATES_DIR, STATIC_DIR
from md_pdf.build.templates import FILE_NAME_FORMAT
from bs4 import BeautifulSoup


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.BASE_VALID_CONFIG = {
            'title': 'test title',
            'input': 'test-files/*.md',
            'output_formats': [
                'html', 'pdf'
            ],
            'output_dir': 'out/',

        }

    def parse_html(self, html):
        return BeautifulSoup(html, 'html.parser')

    def remove_file(self, file):
        try:
            os.remove(file)
        except OSError:
            pass

    def touch_file(self, file):
        open(file, 'w').close()

    def create_fake_templates(self):
        for template in [
            'header',
            'footer',
            'cover'
        ]:
            self.touch_file(FILE_NAME_FORMAT.format(template))

    def extend_config(self, *args):
        base_config = self.BASE_VALID_CONFIG.copy()
        for arg in args:
            base_config = dict(base_config, **arg)
        return base_config

    def delete_templates(self):
        for template in [
            'header.html',
            'footer.html',
            'cover.html',
            'toc.xsl',
        ]:
            self.remove_file(os.path.join(TEMPLATES_DIR, template))

    def tearDown(self):
        self.delete_templates()
        self.remove_file(os.path.join(STATIC_DIR, 'style.css'))

    def call_to_args(self, call):
        args = tuple(call.call_args)[0]
        kwargs = tuple(call.call_args)[1]
        return args, kwargs

