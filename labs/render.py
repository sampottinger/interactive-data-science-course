"""Static site generator for skills labs.

This module provides a command-line tool to render lab tutorials
into static HTML and Markdown pages using Jinja2 templates and YAML data files.

License: BSD-3-Clause
"""
import itertools
import os
import sys

import jinja2
import markdown
import yaml

BASE_USAGE_STR = 'USAGE: python render.py'


def build_usage_str(command, attrs):
  """Build a usage string for a command with its arguments.

  Args:
  command: The command name to build usage string for.
  attrs: List of argument names for the command.

  Returns:
  str: The formatted usage string with bracketed arguments.
  """
  attrs_decorated = map(lambda x: '[%s]' % x, attrs)
  attrs_str = ' '.join(attrs_decorated)
  return BASE_USAGE_STR + ' ' + command + ' ' + attrs_str


USAGE_RENDER_INDEX_ARGS = [
    'template',
    'labs_dir',
    'output'
]
USAGE_RENDER_INDEX_STR = build_usage_str('index', USAGE_RENDER_INDEX_ARGS)
USAGE_RENDER_INDEX_ARGS = len(USAGE_RENDER_INDEX_ARGS) + 1

USAGE_RENDER_TUTORIAL_ARGS = [
    'template',
    'md_template',
    'labs_dir',
    'number',
    'html_output',
    'md_output'
]
USAGE_RENDER_TUTORIAL_STR = build_usage_str('tutorial', USAGE_RENDER_TUTORIAL_ARGS)
USAGE_RENDER_TUTORIAL_ARGS = len(USAGE_RENDER_TUTORIAL_ARGS) + 1

USAGE_RENDER_LIST_ARGS = [
    'labs_dir'
]
USAGE_RENDER_LIST_STR = build_usage_str('list', USAGE_RENDER_LIST_ARGS)
USAGE_RENDER_LIST_ARGS = len(USAGE_RENDER_LIST_ARGS) + 1

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

  members = os.listdir(labs_dir)
  full_paths = map(lambda x: os.path.join(labs_dir, x), members)
  is_lab_dir = lambda x: os.path.basename(x).startswith('Lab_') and os.path.isdir(x)
  unsorted_lab_dirs = filter(is_lab_dir, full_paths)
  lab_dirs = sorted(unsorted_lab_dirs)

  for lab_dir in lab_dirs:
    lab_path = lab_dir

    # Load index.yml from each lab directory
    index_path = os.path.join(lab_path, 'index.yml')
    with open(index_path, 'r') as f:
      lab_meta = yaml.load(f, Loader=yaml.Loader)

    tutorials = []
    lab_members = os.listdir(lab_path)
    is_tutorial_yaml = lambda x: x.endswith('.yaml') and x[0:2].isdigit()
    tutorial_yamls = filter(is_tutorial_yaml, lab_members)
    yaml_files = sorted(tutorial_yamls)

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


def render_html(template_path, template_vals, output_path):
  """Render HTML output from template and write to file.

  Args:
    template_path: Path to the Jinja2 HTML template file.
    template_vals: Dictionary of values to pass to the template.
    output_path: Path where the rendered HTML should be written.
  """
  with open(template_path) as f:
    template = jinja2.Template(f.read())

  result = template.render(**template_vals)
  with open(output_path, 'w') as f:
    f.write(result)


def render_markdown(template_path, template_vals, output_path):
  """Render Markdown output from template and write to file.

  Args:
    template_path: Path to the Jinja2 Markdown template file.
    template_vals: Dictionary of values to pass to the template.
    output_path: Path where the rendered Markdown should be written.
  """
  with open(template_path) as f:
    template = jinja2.Template(f.read())

  result = template.render(**template_vals)
  with open(output_path, 'w') as f:
    f.write(result)


