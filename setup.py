from setuptools import setup


setup(
    name="md-pdf",
    version="1.0",
    install_requires=[
        "beautifulsoup4==4.5.3",
        "dotmap==1.2.17",
        "jinja2==2.9.5",
        "pdfkit==0.6.1",
        "pypandoc==1.3.3",
        "PyYAML==3.12"
    ],
    entry_points="""
        [console_scripts]
        mdp=md_pdf.cli:cli
    """
)
