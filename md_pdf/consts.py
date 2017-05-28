import os

PROJECT_DIR = os.path.dirname(__file__)
WORKING_DIR = os.getcwd()

try:
    ASSETS_DIR = os.path.join(os.environ['APPDATA'], '.mdp')
except KeyError:
    ASSETS_DIR = os.path.join(os.environ['HOME'], '.mdp')


CSL_DIR = os.path.join(ASSETS_DIR, 'csl')
TEMPLATES_DIR = os.path.join(ASSETS_DIR, 'templates')
STATIC_DIR = os.path.join(ASSETS_DIR, 'static')

INTERNAL_ASSETS_DIR = os.path.join(PROJECT_DIR, 'assets')
INTERNAL_STATIC_DIR = os.path.join(INTERNAL_ASSETS_DIR, 'static')
INTERNAL_TEMPLATES_DIR = os.path.join(INTERNAL_ASSETS_DIR, 'templates')


CONFIG_FILE = os.path.join(WORKING_DIR, 'mdp.yml')

CSL_DOWNLOAD_LINK = "https://github.com/citation-style-language/styles/archive/master.zip"

DATE_FORMAT = "%d %B %Y"
TIME_FORMAT = "%H:%M"
DATETIME_FORMAT = "{} {}".format(DATE_FORMAT, TIME_FORMAT)


os.makedirs(ASSETS_DIR, exist_ok=True)
os.makedirs(TEMPLATES_DIR, exist_ok=True)
os.makedirs(STATIC_DIR, exist_ok=True)
