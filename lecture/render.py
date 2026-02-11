"""Static site generator for open educational resource.

This module provides a command-line tool to render OER (open educational resource) lesson content
with standardized structure into static HTML pages. It supports rendering both index pages (course
listings) and individual lesson pages using Jinja2 templates and YAML data files.

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
    'lessons_dir',
    'output'
]
USAGE_RENDER_INDEX_STR = build_usage_str('index', USAGE_RENDER_INDEX_ARGS)
USAGE_RENDER_INDEX_ARGS = len(USAGE_RENDER_INDEX_ARGS) + 1

USAGE_RENDER_LESSON_ARGS = [
    'template',
    'lessons_dir',
    'number',
    'output'
]
USAGE_RENDER_LESSON_STR = build_usage_str('lesson', USAGE_RENDER_LESSON_ARGS)
USAGE_RENDER_LESSON_ARGS = len(USAGE_RENDER_LESSON_ARGS) + 1

USAGE_RENDER_LIST_ARGS = [
    'lessons_dir'
]
USAGE_RENDER_LIST_STR = build_usage_str('list', USAGE_RENDER_LIST_ARGS)
USAGE_RENDER_LIST_ARGS = len(USAGE_RENDER_LIST_ARGS) + 1

USAGE_STR = 'USAGE: python render.py [index | lesson | list]'
MIN_ARGS = 1


def load_yaml(yaml_path):
  """Load a YAML file from the given path.

  Args:
    yaml_path: Path to the YAML file to load.

  Returns:
    dict: The parsed YAML content.
  """
  with open(yaml_path, 'r') as f:
    return yaml.load(f, Loader=yaml.Loader)


def get_section_lessons(section_dir, lessons_dir):
  """Extract section information and lessons from a section directory.

  Args:
    section_dir: Full path to the section directory.
    lessons_dir: Path to the lessons directory containing sections.

  Returns:
    dict: Dictionary with 'name', 'tagline', 'detailed', and 'lessons' keys.
  """
  # Extract section ID from directory name
  dir_basename = os.path.basename(section_dir)
  section_components = dir_basename.split('_')
  id_pieces = section_components[1:]
  section_id = '_'.join(id_pieces)

  section_path = section_dir

  # Load index.yml from section directory
  index_path = os.path.join(section_path, 'index.yml')
  section_meta = load_yaml(index_path)

  # Load all lesson YAML files
  section_members = os.listdir(section_path)
  yaml_only = filter(lambda x: x.endswith('.yaml'), section_members)
  yaml_files = sorted(yaml_only)

  yaml_paths = map(lambda x: os.path.join(section_path, x), yaml_files)
  lessons_lazy = map(load_yaml, yaml_paths)
  lessons = list(lessons_lazy)

  return {
      'name': section_meta['name'],
      'tagline': section_meta['tagline'],
      'detailed': section_meta['detailed'],
      'lessons': lessons,
      'id': section_id
  }


def load_course_from_directory(lessons_dir):
  """Load course structure from directory hierarchy.

  Scans the lessons directory for section subdirectories and loads
  individual YAML lesson files from each section. Also loads index.yml
  from each section directory for section metadata.

  Args:
    lessons_dir: Path to the lessons directory containing section
      subdirectories.

  Returns:
    dict: Dictionary with 'sections' key containing section names
      mapped to section dictionaries with 'name', 'tagline', 'detailed',
      and 'lessons' keys. Section names are derived from directory names
      by stripping numeric prefix (e.g., '01_Hello' -> 'Hello').
  """
  members = os.listdir(lessons_dir)
  full_paths = map(lambda x: os.path.join(lessons_dir, x), members)
  unsorted_directories = filter(lambda x: os.path.isdir(x), full_paths)
  section_dirs = sorted(unsorted_directories)

  get_lesson_from_dir = lambda section_dir: get_section_lessons(
      section_dir, lessons_dir)
  section_info = map(get_lesson_from_dir, section_dirs)
  keyed_sections = map(lambda x: (x['name'], x), section_info)
  sections_by_name = dict(keyed_sections)

  return {'sections': sections_by_name}


def main_index():
  """Command to render an index page."""
  if len(sys.argv) != USAGE_RENDER_INDEX_ARGS + 1:
    print(USAGE_RENDER_INDEX_STR)
    sys.exit(1)

  template_path = sys.argv[2]
  lessons_dir = sys.argv[3]
  output_path = sys.argv[4]

  with open(template_path) as f:
    template = jinja2.Template(f.read())

  data = load_course_from_directory(lessons_dir)

  sections_list = list(data['sections'].values())
  result = template.render(sections=sections_list)
  with open(output_path, 'w') as f:
    f.write(result)


def main_lesson():
  """Command to render a lesson page."""
  if len(sys.argv) != USAGE_RENDER_LESSON_ARGS + 1:
    print(USAGE_RENDER_LESSON_STR)
    sys.exit(1)

  template_path = sys.argv[2]
  lessons_dir = sys.argv[3]
  lesson_number = int(sys.argv[4])
  output_path = sys.argv[5]

  prior_number = lesson_number - 1
  next_number = lesson_number + 1

  with open(template_path) as f:
    template = jinja2.Template(f.read())

  data = load_course_from_directory(lessons_dir)

  sections = data['sections'].values()
  lessons_nested = map(lambda x: x['lessons'], sections)
  lessons = itertools.chain(*lessons_nested)
  lessons_by_number_tuple = map(lambda x: (x['number'], x), lessons)
  lessons_by_number = dict(lessons_by_number_tuple)

  has_prior = prior_number in lessons_by_number
  prior_url = ('/lesson%d.html' % prior_number) if has_prior else None
  has_next = next_number in lessons_by_number
  next_url = ('/lesson%d.html' % next_number) if has_next else None

  lesson = lessons_by_number[lesson_number]

  citations_raw = lesson.get('citations', [])
  citations = map(process_citation, citations_raw) if isinstance(citations_raw, list) else []

  # Convert markdown to HTML if available
  markdown_html = None
  if lesson.get('materials_md', None):
    md_filename = 'lesson%02d.md' % lesson_number
    md_path = os.path.join(lessons_dir, '..', 'support', 'md', md_filename)
    markdown_html = convert_markdown_to_html(md_path)

  template_vals = {
      'number': lesson_number,
      'previous_url': prior_url,
      'next_url': next_url,
      'name': lesson['name'],
      'text': lesson['text'],
      'slides': lesson.get('slides', None),
      'materials_pdf': lesson.get('materials_pdf', None),
      'materials_pptx': lesson.get('materials_pptx', None),
      'materials_md': lesson.get('materials_md', None),
      'markdown_html': markdown_html,
      'links': lesson.get('links', []),
      'assignment': lesson.get('assignment', None),
      'reading': lesson.get('reading', None),
      'citations': list(citations),
      'video': lesson.get('video', None)
  }

  result = template.render(**template_vals)
  with open(output_path, 'w') as f:
    f.write(result)


def process_citation(citation) -> str:
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


def shift_headers(html_content):
  """Shift HTML headers down by 2 levels.

  Shifts all header tags down by 2 levels (h1->h3, h2->h4, etc.)
  to maintain proper document structure. Headers h5 and h6 are capped at h6.

  Args:
    html_content: HTML string containing header tags.

  Returns:
    str: HTML string with shifted header tags.
  """
  # Shift headers down by 2 levels, capping at h6
  # Do this in reverse order to avoid double-shifting
  html_content = html_content.replace('<h6>', '<h6temp>').replace('</h6>', '</h6temp>')
  html_content = html_content.replace('<h5>', '<h6>').replace('</h5>', '</h6>')
  html_content = html_content.replace('<h4>', '<h6>').replace('</h4>', '</h6>')
  html_content = html_content.replace('<h3>', '<h5>').replace('</h3>', '</h5>')
  html_content = html_content.replace('<h2>', '<h4>').replace('</h2>', '</h4>')
  html_content = html_content.replace('<h1>', '<h3>').replace('</h1>', '</h3>')
  html_content = html_content.replace('<h6temp>', '<h6>').replace('</h6temp>', '</h6>')
  return html_content


def convert_markdown_to_html(md_file_path):
  """Convert a markdown file to HTML.

  Reads a markdown file and converts it to HTML using Python-Markdown.
  Headers are shifted down by 2 levels to maintain document structure.

  Args:
    md_file_path: Path to the markdown file to convert.

  Returns:
    str: The HTML content or None if file doesn't exist.
  """
  if not os.path.exists(md_file_path):
    return None

  with open(md_file_path, 'r', encoding='utf-8') as f:
    md_content = f.read()

  html_content = markdown.markdown(md_content)
  html_content = shift_headers(html_content)
  return html_content


def main_list():
  """Command to list all lesson numbers."""
  if len(sys.argv) != USAGE_RENDER_LIST_ARGS + 1:
    print(USAGE_RENDER_LIST_STR)
    sys.exit(1)

  lessons_dir = sys.argv[2]
  data = load_course_from_directory(lessons_dir)

  sections = data['sections'].values()
  lessons_nested = map(lambda x: x['lessons'], sections)
  lessons = itertools.chain(*lessons_nested)
  lesson_numbers = sorted([lesson['number'] for lesson in lessons])

  for number in lesson_numbers:
    print(number)


def main():
  """Main entrypoint for the static MOOC generator."""
  if len(sys.argv) < MIN_ARGS + 1:
    print(USAGE_STR)
    sys.exit(1)

  command = sys.argv[1]
  if command == 'index':
    main_index()
  elif command == 'lesson':
    main_lesson()
  elif command == 'list':
    main_list()


if __name__ == '__main__':
  main()
