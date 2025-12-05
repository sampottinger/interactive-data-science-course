# Lecture 7: Visualization as Science 2

**Stat 198: Interactive Data Science and Visualization**
**Instructor:** A Samuel Pottinger
**Original Instruction Date:** February 12, 2025

## Description

Tour the Gestalt Principles and engage in a hands-on activity to put them into practice. Afterwards, explore color vision including color spaces, perceptually consistent color schemes, tools for color, and general guidance.

## Key Takeaways

This lecture explores how our visual system groups elements through Gestalt Principles and provides practical guidance for using color effectively in data visualization.

### Gestalt Principles
- Allow us to create visual hierarchy in our work.
- Enable combining individual glyphs into larger meaningful structures.
- Are processed pre-attentively by the visual system.
- Guide how viewers group and interpret visual elements.

### Color Theory for Visualization
- RGB is the standard for digital work but not perceptually uniform.
- HSL can be more intuitive for creating color schemes.
- Perceptually uniform color spaces help ensure equal perceptual differences.
- Context heavily influences color perception.

### Practical Color Guidance
- Limit qualitative color schemes to ~6 colors.
- Use established tools (ColorBrewer, I Want Hue) rather than choosing colors ad-hoc.
- Double encode when possible.
- Consider colorblind accessibility from the start.
- Direct labeling can be more effective than color legends.

## Gestalt Principles: Introduction

The Gestalt Principles describe how we pre-attentively perceive glyphs together within scenes. These principles help us understand how parts form together to build a whole.

### Why Gestalt Principles Matter

These principles tell us how to create "hierarchy" within our work. This lets us combine glyphs together to make larger structures, enabling us to build complex visualizations from simpler components.

## Tour of Gestalt Principles
Gestalt Principles offer a structured way to think about compositions of glyphs.

### 1. Emergence
Our visual system can perceive complex forms from simpler elements. We can see complete shapes and patterns emerge from collections of basic visual elements.

**Example:** A dalmatian dog can emerge from a pattern of black spots, demonstrating how our visual system constructs meaningful wholes from parts.

### 2. Closure
We tend to complete incomplete shapes or forms. Our visual system fills in gaps to create complete, recognizable patterns.

**Example:** Dashed outlines of shapes (rectangles, circles, triangles) are perceived as complete shapes even though they are incomplete.

### 3. Reification
The activation of "negative space" where our visual system perceives more spatial information than is actually present in the stimulus.

**Example:**
- Pac-Man-like shapes arranged to suggest a triangle in the negative space
- The Olympic rings symbol creating implied overlap regions

### 4. Common Region
Elements that are located within the same bounded region are perceived as grouped together.

**Example:** A subset of squares enclosed within a light background box are perceived as a distinct group separate from other squares.

### 5. Continuity
Our visual system tends to perceive continuous forms rather than abrupt changes in direction. We follow lines and paths smoothly.

**Example:** Two intersecting curved lines are perceived as continuous paths crossing each other, not as four separate line segments.

### 6. Proximity
Objects that are close to each other are perceived as forming a group.

**Example:** Squares positioned near each other are grouped perceptually, while those spaced farther apart are seen as separate clusters.

### 7. Multistability
Some visual forms can be perceived in multiple stable ways, like the famous Necker Cube which can be seen from two different orientations.

**Example:** The Necker Cube wireframe can be perceived with either the upper-left or lower-right square as the front face.

### 8. Figure/Ground
We distinguish between objects (figure) and their surrounding environment (ground). This is fundamental to visual perception.

**Example:** Rubin's Vase illusion, where viewers can see either a vase (figure) or two faces in profile (ground), but not both simultaneously.

### 9. Invariance
We recognize objects regardless of rotation, scale, translation, or other transformations. Objects maintain their identity across different representations.

**Example:** Stick figures in various orientations, sizes, and styles are all recognized as representing people.

### 10. Pragnanz (Good Form)
Our visual system tends to organize elements into the simplest, most stable, and most regular forms possible. We prefer simple interpretations over complex ones.

**Example:** Overlapping circles (like the Olympic rings) are perceived as complete circles overlapping rather than as complex interconnected shapes.

### 11. Similarity
Elements that share visual characteristics (color, shape, size, orientation) are perceived as related or grouped together.

**Example:** In a grid of squares, those with the same color (blue) are grouped perceptually, separating from squares of different colors (gray).

### 12. Symmetry
Symmetrical elements are perceived as belonging together and forming coherent groups or objects.

