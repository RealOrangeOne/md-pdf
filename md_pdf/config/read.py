import yaml
import os
from md_pdf.consts import CONFIG_FILE


def load_config():
    with open(os.path.join(CONFIG_FILE)) as f:
        return yaml.load(f)