def build_tutorials_by_number(data):
  """Build a dictionary mapping tutorial numbers to tutorial data.

  Args:
    data: Course data dictionary with 'labs' key containing lab information.

  Returns:
    dict: Dictionary mapping tutorial numbers to tutorial dictionaries.
  """
  labs = data['labs']
  tutorials_nested = map(lambda x: x['tutorials'], labs)
  tutorials = itertools.chain(*tutorials_nested)
  tutorials_by_number_tuple = map(lambda x: (x['number'], x), tutorials)
  return dict(tutorials_by_number_tuple)


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

  data = load_labs_from_directory(labs_dir)
  tutorials_by_number = build_tutorials_by_number(data)

  if tutorial_number not in tutorials_by_number:
    print(f'Tutorial {tutorial_number} not found')
    sys.exit(1)

  tutorial = tutorials_by_number[tutorial_number]

  citations_raw = tutorial.get('citations', [])
  processed_citations = map(process_citation, citations_raw)
  citations_realized = list(processed_citations)

  # Process section content
  sections_raw = tutorial.get('sections', [])
  processed_sections = map(process_section_content, sections_raw)
  sections_realized = list(processed_sections)

  template_vals = {
      'number': tutorial_number,
      'name': tutorial['name'],
      'file': tutorial['file'],
      'header': tutorial.get('header', ''),
      'sections': sections_realized,
      'citations': citations_realized
  }

  render_html(template_path, template_vals, html_output_path)
  render_markdown(md_template_path, template_vals, md_output_path)


def process_citation(citation):
  """Prepare a citation to be rendered in HTML.

  Accepts structured citation dictionaries with text, optional doi, and
  optional available fields. Inserts links into citation text to be rendered
  as HTML where DOI values from the 'doi' field expand to https://doi.org/IDENTIFIER.

  Args:
    citation: A dict with 'text', optional 'doi', and optional 'available' keys.

  Returns:
    str: The citation text with links added to be displayed as HTML.
  """
  # Structured format: dict with text, optional doi, and optional available
  text = citation.get('text', '')
  doi = citation.get('doi', '')
  available = citation.get('available', '')

  # Build the output starting with text
  result = text

  # Append DOI link if present
  if doi:
    result += f' doi: <a href="https://doi.org/{doi}">{doi}</a>.'

  # Append available URL if present
  if available:
    if not available.startswith('http://') and not available.startswith('https://'):
      available = 'https://' + available
    result += f' Available: <a href="{available}" target="_blank">{available}</a>'

  return result


def process_section_content(section):
  """Process section content from body, html, or markdown attributes.

  Checks for mutually exclusive content attributes (body, html, markdown).
  Converts markdown to HTML if needed. Applies blockstyle transformation
  if specified.

  Args:
    section: A dict with section data. May contain 'body', 'html', or 'markdown'
      keys for content, and optional 'blockstyle' key.

  Returns:
    dict: The section dict with processed content in 'body' field.

  Raises:
    ValueError: If more than one content attribute is present, or if
      blockstyle value is invalid.
  """
  # Check for mutually exclusive content attributes
  content_attrs = []
  if 'body' in section:
    content_attrs.append('body')
  if 'html' in section:
    content_attrs.append('html')
  if 'markdown' in section:
    content_attrs.append('markdown')

  if len(content_attrs) > 1:
    raise ValueError(
        f'Section "{section.get("short", "unknown")}" has multiple content '
        f'attributes: {", ".join(content_attrs)}. Only one of body, html, or '
        f'markdown is allowed.'
    )

  # Get the content
  content = None
  if 'body' in section:
    content = section['body']
  elif 'html' in section:
    content = section['html']
  elif 'markdown' in section:
    content = markdown.markdown(section['markdown'])

  # Validate and apply blockstyle
  blockstyle = section.get('blockstyle', 'pre')
  if blockstyle not in ['pre', 'blockquote']:
    raise ValueError(
        f'Section "{section.get("short", "unknown")}" has invalid blockstyle '
        f'"{blockstyle}". Only "pre" and "blockquote" are allowed.'
    )

  if blockstyle == 'blockquote' and content:
    content = content.replace('<pre>', '<blockquote>')
    content = content.replace('</pre>', '</blockquote>')

  # Store processed content in body field for template compatibility
  section['body'] = content

  return section


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
