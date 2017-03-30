import yaml
import os
from md_pdf.consts import CONFIG_FILE
from md_pdf.exceptions import ConfigValidationException


def load_config():
    try:
        with open(os.path.join(CONFIG_FILE)) as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        raise ConfigValidationException("Can't find config file at {}".format(CONFIG_FILE))
