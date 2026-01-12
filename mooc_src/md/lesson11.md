# Lesson 11
Formalizing glyphs and encoding devices.

## Objective
Understand empirical evidence for choosing encoding devices and learn techniques for working effectively within design constraints when creating data visualizations.

## Outline
Using Cleveland and McGill's empirical research and practical design techniques, this lecture transitions from understanding the basic ingredients of visualization to knowing when and how to use them effectively.

### Cleveland and McGill's hierarchy of encodings
From most to least accurate for quantitative perception.

  - Position on common scale provides highest accuracy and underpins scatter plots and bar charts.
  - Position on non-aligned scales remains highly accurate.
  - Length is consistently accurate, especially when aligned on common axis.
  - Direction (slope) and angle show moderate accuracy that varies with orientation.
  - Area is useful for contextualizing metrics but has area versus radius perception issues.
  - Volume generally performs poorly, possibly due to 3D representation in 2D media.
  - Curvature shows inconsistent performance.
  - Shading has limited quantitative value.
  - Color saturation has lowest accuracy and is better for branding and qualitative groups.

### Comparing graphics with different encodings
Group activity. Hands-on comparison of visualization approaches demonstrates the hierarchy in practice.

  - Bar charts use position and length (high accuracy) while pie charts use angle (moderate accuracy).
  - Position encoding outperforms color-based encoding for quantitative comparison.
  - Length encoding is more effective than area encoding for the same data.

Visualizations using higher-ranked encoding devices consistently enable more accurate data reading.

### Working within limitations
When we cannot always use the highest-accuracy encoding devices, we have techniques to maximize effectiveness.

  - Dual axes allow plotting of two variables with different scales on the same chart using two y-axes with a shared x-axis (or visa-versa).
  - Shared axes create visual connections between related data through multiple visualizations sharing common axes to facilitate comparison (stacking variables).
  - Direct labeling places data values directly on visualization elements to reduce cognitive load of referencing separate legends or axes (especially good for double encoding stuff which is in a poor encoding device).

### Keeping channels clear
Building on Tufte's concepts about minimizing chart junk.

  - Visual clutter can interfere with encoding devices such as overlapping bars or unnecessary grid lines.
  - Simplify visual elements and use negative space strategically to improve clarity.
  - Align on grids with subtle supporting lines that do not dominate.
  - Ensure distinct visual separation between categories.
  - Every visual element can either encode data or support data reading.

### Example from current events
New York Times Opinion Piece (Feb 28, 2025) demonstrates effective use of position encoding.

  - Uses a two-dimensional scatter plot with negative to positive impact on horizontal axis and less to more consequential on vertical axis.
  - Topics plotted as circles with direct labels for Ukraine, DOGE, Tariffs, Immigration, and others.
  - Demonstrates effective use of position encoding for two dimensions plus categorical labeling.

## Take Aways
This lecture concludes the primitives section of the course which focused on perception and cognitive science for visualization and understanding how the human visual system processes information.

  - Cleveland and McGill provide empirical evidence of a hierarchy where position is the most accurate encoding device while color saturation is least accurate for quantitative data.
  - Techniques like dual axes, shared axes, and direct labeling help work effectively within design constraints.
  - Remove chart junk to keep visual channels clear and ensure every element either encodes data or supports data reading.

Moving forward, the course will explore how to combine these principles with human-centered design, specialized data types, and interactivity.

## Citations

[1] A. Pottinger, "TED Visualization," Gleap.org. Available: https://gleap.org/content/ted_visualization

[2] W. Cleveland and R. McGill, "Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods," *Journal of the American Statistical Association*, 1984. Available: https://www.jstor.org/stable/2288400

[3] "Stack Overflow Annual Developer Survey 2024," Stack Exchange Inc, 2024. Available: https://survey.stackoverflow.co/

[4] C. Ware, "Information Visualization: Perception for Design (Interactive Technologies)," Morgan Kaufmann, 2012.

[5] A. Cairo, "The Truthful Art," New Riders, 2016.

[6] NYT Opinion, "10 Columnists and Writers Rate What Mattered in Trump's First Full Month," *New York Times Company*, 2025. Available: https://www.nytimes.com/interactive/2025/03/01/opinion/trump-administration-first-month.html.
