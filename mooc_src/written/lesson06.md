# Lecture 6: Visualization as Science 1

**Stat 198: Interactive Data Science and Visualization**
**Instructor:** A Samuel Pottinger
**Original Instruction Date:** February 10, 2025

## Description

A look at the human visual system and the connection between the eyes and brain. Explore how we extract visual information from the environment and what that means for data visualization.

## Key Concepts and Takeaways

Summarizing some key ideas from today...

### Visual Processing Principles

1. **Limited Visual Memory**
   - Humans can reliably remember only about 4 visual items.
   - Better to keep information visible than require memorization.
   - Use persistent visual references even if positioned far away.

2. **Avoid Scanning**
   - The fovea and visual memory are limited.
   - Manual scanning is slow and effortful.
   - Better to use features the visual cortex is already good at identifying.

3. **Structure Aids Processing**
   - The brain identifies structure and features, not individual pixels.
   - Think in terms of glyphs (meaningful units) not pixels.
   - Leverage Gestalt principles (to be explored in next lecture).

4. **Relative Perception**
   - What we see depends on surrounding context.
   - Use this to emphasize comparisons or absolute values as needed.
   - Be aware of unintended context effects.

5. **Preattentive Features for Efficiency**
   - Use color, form, size, orientation to enable rapid detection.
   - Avoid forcing users to scan serially through items.
   - Consider combining multiple preattentive features strategically.

## Overview

This lecture transitions into a new way of seeing evidence in the course, examining data visualization through the lens of cognitive and perception science. We explore the biological mechanisms of vision and their implications for designing effective visualizations.

### Course Context

**Where We Are:** History → Design → **Science** → Skills

This lecture marks the beginning of our exploration into the scientific foundations of data visualization, focusing on how human perception and cognition shape our ability to process visual information.

## Main Topics

### 1. The Structure and Behavior of the Eye

Understanding the anatomical and functional aspects of the human eye that are essential for data visualization design.

#### Key Structures
- **Cornea and Lens**: Focus light onto the retina.
- **Iris and Pupil**: Control light intake.
- **Retina**: Contains photoreceptor cells (rods and cones).
- **Fovea**: Small central area of high visual acuity.
- **Optic Nerve**: Transmits visual information to the brain.

#### Three Important Lessons from Eye Anatomy

1. **Limited Sharp Vision**: The fovea means we only see a very small area with sharpness at a time.
   - Implications: Users must move their eyes to see different parts of a visualization clearly.
   - Design consideration: Important information should be positioned to minimize scanning.

2. **Constructed Visual Experience**: Our brain constructs an image over time through multiple fixations.
   - The brain pieces together information from multiple eye movements (saccades).
   - What we "see" is actually a mental reconstruction, not a direct representation.

3. **Luminance vs. Hue Sensitivity**: Our vision is quite sharp for luminance (brightness), but hue (color) perception is complicated.
   - Rod cells: High sensitivity to light intensity, low spatial resolution.
   - Cone cells: Color perception, concentrated in fovea, three types with different wavelength sensitivities.
   - Design implication: Brightness differences are easier to perceive than color differences.

#### Color Vision Sensitivity

The human visual system is sensitive to only a narrow band of the electromagnetic spectrum (approximately 400-700 nanometers). Within this range:

- **Three cone types** with peak sensitivities at different wavelengths:
  - S-cones (short wavelength): ~420 nm (blue).
  - M-cones (medium wavelength): ~530 nm (green).
  - L-cones (long wavelength): ~560 nm (red/yellow-green).

- Color perception results from the relative activation of these three cone types.
- Sensitivity distribution is not uniform across the visible spectrum.

#### Saccadic Eye Movements

**Saccades**: Rapid eye movements that reposition the fovea to different points of interest.

Key characteristics:
- Eyes naturally prefer looking straight ahead.
- Pro-saccades: Moving toward a target.
- Anti-saccades: Moving away from a target (more difficult).
- Visual processing is suppressed during saccades.
- Implications for visualization: Minimize need for extensive scanning.

### 2. The Stages of Visual Processing

How photons become meaningful information through the visual processing pipeline.

#### Visual Pathways in the Brain

