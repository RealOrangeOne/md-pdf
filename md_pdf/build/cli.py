import click
from md_pdf.build.md import read_files
from md_pdf.build.pandoc import build_document, output_html
from md_pdf.build.cover import render_cover
from md_pdf.build.pdf import export_pdf


@click.command('build', short_help="Build document")
@click.argument('in_files', type=click.Path(dir_okay=False, resolve_path=True, writable=True), nargs=-1)
@click.option('--bibliography', '-b', type=click.Path(dir_okay=False, resolve_path=True, writable=True), default=None)
@click.option('--output', '-o', type=click.Path(file_okay=False, resolve_path=True, writable=True), default='out/')
def cli(in_files, bibliography, output):
    data = read_files(in_files)
    doc = build_document(data, bibliography)
    output_html(doc, output)
    render_cover()
    export_pdf(doc, output)
    return 0


