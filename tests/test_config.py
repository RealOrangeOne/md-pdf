from tests import BaseTestCase
from md_pdf.config import read, validate
from md_pdf.exceptions import ConfigValidationException
import os


class ReadConfigTestCase(BaseTestCase):
    def test_reads_config(self):
        config = read.load_config(os.path.abspath('test-files/mdp.yml'))
        self.assertIsInstance(config, dict)

    def test_throws_at_missing_config(self):
        with self.assertRaises(ConfigValidationException):
            read.load_config(os.path.abspath('non-existant'))

