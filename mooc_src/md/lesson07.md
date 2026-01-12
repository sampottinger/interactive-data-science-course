# Lesson 7: Visualization as Science 2
Gestalt principles and color.

## Objective
Understand how the visual system groups elements through Gestalt Principles and apply practical guidance for using color effectively in data visualization.

## Outline
This lecture explores the perceptual foundations of visual grouping and color usage in data visualization. Starting with the Gestalt Principles that govern how we perceive collections of visual elements, we then examine the physical and perceptual aspects of color vision, including color spaces and tools for creating effective color schemes.

### Gestalt Principles
The Gestalt Principles describe how we pre-attentively perceive glyphs together within scenes, helping us understand how parts form together to build a whole.

  - Enable creation of visual hierarchy within visualizations.
  - Allow combining individual glyphs into larger meaningful structures.
  - Processed pre-attentively by the visual system.
  - Guide how viewers group and interpret visual elements.
  - Include emergence, closure, reification, common region, continuity, proximity, multistability, figure/ground, invariance, pragnanz, similarity, symmetry, and common fate.

### Group Activity
Hands-on exploration of Gestalt Principles through physical manipulation.

  - Students arranged blocks of different sizes, colors, and shapes.
  - Demonstrated proximity, continuity, similarity, symmetry, and closure.
  - Reinforced understanding of how these principles work in practice.

### Color Vision Fundamentals
Color perception is based on three types of cone cells in the human eye working together to enable full spectrum vision.

  - Short wavelength (S) cones peak around blue.
  - Medium wavelength (M) cones peak around green.
  - Long wavelength (L) cones peak around red.
  - Color perception is highly contextual and depends on background.
  - Surrounding glyphs can influence how we perceive a color.

### Color Spaces
Different representations of color serve different purposes in visualization work.

  - RGB: Standard for computers and displays, often shown as hex codes.
  - HSL: More intuitive for building color schemes and creating variations.
  - Perceptually uniform color spaces: Ensure equal distances correspond to equal perceptual differences.
  - Equal steps in RGB or HSL do not correspond to equal perceptual differences.

### Tools for Creating Color Schemes
Specialized tools help create effective, accessible color schemes.

  - ColorBrewer: Designed for cartography with sequential, diverging, and qualitative schemes.
  - I Want Hue: Generates perceptually distinct colors with customization options.
  - HSL Color Picker: Interactive tool for understanding color relationships.
  - All tools include consideration for colorblind accessibility.

### Color Usage Recommendations
Evidence-based guidance for effective color use in visualization.

  - Consider avoiding color as a primary encoding device when possible.
  - For quantitative scales, use luminance variation with consistent hue and saturation.
  - For qualitative scales, limit to approximately 6 colors maximum.
  - Double encode when possible (color plus another visual attribute).
  - Account for colorblindness from the start.
  - Consider direct labeling as an alternative to color legends.

## Take Aways
Gestalt Principles and thoughtful color usage form the foundation for creating clear, effective visualizations that leverage how our visual system naturally processes information.

  - Gestalt Principles tell us how to create hierarchy and combine glyphs into larger structures.
  - RGB is the standard for digital work but not perceptually uniform.
  - HSL can be more intuitive for creating color schemes and variations.
  - Perceptually uniform color spaces help ensure equal perceptual differences.
  - Context heavily influences color perception.
  - Limit qualitative color schemes to approximately 6 colors reliably.
  - Use established tools (ColorBrewer, I Want Hue) rather than choosing colors ad-hoc.
  - Double encode when possible and consider direct labeling.
  - Colorblind accessibility should be considered from the start.

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
