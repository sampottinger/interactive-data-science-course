#!/bin/bash
# Build script for MOOC static site generation.
#
# This script renders the MOOC course content into static HTML files by:
# 1. Generating the main index page from the course structure
# 2. Generating individual lesson pages for all lessons
#
# The script uses render.py to process Jinja2 templates with YAML course data
# from the lessons directory, outputting HTML files to the mooc directory.
#
# License: BSD-3-Clause

python3 ./render.py index ./index.html ./lessons ../mooc/index.html

for i in $(python3 ./render.py list ./lessons); do
    python3 ./render.py lesson ./lesson.html ./lessons $i ../mooc/lesson$i.html
done