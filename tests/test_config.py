from tests import BaseTestCase
from md_pdf.config import read, validate
from md_pdf.exceptions import ConfigValidationException
from md_pdf.consts import CSL_DIR
from md_pdf.utils import remove_dir
import os
import datetime
from unittest import skipIf


class ReadConfigTestCase(BaseTestCase):
    def test_reads_config(self):
        config = read.load_config(os.path.abspath('test-files/mdp.yml'))
        self.assertIsInstance(config, dict)

    def test_throws_at_missing_config(self):
        with self.assertRaises(ConfigValidationException):
            read.load_config(os.path.abspath('non-existant'))


class ConfigValidatorBaseTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        validate.validate_config(self.BASE_VALID_CONFIG)


class ValidateSubmissionDateTestCase(ConfigValidatorBaseTestCase):
    def test_transparent_to_datetime(self):
        self.BASE_VALID_CONFIG['submission_date'] = datetime.datetime.now()
        validate.validate_config(self.BASE_VALID_CONFIG)

    def test_transparent_to_date(self):
        self.BASE_VALID_CONFIG['submission_date'] = datetime.datetime.now().date()
        validate.validate_config(self.BASE_VALID_CONFIG)

    def test_transparent_to_time(self):
        self.BASE_VALID_CONFIG['submission_date'] = datetime.datetime.now().time()
        validate.validate_config(self.BASE_VALID_CONFIG)

    def test_valid_date_format(self):
        for date in [
            '2017-01-01',
            '01-01-2017',
            '1st jan 2017',
            '1 january 2017'
        ]:
            self.BASE_VALID_CONFIG['submission_date'] = date
            validate.validate_config(self.BASE_VALID_CONFIG)

    def test_invalid_date_format(self):
        for date in [
            'nothing',
            '31-02-2017',
            '01-2017-01',
            '1st smarch 2017'
        ]:
            self.BASE_VALID_CONFIG['submission_date'] = date
            with self.assertRaises(ConfigValidationException):
                validate.validate_config(self.BASE_VALID_CONFIG)


class ValidateWordcountTestCase(ConfigValidatorBaseTestCase):
    def test_boolean_values_only(self):
        self.BASE_VALID_CONFIG['show_word_count'] = True
        validate.validate_config(self.BASE_VALID_CONFIG)
        self.BASE_VALID_CONFIG['show_word_count'] = False
        validate.validate_config(self.BASE_VALID_CONFIG)

    def test_invalid_values(self):
        for value in [
            'True',
            'False',
            0,
            1
        ]:
            self.BASE_VALID_CONFIG['show_word_count'] = value
            with self.assertRaises(ConfigValidationException):
                validate.validate_config(self.BASE_VALID_CONFIG)



class ValidateTOCTestCase(ConfigValidatorBaseTestCase):
    def test_boolean_values_only(self):
        self.BASE_VALID_CONFIG['toc'] = True
        validate.validate_config(self.BASE_VALID_CONFIG)
        self.BASE_VALID_CONFIG['toc'] = False
        validate.validate_config(self.BASE_VALID_CONFIG)

    def test_invalid_values(self):
        for value in [
            'True',
            'False',
            0,
            1
        ]:
            self.BASE_VALID_CONFIG['toc'] = value
            with self.assertRaises(ConfigValidationException):
                validate.validate_config(self.BASE_VALID_CONFIG)


class ValidateContextTestCase(ConfigValidatorBaseTestCase):
    def test_should_be_dict(self):
        for value in [
            [],
            'dict',
            1
        ]:
            self.BASE_VALID_CONFIG['context'] = value
            with self.assertRaises(ConfigValidationException):
                validate.validate_config(self.BASE_VALID_CONFIG)
        self.BASE_VALID_CONFIG['context'] = {}
        validate.validate_config(self.BASE_VALID_CONFIG)

    def test_non_string_keys(self):
        self.BASE_VALID_CONFIG['context'] = {
            1: 'test'
        }
        with self.assertRaises(ConfigValidationException):
            validate.validate_config(self.BASE_VALID_CONFIG)

    def test_string_keys(self):
        self.BASE_VALID_CONFIG['context'] = {
            '1': 'test'
        }
        validate.validate_config(self.BASE_VALID_CONFIG)

    def test_valid_values(self):
        for value in [
            'test',
            1
        ]:
            self.BASE_VALID_CONFIG['context'] = {
                'test': value
            }
            validate.validate_config(self.BASE_VALID_CONFIG)

    def test_invalid_values(self):
        for value in [
            [],
            {}
        ]:
            self.BASE_VALID_CONFIG['context'] = {
                'test': value
            }
            with self.assertRaises(ConfigValidationException):
                validate.validate_config(self.BASE_VALID_CONFIG)


