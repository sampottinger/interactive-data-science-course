# Skills Labs

This directory contains hands-on tutorials and focused instruction on implementation skills for the Interactive Data Science and Visualization course. These labs may be used for a flipped classroom structure which prioritizes hands-on interaction with instructor support.

## Directory Structure
The labs are organized into six lab directories, each containing YAML source files. Specifically, each lab directory contains:

- `index.yml`: Lab metadata (name, lesson number, subheader)
- Tutorial YAML files: Named with numeric prefix and descriptive name (e.g., `01_python_introduction.yml`)

## YAML Format
YAML files both define a lab which contains one or more tutorials and the tutorials themselves.

### Lab Index (index.yml)
Each lab directory's `index.yml` contains:

| Field     | Required | Description                                             | Type   |
|-----------|----------|---------------------------------------------------------|--------|
| name      | Yes      | Lab name (e.g., "Hello Python")                         | string |
| subheader | Yes      | Brief markdown description of lab focus                 | string |
| lesson    | Yes      | Associated lesson number from main course               | int    |

### Tutorial Files

Each tutorial YAML file defines a single tutorial with the following structure:

| Field     | Required | Description                                                              | Type   |
|-----------|----------|--------------------------------------------------------------------------|--------|
| name      | Yes      | Human-readable tutorial name                                             | string |
| file      | Yes      | Base filename for output (e.g., "python_intro" generates python_intro.html and python_intro.md) | string |
| header    | Yes      | HTML content for tutorial header/introduction                            | html   |
| sections  | Yes      | List of tutorial sections (see below)                                    | list   |
| citations | No       | List of citations with "text" and optional "available" (URL)             | list   |

#### Section Structure
Each section in the `sections` list contains:

| Field      | Required | Description                                      | Type                |
|------------|----------|--------------------------------------------------|---------------------|
| name       | Yes      | Anchor ID for linking to section                 | string              |
| short      | Yes      | Section heading                                  | string              |
| long       | Yes      | Brief description of section content             | string              |
| html       | One of   | Section content in HTML format                   | html                |
| markdown   | One of   | Section content in Markdown format               | markdown            |
| blockstyle | No       | Code block style: "pre" (default) or "blockquote" | string              |

ach section must contain exactly one of `html` or `markdown` for content. However, both cannot be present simultaneously.

#### Best Practices
When writing YAML, please try to observe the following conventions:

- Use `|` (literal block scalar) for `header` and multi-line `html`/`markdown` content
- Use `>` (folded scalar) for simple multi-line strings like `subheader`
- Keep lines to 100 characters or fewer (except long URLs)
- Markdown content supports fenced code blocks with triple backticks
- Use `blockstyle: blockquote` to render code blocks as blockquotes instead of `<pre>` tags

Here is an example of these practices in mind:

```yaml
name: Python Introduction
file: python_intro.html
header: |
  Hello! This tutorial introduces Python fundamentals.
sections:
  - name: setup
    short: Getting set up for Python
    long: Learn how to set up your Python environment
    markdown: |
      Use [Jupyter Lite](https://jupyter.org/try-jupyter/lab/) to get started.

      ```python
      print("Hello, world!")
      ```
  - name: conclusion
    short: Conclusion
    long: Wrap up and next steps
    markdown: |
      You've learned Python basics. Continue to the next tutorial.
citations:
  - text: C. Swaroop, A Byte of Python. 2024. [Online].
    available: https://python.swaroopch.com
```

## Building

To build all lab tutorials, run:

```bash
bash render.sh
```

Or from the repository root:

```bash
cd labs
bash render.sh
```

The render script processes all tutorial YAML files and generates:

- HTML files for web viewing
- Markdown files for accessibility
- An index.html listing all available labs

## Generated Output
Generated tutorials include:

- Skip link for accessibility
- Collapsible table of contents
- Structured sections with anchors
- Code blocks in `<pre>` tags (or `<blockquote>` if blockstyle specified)
- Citations section
- Footer with Creative Commons license information
- Navigation links back to labs index and MOOC homepage

## Additional Information
For detailed contributing guidelines, coding standards, and project structure, see the main [CONTRIBUTING.md](../CONTRIBUTING.md) in the repository root.
