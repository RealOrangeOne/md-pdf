from md_pdf.build.md import read_files
from md_pdf.build.pandoc import build_document, output_html
from md_pdf.build.cover import render_cover
from md_pdf.build.pdf import export_pdf
import os


def build(config):
    data = read_files(os.path.abspath(config.input))
    doc = build_document(data, getattr(config, 'bibliography', None), getattr(config, 'context', None))
    if 'html' in config.output_formats:
        output_html(doc, os.path.abspath(config.output_dir))
    if 'pdf' in config.output_formats:
        render_cover(config.context.toDict())
        export_pdf(doc, config)
