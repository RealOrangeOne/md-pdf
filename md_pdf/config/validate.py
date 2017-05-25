from md_pdf.exceptions import ConfigValidationException
from md_pdf.consts import CSL_DIR
import glob
import os
import logging
from dateutil import parser
import datetime

logger = logging.getLogger(__file__)


REQUIRED_KEYS = [
    'output_dir',
    'output_formats',
    'input'
]


def check_required_keys(config):
    missing_keys = [key for key in REQUIRED_KEYS if key not in config]
    if missing_keys:
        raise ConfigValidationException("Missing required keys: {}".format(", ".join(missing_keys)))


def test_output(config):
    abs_output_dir = os.path.abspath(config['output_dir'])
    if not os.path.isdir(abs_output_dir):
        logger.debug("Creating output directory...")
        os.mkdir(abs_output_dir)
    invalid_formats = [key for key in config['output_formats'] if key not in ['html', 'pdf']]
    if invalid_formats:
        raise ConfigValidationException("Invalid output formats provided: '{}'".format(", ".join(invalid_formats)))


def test_input(config):
    abs_input = os.path.abspath(config['input'])
    if len(glob.glob(abs_input)) == 0:
        raise ConfigValidationException("No files found at {}".format(abs_input))


def validate_bibliography(config):
    if 'bibliography' not in config:
        return
    if 'references' not in config['bibliography']:
        raise ConfigValidationException("Missing References Path")
    if 'csl' not in config['bibliography']:
        raise ConfigValidationException("Missing CSL Name")

    abs_bibliography = os.path.abspath(config['bibliography']['references'])
    if not os.path.isfile(abs_bibliography):
        raise ConfigValidationException("Invalid bibliography path: '{}'".format(abs_bibliography))
    if 'csl' in config['bibliography']:
        if not os.path.isfile(os.path.join(CSL_DIR, "{}.csl".format(config['bibliography']['csl']))):
            raise ConfigValidationException("Could not find CSL '{}'".format(config.bibliography.csl))


def validate_context(config):
    if 'context' not in config:
        return

    if type(config['context']) != dict:
        raise ConfigValidationException("Context must be key:value store")

    non_str_keys = [key for key in config['context'].keys() if type(key) != str]
    if non_str_keys:
        raise ConfigValidationException("Context keys must be strings. Non-strings: {}".format(", ".join(non_str_keys)))

    invalid_values = [value for value in config['context'].values() if type(value) in [list, dict]]
    if invalid_values:
        raise ConfigValidationException("Context keys must be plain. Invalid values: {}".format(", ".join(invalid_values)))


def validate_toc(config):
    if 'toc' not in config:
        return
    if type(config['toc']) != bool:
        raise ConfigValidationException("Table of contents key should be either true or false")


def validate_wordcount(config):
    if 'show_word_count' not in config:
        return
    if type(config['show_word_count']) != bool:
        raise ConfigValidationException("Show word count key should be either true or false")


def validate_submission_date(config):
    if 'submission_date' not in config:
        return
    if type(config['submission_date']) in [datetime.date, datetime.datetime, datetime.time]:
        return
    try:
        parser.parse(config['submission_date'])
    except ValueError:
        raise ConfigValidationException("Invalid Submission Date format")


def validate_config(config):
    logger.debug("Validating Config...")
    for validator in [
        check_required_keys,
        test_input,
        test_output,
        validate_bibliography,
        validate_context,
        validate_toc,
        validate_wordcount,
        validate_submission_date
    ]:
        validator(config)
    logger.debug("Config Ok!")
