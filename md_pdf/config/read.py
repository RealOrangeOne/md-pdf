import yaml
from dotmap import DotMap
import os
from md_pdf.consts import CONFIG_FILE


def load_config():
    with open(os.path.join(CONFIG_FILE)) as f:
        return DotMap(yaml.load(f))
