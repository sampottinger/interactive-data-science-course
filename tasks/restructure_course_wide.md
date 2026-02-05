# Restructure Course-Wide

Reduce duplication in HTML files in the `course_wide` directory and pull out some structured elements.

## Motivation

Right now we have a lot of HTML copy / pasted between the course_wide elements. To improve re-use, we should have common elements in root templates for Jinja and pull out some specific structured elements into YAML files similar to `mooc_src`.

## Components

### Component 1: Clean up shared HTML

**Component completed successfully. All quality checks passed. Code follows project standards.**

Successfully created Jinja2-based templating system for course_wide HTML files. The implementation properly extracts shared HTML elements into base.html and uses template inheritance for syllabus, manual, and rubric pages. The render.py script follows patterns from mooc_src/render.py and produces clean, properly formatted HTML output.

**Key accomplishments**:
- Base template correctly implements all shared HTML structure (head, meta tags, skip link, header, footer)
- All three page templates properly extend base.html with correct block overrides
- License text is accurate for each page (CC-BY International 4.0 for syllabus, CC-BY-NC 4.0 for manual, CC-BY 4.0 for rubric)
- Build process successfully renders templates and copies only final output files
- Code quality verified: proper docstrings, consistent style with mooc_src/render.py, clean output formatting
- All rendered HTML files end with proper newlines and maintain consistent indentation

SAFE TO PROCEED

### Component 2: Clean up shared markdown

- **Status**: Not started
- **Files to create/modify**:
  - `course_wide/base.md` - New base Jinja2 template for markdown output
  - `course_wide/syllabus_template.md` - Jinja2 markdown template for syllabus
  - `course_wide/manual_template.md` - Jinja2 markdown template for manual
  - `course_wide/rubric_template.md` - Jinja2 markdown template for rubric
  - `course_wide/render.py` - Update to also render markdown templates
  - `course_wide/render.sh` - Update to include markdown rendering

**Description**: Extend `render.py` in `course_wide` to also render markdown. Create a `base.md` Jinja2 template that provides shared structure across the markdown versions. Common elements include the "Other formats" line, "See Also" section, and "Works Cited" / license footer. The markdown templates should extend `base.md` and fill in page-specific content.

### Component 3: Course sections YAML

- **Status**: Not started
- **Files to create/modify**:
  - `course_wide/syllabus.yml` - New YAML file with course section lesson data
  - `course_wide/syllabus.html` (template) - Update to render lesson tables from YAML
  - `course_wide/syllabus_template.md` - Update to render lesson tables from YAML
  - `course_wide/render.py` - Update to load and pass YAML data to templates

**Description**: Extract the course sections lesson data from the syllabus into a `syllabus.yml` file. Skip lessons 0 and 26 (optional fully online). Structure:

```yaml
lessons:
  - lesson: 1
    class:
      - text: 4 perspectives on data visualization.
    activity:
      - text: Async introductions.
  - lesson: 2
    class:
      - text: Trying out the 4 perspectives on 4 examples.
    activity:
      - text: Example visualization 1
    reading:
      - text: Media for Thinking the Unthinkable (Victor 2013)
        url: https://vimeo.com/67076984
```

The class, activity, and reading tags should be interpreted as HTML. For readings with URLs, the URL should extend to the entire text as a link, e.g.:
```yaml
  - text: Examples of problematic graphs (Tufte 2001)
    url: https://www.edwardtufte.com/book/the-visual-display-of-quantitative-information/
```

Update rendering for both HTML and markdown templates to use the YAML data.

### Component 4: Link to lesson from syllabus and reading by day

- **Status**: Not started
- **Files to create/modify**:
  - `course_wide/syllabus.yml` - Remove root `url` field from lessons
  - `course_wide/syllabus.html` (template) - Link day number to lesson page
  - `course_wide/syllabus_template.md` - Link day number to lesson page
  - `course_wide/manual.html` (template) - Render reading table by day from YAML
  - `course_wide/manual_template.md` - Render reading table by day from YAML

**Description**: Two changes:
1. Change the day number in the syllabus course sections tables to link to the lesson page (e.g., day 5 links to `/lesson5.html`). Remove the root `url` field from each lesson in `syllabus.yml` since it's obvious from the lesson/day number.
2. Switch the reading table in the manual from week-based (Week, Day 1, Day 2) to day-based. Use reading data from `syllabus.yml`, rendering from the same YAML file.

### Component 5: Rubric in YAML

- **Status**: Not started
- **Files to create/modify**:
  - `course_wide/syllabus.yml` - Add rubric sections and items data
  - `course_wide/rubric.html` (template) - Render rubric tables from YAML
  - `course_wide/rubric_template.md` - Render rubric tables from YAML
  - `course_wide/render.py` - Pass rubric data to rubric templates

**Description**: Create a root object in `syllabus.yml` next to `lessons` (below it). Encode the rubric criteria:

```yaml
rubric:
  sections:
    - name: Completeness
      weight: 30%
    - name: Materials / Concepts
      weight: 30%
    - name: Tech / Program Correct
      weight: 20%
    - name: Explore / Express
      weight: 20%
  items:
    - category: Completeness
      criterion: Submission follows instructions.
      starts: Assignment 7 (Creative Code 1)
    - category: Completeness
      criterion: Appropriate / required density.
      starts: Assignment 9 (Census 1)
    ...
```

Update rubric HTML and markdown templates to render from this YAML data.

### Component 6: Update docs

- **Status**: Not started
- **Files to modify**:
  - `README.md` - Update to reflect course_wide rendering changes
  - `CONTRIBUTING.md` - Update if needed to reflect new structure

**Description**: Update `README.md` and, if needed, `CONTRIBUTING.md` to reflect changes from this task. This includes documenting the new `course_wide/render.py`, the `syllabus.yml` data file, the Jinja2 template structure for course_wide, and any changes to the build process.

### Component 7: Update build scripts and GitHub Actions

- **Status**: Not started
- **Files to modify**:
  - `.github/workflows/deploy.yaml` - Update Python checks and upload steps
  - `build.sh` - Any final adjustments needed

**Description**: Update build infrastructure to account for the new `course_wide/render.py` and template files:
1. Update `.github/workflows/deploy.yaml` to include `course_wide/*.py` in pyflakes and pycodestyle checks (currently only checks `mooc_src/*.py`).
2. Fix the "Upload course wide" step in deploy.yaml - it currently uploads raw `./course_wide/*` directly, which would now include template files (`*_template.html`, `*_template.md`, `base.html`, `base.md`, `render.py`, `render.sh`, `syllabus.yml`). It should upload from `./mooc/course_wide/` instead since the build step already copies only the appropriate files there.
3. Verify the full build pipeline works end-to-end.
