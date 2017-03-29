from md_pdf.exceptions import ConfigValidationException
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


def validate_config(config):
    check_required_keys(config)
    test_output(config)


