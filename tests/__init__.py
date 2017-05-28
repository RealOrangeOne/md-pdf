import unittest
import os
from md_pdf.consts import TEMPLATES_DIR, STATIC_DIR


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

    def removeFile(self, file):
        try:
            os.remove(file)
        except OSError:
            pass

    def deleteTemplates(self):
        for template in [
            'header.html',
            'footer.html',
            'cover.html',
            'toc.xsl',
        ]:
            self.removeFile(os.path.join(TEMPLATES_DIR, template))

    def tearDown(self):
        self.deleteTemplates()
        self.removeFile(os.path.join(STATIC_DIR, 'style.css'))

