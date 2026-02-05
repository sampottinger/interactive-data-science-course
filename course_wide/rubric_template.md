{% extends "base.md" %}

{% block title %}Code Projects Rubric{% endblock %}

{% block description %}
Across the course, you will be asked to submit code for 7 regular assignments and the final project. This rubric describes how these exercises are scored. Specifically, as we gain more skills, we can add more criteria to our rubric until reaching the final!
{% endblock %}

{% block other_formats %}[HTML version](rubric.html) | [Markdown version](rubric.md) (you are here) | [PDF version](rubric.pdf) (from UC Berkeley Spring 2025 teaching){% endblock %}

{% block content %}
## Category Weights

There are 4 categories of criteria with the weighting below. This weighting is maintained regardless of assignment.

| **Category**           | **Weight** |
|------------------------|------------|
{% for section in rubric_sections %}| {{ section.name }}{{ ' ' * (22 - section.name|length) }} | {{ section.weight }}{{ ' ' * (10 - section.weight|length) }} |
{% endfor %}

## Rubric Criteria by Assignment

The goal of this rubric really is to help structure feedback, provide ideas to keep in mind as learners build work, and help you understand what instructors may choose to focus on. Each individual criterion is worth one point within its category.

| **Category**  | **Criterion**                                                      | **First Assignment**                  |
|---------------|--------------------------------------------------------------------|---------------------------------------|
{% for item in rubric_items %}| {{ item.category }}{{ ' ' * (13 - item.category|length) }} | {{ item.criterion }}{{ ' ' * (66 - item.criterion|length) }} | {{ item.starts }}{{ ' ' * (37 - item.starts|length) }} |
{% endfor %}

## Notes

Some take-aways:

- Each criterion within a category is worth one point.
- Criteria accumulate as the course progresses.
- Once a criterion is introduced, it continues to apply in subsequent assignments.
{% endblock %}

{% block see_also_links %}
- [Course Manual](/course_wide/manual.html) - Detailed guidance for students and instructors
- [Course Syllabus](/course_wide/syllabus.html) - Formal curriculum and weekly schedule
{% endblock %}
{% block works_cited %}{% endblock %}
