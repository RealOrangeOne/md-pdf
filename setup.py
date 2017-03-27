from setuptools import setup


setup(
    name="md-pdf",
    version="1.0",
    install_requires=[
        "beautifulsoup4==4.5.3",
        "click==6.7.0",
        "jinja2==2.9.5",
        "pdfkit==0.6.1",
        "pypandoc==1.3.3"
    ],
    entry_points="""
        [console_scripts]
        mdp=src.cli:cli
    """
)
