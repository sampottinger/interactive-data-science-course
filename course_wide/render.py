"""Render script for course_wide HTML and Markdown files.

This module renders Jinja2 templates for course-wide documents
(syllabus, manual, rubric) into static HTML and Markdown files.
It follows a similar structure to lecture/render.py but is
specifically tailored for the course_wide directory structure.

License: BSD-3-Clause
"""
import os
import sys

import jinja2
import yaml

USAGE_ARGS = [
  'syllabus',
  'manual',
  'rubric',
  'syllabus_md',
  'manual_md',
  'rubric_md',
  'all'
]
USAGE_ARGS_STR = ' | '.join(USAGE_ARGS)
USAGE_STR = f'USAGE: python render.py [{USAGE_ARGS_STR}]'
MIN_ARGS = 1


def get_template_loader():
    """Create a Jinja2 FileSystemLoader for the course_wide directory.

    Returns:
        jinja2.Environment: Configured Jinja2 environment with template loader.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    loader = jinja2.FileSystemLoader(script_dir)
    return jinja2.Environment(loader=loader)


def load_course_data():
    """Load course data from course_wide.yml.

    Returns:
        dict: Course data containing sections, lessons, and rubric information.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    course_wide_path = os.path.join(script_dir, 'course_wide.yml')

    with open(course_wide_path, 'r') as f:
        data = yaml.safe_load(f)

    return data


def render_syllabus():
    """Render the syllabus HTML from template."""
    env = get_template_loader()
    template = env.get_template('syllabus_template.html')

    course_data = load_course_data()

    meta = course_data['meta']['syllabus']
    context = {
        'title': meta['title'].strip(),
        'description': meta['description'].strip(),
        'og_title': meta['og_title'].strip(),
        'og_description': meta['og_description'].strip(),
        'og_url': meta['og_url'].strip(),
        'twitter_title': meta['twitter_title'].strip(),
        'twitter_description': meta['twitter_description'].strip(),
        'sections': course_data['sections'],
        'lessons': course_data['lessons']
    }

    result = template.render(**context)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, 'syllabus.html')
    with open(output_path, 'w') as f:
        f.write(result)
        if not result.endswith('\n'):
            f.write('\n')

    print('Rendered syllabus.html')


def render_manual():
    """Render the manual HTML from template."""
    env = get_template_loader()
    template = env.get_template('manual_template.html')

    course_data = load_course_data()

    meta = course_data['meta']['manual']
    context = {
        'title': meta['title'].strip(),
        'description': meta['description'].strip(),
        'og_title': meta['og_title'].strip(),
        'og_description': meta['og_description'].strip(),
        'og_url': meta['og_url'].strip(),
        'twitter_title': meta['twitter_title'].strip(),
        'twitter_description': meta['twitter_description'].strip(),
        'lessons': course_data['lessons']
    }

    result = template.render(**context)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, 'manual.html')
    with open(output_path, 'w') as f:
        f.write(result)
        if not result.endswith('\n'):
            f.write('\n')

    print('Rendered manual.html')


def render_rubric():
    """Render the rubric HTML from template."""
    env = get_template_loader()
    template = env.get_template('rubric_template.html')

    course_data = load_course_data()

    meta = course_data['meta']['rubric']
    context = {
        'title': meta['title'].strip(),
        'description': meta['description'].strip(),
        'og_title': meta['og_title'].strip(),
        'og_description': meta['og_description'].strip(),
        'og_url': meta['og_url'].strip(),
        'twitter_title': meta['twitter_title'].strip(),
        'twitter_description': meta['twitter_description'].strip(),
        'rubric_sections': course_data['rubric']['sections'],
        'rubric_items': course_data['rubric']['items']
    }

    result = template.render(**context)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, 'rubric.html')
    with open(output_path, 'w') as f:
        f.write(result)
        if not result.endswith('\n'):
            f.write('\n')

    print('Rendered rubric.html')


def render_syllabus_md():
    """Render the syllabus Markdown from template."""
    env = get_template_loader()
    template = env.get_template('syllabus_template.md')

    course_data = load_course_data()

    context = {
        'sections': course_data['sections'],
        'lessons': course_data['lessons']
    }

    result = template.render(**context)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, 'syllabus.md')
    with open(output_path, 'w') as f:
        f.write(result)
        if not result.endswith('\n'):
            f.write('\n')

    print('Rendered syllabus.md')


def render_manual_md():
    """Render the manual Markdown from template."""
    env = get_template_loader()
    template = env.get_template('manual_template.md')

    course_data = load_course_data()

    context = {
        'lessons': course_data['lessons']
    }

    result = template.render(**context)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, 'manual.md')
    with open(output_path, 'w') as f:
        f.write(result)
        if not result.endswith('\n'):
            f.write('\n')

    print('Rendered manual.md')


def render_rubric_md():
    """Render the rubric Markdown from template."""
    env = get_template_loader()
    template = env.get_template('rubric_template.md')

    course_data = load_course_data()

    context = {
        'rubric_sections': course_data['rubric']['sections'],
        'rubric_items': course_data['rubric']['items']
    }

    result = template.render(**context)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, 'rubric.md')
    with open(output_path, 'w') as f:
        f.write(result)
        if not result.endswith('\n'):
            f.write('\n')

    print('Rendered rubric.md')


def main():
    """Main entrypoint for the course_wide renderer."""
    if len(sys.argv) < MIN_ARGS + 1:
        print(USAGE_STR)
        sys.exit(1)

    command = sys.argv[1]

    command_strategies = {
        'syllabus': [render_syllabus],
        'manual': [render_manual],
        'rubric': [render_rubric],
        'syllabus_md': [render_syllabus_md],
        'manual_md': [render_manual_md],
        'rubric_md': [render_rubric_md],
        'all': [
            render_syllabus,
            render_manual,
            render_rubric,
            render_syllabus_md,
            render_manual_md,
            render_rubric_md
        ]
    }

    strategies = command_strategies.get(command)
    if strategies:
        for strategy in strategies:
            strategy()
    else:
        print(f'Unknown command: {command}')
        print(USAGE_STR)
        sys.exit(1)


if __name__ == '__main__':
    main()
