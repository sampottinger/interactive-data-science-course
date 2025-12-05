# Lecture 5: Visualization as Design

**Stat 198: Interactive Data Science and Visualization**
**Instructor:** A Samuel Pottinger
**Original Instruction Date:** February 5, 2025

## Description

A look at some historic figures in data visualization along with a discussion of Tufte. Also, a look at some demonstrative examples to refine our language for discussing information design. All of this sets the stage for glyphs and our transition into cognitive and perception science.

## Key Takeaways

This lecture traces the historical evolution of data visualization and introduces foundational design principles while acknowledging their limitations.

1. **Historical Evolution**: Data visualization has evolved over centuries, with each pioneer contributing unique perspectives.
2. **Design Principles**: Tufte provided actionable guidelines that remain influential today.
3. **Critical Evaluation**: Understanding both the value and limitations of design principles.
4. **Empirical Foundation**: Modern visualization must be grounded in scientific understanding of human perception.
5. **Context Matters**: Who is remembered in history reflects systemic biases that we must acknowledge.

## Overview of Section 2: Primitives
We already got through the first section of the class! The course's second section introduces foundational concepts for understanding data visualization through multiple lenses:

- **Visualization as Design**: Investigating early design ideas that continue to shape data visualization and understanding how we arrived at current practices.
- **Visualization as Science 1**: Foundational cognitive and perception science principles and studies.
- **Visualization as Science 2**: Application of cognitive science and perception principles to data visualization.
- **Skills Labs**: Exploring the primitives available for drawing and how to draw with data.
- **Formalizing Glyphs**: Cleveland and McGill tie it all together with actionable visualization recommendations for using primitives.

## Today's Topics

1. **Pioneers of Data Visualization**: Important historical figures and pieces.
2. **Ideas of Tufte**: Overview of key concepts from Edward Tufte.
3. **Problematic Graphs**: Analysis of graphics with potential issues.
4. **After Tufte**: Evolution beyond Tufte's work and the foundation for the 4 perspectives.

## Pioneers of Data Visualization
This lecture provides a rapid overview of data visualization history - just one person per century. It's important to acknowledge who is remembered and who is left out of traditional historical narratives. The course will revisit history more thoroughly later.

### Michael Florent van Langren (1600s)

**Contribution**: Created the earliest known "statistical graphic" in 1644

**Work**: "Grados de la Longitud" - visualized different estimates of the distance from Toledo to Rome, representing uncertainty and variation in measurements. Though not as well-known as later pioneers, this work established the foundation for graphical representation of statistical data.

**Legacy**: Van Langren established visual representation for conveying numeric information.

### William Playfair (1700s)

**Contribution**: Often called the parent of modern data visualization

**Key Innovations**:
- Created common patterns used today, including the pie chart
- Popularized existing forms like the bar chart and area chart
- Demonstrated time series visualization with exports and imports

**Notable Work**: 1786 visualization showing "Exports and Imports to and from Denmark & Norway from 1700 to 1780", featuring dual area charts showing balance of trade.

**Legacy**: Playfair's innovations fundamentally shaped modern data visualization by creating and popularizing many chart types still in use today.

### Florence Nightingale (1800s)

**Contribution**: Pioneered graphical storytelling and data visualization for advocacy

**Notable Work**: "Diagram of the Causes of Mortality in the Army in the East" (1858)
- Rose diagram (coxcomb chart) showing causes of death during the Crimean War
- Demonstrated that epidemic diseases caused more deaths than battlefield injuries
- Effectively used data visualization for change and argument
- Influenced public health policy through compelling visual evidence

**Legacy**: Nightingale pioneered the use of data visualization as a tool for advocacy and policy change, demonstrating how visual evidence could drive meaningful social reform.

### W.E.B. Du Bois (1900s)

**Contribution**: Changed how we think about data visualization as message

**Key Impact**:
- Used data visualization in sociological settings to advocate for social justice
- Created innovative and artistic visualizations for the 1900 Paris Exposition
- Design ideas continue to influence modern data visualization
- Demonstrated the power of visualization to communicate about inequality and social issues

**Notable Work**: "Proportion of Freemen and Slaves Among American Negroes" - use of area and color to convey stark inequalities.

**Legacy**: Influential in establishing data visualization as a tool for social commentary.

### Donald Bitzer (Today)

**Contribution**: Pioneered ideas around interactive media and explorable explanations

**Key Innovation**: PLATO system in the 1960s
- Early computer-based education system
- Interactive simulations and visualizations
- 1960s precursor to work by Bret Victor
- Demonstrated potential of computational media for exploration and learning

