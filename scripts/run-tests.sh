#!/usr/bin/env bash

set -e

coverage run --source=md_pdf -m unittest -v $@

coverage report
coverage html
