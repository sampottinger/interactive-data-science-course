# Course-Wide Materials
This directory contains course-wide materials that apply across all lessons of the Interactive Data Science and Visualization course. These include the syllabus, course manual, and grading rubric.

## YAML Structure
The `course_wide.yml` file contains all structured data for course-wide materials:

### Meta Section
Contains information for metadata tags including those for social media. Here is the syllabus:

```yaml
meta:
  syllabus:
    title: Page title
    description: Meta description
    og_title: Open Graph title
    og_description: Open Graph description
    og_url: Canonical URL
    twitter_title: Twitter card title
    twitter_description: Twitter card description
```

Similar metadata blocks exist for `manual` and `rubric`.

### Sections
List of course sections:

| Field    | Required | Description                                      | Type   |
|----------|----------|--------------------------------------------------|--------|
| name     | Yes      | Section name (e.g., "Hello", "Primitives")       | string |
| number   | Yes      | Section number (1-7)                             | int    |
| tagline  | Yes      | One-sentence tagline for the section             | string |
| detailed | Yes      | Longer description of section content and goals  | string |

```yaml
sections:
  - name: Hello
    number: 1
    tagline: Begin with an initial exploration of key ideas.
    detailed: >
      We start our journey together by motivating why data visualization
      is useful...
```

### Lessons

List of daily lessons nested under sections:

| Field    | Required | Description                                  | Type   |
|----------|----------|----------------------------------------------|--------|
| lesson   | Yes      | Day number (0-indexed)                       | int    |
| section  | Yes      | Section name this lesson belongs to          | string |
| reading  | No       | List of reading items for this lesson        | list   |
| class    | No       | List of class activity items                 | list   |
| activity | No       | List of homework/out-of-class activity items | list   |

Each item in `reading`, `class`, and `activity` lists must use either `html` or `markdown` for content. Only one content attribute is allowed per item (must use ither html or markdown but not both). Here is a full example:

```yaml
lessons:
  - lesson: 1
    section: Hello
    reading:
      - markdown: >
          [Media for Thinking the Unthinkable
          (Victor 2013)](https://vimeo.com/67076984)
    class:
      - markdown: 4 perspectives on data visualization.
    activity:
      - markdown: Async introductions.
```

For items requiring HTML (multiple links, complex formatting), use the `html` attribute:

```yaml
  - lesson: 10
    section: Combination
    reading:
      - html: >
          <a href="https://example.com/paper1">Paper 1 (Author 2020)</a> and
          <a href="https://example.com/paper2">Paper 2 (Author 2021)</a>
```

### Rubric
List of grading criteria organized by category:

| Field     | Required | Description                                          | Type   |
|-----------|----------|------------------------------------------------------|--------|
| category  | Yes      | Rubric category (e.g., "Completeness", "Materials")  | string |
| criterion | Yes      | Specific grading criterion                           | string |
| starts    | Yes      | First assignment where this criterion applies        | string |

```yaml
rubric:
  - category: Completeness
    criterion: All parts attempted.
    starts: Assignment 7 (Creative Code 1)
  - category: Materials
    criterion: Readable use of preattentive features.
    starts: Assignment 7 (Creative Code 1)
```

At time of writing, the categories are:

- **Completeness**: Assignment completion and ethical representation
- **Materials**: Visual design principles (preattentive features, Gestalt, encodings, affordances, etc.)
- **Tech**: Technical execution (code quality, documentation, accessibility)
- **Explore**: User experience (interpretability, hierarchy, domain understanding, user agency)

## Templates
The course-wide materials use Jinja2 templates with template inheritance:

- **Base templates** (`base.html`, `base.md`): Shared structure with blocks for content
- **Page templates**: Extend base templates and override specific blocks
- **Variables**: Templates receive data from `course_wide.yml` (sections, lessons, rubric, meta)

This in mind, use the following procedure to modify course-wide materials:

1. **Edit structured data**: Update `course_wide.yml` to change sections, lessons, or rubric
2. **Edit templates**: Modify `*_template.html` or `*_template.md` files to change page structure
3. **Edit base templates**: Update `base.html` or `base.md` to change shared elements
4. **Rebuild**: Run `bash render.sh` to regenerate output files

## Best Practices
Please try to observe the following YAML best practices:

- Use `>` (folded scalar) for multi-line strings
- Keep lines to 100 characters or fewer (exceptions for long URLs)
- Avoid trailing whitespace
- Use consistent indentation (2 spaces)
- Use Markdown format for simple prose and single links
- Use HTML format for items with multiple inline citations or complex formatting

## Building
To build all course-wide materials, run from the `course_wide` directory:

```bash
bash render.sh
```

Or from the repository root:

```bash
cd course_wide
bash render.sh
```

The render script:
1. Loads data from `course_wide.yml`
2. Processes content attributes (`html` or `markdown`) and converts to `text` field
3. Renders templates with processed data
4. Generates HTML and Markdown output files

## Generated Output
The build process creates:

- **syllabus.html** and **syllabus.md**: Complete course curriculum with sections and daily lessons
- **manual.html** and **manual.md**: Detailed course manual with readings, labs, and assignment guidance
- **rubric.html** and **rubric.md**: Grading criteria for all assignments

PDF versions are maintained separately from a teaching of the course at UC Berkeley with graphic design elements and updated as needed.

## Additional Information
For detailed contributing guidelines, coding standards, and project structure, see the main [CONTRIBUTING.md](../CONTRIBUTING.md) in the repository root.