**Legacy**: Established foundations for modern interactive data visualization and explorable explanations decades before they became mainstream.

## Edward Tufte and His Ideas

### Introduction to Tufte

Edward Tufte has been enormously influential in data visualization:

- Brought many people into information design through touring workshops and popular books.
- His perspective fundamentally shapes data visualization today.
- Many people now disagree with some of his ideas, but his influence is undeniable.
- His ideas should be understood as guidelines many follow as standard advice, not absolute rules.
- His concepts are readily applicable even with basic tools like Google Sheets.

### Tufte's Key Concepts

#### 1. Lie Factor

**Definition**:
```
Lie Factor = (size of effect shown in graphic) / (size of effect in data)
```

**Principle**: The visual representation should accurately reflect the magnitude of change in the underlying data. A lie factor significantly different from 1.0 indicates visual distortion.

**Example**: The famous fuel economy standards graphic from the New York Times (1978).

- Visual representation exaggerated the change in fuel standards.
- Area representation made small numerical differences appear dramatic.
- The length of the line representing 18 mpg (1978) was 0.6 inches.
- The length representing 27.5 mpg (1985) was 5.3 inches.
- This created a misleading visual impression of the rate of change.

#### 2. Chartjunk

**Definition**: Visual elements in a chart that don't convey data or assist comprehension.

**Examples**:

- Decorative icons or illustrations.
- Unnecessary 3D effects.
- Excessive grid lines.
- Ornamental borders or patterns.
- Pictorial representations that distort data.

**Principle**: Remove non-essential visual elements to let the data speak clearly. Each element should serve a purpose in conveying information.

#### 3. Data-Ink Ratio

**Definition**: The proportion of a graphic's ink devoted to displaying data.

**Formula Concept**:

```
Data-Ink Ratio = (Data-Ink) / (Total Ink Used)
```

**Principle**: Maximize the data-ink ratio by removing non-data ink where possible.

**Application**:

- Remove unnecessary grid lines.
- Eliminate redundant labels.
- Simplify axes where appropriate.
- Use direct labeling instead of legends when possible.
- Present data in its simplest effective form.

**Example**: Progression from a bar chart with full grid and axes to a minimalist table showing just the essential numbers.

#### 4. Data Density

**Definition**: The amount of data displayed per unit area of the graphic.

**Principle**: Increase data density within reason to show more information in less space.

**Benefits**:

- Allows comparison across more data points.
- Reveals patterns that might be hidden in sparse displays.
- Makes efficient use of reader's attention.

**Example**: Adding gas prices to the fuel standard chart.

- Shows relationship between two related variables.
- Uses dual y-axes (though this technique itself is debated).
- Provides richer context through additional data layer.

**Historical Example**: Sparklines and small multiples showing Euro foreign exchange rates across multiple currencies and time periods.

## Problematic Graphics: Group Activity

Examine "darts" (problematic visualizations) identified by Michael Friendly. These examples motivated Tufte's work on principles for effective data visualization.

### Purpose

- Identify common visualization mistakes
- Understand why certain design choices create confusion
- Develop critical eye for evaluating visualizations
- Apply Tufte's principles to real-world examples

### Activity Structure

- Groups examined different sections of problematic visualizations
- Each group selected a favorite example to share
- Class discussion of what makes these visualizations problematic
- Connection to Tufte's principles (lie factor, chartjunk, data-ink ratio, data density)

## The Legacy of Tufte

Tufte has been essential and wildly influential. However, there have been some efforts to reconsider his ideas has visualization has evolved.

### Critiques of Tufte

**Matthew Dunnigan** (Principal User Research Manager, Microsoft):

> "Specifically, it seems like he pulls some of his design principles out [of] thin air, and the design improvements they generate are not scientifically validated..."

### Key Limitations

1. **Lack of Empirical Validation**: Many of Tufte's principles were based on aesthetic judgment rather than controlled studies.
2. **Overemphasis on Minimalism**: Removing all "non-data ink" may sometimes reduce comprehension.
3. **Context Matters**: Different audiences and purposes may require different approaches.
4. **Message vs. Efficiency**: Sometimes "inefficient" designs create stronger emotional impact.

### Moving Forward: Bringing in Empirical Approaches

This lecture brings us to the doorstep of modern data visualization by:

1. **Establishing Historical Context**: Understanding where design principles originated.
2. **Introducing Design Vocabulary**: Lie factor, chartjunk, data-ink ratio, data density.
3. **Recognizing Limitations**: Acknowledging that aesthetic principles alone are insufficient.

**The Next Step**: Crossing the threshold into scientific understanding

- Cognitive and perception science principles.
- Empirical studies of encoding devices.
- Channel effectiveness research.
- Evidence-based design recommendations.

