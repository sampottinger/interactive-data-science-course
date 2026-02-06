# Contributing to IDSV
Thank you for contributing to Interactive Data Science and Visualization! Your time and efforts can help ensure this open educational resource (OER) continues to grow and serve more learners into the future. We appreciate you, your ideas, and your time. Before starting, please review the following.

## Philosophy
Interactive Data Science and Visualization is intended as a hands-on exploration of information design and explorable digital media.

### Inclusive
It is important that the course not only discusses ethics and accessibility but is itself ethical and accessible. Towards that end, all videos must have manually confirmed captions in English at minimum. Furthermore, we strive to use language which is inviting and inclusive of learners from many backgrounds.

### Flexible
The structure of instruction should consider that folks may be joining for different reasons where some use the full class and others take individual pieces. Sections of the course may build on each other but reasonable steps should be taken to allow for modularity where possible.

### Open
The course must be fully open with code released under BSD and non-code materials in CC-BY-NC 4.0. The CC-BY-NC 4.0 is used due to some incorporated educational materials' licensing. All software should be open when possible.

### Holistic
Data visualization is science and art. We are committed to multi-disciplinary instruction which pulls from multiple perspectives and which treats this topical area as both a question of implementation (programming / engineering) and design with balanced instruction in both. We believe this necessarily involves instruction which pulls from humanities and social sciences.

### Experiential
It is strongly encouraged that all full lessons include a hands-on activity to allow for demonstration of concepts. Some exceptions are made for lessons which are logistically oriented.

## Limitations
We will continue to strive towards our objectives above. However, we recognize the following limitations at this time:

 - We currently only offer instruction and materials in English.
 - We allow use of Vimeo as practical for hosting of larger video files with captions for accessibility.
 - Use of proprietary AI assistants for the AI section of the course is currently allowed while open weights AI models / infrastructure improve.
 - We remain committed to primarily teaching through Python-based exercises.

These limitations are largely driven by resource constraints and we welcome new volunteers via GitHub issue to help us further improve! However, please understand that we may keep these scope constraints depending on current community capacity.

## Structure
There are two major areas of the course materials: the MOOC source and the skills labs.

### MOOC Source
This includes the "lecture" class materials. All lessons must have, at minimum, a yaml entry. However, other materials may appear as well. These materials are rendered into a content management system with formalized / standardized templates.

The MOOC source is organized in `lecture/` with the following structure:
 - `lessons/`: Section directories containing per-lesson YAML files and section metadata
 - `support/`: Supporting materials organized by type (md, pdf, pptx, web, misc)
 - `citations/`: Citation files for lessons

#### YAML
Course lessons are organized in the `lecture/lessons/` directory. This
directory contains numbered section subdirectories (e.g., `01_Hello`,
`02_Primitives`), each containing individual YAML files for each lesson
and an `index.yml` file with section metadata. Each lesson YAML file
represents a single lesson as a top-level mapping. Lesson files are named with a numeric prefix
followed by a descriptive name (e.g., `00_hello_preface.yaml`,
`01_hello_visualization.yaml`).

Each section directory must also contain an `index.yml` file with section
metadata:

| **Field** | **Required** | **Purpose**                                           | **Type** |
| --------- | ------------ | ----------------------------------------------------- | -------- |
| name      | Yes          | The section name (e.g., "Hello", "Primitives").       | string   |
| tagline   | Yes          | A brief one-sentence tagline for the section.         | string   |
| detailed  | Yes          | Longer description of the section content and goals.  | string   |

The `detailed` field should use `>` (folded scalar) for multi-line content
and follow the same line length guidelines as lesson YAML files (100
characters or fewer).

Each lesson may have:

| **Field**      | **Required** | **Purpose**                                                                                              | **Type** |
| -------------- | ------------ | -------------------------------------------------------------------------------------------------------- | -------- |
| number         | Yes          | The 0-indexed ID of the lesson unique across the course.                                                 | int      |
| name           | Yes          | Human readable short name (used in index).                                                               | string   |
| text           | Yes          | Short description of the lesson.                                                                         | html     |
| materials_pdf  | Recommended  | Flag indicating if a PDF version of the lesson is available.                                             | bool     |
| materials_pptx | Recommended  | Flag indicating if a PowerPoint (PPTX) version of the lesson is available.                               | bool     |
| materials_md   | Recommended  | Flag indicating if a markdown version of the lesson is available.                                        | bool     |
| citations      | Recommended  | Flag indicating if there are citations for the lecture.                                                  | bool     |
| assignment     | No           | Long-form description of the out of lesson (like homework) exercise associated with the lesson (if any). | html     |
| reading        | No           | Long-form description of the out of lesson (like homework) reading associated with the lesson (if any).  | html     |
| links          | No           | List of links (with `text` and `url` fields) which are mentioned in the lesson.                          | list     |
| video          | No           | The Vimeo ID of the video associated with the lesson.                                                    | int      |

