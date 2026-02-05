# Forms

In our previous tutorial which rounded off Skills Labs 1 and 2, we explored object-oriented programming through building an interactive simulation. In this tutorial, we start Skills Lab 3 by looking at the first preattentive feature form. To explore this valuable tool for data visualization, we will investigate drawing different shapes. For the next few tutorials, it is recommened you use the Sketchingpy online sketchbook if you don't want to setup the library locally.

## Contents


- [Ellipse](#ellipse)

- [Rectangle](#rectangle)

- [Arc](#arc)

- [Line](#line)

- [Curve](#curve)

- [Shape](#shape)

- [Next](#next)



## Ellipse

We have seen some circles already but we will start our journey through forms with ellipses. An ellipse is a circular object that is a circle if the width and height are the same. These can be useful for structures like scatterplots or bubble plots. To explore our options, we will look at different "modes" for how to indicate the shape of an ellipse. Let's start by drawing a simple ellipse sized according to radius: import sketchingpy sketch = sketchingpy.Sketch2D(500, 500) sketch.set_ellipse_mode('radius') sketch.draw_ellipse(250, 250, 20, 20) sketch.show() Go ahead and run this a few times. Each time try changing the following: Change ellipse mode from radius to the following: radius, center, corner, corners. Change the parameters provided to draw_ellipse. For example, change from (250, 250, 10, 10) to (100, 150, 10, 20). How does the figure change as a result of your edits? The mode impacts how the parameters to draw_ellipse are interpreted. For example, in radius, center, and corner, the first two parameters are the position and last two parameters are the size. However, for corners, all four parameters are positions. Here is a comparison of all four modes: import sketchingpy sketch = sketchingpy.Sketch2D(500, 500) sketch.set_ellipse_mode('corners') sketch.draw_ellipse(250, 250, 20, 20) sketch.set_ellipse_mode('radius') sketch.draw_ellipse(250, 250, 20, 20) sketch.set_ellipse_mode('center') sketch.draw_ellipse(250, 250, 20, 20) sketch.set_ellipse_mode('corner') sketch.draw_ellipse(250, 250, 20, 20) sketch.show() To formalize what you just learned, check out the reference for set_ellipse_mode.


## Rectangle

Let's continue to rectangles. These can be useful for things like bar plots, butterfly plots, or treemaps. This works similarly to ellipses and, even though it seems a little counter-intutitive at first, these can also have radius. import sketchingpy sketch = sketchingpy.Sketch2D(500, 500) sketch.set_rect_mode('radius') sketch.draw_rect(250, 250, 20, 20) sketch.show() Let's do the same experiments as before: Change rect mode from radius to the following: radius, center, corner, corners. Change the parameters provided to draw_rect. For example, change from (250, 250, 10, 10) to (100, 150, 10, 20). Once again, let's try comparing by piling these rectangles on top of each other. import sketchingpy sketch = sketchingpy.Sketch2D(500, 500) sketch.set_rect_mode('corners') sketch.draw_rect(250, 250, 20, 20) sketch.set_rect_mode('radius') sketch.draw_rect(250, 250, 20, 20) sketch.set_rect_mode('center') sketch.draw_rect(250, 250, 20, 20) sketch.set_rect_mode('corner') sketch.draw_rect(250, 250, 20, 20) sketch.show() Once again, see the reference for set_rect_mode.


## Arc

I want to get to custom shapes in a moment but there's one last element to put into your tool chest. A quick glance at the chart wizard in spreadsheet software might make it seem like arcs aren't that important but, on the contrary, they can be used for many very useful structures even if they are less common outside of a pie chart. Indeed, arcs are an essential ingredient in arc diagrams, sunbursts, chord diagrams, and doughnut charts among others. Start with this code which draws a simple arc: import sketchingpy sketch = sketchingpy.Sketch2D(500, 500) sketch.set_ellipse_mode('radius') sketch.set_angle_mode('degrees') sketch.draw_arc(250, 250, 40, 40, 0, 90) sketch.show() Now, let's do a similar investigation as we did for ellipses and rectangles: Change arc mode from radius to the following: radius, center, corner, corners. Change the parameters provided to draw_arc. Learn more at the draw_arc documentation. Note that we are using degrees here to specify angles. You can change to radians using set_angle_mode.


## Line

So far, we've worked with pre-defined shapes. However, Sketchingpy lets us make new forms as well. To explore how we can go about creating these shapes, let's briefly return to draw_line as we saw in previous tutorials. Here's an example: import sketchingpy sketch = sketchingpy.Sketch2D(500, 500) sketch.draw_line(230, 270, 270, 270) sketch.show() However, let's do this another way. We will see why this might help in a moment: import sketchingpy sketch = sketchingpy.Sketch2D(500, 500) shape = sketch.start_shape(230, 270) shape.add_line_to(270, 270) shape.end() sketch.draw_shape(shape) sketch.show() While this seems like extra code to achieve the same result at first, let's take this one step further with multiple connected line segments which could be useful for things like line charts and area plots or custom forms. import sketchingpy sketch = sketchingpy.Sketch2D(500, 500) shape = sketch.start_shape(230, 270) shape.add_line_to(270, 270) shape.add_line_to(250, 230) shape.end() sketch.draw_shape(shape) sketch.show() Note that Sketchingpy tries to color in the shape to make a figure. If you want to stop that, use sketch.clear_fill before calling sketch.draw_shape but we will investigate that more later.


## Curve

Some charts like Sankey Diagrams require non-arc curves which are very often achieved through bezier curves which have two "control points" which you can think of as "pulling" the edge away from a straight path from start to finish. We can draw those too! Let's modify our shape just a little bit: import sketchingpy sketch = sketchingpy.Sketch2D(500, 500) shape = sketch.start_shape(230, 270) shape.add_line_to(270, 270) shape.add_bezier_to(280, 250, 250, 230, 270, 210) shape.end() sketch.draw_shape(shape) sketch.show() Try changing the parameters a bit but also see the documentation for add_bezier_to.


## Shape

Now we can tie it all together. Let's make a custom shape (triangle) and put it next to some of the prebuilt shapes (circle and square): import sketchingpy sketch = sketchingpy.Sketch2D(500, 500) sketch.set_ellipse_mode('radius') sketch.draw_ellipse(150, 250, 20, 20) shape = sketch.start_shape(230, 270) shape.add_line_to(270, 270) shape.add_line_to(250, 230) shape.close() sketch.draw_shape(shape) sketch.set_rect_mode('radius') sketch.draw_rect(350, 250, 20, 20) sketch.show() Note that there are two ways to finish a shape: end or close. Try changing close to end to learn more.


## Next

We have some shapes! Now, continue on to Tutorial 5 to learn about our next preattentive feature: color and styling.




## Citations


- A. Pottinger, "Sketchingpy." Sketchingpy Project, 2024. [Online]. Available: https://sketchingpy.org/

- R. Fong, "Bezier curves." Rflog, 2023. [Online]. Available: https://rfong.github.io/creative-coding/bezier/

- Y. Holtz, "From Data to Viz." Data to Viz, 2018. [Online]. Available: https://www.data-to-viz.com/

- Ferdio, "Data Viz Project." Ferdio, n.d. [Online]. Available: https://datavizproject.com/

