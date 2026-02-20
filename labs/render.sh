#!/bin/bash
# Build script for labs static site generation.
#
# This script renders the labs tutorial content into static HTML and Markdown files by:
# 1. Generating the main index page from the lab structure
# 2. Generating individual tutorial pages for all tutorials
#
# The script uses render.py to process Jinja2 templates with YAML lab data
# from the Lab_* directories, outputting HTML and Markdown files to the labs directory.
#
# License: BSD-3-Clause

python3 ./render.py index ./index_template.html . ./index.html

for i in $(python3 ./render.py list .); do
    file=$(python3 ./render.py place . $i)

    html_file="$file"
    md_file="${file%.html}.md"

    python3 ./render.py tutorial ./tutorial.html ./tutorial.md . $i ./$html_file ./$md_file
done
