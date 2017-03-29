from md_pdf.exceptions import ConfigValidationException


REQUIRED_KEYS = [
    'output',
    'input'
]


def check_required_keys(config):
    missing_keys = [key for key in REQUIRED_KEYS if key not in config]
    if missing_keys:
        raise ConfigValidationException("Missing required keys: {}".format(", ".join(missing_keys)))


def validate_config(config):
    check_required_keys(config)


