import click
from md_pdf.build.md import read_files

@click.command('build', short_help="Build document")
@click.argument('in_files', type=click.Path(dir_okay=False, resolve_path=True, writable=True), nargs=-1)
@click.option('--output', '-o', type=click.Path(file_okay=False, resolve_path=True, writable=True), default='out/')
def cli(in_files, output):
    data = read_files(in_files)
    print(data)
