"""Static site generator for open educational resource.

This module provides a command-line tool to render OER (open educational resource) lesson content
with standardized structure into static HTML pages. It supports rendering both index pages (course
listings) and individual lesson pages using Jinja2 templates and YAML data files.

License: BSD-3-Clause
"""
import itertools
import os
import re
import sys

import jinja2
import yaml

USAGE_RENDER_INDEX_STR = \
    'USAGE: python render.py index [template] [lessons_dir] [output]'
USAGE_RENDER_INDEX_ARGS = 4

USAGE_RENDER_LESSON_STR = \
    'USAGE: python render.py lesson [template] [lessons_dir] [number] [output]'
USAGE_RENDER_LESSON_ARGS = 5

USAGE_RENDER_LIST_STR = 'USAGE: python render.py list [lessons_dir]'
USAGE_RENDER_LIST_ARGS = 2

USAGE_STR = 'USAGE: python render.py [index | lesson | list]'
MIN_ARGS = 1


def load_course_from_directory(lessons_dir):
  """Load course structure from directory hierarchy.

  Scans the lessons directory for section subdirectories and loads
  individual YAML lesson files from each section. Returns a dictionary
  matching the structure previously loaded from course.yml.

  Args:
    lessons_dir: Path to the lessons directory containing section
      subdirectories.

  Returns:
    dict: Dictionary with 'sections' key containing section names
      mapped to lists of lesson dictionaries. Section names are
      derived from directory names by stripping numeric prefix and
      lowercasing (e.g., '01_Hello' -> 'hello').
  """
  sections = {}

  section_dirs = sorted([
      d for d in os.listdir(lessons_dir)
      if os.path.isdir(os.path.join(lessons_dir, d))
  ])

  for section_dir in section_dirs:
    section_name = section_dir.split('_', 1)[1]
    section_path = os.path.join(lessons_dir, section_dir)

    lessons = []
    yaml_files = sorted([
        f for f in os.listdir(section_path)
        if f.endswith('.yaml')
    ])

    for yaml_file in yaml_files:
      yaml_path = os.path.join(section_path, yaml_file)
      with open(yaml_path, 'r') as f:
        lesson = yaml.load(f, Loader=yaml.Loader)
        lessons.append(lesson)

    sections[section_name] = lessons

  return {'sections': sections}


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

  result = template.render(sections=data['sections'])
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
  lessons = itertools.chain(*sections)
  lessons_by_number_tuple = map(lambda x: (x['number'], x), lessons)
  lessons_by_number = dict(lessons_by_number_tuple)

  has_prior = prior_number in lessons_by_number
  prior_url = ('/lesson%d.html' % prior_number) if has_prior else None
  has_next = next_number in lessons_by_number
  next_url = ('/lesson%d.html' % next_number) if has_next else None

  lesson = lessons_by_number[lesson_number]

  has_citations = lesson.get('citations', False)
  citations_raw = load_citations_from_file(lesson_number) if has_citations else []

  citations = map(process_citation, citations_raw)

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
      'links': lesson.get('links', []),
      'assignment': lesson.get('assignment', None),
      'reading': lesson.get('reading', None),
      'citations': list(citations),
      'video': lesson.get('video', None)
  }

  result = template.render(**template_vals)
  with open(output_path, 'w') as f:
    f.write(result)


def load_citations_from_file(lesson_number: int) -> list:
  """Load citations from a text file for a given lesson.

  Load citations from text file if available. If file doesn't exist, returns
  an empty list. Skip empty lines and whitespace-only lines.

  Args:
    lesson_number: The 0-indexed lesson number.

  Returns:
    list: A list of citation strings, or an empty list if the file doesn't exist.
  """
  citations_file = f'citations/lesson{lesson_number:02d}.txt'
  try:
    with open(citations_file, 'r') as f:
      stripped = map(str.strip, f)
      no_empty = filter(None, stripped)
      realized = list(no_empty)
      return realized
  except FileNotFoundError:
    return []


def process_citation(citation: str) -> str:
  """Prepare a citation to be rendered in HTML.

  Insert links into citation text to be rendered as HTML where:

   - DOI mentions like "doi: 10.1080/01621459.1984.10478080" expand to
     https://www.doi.org/10.1080/01621459.1984.10478080.
   - Text which starts with http:// or https:// will become a link to the URL.

  Args:
    citation: The citation text into which HTML links should be added.

  Returns:
    str: The citation text with links added to be displayed as HTML.
  """

  url_pattern = r'(https?://[^\s]+)'
  citation = re.sub(url_pattern,
                    lambda m: f'<a href="{m.group(1)}">{m.group(1)}</a>',
                    citation)

  doi_pattern = r'doi:\s*([\d\.]+/[\w\d\.\-\/]+)'
  citation = re.sub(
      doi_pattern, lambda m:
      f'doi: <a href="https://www.doi.org/{m.group(1)}">{m.group(1)}</a>',
      citation)

  return citation


def main_list():
  """Command to list all lesson numbers."""
  if len(sys.argv) != USAGE_RENDER_LIST_ARGS + 1:
    print(USAGE_RENDER_LIST_STR)
    sys.exit(1)

  lessons_dir = sys.argv[2]
  data = load_course_from_directory(lessons_dir)

  sections = data['sections'].values()
  lessons = itertools.chain(*sections)
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