**Example:** Pairs of brackets [ ] and { } are perceived as related pairs due to their symmetry.

### 13. Common Fate
Elements moving in the same direction or with the same velocity are perceived as a unified group.

**Example:** Arrows moving in the same direction are grouped together, while those moving in different directions are perceived as separate.

## Group Activity: Building with Gestalt Principles

Students worked in groups to build visual representations demonstrating:

- Proximity
- Continuity
- Similarity
- Symmetry
- Closure

Using provided blocks of different sizes, colors, and shapes, participants arranged them to exemplify each Gestalt principle. This hands-on activity reinforced understanding of how these principles work in practice.

## Color Vision
Color is something we will revisit a few times in the course. However, let's look at it from a physical perspective.

### Components of Color

Color perception is based on three types of cone cells in the human eye:
- **Short wavelength (S) cones**: Peak sensitivity around 420nm (blue).
- **Medium wavelength (M) cones**: Peak sensitivity around 530nm (green).
- **Long wavelength (L) cones**: Peak sensitivity around 560nm (red/yellow).

These three cone types work together to enable us to perceive the full spectrum of visible colors through their combined responses to different wavelengths of light.

### Contextual Nature of Color

Color perception is highly contextual:

- Colors appear different depending on the background.
- Surrounding glyphs can influence how we perceive a color.
- The same RGB values can appear as different colors in different contexts.

## Color Spaces
We only touch on color spaces at a high level but it is important to understand how we tell computers about different colors as some representations may be useful in some settings over others.