##### Additional distinctions
Though both may be used in a "homework" role subject to class structure (i.e. flipped classroom), note that `assignment` is distinct from `reading` in that the former generally does not have some kind of work product produced by learners to be submitted to teachers. These are both distinct from `links` which are intended to provide access to materials which help complete the lesson itself.

##### Best practices
Note that the following are recommended in YAML:

 - The html fields should use `>` instead of regular single or double quote strings.
 - Non-supported or deprecated fields (such as `slides`) should be removed.
 - Recommended fields should be specified even if using default values.
 - Fields which are marked as "no" for required should not be included if using the default value.
 - Leading and trailing whitespace on strings may be left in place if it improves the readability of the yaml file but should otherwise be removed.
 - Avoid JSON object notation.
 - Please keep lines to 100 characters or fewer. Exceptions made for very long URLs.

Here is an example of a poorly implemented entry:

```
  - number: 3
    name: Hello Creative Python
    video: 1049110017
    slides: true
    materials_pdf: true
    materials_pptx: true
    materials_md: true
    text: 'A hands-on first look at how we can use Python for creative coding. See tutorials at <a href="/labs">Labs</a>.

      '
    assignment: "Revisit the visualization from the last exercise. What might the 4 perspectives say about this visualization?\n\
      <ul>\n  <li>What visual encoding devices are used?</li>\n  <li>What task or user journey is being accomplished through\
      \ the piece?</li>\n  <li>Does the piece try to also convey an emotion and, if so, how?</li>\n  <li>Does the piece invite\
      \ the reader to reach new their own conclusions about the data and, if so, how?</li>\n</ul>\nPlease write 4 - 8 sentences.\n"
    reading: Optionally review <a href="https://python.swaroopch.com">A Byte of Python</a> if you want to brush up on (or
      learn) the fundamentals of Python.
    citations: true
    links: [{"text": "Skills Labs", "url": "/labs"}, {"text": "Sketchingpy Online Sketchbook", "url": https://editor.sketchingpy.org/}]
```

Here is a well implemented entry:

```
  - number: 3
    name: Hello Creative Python
    video: 1049110017
    materials_pdf: true
    materials_pptx: true
    materials_md: true
    text: >
      A hands-on first look at how we can use Python for creative coding. See tutorials at <a href="/labs">Labs</a>.
    assignment: >
      Revisit the visualization from the last exercise. What might the 4 perspectives say about this visualization?

      <ul>
        <li>What visual encoding devices are used?</li>
        <li>What task or user journey is being accomplished through the piece?</li>
        <li>Does the piece try to also convey an emotion and, if so, how?</li>
        <li>Does the piece invite the reader to reach new their own conclusions about the data and, if so, how?</li>
      </ul>
      
      Please write 4 - 8 sentences.
    reading: >
      Optionally review <a href="https://python.swaroopch.com">A Byte of Python</a> if you want to brush up on (or learn) the fundamentals of Python.
    citations: true
    links:
    - text: Skills Labs
      url: /labs
    - text: Sketchingpy Online Sketchbook
      url: https://editor.sketchingpy.org/
```

#### Citations
Each lesson with citations should have a file in the form of `lesson00.txt` within `lecture/citations`. Each line should contain a single citation. Empty lines (including those containing only whitespace) are ignored. These files should end with a single empty line.

#### Markdown
It is strongly recommended that all lessons contain a markdown version as it is the most accessible format where possible. The intention is provide a self-contained text version of the lesson.

We require files in the form `lesson00.md` where each should have the following structure:

 - **Header**: Lesson number and name with very brief description.
 - **Objective**: 1 - 4 sentences describing the objective and purpose of the lesson.
 - **Outline**: Brief 1 - 4 sentences describing the content of the lcture followed by subsections with the components of the lesson each containing short descriptions and bullet points.
 - **Take Aways**: Ideally 1 sentence overview of what should be remembered from the lesson followed by bullet points.
 - **Citations**: Citations which may match or be close to the citation file for the lesson.

