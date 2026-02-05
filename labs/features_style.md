# Color and Style

In our previous tutorial which explored form as a preattentive feature, we investigated drawing different shapes. In this tutorial, we continue Skills Lab 3 by looking at our next preattentive features color. Indeed, color is one part of a broader set of glyph attributes often referred to simply as style. This suite of options can help as important encoding device and, when used together with other preattentive features, can help increase data density.

## Contents


- [Hex Codes](#hex)

- [Fill](#fill)

- [Transparency](#transparency)

- [Stroke](#stroke)

- [Weight](#weight)

- [Context](#context)

- [Next](#next)



## Hex Codes

Our glyphs can actually have multiple potential colors at the same time. However, the first step is finding the color we want. We discussed some options in class: ColorBrewer and I Want Hue both provide good options. If you have Python installed on your machine, you might also take a look at Viscm. Finally, if you just need to manipulate some colors, a great tool is HSL Color Picker, which can work on multiple color spaces at the same time.


## Fill

The easiest place to start for styling in Sketchingpy is the fill color for a shape. Let's use circles to demonstrate! import sketchingpy sketch = sketchingpy.Sketch2D(500, 500) sketch.set_fill("#a6cee3") sketch.draw_ellipse(150, 250, 100, 100) sketch.clear_fill() sketch.draw_ellipse(250, 250, 100, 100) sketch.set_fill("#b2df8a") sketch.draw_ellipse(350, 250, 100, 100) sketch.show()


## Transparency

With our circles overlapping, we notice that what is drawn first goes at the bottom. We can control transparency to create layered effects. Learn more about transparency and the alpha channel.


## Stroke

In addition to fill, shapes can have a stroke or outline. Learn how to control stroke colors and create shapes with just outlines.


## Weight

The thickness of strokes can be controlled with weight settings. This is useful for emphasis and visual hierarchy.


## Context

Color choices should consider context, accessibility, and cultural meanings. Learn about best practices for using color in visualization.


## Next

Continue on to Tutorial 6 to learn about position as a preattentive feature.




## Citations


- A. Pottinger, "Sketchingpy." Sketchingpy Project, 2024. [Online]. Available: https://sketchingpy.org/

- C. Brewer, "ColorBrewer 2.0." [Online]. Available: https://colorbrewer2.org/

- HSL Color Picker. [Online]. Available: https://hslpicker.com/

