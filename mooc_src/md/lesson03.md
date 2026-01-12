# Lesson 3: Skills Lab 1
Hello Creative Python!

## Objective
Gain foundational Python skills and learn creative coding techniques through browser-based tutorials to prepare for data visualization work.

## Outline
This hands-on session introduces Skills Lab 1, which provides practical Python instruction through two sequential tutorials designed for different experience levels. Both tutorials use browser-based environments requiring no local installation.

### Tutorial structure
Skills Lab 1 offers two complementary tutorials with distinct entry points.

  - Tutorial 1 is oriented towards those with less prior Python experience.
  - Tutorial 2 should be accessible after Tutorial 1 but may be quick for those with Python expertise.
  - Goal is to complete tutorials 1 and 2.
  - All tutorials available at https://mooc.interactivedatascience.courses/labs.

### Technical setup
Both tutorials run entirely in the browser with no installation required.

  - Tutorial 1 uses Jupyter Lite for an interactive Python learning environment.
  - Tutorial 2 uses the Sketchingpy Sketchbook for creative coding.
  - You only need a web browser to access both environments.
  - No local software installation or configuration needed.

### Sketchingpy code example
The lecture demonstrates basic Sketchingpy syntax for creating interactive graphics.

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

This:

  - Creates a drawing canvas (sketch).
  - Draws static elements (lines).
  - Responds to user input (mouse position).

### Flipped classroom approach
This lecture follows a flipped classroom model to support hands-on exploration.

### Connection to course themes
These exercises build technical foundations supporting the four perspectives introduced in Lecture 1.

  - Data Visualization as Representation: Learning to map data to visual elements using code.
  - Data Visualization as Task: Understanding how to build tools for specific user needs.
  - Data Visualization as Message: Creating graphics that convey meaning and emotion.
  - Data Visualization as Dialogue: Building interactive experiences that respond to user input.

### Creative coding philosophy
The use of Sketchingpy emphasizes code as a creative medium.

  - Code as a creative medium.
  - Iteration and experimentation.
  - Direct manipulation of visual elements.
  - Building custom visualizations beyond pre-made chart types.

### Additional resources
Optional materials to supplement your learning experience.

  - Lecture video available at https://vimeo.com/1049110017.
  - Optionally review A Byte of Python at https://python.swaroopch.com if you want to brush up on (or learn) the fundamentals of Python.
  - Skills Labs at https://mooc.interactivedatascience.courses/labs.
  - Sketchingpy Online Sketchbook at https://editor.sketchingpy.org/.

## Take Aways
Browser-based tools like Jupyter Lite and Sketchingpy make Python programming accessible with no installation barriers while creative coding provides a foundation for building custom data visualizations.

  - Tutorial 1 covers Python fundamentals for those with less prior experience.
  - Tutorial 2 introduces creative coding with Sketchingpy.
  - Both tutorials are browser-based with instant feedback and no setup required.
  - Code serves as a creative medium for direct manipulation of visual elements.
  - These technical skills support all four course perspectives on data visualization.

## Citations

[1] Thanks to https://badriadhikari.github.io/data-viz-workshop-2021/minards/ for imagery.

[2] A. Pottinger and Sketchingpy Contributors, "Sketchingpy," Sketchingpy Project, 2025. Available: https://sketchingpy.org/

[3] C. H. Swaroop, "A Byte of Python," 2003. Available: https://python.swaroopch.com
