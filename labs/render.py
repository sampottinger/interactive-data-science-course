"""Static site generator for skills labs.

This module provides a command-line tool to render lab tutorials
into static HTML and Markdown pages using Jinja2 templates and YAML data files.

License: BSD-3-Clause
"""
import os
import sys

import jinja2
import yaml

USAGE_RENDER_INDEX_STR = \
    'USAGE: python render.py index [template] [labs_dir] [output]'
USAGE_RENDER_INDEX_ARGS = 4

USAGE_RENDER_TUTORIAL_STR = \
    'USAGE: python render.py tutorial [template] [md_template] ' + \
    '[labs_dir] [number] [html_output] [md_output]'
USAGE_RENDER_TUTORIAL_ARGS = 7

USAGE_RENDER_LIST_STR = 'USAGE: python render.py list [labs_dir]'
USAGE_RENDER_LIST_ARGS = 2

USAGE_STR = 'USAGE: python render.py [index | tutorial | list]'
MIN_ARGS = 1


def load_labs_from_directory(labs_dir):
    """Load lab structure from directory hierarchy.

    Scans the labs directory for Lab_* subdirectories and loads
    individual YAML tutorial files from each lab. Also loads index.yml
    from each lab directory for lab metadata.

    Args:
        labs_dir: Path to the labs directory containing Lab_*
            subdirectories.

    Returns:
        dict: Dictionary with 'labs' key containing list of lab
            dictionaries with 'name', 'subheader', 'lesson', and
            'tutorials' keys.
    """
    labs = []

    lab_dirs = sorted([
        d for d in os.listdir(labs_dir)
        if d.startswith('Lab_') and os.path.isdir(os.path.join(labs_dir, d))
    ])

    for lab_dir in lab_dirs:
        lab_path = os.path.join(labs_dir, lab_dir)

        # Load index.yml from each lab directory
        index_path = os.path.join(lab_path, 'index.yml')
        with open(index_path, 'r') as f:
            lab_meta = yaml.load(f, Loader=yaml.Loader)

        tutorials = []
        yaml_files = sorted([
            f for f in os.listdir(lab_path)
            if f.endswith('.yaml') and f[0:2].isdigit()
        ])

        for yaml_file in yaml_files:
            yaml_path = os.path.join(lab_path, yaml_file)
            with open(yaml_path, 'r') as f:
                tutorial = yaml.load(f, Loader=yaml.Loader)
                # Extract tutorial number from filename
                tutorial_num = int(yaml_file.split('_')[0])
                tutorial['number'] = tutorial_num
                tutorials.append(tutorial)

        lab_info = {
            'name': lab_meta['name'],
            'subheader': lab_meta['subheader'],
            'lesson': lab_meta.get('lesson', None),
            'tutorials': tutorials
        }
        labs.append(lab_info)

    return {'labs': labs}


def main_index():
    """Command to render the labs index page."""
    if len(sys.argv) != USAGE_RENDER_INDEX_ARGS + 1:
        print(USAGE_RENDER_INDEX_STR)
        sys.exit(1)

    template_path = sys.argv[2]
    labs_dir = sys.argv[3]
    output_path = sys.argv[4]

    with open(template_path) as f:
        template = jinja2.Template(f.read())

    data = load_labs_from_directory(labs_dir)

    result = template.render(labs=data['labs'])
    with open(output_path, 'w') as f:
        f.write(result)


def main_tutorial():
    """Command to render a tutorial page in HTML and Markdown."""
    if len(sys.argv) != USAGE_RENDER_TUTORIAL_ARGS + 1:
        print(USAGE_RENDER_TUTORIAL_STR)
        sys.exit(1)

    template_path = sys.argv[2]
    md_template_path = sys.argv[3]
    labs_dir = sys.argv[4]
    tutorial_number = int(sys.argv[5])
    html_output_path = sys.argv[6]
    md_output_path = sys.argv[7]

    with open(template_path) as f:
        html_template = jinja2.Template(f.read())

    with open(md_template_path) as f:
        md_template = jinja2.Template(f.read())

    data = load_labs_from_directory(labs_dir)

    # Find the tutorial with the given number
    tutorial = None
    for lab in data['labs']:
        for tut in lab['tutorials']:
            if tut['number'] == tutorial_number:
                tutorial = tut
                break
        if tutorial:
            break

    if not tutorial:
        print(f'Tutorial {tutorial_number} not found')
        sys.exit(1)

    # Process citations if they exist
    citations_raw = tutorial.get('citations', [])
    citations = [process_citation(c) for c in citations_raw]

    template_vals = {
        'number': tutorial_number,
        'name': tutorial['name'],
        'file': tutorial['file'],
        'header': tutorial.get('header', ''),
        'sections': tutorial.get('sections', []),
        'citations': citations
    }

    # Render HTML
    html_result = html_template.render(**template_vals)
    with open(html_output_path, 'w') as f:
        f.write(html_result)

    # Render Markdown
    md_result = md_template.render(**template_vals)
    with open(md_output_path, 'w') as f:
        f.write(md_result)


def process_citation(citation):
    """Prepare a citation to be rendered in HTML.

    Convert citation from YAML format (with 'text' and 'available' fields)
    to HTML format with links.

    Args:
        citation: Dictionary with 'text' and 'available' keys.

    Returns:
        str: The citation text with link added to be displayed as HTML.
    """
    text = citation.get('text', '')
    url = citation.get('available', '')

    if url:
        # Make sure URL has protocol
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'https://' + url
        return f'{text} Available: <a href="{url}" target="_blank">{url}</a>'
    else:
        return text


def main_list():
    """Command to list all tutorial numbers."""
    if len(sys.argv) != USAGE_RENDER_LIST_ARGS + 1:
        print(USAGE_RENDER_LIST_STR)
        sys.exit(1)

    labs_dir = sys.argv[2]
    data = load_labs_from_directory(labs_dir)

    tutorial_numbers = []
    for lab in data['labs']:
        for tutorial in lab['tutorials']:
            tutorial_numbers.append(tutorial['number'])

    tutorial_numbers.sort()

    for number in tutorial_numbers:
        print(number)


def main():
    """Main entrypoint for the labs static site generator."""
    if len(sys.argv) < MIN_ARGS + 1:
        print(USAGE_STR)
        sys.exit(1)

    command = sys.argv[1]
    if command == 'index':
        main_index()
    elif command == 'tutorial':
        main_tutorial()
    elif command == 'list':
        main_list()


if __name__ == '__main__':
    main()
