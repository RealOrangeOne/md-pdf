from scss import Compiler
from md_pdf.consts import STATIC_DIR
from md_pdf.build.pdf import STYLE_FILE
import os


STYLE_SRC_FILE = os.path.join(STATIC_DIR, 'style.scss')


def render_css():
    compiler = Compiler()
    with open(STYLE_SRC_FILE) as f:
        style = f.read()
    with open(STYLE_FILE, 'w') as f:
        data = compiler.compile_string(style)
        f.write(data)
        return data
