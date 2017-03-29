from jinja2 import Template
from md_pdf.consts import PROJECT_DIR
import os


COVER_TEMPLATE = os.path.join(PROJECT_DIR, 'assets', 'cover-template.html')
OUTPUT_COVER_FILE = os.path.join(PROJECT_DIR, 'assets', 'cover.html')


def render_cover(context={}):
    with open(COVER_TEMPLATE) as f:
        template = Template(f.read())
    with open(OUTPUT_COVER_FILE, "w") as f:
        cover = template.render(context)
        f.write(cover)
        return cover
