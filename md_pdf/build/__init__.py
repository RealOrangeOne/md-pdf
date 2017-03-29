from md_pdf.consts import WORKING_DIR
from md_pdf.build.md import read_files
from md_pdf.build.pandoc import build_document, output_html
from md_pdf.build.cover import render_cover
from md_pdf.build.pdf import export_pdf
import os


def build(args, config):
    data = read_files(os.path.join(WORKING_DIR, '*.md'))
    doc = build_document(data, os.path.join(WORKING_DIR, 'bib.yaml'))
    output_html(doc, os.path.join(WORKING_DIR, 'out'))
    render_cover()
    export_pdf(doc, os.path.join(WORKING_DIR, 'out'))