Citations from the markdown may differ from the txt citations file where required for assignments / activities outside the lesson itself.

#### PDF / PPTX
Slides should be provided as PDF files with optional but encouraged PPTX versions. There should be a title slide and a slide indicating creative commons license.

#### Support
All lesson materials (markdown, PDF, and PPTX files) are stored under `lecture/support/` to organize supporting materials in a central location. The support directory contains:

 - `md/`: Markdown versions of all lessons
 - `pdf/`: PDF slide decks for all lessons
 - `pptx/`: PowerPoint source files for all lessons
 - `web/`: Web assets used across multiple lessons
 - `misc/`: Miscellaneous files for specific lesson activities (datasets, supplemental documents, etc.)

Files beyond the standard lesson materials are also allowed in the `misc/` subdirectory. In general, these are files used across multiple lessons or special files supporting specific lesson activities.

### Skills Labs
During original teaching of this course as Stat 198 at UC Berkeley, the skills labs were taught using a flipped classroom structure. These are distinct to regular lessons in that there is minimal to no lecture component. Instead, time is spent on one or more directly interactive activities.

Skills labs are organized in the `labs/` directory with the following structure:
 - `Lab_1/`, `Lab_2/`, etc.: Lab-specific directories containing YAML source files
 - Each lab directory contains an `index.yml` with lab metadata (name, lesson) and tutorial YAML files named with a numeric prefix followed by a descriptive name (e.g., `01_python_introduction.yaml`, `02_python_graphics.yaml`)
 - Tutorial YAML files define individual tutorials with name, file, header, sections, and citations
 - Templates: `tutorial.html`, `index_template.html`, `tutorial.md` for rendering
 - `render.py` and `render.sh` to generate HTML and Markdown output from YAML sources

The YAML-based structure allows for consistent formatting and easier maintenance. Tutorial YAML files follow this structure:

| **Field** | **Required** | **Purpose** | **Type** |
| --------- | ------------ | ----------- | -------- |
| name      | Yes          | Human readable name of the tutorial. | string |
| file      | Yes          | Base filename for output (e.g., "python_intro" generates python_intro.html and python_intro.md). | string |
| header    | Yes          | HTML content for the tutorial header/introduction. | html |
| sections  | Yes          | List of tutorial sections, each with "name" (anchor ID), "short" (heading), "long" (description), and "body" (content). | list |
| citations | No           | List of citations, each with "text" and optional "available" (URL). | list |

HTML fields should use `>` for folded scalars as with lesson YAML files. Generated tutorials include:

 - A contents `details` tag.
 - Use of header, main, and sections for accessibility including skip link.
 - Use of `pre` for code sections.
 - A `details` tag for citations.
 - Formal `footer` with license information.
 - Header which links back to labs and MOOC homepage.

These should be fully static pages (HTML, CSS, JS) and automated use of server-side components is currently disallowed.

## Content management
Both skills labs and regular lessons (MOOC source) compile materials to a static website using `render.py` scripts. This takes advantage of very limited open source libraries. At this time, only jinja2 and pyyaml are allowed in this process. Please keep `render.sh` scripts up to date such that they build all lessons and labs. The only external service currently allowed is Vimeo.

## Standards
Please follow conventions of existing code and materials where possible. Please also ensure:

 - MOOC source materials build successfully before opening pull requests.
 - All public or top level members in JS / Python have docstring or JSDoc. 
 - Checks from `pycodestyle` pass.
 - Checks from `eslint` pass.
 - Only `pnpm` and not `npm` are used for security purposes.
 - Use virtualenv where possible but ensure venv and node modules are excluded from git (are present in gitignore).

Refrain from using webpack or typescript (JS resources should be deployed directly). Please use vanilla JS where possible.

## AI Assistants
The original version of this class was made without AI. In general, completely new course materials should be written manually. However, AI may absolutely assist with "logistical" or "mechanical" edits or adapting / refining existing material / code (like proofreading). Specifically, we invite experimentation in the AI skills labs for playing with AI assistants in taking a more active role in preparing materials given the level of AI engagement expected. Please just exercise close supervision and manual validation of changes made. Use of AI assistants for any non-trivial edits should be disclosed, like through co-author in git commit which is sufficient for transparency.