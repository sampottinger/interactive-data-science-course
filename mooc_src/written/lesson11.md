# Lecture 11: Formalizing Glyphs

**Stat 198: Interactive Data Science and Visualization**
**Instructor:** A Samuel Pottinger
**Original Instruction Date:** March 3, 2025

## Description

Consider essential empirical evidence regarding encoding devices from Cleveland and McGill. Also, examine important techniques that allow us to re-use high value encoding devices. Specifically, learn more about dual axes, shared axes, and direct labeling.

## Key Takeaways

This lecture transitions from understanding the basic ingredients of visualization to knowing when and how to use them effectively. It provides empirical evidence for choosing encoding devices and practical techniques for working within design constraints.

### Cleveland and McGill's Hierarchy of Encodings

From most to least accurate for quantitative perception:

1. **Position on common scale** (highest accuracy) - underpins scatter plots and bar charts
2. **Position on non-aligned scales** - still highly accurate
3. **Length** - consistently accurate, especially when aligned on common axis
4. **Direction (slope) and Angle** - moderate accuracy, varies with orientation
5. **Area** - useful for contextualizing metrics, but note area vs radius considerations
6. **Volume** - generally performs poorly, possibly due to 3D representation in 2D media
7. **Curvature** - inconsistent performance
8. **Shading** - limited quantitative value
9. **Color saturation** (lowest accuracy) - better for branding and qualitative groups

## Theory and Examples
The long awaited Cleveland and McGill lecture!

### 1. Cleveland and McGill: Ranking of Encodings

**The Premise**: Moving from meeting the ingredients to understanding when to use them.

**Key Findings**:
- **Position is paramount**: The highest accuracy encoding device underpins scatter plots and aligns with preattentive features and Gestalt Principles.
- **Length is reliable**: Typically has an easy fix - align against a common axis for consistency.
- **Direction and angle vary**: Evidence shows we perform better with angles closer to cardinal directions, which is why pie charts may perform relatively poorly.
- **Area has limitations**: Good for less important "contextualizing" metrics. Has the issue of area vs radius perception.
- **Volume rarely works well**: May be partially due to 3D representation within 2D media.
- **Color is unreliable for quantitative data**: Better for branding, emotion, and aesthetic than conveying quantitative information. May serve a purpose for a limited number of qualitative groups. Lightness generally better than hue.

### 2. Group Activity: Comparing Graphic Accuracy

The lecture included hands-on comparison of different visualization approaches:

**Comparison 1**: Bar chart vs Pie chart
- Bar charts use position/length (high accuracy encodings)
- Pie charts use angle (moderate accuracy, varies by position)

**Comparison 2**: Bar chart vs Table with color encoding
- Demonstrates how position encoding outperforms color-based encoding for quantitative comparison

**Comparison 3**: Bubble chart vs Heatmap
- Explores the challenges of area encoding versus position and color

**Comparison 4**: Bar chart vs Bubble chart (horizontal layout)
- Compares length encoding versus area encoding for the same data

**Key Insight**: Visualizations using higher-ranked encoding devices (position, length) consistently outperform those using lower-ranked devices (area, angle, color) for accurate data reading.

### 3. Working Within Limitations

When we can't always use the highest-accuracy encoding devices, we have techniques to maximize effectiveness:

#### Dual Axes
- Allows plotting of two variables with different scales on the same chart
- Uses two y-axes (left and right) with a shared x-axis
- Example: Age vs Years of Coding and Satisfaction
  - Left axis: Average Years of Coding (0-60)
  - Right axis: Average Satisfaction Score (0.00-1.00)
  - Shared x-axis: Age Group (20-60+)
- Enables comparison of trends between variables with different units

#### Shared Axes
- Multiple visualizations share common axes to facilitate comparison
- Creates visual connections between related data
- Example: Stack Overflow Developer Survey 2024 visualization showing:
  - Satisfaction scores across age groups
  - AI usage patterns
  - Years of programming experience
  - Count distributions
- Features:
  - Main plot with clear focus
  - Supporting plots aligned on shared scales
  - Direct visual comparison enabled by alignment
  - Intentional labeling highlighting key findings (e.g., "25% of non-AI users score 0.8", "Avg satisfaction for 65+: 0.8")

#### Direct Labeling
- Placing data values directly on visualization elements
- Reduces cognitive load of referencing separate legends or axes
- Two approaches demonstrated:
  1. Without direct labels: Requires readers to reference y-axis
  2. With direct labels: Percentages displayed on bars (1%, 3%, 4%, 7%, 13%, 22%, 26%, 12%, 8%)
- Benefits:
  - Faster comprehension
  - Reduced eye movement
  - More precise value communication
  - Better accessibility

### 4. Revisiting Chart Junk: Keeping Channels Clear

Building on Tufte's concepts, the lecture explores how to maintain clear visual channels:

**The Problem**: Visual clutter can interfere with encoding devices
- Example: Overlapping bars in grouped bar charts can create visual confusion
- Unnecessary grid lines can compete with data

