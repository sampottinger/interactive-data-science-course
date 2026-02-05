# Lesson 6: Visualization as Science 1
The visual processing system.

## Objective
Explore the human visual system and its connection to data visualization design, examining how we extract visual information from the environment and what that means for creating effective visualizations.

## Outline
This lecture transitions into a the first perspective in the course, examining data visualization through the lens of cognitive and perception science. We explore the biological mechanisms of vision and their practical implications for designing effective visualizations.

### The structure and behavior of the eye
Understanding the anatomical and functional aspects essential for data visualization design.

  - The fovea means we only see a very small area with sharpness at a time.
  - Our brain constructs an image over time through multiple saccades.
  - Our vision is quite sharp for luminance (brightness) but hue (color) perception is complicated.
  - Key structures include the cornea, lens, iris, pupil, retina, fovea, and optic nerve.
  - Rod cells provide high sensitivity to light intensity with low spatial resolution.
  - Cone cells enable color perception with three types having different wavelength sensitivities.
  - Saccadic eye movements reposition the fovea to different points of interest, with visual processing suppressed during movement.

### The stages of visual processing
How photons become meaningful information through the visual processing pipeline.

  - Photoreceptors convert light to neural signals processed through retinal layers.
  - Information transmits via the optic nerve to the visual cortex (V1/V2) and specialized areas that construct higher order information.
  - The dorsal pathway ("where") processes spatial location and motion, important for position-based encodings.
  - The ventral pathway ("what") processes object recognition and identification, important for form-based encodings.
  - Two competing forms of processing.
    - Feature-driven (bottom-up) processing operates automatically and fast, driven by stimulus properties without conscious attention.
    - Context-driven (top-down) processing is influenced by knowledge and expectations, requiring cognitive effort.
  - Humans can reliably remember only about 4 visual items, making it better to keep information visible.
  - The fovea and visual memory are limited, so manual scanning is slow and effortful.
  - The brain identifies structure and features (glyphs) not individual pixels.

### Contrast and relative processing
How relative processing becomes important to visual understanding.

  - Visual perception is generally relative, not absolute, with what we perceive depending heavily on surrounding context.
  - The visual system is optimized for detecting differences and edges rather than absolute values.
  - The checker shadow illusion demonstrates how context changes perception even when luminance is identical.
  - Mach bands show perceived light and dark bands at boundaries that result from lateral inhibition enhancing edge detection.
  - The railroad track illusion demonstrates how perspective cues and top-down processing affect size perception.
  - To emphasize relative comparisons, have visual elements touch each other or share backgrounds.
  - To emphasize absolute values, use borders or consistent backgrounds to provide a stable reference frame.
  - Ensure sufficient contrast to background if reliable reading of figures is required.

### Preattentive features
Visual properties that can be detected quickly and automatically without conscious scanning.

  - Preattentive features can be processed in parallel across the visual field, allowing rapid detection without focused "conscious" attention.
  - They reduce cognitive load, enable quick pattern detection, and avoid slow serial scanning.
  - Color features include hue (color identity), saturation (color intensity), and brightness/luminance.
  - Form features include shape (circle, square, triangle), size (length, area), orientation (angle, tilt), enclosure, line width, and curvature.
  - Position features include spatial location, proximity, and alignment (to be explored more with Gestalt principles).
  - Motion features include flicker and direction of movement (to be explored in game design and interactivity section).
  - The exact list of preattentive features varies somewhat from author to author as research continues.
  - Effectiveness depends on number of distractors, degree of difference, and combination of features (which can interfere with each other).
  - Use preattentive features strategically to enable rapid detection and avoid forcing users to scan serially through items.

### Group activity
Use of graduation and annual cost dataset with task of highlighting Berkeley from a number of different univerisites.

## Take Aways
Understanding human visual perception provides concrete principles for creating effective data visualizations that work with, rather than against, our visual processing system.

  - Limited visual memory means keeping information visible is better than requiring memorization, even if positioned far away.
  - Avoid scanning
    - Using visual aspects the visual cortex is already good at identifying.
    - Preattentive features like color, form, size, and orientation
    - Enable rapid detection and efficient visual search.
  - Structure aids processing because the brain identifies meaningful units (glyphs) not individual pixels.
  - What we see depends on surrounding context, so manipulate borders to emphasize comparisons or absolute values as needed.

## Citations

[1] B. Adhikari, "Marey's train schedule," University of Missouri Saint Louis, 2021. Available: https://badriadhikari.github.io/data-viz-workshop-2021/minards/

[2] S. Bell, "Introduction and Perceptual Elements of Colour," University of Saskatchewan. Available: https://openpress.usask.ca/introgeomatics/chapter/introduction-and-perceptual-elements-of-colour/

[3] J. Harvey, "The evolution of the human eye," TED Ed, 2015. Available: https://www.youtube.com/watch?v=qrKZBh8BL_U

[4] D. Camors, Y. Trotter, P. Pouget, S. Gilardeau & J. Durand, "Visual straight-ahead preference in saccadic eye movements," Nature Communications, 2016. Available: https://www.nature.com/articles/srep23124

[5] OSC Rice, "Vision," Washington State University. Available: https://opentext.wsu.edu/psych105nusbaum/chapter/vision/

[6] "Vision," CourseHero. Available: https://www.coursehero.com/study-guides/wmopen-psychology/outcome-vision/

[7] E. Adelson, "Checker shadow illusion," Wikimedia, 2018. Available: https://en.wikipedia.org/wiki/Checker_shadow_illusion#/media/File:Checker_shadow_illusion.svg

[8] DancingPhilosopher, "Mach Bands," Wikimedia, 2012. Available: https://en.wikipedia.org/wiki/Optical_illusion#/media/File:Mach_bands_-_animation.gif

[9] US Department of Education, "College Scorecard," US Department of Education. Available: https://collegescorecard.ed.gov/search/?sort=salary:desc&page=0&state=CA

[10] C. Ware, Information Visualization: Perception for Design. MK Press.

[11] C. Ware, Visual Thinking for Design. MK Press.

## License

This lesson is part of [Interactive Data Science and Visualization](https://mooc.interactivedatascience.courses/) and is released under a [CC-BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/deed.en) license.
