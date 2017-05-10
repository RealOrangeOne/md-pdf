# Installation

### Installing dependencies
These applications will not be installed with `md-pdf`, so need to be installed through your OS's package manager.
- `pandoc`
- `pandoc-citeproc`
- `wkhtmltopdf` (With QT - [See Here](https://pypi.python.org/pypi/pdfkit))


#### Arch Linux
    yaourt -S pandoc pandoc-citeproc wkhtmltopdf-static
    
#### Ubuntu
    sudo apt install pandoc pandoc-citeproc

To install the correct version of `wkhtmltopdf`, you will need to build it yourself using [this script](https://github.com/JazzCore/python-pdfkit/blob/master/travis/before-script.sh).

#### Windows
__Note__: Windows is an untested platform, these installation instructions are only theoretical!

Pandoc (and `pandoc-citeproc`) can be installed using the installer found [here](https://github.com/jgm/pandoc/releases/).

`wkhtmltopdf` can be installed from the [official website](https://wkhtmltopdf.org/downloads.html).


### Installing `md-pdf`.
This application isn't available through Pypi directly, but can still be installed using pip.
    
    pip install https://github.com/RealOrangeOne/md-pdf
    
This should install the rest of the dependencies. To check it installed correctly, you can run this:
    
    mdp --help
If you see the help information, it's installed correctly. If not, please submit an [issue](https://github.com/RealOrangeOne/md-pdf).
