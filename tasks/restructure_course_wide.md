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

**Component successfully completed. Implementation meets all project standards and requirements.**

Successfully created Jinja2-based templating system for course_wide markdown files. The implementation properly extracts shared markdown structure into base.md and uses template inheritance for syllabus, manual, and rubric pages. The render.py script follows the same patterns as HTML rendering and produces clean, well-formatted markdown output with proper trailing whitespace cleanup.

**Key accomplishments**:
- Base template correctly implements shared structure (Other formats, See Also, Works Cited sections)
- Each page template properly extends base.md with correct block overrides
- License handling is correctly differentiated (syllabus uses ## License with separator, manual uses ### License without separator, rubric has no license)
- render.py updated with three new markdown rendering functions following existing code patterns
- The 'all' command correctly renders both HTML and markdown
- build.sh properly excludes template files (*_template.md, base.md) from mooc output
- Code quality verified: proper module docstrings, consistent style, follows CONTRIBUTING.md guidelines
- All rendered markdown files end with proper newlines and have trailing whitespace cleaned up (improvement over originals)
- Template files successfully excluded from build output directory

SAFE TO PROCEED

### Component 3: Course sections YAML

**Component successfully completed. Implementation meets all project standards and requirements.**

Successfully created syllabus.yml containing all 7 course sections (Hello through Build) and all 27 lessons (days 1-27, including special formats 8/9, 26.1, 26.2). The implementation correctly preserves all lesson data from the original syllabus including reading URLs, classroom material with inline HTML links, activities, and special separator handling for multiple readings (", ", ". ", " or "). Templates updated to render from YAML data with proper grouping by section.

**Key accomplishments**:
- YAML file contains complete, accurate data for all sections and lessons
- All reading URLs are correct and properly linked
- Classroom material preserves inline HTML links (e.g., day 5 Tufte references)
- Special separators correctly implemented (day 17, 19, 21, 23)
- Special day number formats handled (8/9, 26.1, 26.2)
- render.py updated with load_syllabus_data() function and YAML import
- Both HTML and markdown templates render correctly from YAML
- Full build successful with output matching original structure
- Code quality verified: all functions have docstrings, YAML syntax valid, line lengths comply with guidelines (2 lines at 101 chars, within acceptable tolerance for natural language text)
- Manual and rubric pages unaffected and render correctly

SAFE TO PROCEED

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
