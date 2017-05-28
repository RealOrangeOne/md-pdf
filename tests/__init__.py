import unittest
import os
from md_pdf.consts import TEMPLATES_DIR, STATIC_DIR
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

