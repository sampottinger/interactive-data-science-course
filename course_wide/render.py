"""Render script for course_wide HTML and Markdown files.

This module renders Jinja2 templates for course-wide documents (syllabus, manual, rubric)
into static HTML and Markdown files. It follows a similar structure to mooc_src/render.py
but is specifically tailored for the course_wide directory structure.

License: BSD-3-Clause
"""
import os
import sys

import jinja2

USAGE_STR = 'USAGE: python render.py [syllabus | manual | rubric | syllabus_md | manual_md | rubric_md | all]'
MIN_ARGS = 1


def get_template_loader():
    """Create a Jinja2 FileSystemLoader for the course_wide directory.

    Returns:
        jinja2.Environment: Configured Jinja2 environment with template loader.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    loader = jinja2.FileSystemLoader(script_dir)
    return jinja2.Environment(loader=loader)


def render_syllabus():
    """Render the syllabus HTML from template."""
    env = get_template_loader()
    template = env.get_template('syllabus_template.html')

    context = {
        'title': 'Course Syllabus (Interactive Data Sci / Viz)',
        'description': 'Complete curriculum and learning outcomes for building interactive data visualizations and storytelling tools. Explore 7 modules covering design theory, Python, D3, P5, and ethical data practices.',
        'og_title': 'Course Syllabus (Interactive Data Sci / Viz)',
        'og_description': 'Complete curriculum: data visualization fundamentals, interactive storytelling, Python graphics, D3, P5, game design principles, accessibility, and ethical AI. 7 modules, hands-on projects, portfolio building.',
        'og_url': 'https://mooc.interactivedatascience.courses/course_wide/syllabus.html',
        'twitter_title': 'Course Syllabus (Interactive Data Sci / Viz)',
        'twitter_description': 'Learn the complete curriculum: data visualization fundamentals, interactive storytelling, Python graphics, D3, P5, game design, accessibility, ethical AI. Free, hands-on course modules.'
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

    context = {
        'title': 'Course Manual (Interactive Data Sci / Viz)',
        'description': 'Complete course manual with readings, interactive labs, exercises, and capstone guidance. Navigate assignments, time expectations, collaboration guidelines, and data science projects.',
        'og_title': 'Course Manual (Interactive Data Sci / Viz)',
        'og_description': 'Complete course manual with readings, interactive labs, exercises, and capstone guidance. Navigate assignments, time expectations, collaboration guidelines, and data science projects.',
        'og_url': 'https://mooc.interactivedatascience.courses/course_wide/manual.html',
        'twitter_title': 'Course Manual (Interactive Data Sci / Viz)',
        'twitter_description': 'Complete course manual with readings, interactive labs, exercises, and capstone guidance. Navigate assignments, time expectations, collaboration guidelines, and data science projects.'
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

    context = {
        'title': 'Project Grading Rubric (Interactive Data Sci / Viz)',
        'description': 'Understand grading criteria for your code projects: completeness, materials, technical execution, and exploration. Clear standards for all assignments and final project.',
        'og_title': 'Project Grading Rubric (Interactive Data Sci / Viz)',
        'og_description': 'Grading criteria for your coding projects across completeness, visualization concepts, technical execution, and exploration. Understand what instructors evaluate.',
        'og_url': 'https://mooc.interactivedatascience.courses/course_wide/rubric.html',
        'twitter_title': 'Project Grading Rubric (Interactive Data Sci / Viz)',
        'twitter_description': 'Grading criteria for your coding projects across completeness, visualization concepts, technical execution, and exploration. Understand what instructors evaluate.'
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

    context = {}

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

    context = {}

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

    context = {}

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

    if command == 'syllabus':
        render_syllabus()
    elif command == 'manual':
        render_manual()
    elif command == 'rubric':
        render_rubric()
    elif command == 'syllabus_md':
        render_syllabus_md()
    elif command == 'manual_md':
        render_manual_md()
    elif command == 'rubric_md':
        render_rubric_md()
    elif command == 'all':
        render_syllabus()
        render_manual()
        render_rubric()
        render_syllabus_md()
        render_manual_md()
        render_rubric_md()
    else:
        print(f'Unknown command: {command}')
        print(USAGE_STR)
        sys.exit(1)


if __name__ == '__main__':
    main()