class ValidateBibliographyTestCase(ConfigValidatorBaseTestCase):
    def test_contains_all_keys(self):
        self.BASE_VALID_CONFIG['bibliography'] = {}
        with self.assertRaises(ConfigValidationException):
            validate.validate_config(self.BASE_VALID_CONFIG)
        self.BASE_VALID_CONFIG['bibliography'] = {
            'references': 'test'
        }
        with self.assertRaises(ConfigValidationException):
            validate.validate_config(self.BASE_VALID_CONFIG)
        self.BASE_VALID_CONFIG['bibliography'] = {
            'csl': 'test'
        }
        with self.assertRaises(ConfigValidationException):
            validate.validate_config(self.BASE_VALID_CONFIG)

    def test_valid_references(self):
        self.BASE_VALID_CONFIG['bibliography'] = {
            'references': 'non-existant',
            'csl': 'chicago-author-date'
        }
        with self.assertRaises(ConfigValidationException):
            validate.validate_config(self.BASE_VALID_CONFIG)
        self.BASE_VALID_CONFIG['bibliography']['references'] = 'test-files/bib.yaml'
        validate.validate_config(self.BASE_VALID_CONFIG)

    @skipIf(not os.path.isdir(CSL_DIR), 'Missing CSL Files')
    def test_valid_csl(self):
        self.BASE_VALID_CONFIG['bibliography'] = {
            'references': 'test-files/bib.yaml',
            'csl': 'nothing'
        }
        with self.assertRaises(ConfigValidationException):
            validate.validate_config(self.BASE_VALID_CONFIG)
        self.BASE_VALID_CONFIG['bibliography']['csl'] = 'chicago-author-date'
        validate.validate_config(self.BASE_VALID_CONFIG)


class ValidateInputTestCase(ConfigValidatorBaseTestCase):
    def test_no_matches(self):
        self.BASE_VALID_CONFIG['input'] = 'test-files/*.mp4'
        with self.assertRaises(ConfigValidationException):
            validate.validate_config(self.BASE_VALID_CONFIG)

    def test_invalid_glob(self):
        self.BASE_VALID_CONFIG['input'] = 'test-files/'
        with self.assertRaises(ConfigValidationException):
            validate.validate_config(self.BASE_VALID_CONFIG)


class ValidateOutputTestCase(ConfigValidatorBaseTestCase):
    def tearDown(self):
        super().tearDown()
        remove_dir('test-files/test')

    def test_creates_output_dir(self):
        self.assertFalse(os.path.isdir('test-files/test'))
        self.BASE_VALID_CONFIG['output_dir'] = 'test-files/test'
        validate.validate_config(self.BASE_VALID_CONFIG)
        self.assertTrue(os.path.isdir('test-files/test'))

    def test_valid_output_formats(self):
        for format in [
            'html',
            'pdf'
        ]:
            self.BASE_VALID_CONFIG['output_formats'] = [format]
            validate.validate_config(self.BASE_VALID_CONFIG)

    def test_invalid_output_formats(self):
        for format in [
            'text',
            'foo'
        ]:
            self.BASE_VALID_CONFIG['output_formats'] = [format]
            with self.assertRaises(ConfigValidationException):
                validate.validate_config(self.BASE_VALID_CONFIG)

    def test_part_invalid_format(self):
        self.BASE_VALID_CONFIG['output_formats'] = ['html', 'foo']
        with self.assertRaises(ConfigValidationException):
            validate.validate_config(self.BASE_VALID_CONFIG)


class ValidateRequiredKeysTestCase(ConfigValidatorBaseTestCase):
    def test_required_keys(self):
        for key in validate.REQUIRED_KEYS:
            base_config = self.BASE_VALID_CONFIG.copy()
            del base_config[key]
            with self.assertRaises(ConfigValidationException):
                validate.validate_config(base_config)
