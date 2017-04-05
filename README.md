# MD-PDF

[![CircleCI](https://img.shields.io/circleci/project/github/RealOrangeOne/md-pdf.svg?style=flat-square)](https://circleci.com/gh/RealOrangeOne/md-pdf/)
[![Github Releases](https://img.shields.io/github/downloads/RealOrangeOne/md-pdf/latest/total.svg?style=flat-square)](https://github.com/RealOrangeOne/md-pdf)

Convert markdown files into PDF Documents.

### Features
- Multiple output formats
- Bibliography with 1400+ referencing formats
- Templating support (powered by [`jinja2`](http://jinja.pocoo.org/))
- Cover pages
- Page numbers in footer
- Student / TurnItIn Number in header / cover

__Note__: All features are completely optional


### Usage
    $ mdp --help
    usage: mdp [-h] [-v] [--update-csl]
    
    optional arguments:
      -h, --help     show this help message and exit
      -v, --verbose  Set verbosity level (repeat argument)
      --update-csl   Update CSL files

### Configuration
An example configuration file can be found [Here](https://github.com/RealOrangeOne/md-pdf/blob/master/test-files/mdp.yml).
