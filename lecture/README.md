# Lecture Materials

This directory contains the lesson materials for the Interactive Data Science and Visualization MOOC. These traditional lecture-style lessons mix classic instruction with shorter hands-on activities. Specifically, these correspond to individual lessons originally taught in the classroom.

## YAML Format
The course is broken into multiple sections represented as directories containing the individual lessons.

### Section Index (index.yml)
Each section directory's `index.yml` contains metadata:

| Field    | Required | Description                                      | Type   |
|----------|----------|--------------------------------------------------|--------|
| name     | Yes      | Section name (e.g., "Hello", "Primitives")       | string |
| tagline  | Yes      | One-sentence tagline for the section             | string |
| detailed | Yes      | Longer description of section content and goals  | string |

Use `>` (folded scalar) for multi-line `detailed` content. Keep lines to 100 characters or fewer.

### Lesson Files
Each lesson YAML file (named with numeric prefix like `00_hello_preface.yml`) represents a single lesson:

| Field          | Required    | Description                                                              | Type   |
|----------------|-------------|--------------------------------------------------------------------------|--------|
| number         | Yes         | 0-indexed lesson ID unique across the entire course                      | int    |
| name           | Yes         | Human-readable short name (used in index)                                | string |
| text           | Yes         | Short description of the lesson                                          | html   |
| materials_pdf  | Recommended | Flag indicating PDF version availability                                 | bool   |
| materials_pptx | Recommended | Flag indicating PowerPoint version availability                          | bool   |
| materials_md   | Recommended | Flag indicating markdown version availability                            | bool   |
| citations      | Recommended | List of citation objects (see below)                                     | list   |
| assignment     | No          | Long-form description of out-of-lesson exercise (homework)               | html   |
| reading        | No          | Long-form description of out-of-lesson reading                           | html   |
| links          | No          | List of links mentioned in lesson (with "text" and "url" fields)         | list   |
| video          | No          | Vimeo ID for lesson video                                                | int    |

Note that `assignment` is for exercises without a work product submission, while `reading` is for assigned readings. Both are distinct from `links`, which provide access to materials needed during the lesson itself.

### Citations
Citations are provided as inline YAML lists. Each citation contains:

| Field     | Required    | Description                                           | Type   |
|-----------|-------------|-------------------------------------------------------|--------|
| text      | Yes         | Citation body (IEEE-derivative format recommended)    | string |
| doi       | No          | DOI identifier (e.g., "10.1080/01621459.1984.10478080") | string |
| available | No          | URL where resource can be accessed                    | string |

Though we use an IEEE-like format, please do not include "Available:" or "doi:" prefix in `text` as these are generated automatically. That said, a citation may have `doi`, `available`, both, or neither. Additionally, for `text` values exceeding 100 characters, use `>` (folded scalar) and keep lines under 100 characters. However, do not break URLs across lines.

### Best Practices
Please try to maintain the following general practices:

- HTML fields should use `>` (folded scalar) for multi-line content
- Keep lines to 100 characters or fewer (except very long URLs)
- Remove non-supported or deprecated fields (such as `slides`)
- Specify recommended fields even if using default values
- Don't include optional fields if using default values
- Remove leading/trailing whitespace unless it improves readability
- Avoid JSON object notation

That in mind, here is a complete lesson:

```yaml
number: 1
name: Hello Visualization
video: 1047306328
materials_pdf: true
materials_pptx: true
materials_md: true
text: >
  A detailed overview of the course which introduces central concepts,
  what you will learn, and what we will be doing together.
assignment: >
  Please write about 4 sentences reflecting on what you are hoping to
  gain from the course.
reading: >
  Watch the excellent <a href="https://vimeo.com/67076984">Media for
  Thinking the Unthinkable lecture</a> by Bret Victor.
links:
  - text: Course Homepage
    url: https://mooc.interactivedatascience.courses/
citations:
  - text: >
      J. Snow, On the mode of communication of cholera. London: John
      Churchill, 1855.
    available: https://archive.org/details/b28985266/page/n57/mode/2up
```

## Supporting Materials
In addition to the individual lesson information in the YAML file, supporting materials are stored in `lecture/support/`:

- **md/**: Markdown versions of lessons (required for all lessons). Files named `lesson00.md`, `lesson01.md`, etc.
- **pdf/**: PDFs like slide decks with title slide and CC license slide
- **pptx/**: PowerPoint source files (optional)
- **web/**: Web assets used across multiple lessons (images, CSS, JavaScript)
- **misc/**: Miscellaneous files for specific lesson activities (datasets, supplemental documents)

Each markdown lesson (`lesson00.md`) should include:

1. **Header**: Lesson number and name with very brief description
2. **Objective**: 1-4 sentences describing the lesson's objective and purpose
3. **Outline**: Brief description followed by subsections with short descriptions and bullet points
4. **Take Aways**: 1 sentence overview followed by bullet points
5. **Citations**: Citations (may differ from YAML citations if needed for assignments/activities)

These markdown files are also rendered in the lesson HTML page in the course website under a `details` tag.

## Building
To build all lessons, run from the `lecture` directory:

```bash
bash render.sh
```

Or from the repository root:

```bash
cd lecture
bash render.sh
```

The render script processes all lesson YAML files and section index files to generate the course website structure.

## Additional Information
For detailed contributing guidelines, coding standards, and project structure, see the main [CONTRIBUTING.md](../CONTRIBUTING.md) in the repository root.
