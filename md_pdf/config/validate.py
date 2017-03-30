from md_pdf.exceptions import ConfigValidationException
from md_pdf.consts import CSL_DIR
import glob
import os


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
    abs_output_dir = os.path.abspath(config.output_dir)
    if not os.path.isdir(abs_output_dir):
        raise ConfigValidationException("Can't find output directory '{}'".format(abs_output_dir))
    if not config.output_formats:
        raise ConfigValidationException("No output formats specified")
    invalid_formats = [key for key in config.output_formats if key not in ['html', 'pdf']]
    if invalid_formats:
        raise ConfigValidationException("Invalid output formats provided: '{}'".format(", ".join(invalid_formats)))


def test_input(config):
    abs_input = os.path.abspath(config.input)
    if len(glob.glob(abs_input)) == 0:
        raise ConfigValidationException("No files found at {}".format(abs_input))


def validate_bibliography(config):
    if 'bibliography' not in config:
        return
    if 'references' not in config.bibliography:
        raise ConfigValidationException("Missing References Path")

    abs_bibliography = os.path.abspath(config.bibliography.references)
    if not os.path.isfile(abs_bibliography):
        raise ConfigValidationException("Invalid bibliography path: '{}'".format(abs_bibliography))
    if 'csl' in config.bibliography:
        if not os.path.isfile(os.path.join(CSL_DIR, "{}.csl".format(config.bibliography.csl))):
            raise ConfigValidationException("Could not find CSL '{}'".format(config.bibliography.csl))


def validate_config(config):
    check_required_keys(config)
    test_input(config)
    test_output(config)
    validate_bibliography(config)


