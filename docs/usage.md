# Usage
    $ mdp --help
    usage: mdp [-h] [-v] [--update-csl]
    
    optional arguments:
      -h, --help     show this help message and exit
      -v, --verbose  Set verbosity level (repeat argument)
      --update-csl   Update CSL files

## Running the application
Assuming you're in a directory with a valid `mdp.yml` file, simply run `mdp` to build your files to the output directory!

## Downloading CSL Files
In order to use referencing properly, `csl` files need to be downloaded. These tell `md-pdf` what style of referencing you're using, and how to output the bibliography.

To download these, simply run:

    mdp --update-csl

This will download the `csl` files into the install directory of the application. It only needs to be run once, however can be run whenever to update the definitions from [here](https://github.com/citation-style-language/styles/).

## Verbosity
By default, when building, the application doesn't output anything to the console. It simply runs, and terminates when it's finished. Obviously errors are still reported.

To increase the verbosity level, simply add the `-v` argument when running the application. This can be chained a maximum of 3 times (`-vvv`), subsequent repetition will be ignored.