The following lectures will explore how scientific methods validate, refine, or challenge traditional design wisdom, culminating in one of the most important ideas: **channel effectiveness**.

## Activities
As before, continue what you started in class by reviewing these additional materials and activities.

### Lecture Video
[Watch Lecture 5: Visualization as Design on Vimeo](https://vimeo.com/1053582417)

### Assignment
Find another visualization but limit yourself to agencies and dedicated graphics teams within newsrooms. Examples: Periscopic, Stamen, Fathom, Accurat, or NYT Graphics. Please answer the following:
- Which encoding devices are used within this piece?
- What would Tufte say about the lie-factor, data-ink ratio, and data density?

Please write 4-8 sentences.

### Reading
Please start to explore the core essential concept of pre-attentive attributes through the reading at Kesavan (2018).

### Links
- [Darts (data visualization examples)](https://www.datavis.ca/gallery/lie-factor.php)
- [The Greatest Ever Infographic (shown in class)](https://youtu.be/3T7jMcstxY0?feature=shared)

## Citations

[1] B. Adhikari, "Marey's train schedule," University of Missouri Saint Louis, 2021. Available: https://badriadhikari.github.io/data-viz-workshop-2021/minards/

[2] M. van Langren, "Grados de la Longitud," 1644. Available: https://commons.wikimedia.org/wiki/File:Grados_de_la_Longitud.jpg

[3] J. Norman, "Michael Florent van Langren issues the Earliest Known Graph of Statistical Data," History of Information, 2013. Available: https://www.historyofinformation.com/detail.php?id=3415

[4] W. Playfair, "Time Series of Exports and Imports of Denmark and Norway," Commercial and Political Atlas, 2011. Available: https://en.wikipedia.org/wiki/William_Playfair#/media/File:Playfair_TimeSeries-2.png

[5] D. Bellhouse, "The Flawed Genius of William Playfair: The Story of the Father of Statistical Graphics," University of Toronto Press, 2023. Available: https://www.jstor.org/stable/10.3138/jj.6167271

[6] M. Callejon, "Masters series: William Playfair, the father of statistical graphics," Flourish, 2023. Available: https://flourish.studio/blog/masters-william-playfair-father-of-statistical-graphics/

[7] H. Hering, "Florence Nightingale Portrait," 1860. Available: https://en.wikipedia.org/wiki/Florence_Nightingale#/media/File:Florence_Nightingale_(H_Hering_NPG_x82368).jpg

[8] J. Mansky, "W.E.B. Du Bois' Visionary Infographics Come Together for the First Time in Full Color," Smithsonian Magazine, 2018. Available: https://www.smithsonianmag.com/history/first-time-together-and-color-book-displays-web-du-bois-visionary-infographics-180970826/

[9] University of Illinois, "Faculty portrait photograph of Professor of Electrical Engineering Donald Bitzer," University of Illinois, 1971. Available: https://archon.library.illinois.edu/archives/index.php?p=digitallibrary%2Fdigitalcontent&id=7887

[10] J. Scott, "5.08 of BBS: The Documentary," Textfiles, 2005. Available: https://en.wikipedia.org/wiki/PLATO_%28computer_system%29#/media/File:PLATO_chem_exp.jpg

[11] B. Leroy, "Review of Tufte's The Visual Display of Quantitative Information," Carnegie Mellon University, 2018. Available: https://benjaminleroy.github.io/pages/blog/public/post/2018/05/16/review-of-tufte-s-the-visual-display-of-quantitative-information/

[12] M. Friendly, "Darts," York University, 2025. Available: https://www.datavis.ca/gallery/lie-factor.php

[13] Princeton University, "Public Lectures: Edward Tufte (Photo)," Princeton University. Available: https://lectures.princeton.edu/lectures/2013/edward-tufte

[14] Union of Concerned Scientists, "Brief History of US Fuel Efficiency Standards," Union of Concerned Scientists, 2017. Available: https://www.ucsusa.org/resources/brief-history-us-fuel-efficiency

[15] N. Vega, "A gallon of gas was 65 cents in 1978—here's how much it cost every year since," CNBC, 2022. Available: https://www.cnbc.com/2022/04/13/how-much-gas-cost-every-year-since-1978.html

[16] M. Dunnigan, "Why Tufte is Wrong," Medium, 2014. Available: https://medium.com/@MattDuignan/why-tuftes-wrong-a9bd6a14ff8e

[17] B. Adhikari, "Data Density," University of Missouri Saint Louis, 2021. Available: https://badriadhikari.github.io/data-viz-workshop-2021/Tufte/Chapter_8/