**From Eye to Brain:**
1. Photoreceptors (rods and cones) convert light to neural signals.
2. Signals processed through retinal layers.
3. Information transmitted via optic nerve.
4. Processing in visual cortex (V1/V2).
5. Higher-level processing in specialized areas (V3, V3A, V4, V5/MT).

**Two Primary Visual Pathways:**

1. **Dorsal Pathway ("Where")**:
   - Processes spatial location and motion.
   - Helps with spatial awareness and navigation.
   - Important for understanding position-based encodings.

2. **Ventral Pathway ("What")**:
   - Processes object recognition and identification.
   - Face and object recognition areas.
   - V4 particularly involved in color processing.
   - Important for understanding form-based encodings.

#### Two Processing Modes

**Feature-Driven (Bottom-Up) Processing:**
- Automatic, fast processing based on visual features.
- Driven by properties of the stimulus itself.
- Operates without conscious attention.
- Foundation of preattentive features.

**Context-Driven (Top-Down) Processing:**
- Influenced by knowledge, expectations, and context.
- Requires cognitive effort.
- Can override or modify bottom-up processing.
- Explains why context matters in interpretation.

### 3. Contrast and Relative Processing

How relative processing becomes important to visual understanding.

#### The Role of Contrast

**Key Principle:** Visual perception is fundamentally relative, not absolute.

What we perceive depends heavily on surrounding context. The visual system is optimized for detecting differences and edges rather than absolute values.

#### Visual Illusions Demonstrating Relative Processing

**Checker Shadow Illusion:**
- Squares A and B appear to be different shades.
- They are actually the same luminance.
- Context (shadow, surrounding checkerboard pattern) changes perception.
- Demonstrates: The brain interprets values relative to their surroundings.

**Mach Bands:**
- Perceived light and dark bands at boundaries between gradients.
- Not actually present in the stimulus.
- Result of lateral inhibition in visual processing.
- Demonstrates: Visual system enhances edge detection.

**Railroad Track Illusion:**
- Two identical yellow bars appear different sizes.
- Perspective cues affect size perception.
- Context creates expectations that override actual measurements.
- Demonstrates: Top-down processing influences perception.

#### Design Implications

**Emphasizing Relative Comparisons:**
- Have visual elements touch each other or share backgrounds.
- Removes consistent reference frame.
- Emphasizes differences between adjacent values.
- Useful when relative comparison is the goal.

**Emphasizing Absolute Values:**
- Use borders or consistent backgrounds.
- Provides stable reference frame.
- Allows for absolute value extraction.
- Useful when specific values need to be read accurately.

**Ensuring Sufficient Contrast:**
- If reliable reading of figures is required, ensure sufficient contrast to background.
- Important for accessibility.
- Will be revisited in accessibility lecture.

### 4. Preattentive Features

Visual properties that can be detected quickly and automatically without conscious scanning.

#### What Are Preattentive Features?

**Definition:** Visual properties that can be processed in parallel across the visual field, allowing rapid detection (typically < 250 milliseconds) without focused attention.

**Why They Matter:**
- Reduce cognitive load.
- Enable quick pattern detection.
- Avoid slow serial scanning.
- Work with limited visual memory (approximately 4 items).

#### Categories of Preattentive Features

**1. Color**
- Hue (color identity).
- Saturation (color intensity).
- Brightness/luminance.

Examples:
- Spotting a red circle among gray circles.
- Identifying a dark element among light elements.

**2. Form**
- Shape (circle, square, triangle).
- Size (length, area).
- Orientation (angle, tilt).
- Enclosure.
- Line width.
- Curvature.

Examples:
- Finding a tilted square among aligned squares.
- Spotting a circle among squares.
- Identifying a larger element among smaller ones.

**3. Position** (Saved for later discussion)
- Spatial location.
- Proximity.
- Alignment.

**4. Motion** (Saved for game design/interactivity section)
- Flicker.
- Direction of movement.

#### Important Notes on Preattentive Features

- The exact list varies somewhat from author to author.
- Research continues to refine our understanding.
- Effectiveness can depend on:
  - Number of distractors.
  - Degree of difference.
  - Combination of features (can interfere with each other).

## In-Class Activities