### RGB (Red, Green, Blue)
- **What it is:** The standard color space used by computers and displays.
- **How it works:** Combines varying intensities of red, green, and blue light.
- **Representation:** Often shown as hex codes (e.g., #0099AA or #266b73).
- **When to use:** Default for most coding and digital work.

### HSL (Hue, Saturation, Lightness)
- **Hue:** The color itself, represented as degrees around a color wheel (0-360°).
- **Saturation:** The intensity or purity of the color (0-100%).
- **Lightness:** How light or dark the color is (0-100%).

**Advantages:**
- More intuitive for building color schemes.
- Useful for creating variations of a color.
- Creating shadows often involves decreasing luminance and saturation.
- Easier to maintain perceptual relationships.

### Perceptually Uniform Color Spaces

Standard color spaces like RGB and HSL are not perceptually uniform - equal steps in the color space don't correspond to equal perceptual differences. This is why the CIE chromaticity diagram and perceptually uniform color spaces were developed.

**Challenge:** Equal distances in RGB or HSL space do not correspond to equal perceptual differences. Some color transitions appear more dramatic than others even with the same numerical change.

**Solution:** Perceptually uniform color spaces attempt to ensure that equal distances in the color space correspond to equal perceptual differences in human vision.

## Creating Color Schemes
Some courses dig deeper into color theory. Here, we will just look at some foundational tools in an information design context.

### ColorBrewer
- Designed specifically for cartography and data visualization.
- Provides color schemes that are:
  - Sequential (for ordered data).
  - Diverging (for data with a meaningful midpoint).
  - Qualitative (for categorical data).
- Built-in consideration for colorblind users.
- Shows how schemes work on maps.
- **URL:** https://colorbrewer2.org/

### I Want Hue
- Generates perceptually distinct colors.
- Allows customization of color space regions.
- Can optimize for colorblind accessibility.
- Useful for qualitative schemes with many categories.
- Provides more granular control than ColorBrewer.
- **URL:** https://medialab.github.io/iwanthue/

### HSL Color Picker
- Interactive tool for selecting colors in HSL space.
- Useful for understanding relationships between hue, saturation, and lightness.
- Can convert between RGB, HSL, and hex formats.
- **URL:** https://hslpicker.com/#ffd900

## Color Usage Recommendations

1. **Consider avoiding color as a primary encoding device**
   - Reserve color for aesthetic and branding purposes when possible.
   - Use other visual encoding devices (position, length, area) as primary channels.

2. **For quantitative scales:**
   - Consider using only luminance variation.
   - Keep hue and saturation consistent.
   - This approach works better for small glyphs.
   - Use tools like ColorBrewer for gradient schemes.

3. **For qualitative scales:**
   - Limit to approximately 6 colors maximum for reliable discrimination.
   - Use ColorBrewer or I Want Hue to generate schemes.
   - Consider direct labeling as an alternative to color legends.
   - Remember that many users will struggle to distinguish more than 6 colors.

4. **Double encoding when possible:**
   - Use color plus another visual attribute (shape, pattern, position).
   - Ensures the visualization works even without color.
   - Improves accessibility for colorblind users.

5. **Account for colorblindness:**
   - Use colorblind-safe palettes.
   - Don't rely solely on color to convey information.
   - Test visualizations with colorblind simulation tools.

Remember that color is contextual:

- Background color affects perception.
- Nearby glyphs influence color appearance.
- Size of colored elements affects how colors are perceived.
- Consider the full visual context when choosing colors.

## Examples Demonstrating Color Principles
We look at a few examples that put our ideas into practice.

### Poor Color Usage
A pie chart with 10 different colored segments representing university population categories (Freshman, Sophomore, Junior, Senior, Graduate Masters, Graduate PhD, Staff Permanent, Staff Temporary, Faculty, Visitor) demonstrates the limitation of using too many colors.

**Problems:**
- Too many colors (10) to distinguish reliably.
- Small segments make color discrimination even harder.
- Legend lookup is required, breaking visual flow.
- Cognitive load is high.

### Improved Approach
The same data shown with direct labels on segments, where only the categories are labeled:
- Freshman: 33.9%.
- Sophomore: 25.4%.
- Junior: 16.9%.

**Improvements:**
- Direct labeling reduces need for legend.
- Focus on major categories.
- Easier to understand at a glance.

## Activities
As before, continue what you started in class by reviewing these additional materials and activities.

### Lecture Video
[Watch Lecture 7: Visualization as Science 2 on Vimeo](https://vimeo.com/1055836472)

### Assignment
Return to your Job Satisfaction exercise. Make a new graphic that displays the same variables but use a different visual representation. For example, if you previously chose a scatter plot, try a heatmap or bar chart. It doesn't necessarily need to be better or worse. It just needs to be different. Finally, write 3-4 sentences about how your plot uses pre-attentive variables.

### Reading
We are getting a look at the Gestalt Principles through [Gestalt - The Parts and the Whole by Extra Credits](https://youtu.be/c1qdyszaeTU?feature=shared).

### Links
- [Activity as a PowerPoint file](/mooc/support/lecture7.pptx)

## Citations

[1] B. Adhikari, "Marey's train schedule," University of Missouri Saint Louis, 2021. Available: https://badriadhikari.github.io/data-viz-workshop-2021/minards/

[2] C. Ware, "Information Visualization: Perception for Design," MK Press.

[3] C. Ware, "Visual Thinking for Design," MK Press.

[4] Interaction Design Foundation - IxDF. "What are the Gestalt Principles?" Interaction Design Foundation - IxDF. Available: https://www.interaction-design.org/literature/topics/gestalt-principles (accessed Feb. 12, 2025).

[5] MRMW, "Reification," Wikimedia, 2020. Available: https://en.wikipedia.org/wiki/Gestalt_psychology#/media/File:Reification.svg

[6] B. Young, "Cross Keys," Wikimedia, 2011. Available: https://en.wikipedia.org/wiki/Gestalt_psychology#/media/File:CrossKeys.png

[7] "Vision," CourseHero. Available: https://www.coursehero.com/study-guides/wmopen-psychology/outcome-vision/

[8] R. Madsen, "Perceptually uniform color spaces," Programming Design Systems, 2020. Available: https://programmingdesignsystems.com/color/perceptually-uniform-color-spaces/

[9] SharkD, "RGB Cube," Wikimedia, 2010. Available: https://en.wikipedia.org/wiki/RGB_color_spaces#/media/File:RGB_Cube_Show_lowgamma_cutout_b.png

[10] J. Rus, "HSL and HSV Models," Wikimedia, 2010. Available: https://en.wikipedia.org/wiki/RGB_color_spaces#/media/File:RGB_Cube_Show_lowgamma_cutout_b.png

[11] K. Cherry, "Figure / Ground Perception in Psychology," Verywell Mind, 2023. Available: https://www.verywellmind.com/what-is-figure-ground-perception-2795195

[12] C. Brewer, M Harrower, and The Pennsylvania State University, "Colorbrewer 2.0," The Pennsylvania State University, 2013. Available: https://colorbrewer2.org/

[13] M. Jacomy, "I Want Hue," Sciences-Po Medialab, 2024. Available: https://medialab.github.io/iwanthue/

[14] B. Mathis "HSL Color Picker," 2024. Available: https://hslpicker.com/#ffd900
