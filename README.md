# Interactive Data Science and Visualization
An open online course serving both as a stand-alone massive open online course (MOOC) and re-usable open educational resources (OER) which can be adapted to other instructional opportunities.

## Purpose
Interactive Data Science and Visualization takes a multi-disciplinary perspective on building compelling digital pieces to engage with data. We start with traditional information design with a focus on perception science and data visualization-focused methods adjacent to user-centered design. However, we then extend that using lenses from interaction design, media studies, sociology, anthropology, and game design in order to deeply consider the role of audience with complexity and to understand how to foster co-creation of meaning through interactivity. This allows us to prepare data visualization for a future where computation enables new engaging experiences with data beyond a traditional view of data encoding and task completion. Finally, instruction also considers use of AI.

This self-paced massive open online course (MOOC) is a thoughtful upgrade to Stat 198 taught at the University of California, Berkeley in 2025. It adds additional resources and optional lessons along with modifications for a fully online experience. That said, it also offers modularity where these re-usable open educational materials can be adapted to other instruction.

## Using
The course materials are available online for free at [https://mooc.interactivedatascience.courses](https://mooc.interactivedatascience.courses/). This includes:

 - Syllabus and course manual available as PDF, Markdown, and HTML.
 - Individual lessons and lesson plans available as Markdown.
 - Lecture slides and visual materials available as PDF or PPTX.
 - Videos with manually confirmed captions (hosted by vimeo).
 - Skills labs with all supporting materials required for hands-on engagement.

The course website may also be constructed using the source available in this repository as described in the [Developing](#developing) and [Deploying](#deploying) sections.

## Developing
The course materials in this repository are built into a complete website through a small Python script.

### Structure
The source materials for these resources are divided into three directories:

 - **Course-wide materials** (`/course_wide`): These are resources which apply across many or all lessons of the course and are wide-ranging documents such as the course manual and syllabus as well as grading rubric. In general, these should be provided in html, markdown, and PDF.
 - **Skills labs** (`/labs`): Hands-on tutorials and focused instruction on implementation skills. These are often recommended for a flipped classroom structure.
 - **Individual lessons** (`/mooc_src`): Traditional lectures that mix classic instruction and shorter hands-on activities intended for a traditional classroom structure.

### Dev Container
The recommended approach to establishing a local development environment is through a [dev container](https://containers.dev/). This can be as simple as opening this repository in a [GitHub Codespace](https://github.com/features/codespaces) instance. Alternatively, you can set up a local dev container through an IDE like [VSCode](https://code.visualstudio.com/docs/devcontainers/create-dev-container) or [IntelliJ](https://www.jetbrains.com/help/idea/connect-to-devcontainer.html). If preferred, you can also use a [dev container from the command line](https://github.com/devcontainers/cli).

### Manual Setup
If you want to skip the dev container, you will need to [install Python](https://docs.python-guide.org/starting/installation/). Afterwards, it is recommended that you [create a virtual environment](https://docs.python-guide.org/dev/virtualenvs/) in the same directory where this repository is cloned like so:

```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

Regardless, install the requirements:

```bash
$ pip install -r requirements.txt
```

For some operations like linting, [eslint](https://eslint.org/) is recommended as it is used by CI / CD. We recommend installing [pnpm](https://pnpm.io/) and then getting requirements:

```bash
$ npx eslint 'mooc_src/**/*.js'
```

### Building
Build the lessons through `mooc_src`:

```bash
$ cd mooc_src
$ bash render.sh
```

Alternatively, build the full course by using `build.sh` in the root of the repository:

```bash
$ bash build.sh
```

This will create a full build in the `mooc` directory.

### AI assistants
If desired, subagents can help with development activities. These are available under the Claude Code-style. See [.claude/agents](https://github.com/sampottinger/interactive-data-science-course/tree/main/.claude/agents).

### Contributing
For those interested in contributing to this open source project, thank you! In addition to additional logistical instructions in this README for building the course website, please see also our [contributing guide](https://github.com/sampottinger/interactive-data-science-course/blob/aa4f19e55f90a5574fac67c92b490fbc830b0f72/CONTRIBUTING.md). That said, it is recommended that the following pass prior to commit:

```bash
$ pyflakes mooc_src/*.py
$ pycodestyle mooc_src/*.py
$ npx eslint 'mooc_src/**/*.js'
```

## Deploying
You can either make a deployment to your own server or the official website.

### Host yourself
Having created a build, the `mooc` directory can be served through a web server like a Python local development server:

```bash
$ cd mooc
$ python3 -m http.server
```

You can also use [Nginx](https://nginx.org/), [Tomcat](https://tomcat.apache.org/), [Apache Server](https://httpd.apache.org/), or anything else capable of static serving.

### Deploy to official site
To deploy to [the official website](https://mooc.interactivedatascience.courses/), first [make a pull request on GitHub](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request). Then, when it is merged to the `main` branch, it will be deployed automatically through [GitHub Actions](https://docs.github.com/en/actions).

## Open source
Various lessons and activities within this course may use different technologies and each have their own citations listing. That said, the course itself uses the following:

 - [eslint](https://eslint.org/) under an [MIT license](https://github.com/eslint/eslint/blob/main/LICENSE).
 - [eslint-config-google](https://github.com/google/eslint-config-google) under an [Apache 2.0 license](https://github.com/google/eslint-config-google/blob/main/LICENSE).
 - [Jinja2](https://jinja.palletsprojects.com/) under a [BSD 3 Clause license](https://jinja.palletsprojects.com/en/3.1.x/license/).
 - [pip](https://pip.pypa.io/) under an [MIT license](https://github.com/pypa/pip/blob/main/LICENSE.txt).
 - [pnpm](https://pnpm.io/) under an [MIT license](https://github.com/pnpm/pnpm/blob/main/LICENSE).
 - [pycodestyle](https://pycodestyle.pycqa.org/) under an [MIT license](https://github.com/PyCQA/pycodestyle/blob/main/LICENSE).
 - [pyflakes](https://github.com/PyCQA/pyflakes) under an [MIT license](https://github.com/PyCQA/pyflakes/blob/main/LICENSE).
 - [PyYAML](https://pyyaml.org/) under an [MIT license](https://github.com/yaml/pyyaml/blob/main/LICENSE).
 - [Python](https://www.python.org/) under a [PSF license](https://docs.python.org/3/license.html).
 - [sketchingpy](https://sketchingpy.org/) under a [BSD 3 Clause license](https://codeberg.org/sketchingpy/Sketchingpy/src/branch/main/LICENSE.md).

For those using our CI / CD, note that our automation uses GitHub Actions [as described in our GitHub Actions build script](https://github.com/sampottinger/interactive-data-science-course/blob/main/.github/workflows/deploy.yaml).

## License
All code is available under the BSD license. All other materials CC BY-NC-SA 4.0 (some resources used are also under CC or CC BY-NC-SA license). See [full license](https://github.com/sampottinger/interactive-data-science-course/blob/main/LICENSE.md) for more details.