**Solutions**:
1. **Simplify visual elements**: Remove decorative elements that don't encode data
2. **Use negative space**: Strategic whitespace improves clarity
3. **Align on grids**: Subtle grid lines support reading without dominating
4. **Separate groups clearly**: Ensure distinct visual separation between categories

**Evolution Shown**:
- Initial visualization: Cluttered grouped bars with overlapping elements
- Improved version: Shared axes layout with clear separation, intentional labeling, and clean presentation

**Key Principle**: Every visual element should either encode data or support data reading. Remove everything else.

### 5. Upcoming Assignment Guidance

The lecture previewed design principles for future assignments:

1. **Intentional labeling**: Place labels strategically to guide reader attention
2. **Removal of chartjunk**: Eliminate unnecessary visual elements
3. **Negative space grid**: Use whitespace effectively with subtle supporting gridlines
4. **Shared axes styling**: Align multiple views to enable comparison
5. **Future consideration**: Interaction to reduce visual complexity

### 6. Example from Current Events

**New York Times Opinion Piece** (Feb 28, 2025): "10 Columnists and Writers Rate What Mattered in Trump's First Full Month"

- Uses a two-dimensional scatter plot approach
- Axes:
  - Horizontal: Negative Impact to Positive Impact
  - Vertical: Less Consequential to More Consequential
- Topics plotted as circles with direct labels (Ukraine, DOGE, Tariffs, Immigration, etc.)
- Demonstrates effective use of position encoding for two dimensions plus categorical labeling

## Connection to Course Themes

### Primitives Section Context

This lecture concludes the "Primitives" section of the course, which focused on:
- Perception and cognitive science for visualization
- Understanding how the human visual system processes information
- Evidence-based design decisions
- Fundamental building blocks (glyphs, encoding devices)

### Looking Ahead

Moving from primitives to combination:
- Next sections will explore how to combine these principles
- Integration with human-centered design
- Application to specialized data types (geospatial, graphs)
- Incorporation of interactivity and game design concepts

## Activities
As always, we have some follow up activities to supplement the lecture itself.

### Lecture Video
[Watch Lecture 11: Formalizing Glyphs on Vimeo](https://vimeo.com/1061901487)

### Assignment

We have a fantastic opportunity to apply recent class concepts through an exploration of US Census American Community Survey (2024) results.

**Introduction**: We will be working with a dataset derived from US Census data. Though originally designed for use in understanding "income gaps" between different groups of people, it can also be used to explore other questions about economics and work. It can explore differing levels of participation in different occupations, unemployment rates, and regional trends. There are a lot of variables to explore! This project will provide a space to experiment with encoding devices, data density, preattentive features, and more.

**Objective**: Please visualize a subset of variables from this dataset. If using shared axes, please have a clear "main plot" from which those axes are shared. For this assignment, please include 4 or more variables. For example, you could visualize unemployment and wage (2 variables) by age and gender (2 variables). This would be a total of 4 variables (unemployment, wage, age, gender).

**Data**: You may use the [EPI Microdata Extracts](https://microdata.epi.org) directly but I recommend using the Income Gaps CSV instead to focus your time on the visual elements of this project. If you are using the [Income Gaps CSV file](https://incomegaps.com/data.csv), I also recommend using [data_model.py](https://github.com/sampottinger/incomegaps/blob/main/preprocess/data_model.py) as described in the [Income Gaps CSV documentation](https://github.com/sampottinger/incomegaps?tab=readme-ov-file#data). If using the online editor for Sketchingpy, just download [data_model.py](https://github.com/sampottinger/incomegaps/blob/main/preprocess/data_model.py) and add it to your sketchbook.

**Tech**: Though you may be able to complete Assignment 9 using prebuilt charts like through Matplotlib, you may find it more difficult to continue using it for later exercises where detailed control over each element of your graphic will be essential. Therefore, I recommend using Python and Sketchingpy. To help, see also [the code I used for my Stack Overflow Developers Survey example](https://gist.github.com/sampottinger/f69bd39def0cd05268d5a639d49f354e).

### Reading

Start taking a look through [https://www.data-to-viz.com](https://www.data-to-viz.com). We will dig in deeper together soon!

## Citations

[1] A. Pottinger, "TED Visualization," Gleap.org. Available: https://gleap.org/content/ted_visualization

[2] W. Cleveland and R. McGill, "Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods," *Journal of the American Statistical Association*, 1984. Available: https://www.jstor.org/stable/2288400

[3] "Stack Overflow Annual Developer Survey 2024," Stack Exchange Inc, 2024. Available: https://survey.stackoverflow.co/

[4] C. Ware, "Information Visualization: Perception for Design (Interactive Technologies)," Morgan Kaufmann, 2012.

[5] A. Cairo, "The Truthful Art," New Riders, 2016.

[6] NYT Opinion, "10 Columnists and Writers Rate What Mattered in Trump's First Full Month," *New York Times Company*, 2025. Available: https://www.nytimes.com/interactive/2025/03/01/opinion/trump-administration-first-month.html.
