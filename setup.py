from setuptools import setup, find_packages


setup(
    name="md-pdf",
    version="1.0",
    install_requires=[
        "beautifulsoup4==4.5.3",
        "jinja2==2.9.5",
        "pdfkit==0.6.1",
        "progressbar2==3.16.0",
        "pypandoc==1.3.3",
        "pyscss==1.3.5",
        "PyYAML==3.12"
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    package_data={
        '': ['*.js', '*.css', '*.html']
    },
    entry_points="""
        [console_scripts]
        mdp=md_pdf.cli:cli
    """
)
