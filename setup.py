from setuptools import setup, find_packages
from md_pdf import __version__

setup(
    name="md-pdf",
    version=__version__,
    use_scm_version=True,
    install_requires=[
        "beautifulsoup4==4.5.3",
        "jinja2==2.9.5",
        "pdfkit==0.6.1",
        "progressbar2==3.16.0",
        "pypandoc==1.3.3",
        "pyscss==1.3.5",
        "python-dateutil==2.6.0",
        "PyYAML==3.12",
        "word-count==0.1.0"
    ],
    setup_requires=['setuptools_scm'],
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    entry_points="""
        [console_scripts]
        mdp=md_pdf.cli:cli
    """
)
