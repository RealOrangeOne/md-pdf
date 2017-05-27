import unittest
import os
from md_pdf.consts import TEMPLATES_DIR


class BaseTestCase(unittest.TestCase):
    def deleteTemplates(self):
        for template in [
            'header.html',
            'footer.html',
            'cover.html',
            'toc-xml',
        ]:
            try:
                os.remove(os.path.join(TEMPLATES_DIR, template))
            except OSError:
                pass

    def tearDown(self):
        self.deleteTemplates()
