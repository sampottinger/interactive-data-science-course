# Lecture 3: Hello Creative Python

**Stat 198: Interactive Data Science and Visualization**
**Instructor:** A Samuel Pottinger
**Original Instruction Date:** January 29, 2025

## Description

A hands-on first look at how we can use Python for creative coding. This lecture introduces Skills Lab 1, which focuses on learning Python fundamentals and creative coding using Sketchingpy. Students work through browser-based tutorials that require no local installation.

## Key Takeaways

This lecture introduces practical Python programming for data visualization through accessible, browser-based tools.

### Browser-Based Development
Both Jupyter Lite and the Sketchingpy Sketchbook represent modern approaches to programming education:

- No installation barriers.
- Instant feedback.
- Accessible from any device.
- Reduced technical setup time.

### Sketchingpy Code Example
The lecture demonstrates basic Sketchingpy syntax for creating interactive graphics:

```python
import sketchingpy
import time

sketch = sketchingpy.Sketch2D(500, 400)

center_x = 500 / 2
center_y = 400 / 2
end_x = 100
end_y = 50
sketch.draw_line(center_x, center_y, end_x, end_y)

def draw_moving_line(target):
    mouse = sketch.get_mouse()
    sketch.draw_line(250, 200, mouse.get_pointer_x(), mouse.get_pointer_y())

sketch.on_step(draw_moving_line)

sketch.show()
```

This example illustrates:

- Creating a drawing canvas (sketch).
- Drawing static elements (lines).
- Responding to user input (mouse position).
- Creating interactive animations.

## Skills Lab 1 Overview

Skills Lab 1 provides a practical introduction to Python programming for data visualization through two sequential tutorials designed to accommodate different experience levels.

### Tutorial Structure

**Tutorial 1: Python Fundamentals**
- Oriented towards learners with less prior Python experience.
- Uses Jupyter Lite for an interactive learning environment.
- Covers basic Python concepts needed for data visualization.

**Tutorial 2: Creative Coding with Sketchingpy**
- Should be accessible after completing Tutorial 1.
- May be quick for those with Python expertise.
- Uses the Sketchingpy sketchbook environment.
- Introduces creative coding concepts for visualization.

### Technical Setup

**No Installation Required**
- All tutorials run in a web browser.
- Tutorial 1 uses Jupyter Lite.
- Tutorial 2 uses the Sketchingpy Sketchbook.
- Both environments are browser-based and require no local setup.

**Access Point**
- All tutorials available at: https://mooc.interactivedatascience.courses/labs.

### Learning Objectives

The goal for this session is to:
- Complete Tutorials 1 and 2.
- Gain foundational Python skills.
- Learn basic creative coding techniques.
- Prepare for more advanced visualization work.

## Approach
This lecture follows a flipped classroom approach where:

- Students work through tutorials at their own pace
- Hands-on learning takes precedence over passive lectures
- Peer support is available through dedicated help channels
- The instructor provides guidance as needed

## Connection to Course Themes
As you take this first step into code for this course, consider how these exercises relate to broader courase objectives.

### The Four Perspectives Applied
This skills lab builds technical foundations that support all four perspectives introduced in Lecture 1:

1. **Data Visualization as Representation**: Learning to map data to visual elements using code
2. **Data Visualization as Task**: Understanding how to build tools for specific user needs
3. **Data Visualization as Message**: Creating graphics that convey meaning and emotion
4. **Data Visualization as Dialogue**: Building interactive experiences that respond to user input

### Creative Coding Philosophy
The use of Sketchingpy emphasizes:

- Code as a creative medium
- Iteration and experimentation
- Direct manipulation of visual elements
- Building custom visualizations beyond pre-made chart types

## Activities
As always, we have some additional items available to supplement your experience of these materials.

### Lecture Video
[Watch Lecture 3: Hello Creative Python on Vimeo](https://vimeo.com/1049110017)

### Assignment
Revisit the visualization from the last exercise. What might the 4 perspectives say about this visualization?

- What visual encoding devices are used?
- What task or user journey is being accomplished through the piece?
- Does the piece try to also convey an emotion and, if so, how?
- Does the piece invite the reader to reach new their own conclusions about the data and, if so, how?

Please write 4 - 8 sentences.

### Reading
Optionally review [A Byte of Python](https://python.swaroopch.com) if you want to brush up on (or learn) the fundamentals of Python.

### Links
- [Skills Labs](https://mooc.interactivedatascience.courses/labs)
- [Sketchingpy Online Sketchbook](https://editor.sketchingpy.org/)

## Citations

[1] Thanks to https://badriadhikari.github.io/data-viz-workshop-2021/minards/ for imagery.