**Dataset:** California universities with graduation rates and annual costs

| School | Graduation Rate | Annual Cost |
|--------|----------------|-------------|
| Santa Clara University | 92% | $44,000 |
| Stanford University | 97% | $11,000 |
| California Institute of Technology | 94% | $17,000 |
| UC Berkeley | 94% | $17,000 |
| USC | 93% | $29,000 |
| UC Davis | 89% | $16,000 |
| Loyola Marymount University | 82% | $45,000 |
| San Jose State University | 75% | $14,000 |
| UC Santa Barbara | 86% | $15,000 |
| UC Irvine | 87% | $12,000 |
| UCLA | 93% | $16,000 |
| CA State Sacramento | 70% | $11,000 |

**Task:** Work with a partner to use preattentive features to highlight UC Berkeley in a visualization.

**Objective:** Practice applying preattentive features concepts by creating a visualization that makes Berkeley stand out quickly without requiring scanning.

## Looking Ahead

**Science 2 (Lecture 7):**
- More on preattention and color vision.
- Gestalt principles.
- Color spaces and perceptually consistent color schemes.

**Skills Labs:**
- Playing with visual processing.
- Exploring form, motion, and interaction in code.
- Building on Sketchingpy foundations.

**Formalizing Glyphs (Lecture 11):**
- Encoding: how we put information into graphics.
- Decoding: how our brains extract that information.
- Revisiting dimensions and attributes.

## Activities
As before, continue what you started in class by reviewing these additional materials and activities.

### Lecture Video
[Watch Lecture 6: Visualization as Science 1 on Vimeo](https://vimeo.com/1055340727)

### Assignment
Plot job satisfaction from the Stack Overflow Developer Survey using your preferred software. This can be done in spreadsheet software if desired! Your plot could be a bar chart, a scatterplot, a heatmap, etc. You don't need to plot all variables but, instead, can focus on a small subset of interest. Please provide 2 - 4 sentences describing how this representation uses pre-attentive features. You may use a [simplified dataset](/support/stackoverflow.xlsx) prepared for you or the [original full dataset from Stack Overflow](https://survey.stackoverflow.co).

### Reading
We are getting a look at the Gestalt Principles through [Gestalt - The Parts and the Whole by Extra Credits](https://youtu.be/c1qdyszaeTU?feature=shared).

### Links
- [The evolution of the human eye (shown in class)](https://www.youtube.com/watch?v=qrKZBh8BL_U)

## Citations

[1] B. Adhikari, "Marey's train schedule," University of Missouri Saint Louis, 2021. Available: https://badriadhikari.github.io/data-viz-workshop-2021/minards/

[2] S. Bell, "Introduction and Perceptual Elements of Colour," University of Saskatchewan. Available: https://openpress.usask.ca/introgeomatics/chapter/introduction-and-perceptual-elements-of-colour/

[3] J. Harvey, "The evolution of the human eye," TED Ed, 2015. Available: https://www.youtube.com/watch?v=qrKZBh8BL_U

[4] D. Camors, Y. Trotter, P. Pouget, S. Gilardeau & J. Durand, "Visual straight-ahead preference in saccadic eye movements," *Nature Communications*, 2016. Available: https://www.nature.com/articles/srep23124

[5] OSC Rice, "Vision," Washington State University. Available: https://opentext.wsu.edu/psych105nusbaum/chapter/vision/

[6] "Vision," CourseHero. Available: https://www.coursehero.com/study-guides/wmopen-psychology/outcome-vision/

[7] E. Adelson, "Checker shadow illusion," Wikimedia, 2018. Available: https://en.wikipedia.org/wiki/Checker_shadow_illusion#/media/File:Checker_shadow_illusion.svg

[8] DancingPhilosopher, "Mach Bands," Wikimedia, 2012. Available: https://en.wikipedia.org/wiki/Optical_illusion#/media/File:Mach_bands_-_animation.gif

[9] US Department of Education, "College Scorecard," US Department of Education. Available: https://collegescorecard.ed.gov/search/?sort=salary:desc&page=0&state=CA

[10] C. Ware, *Information Visualization: Perception for Design*. MK Press.

[11] C. Ware, *Visual Thinking for Design*. MK Press.
