# Body Standardizer Agent Memory

## Project Overview
- Working on markdown migration task for Interactive Data Science course
- Converting legacy `body` attributes (labs) to `html` or `markdown`
- Component 1 (render.py) already supports all three mutually exclusive attributes

## Key Patterns: html vs markdown in labs

- **Use markdown**: Pure prose, simple links (converted to markdown syntax)
- **Use html**: Code blocks, `<details>` tags, complex mixed content
  - Code blocks: `<pre>` tags needed (fenced backticks require extension)
  - Details: Collapsible sections unsupported in markdown
  - Mixed: prose + code + details → must use html

## YAML Scalars
- `>` (folded): Collapses newlines. Good for prose, breaks code.
- `|` (literal): Preserves newlines. Better for code, but markdown still renders as text without fenced_code extension.

## Known Issue: Whitespace in Code Blocks
- Original files: `<pre>` content with `>` folded scalar loses newlines
- Example: `import sketchingpy\nimport time` → `import sketchingpy import time`
- This is legacy issue (Component 7), not migration problem
- Out of scope for Component 2

## Conversion for 03_python_objects.yaml
- 3 sections → markdown (recap, exercise, next)
- 9 sections → html (classes, sketch, ball, motion, simulation, draw, mouse, interacting, cleanup)
- All 12 sections migrated from body attribute
- Build passes successfully

## Conversion for 07_orientation.yaml
- 3 sections → html (rotate, rotate-and-translate, next)
- All sections have <pre> code blocks and mixed content (prose + code + <details> in third section)
- Removed target="_blank" from 2 citation links
- Build passes successfully

## Conversion for 08_text.yaml
- 5 sections → html (font, text, horizontal-align, vertical-align, next)
- All sections have <pre> code blocks or complex HTML structure (lists, <details> tags)
- Removed target="_blank" from external link in "next" section
- Build passes successfully
- Fixed whitespace in 3 code blocks: Removed 6 spaces of extra indentation in text, horizontal-align, and vertical-align sections

## 02_python_graphics.yaml Analysis
- 11 total sections: 8 html + 3 markdown (ALREADY OPTIMAL)
- ALL 8 html sections contain `<details>` tags (must stay html)
- 3 markdown sections already properly formatted
- NO CONVERSION NEEDED: All convertible sections already use markdown
- Build passes, all sections at 2-space indent, no whitespace issues in output

## Conversion for 12_js.yaml
- 5 total sections: 4 markdown + 1 html
- Sections 1-4 (motivation, p5, javascript-itself, d3): Converted from body to markdown
- Section 5 (next): Converted from body to html (contains `<details>` tag)
- All target="_blank" attributes removed from links during conversion
- Markdown links use proper syntax: [text](url)
- Build passes successfully, all sections at 2-space indent

## Conversion for 14_ai_advanced.yaml
- 11 total sections: 2 markdown + 9 html
- Sections converted to markdown: motivation (prose + links), reflection (prose + bullets)
- Sections staying as html: All others contain `<blockquote class="prompt">` (HTML-only styled blockquote)
- setup, importing-knowledge, scaffolding, data, draw-outlines, draw-years, draw-body, finishing-touches: All use html
- No target="_blank" attributes found in original
- Build passes successfully, all sections at 2-space indent, styled blockquotes preserved

## 10_user_loops.yaml Analysis
- 5 total sections: 4 markdown + 1 html
- NO PYTHON CODE in this file at all
- All sections use modern attributes (markdown and html), not legacy body/text
- Content is purely conceptual: about-loops, simulation, loops, terminology, next
- No code blocks, no `<pre>`, no indentation/newline issues
- NO CHANGES NEEDED: File is already properly formatted

## 11_data.yml (Lab_4) Processing
- 10 total sections: 2 markdown + 8 html (motivation, prepare, load-data, holding-data, position, axes-title, data-glyphs, conditional-formatting, constants, reflection, next)
- All sections already use modern attributes (markdown and html), not legacy body/text
- Fixed indentation in 11 Python code blocks within `<pre>` tags
  - parse_fuel_standard_change: Removed extra indentation (8→4 spaces)
  - FuelStandardChange class: Removed extra indentation (8→4 spaces)
  - _draw_axis: Removed extra indentation (8→4 spaces)
  - _draw_title: Removed extra indentation (8→4 spaces)
  - _draw_change: Removed extra indentation (8→4 spaces)
  - draw: Removed extra indentation (8→4 spaces)
  - _determine_annotation (2 versions): Removed extra indentation (8→4 spaces)
  - sketch.draw_ellipse examples: Removed extra indentation
  - sketch.push_transform example: Removed extra indentation
  - year/start_year/end_year snippet: Removed extra indentation
- No attribute migrations needed: File already uses html/markdown correctly
- Summary: Fixed indentation in all code blocks, no other changes needed

## 12_js.yml (Lab_5) - Verification Pass
- File is JavaScript-focused tutorial, NO Python code snippets present
- Already migrated: 4 markdown + 1 html (previously converted from body attribute)
- No whitespace, newline, or indentation issues found
- All sections using correct modern attributes (markdown/html)
- No action needed - file in correct state, already processed

## 13_ai_basics.yml (Lab_6) - Verification Pass
- File is AI-focused conceptual tutorial, NO Python code snippets present
- Contains 7 sections: 3 markdown + 4 html
- Markdown sections: motivation, role, prepare, reflection, next (prose + single markdown code fence for pip)
- HTML sections: initial-request, first-iteration, refining-labels, final-polish (blockquotes with AI prompts)
- All sections already use modern attributes (markdown/html), not legacy body/text
- No indentation/newline/whitespace issues in code (no Python code blocks exist)
- No action needed - file in correct state, not applicable to fix-python-snippets task

## 14_ai_advanced.yml (Lab_6) - Final Verification Pass
- File is advanced AI techniques tutorial, NO Python code snippets present
- Contains 11 sections: 2 markdown + 9 html (ALREADY OPTIMAL)
- Markdown sections: motivation, reflection (prose + bullets)
- HTML sections: setup, importing-knowledge, scaffolding, data, draw-outlines, draw-years, draw-body, finishing-touches (prose + `<blockquote class="prompt">` for AI prompts)
- All sections already use modern attributes (markdown/html), not legacy body/text
- No Python code blocks with indentation/newline issues - only shell commands and AI prompts
- setup section has shell commands (`mkdir`, `cd`, `echo`, `python3`, `pip`, `source`, `claude`) in `<pre>` tags - these are NOT Python code and require no fixes
- No action needed - file already in correct state, not applicable to fix-python-snippets task (no Python code to fix)
