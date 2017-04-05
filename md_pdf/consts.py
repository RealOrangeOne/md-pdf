import os

PROJECT_DIR = os.path.dirname(__file__)
WORKING_DIR = os.getcwd()
ASSET_DIR = os.path.join(PROJECT_DIR, 'assets')

CSL_DIR = os.path.join(ASSET_DIR, 'csl')
TEMPLATES_DIR = os.path.join(ASSET_DIR, 'templates')
STATIC_DIR = os.path.join(ASSET_DIR, 'static')

CONFIG_FILE = os.path.join(WORKING_DIR, 'mdp.yml')

CSL_DOWNLOAD_LINK = "https://github.com/citation-style-language/styles/archive/master.zip"
