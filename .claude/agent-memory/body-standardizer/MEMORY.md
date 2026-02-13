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
