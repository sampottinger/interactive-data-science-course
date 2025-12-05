import itertools
import re
import sys

import jinja2
import yaml

USAGE_RENDER_INDEX_STR = 'USAGE: python render.py index [template] [yaml] [output]'
USAGE_RENDER_INDEX_ARGS = 4

USAGE_RENDER_LESSON_STR = 'USAGE: python render.py lesson [template] [yaml] [number] [output]'
USAGE_RENDER_LESSON_ARGS = 5

USAGE_STR = 'USAGE: python render.py [index | lesson]'
MIN_ARGS = 1


def main_index():
  """Command to render an index page."""
  if len(sys.argv) != USAGE_RENDER_INDEX_ARGS + 1:
    print(USAGE_RENDER_INDEX_STR)
    sys.exit(1)

  template_path = sys.argv[2]
  data_path = sys.argv[3]
  output_path = sys.argv[4]

  with open(template_path) as f:
    template = jinja2.Template(f.read())

  with open(data_path, 'r') as f:
    data = yaml.load(f, Loader=yaml.Loader)

  result = template.render(sections=data['sections'])
  with open(output_path, 'w') as f:
    f.write(result)


def main_lesson():
  """Command to render a lesson page."""
  if len(sys.argv) != USAGE_RENDER_LESSON_ARGS + 1:
    print(USAGE_RENDER_LESSON_STR)
    sys.exit(1)

  template_path = sys.argv[2]
  data_path = sys.argv[3]
  lesson_number = int(sys.argv[4])
  output_path = sys.argv[5]

  prior_number = lesson_number - 1
  next_number = lesson_number + 1

  with open(template_path) as f:
    template = jinja2.Template(f.read())

  with open(data_path, 'r') as f:
    data = yaml.load(f, Loader=yaml.Loader)

  sections = data['sections'].values()
  lessons = itertools.chain(*sections)
  lessons_by_number_tuple = map(lambda x: (x['number'], x), lessons)
  lessons_by_number = dict(lessons_by_number_tuple)

  has_prior = prior_number in lessons_by_number
  prior_url = ('/mooc/lesson%d.html' % prior_number) if has_prior else None
  has_next = next_number in lessons_by_number
  next_url = ('/mooc/lesson%d.html' % next_number) if has_next else None

  lesson = lessons_by_number[lesson_number]

  citations_raw = lesson.get('citations', [])
  citations = map(process_citation, citations_raw)

  template_vals = {
      'number': lesson_number,
      'previous_url': prior_url,
      'next_url': next_url,
      'name': lesson['name'],
      'text': lesson['text'],
      'slides': lesson.get('slides', None),
      'links': lesson.get('links', []),
      'assignment': lesson.get('assignment', None),
      'reading': lesson.get('reading', None),
      'citations': list(citations),
      'video': lesson.get('video', None)
  }

  result = template.render(**template_vals)
  with open(output_path, 'w') as f:
    f.write(result)


def process_citation(citation: str) -> str:
  """Prepare a citation to be rendered in HTML.
  
  Insert links into citation text to be rendered as HTML where links are generated in two 
  circumstances. First, when a DOI is mentioned like "doi: 10.1080/01621459.1984.10478080" where
  a link is inserted to https://www.doi.org/10.1080/01621459.1984.10478080. Similarly, any text
  which starts with http:// or https:// will become a link to the URL in text up until a non-URL
  encoded whitespace character (ie up until a space but not a %20 so that %20 is included in the
  URL and link text).

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


if __name__ == '__main__':
  main()
