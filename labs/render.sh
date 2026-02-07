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
    # Get the file name for this tutorial from the YAML
    file=$(python3 -c "
import os
import yaml
labs_dir = '.'
lab_dirs = sorted([d for d in os.listdir(labs_dir) if d.startswith('Lab_') and os.path.isdir(os.path.join(labs_dir, d))])
for lab_dir in lab_dirs:
    lab_path = os.path.join(labs_dir, lab_dir)
    yaml_files = sorted([f for f in os.listdir(lab_path) if f.startswith('tutorial_') and f.endswith('.yaml')])
    for yaml_file in yaml_files:
        tutorial_num = int(yaml_file.split('_')[1].split('.')[0])
        if tutorial_num == $i:
            yaml_path = os.path.join(lab_path, yaml_file)
            with open(yaml_path, 'r') as f:
                tutorial = yaml.load(f, Loader=yaml.Loader)
                print(tutorial['file'])
                exit(0)
")

    html_file="$file"
    md_file="${file%.html}.md"

    python3 ./render.py tutorial ./tutorial.html ./tutorial.md . $i ./$html_file ./$md_file
done
