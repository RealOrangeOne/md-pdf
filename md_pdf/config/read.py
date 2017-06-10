import yaml
from md_pdf.consts import CONFIG_FILE
from md_pdf.exceptions import ConfigValidationException


def load_config(location: str=CONFIG_FILE) -> str:
    try:
        with open(location) as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        raise ConfigValidationException("Can't find config file at {}".format(CONFIG_FILE))
