# Lecture 12: Patterns

**Stat 198: Interactive Data Science and Visualization**
**Instructor:** A Samuel Pottinger
**Original Instruction Date:** March 5, 2025

## Description

A tour through common chart types used for different situations as well as common terminology and a brief introductory mention of domains and tasks.

## Key Takeaways

This lecture provides a foundational understanding of data terminology, visualization patterns, and introduces the user-centered approach of domains and tasks. Students learn to select appropriate chart types based on the number and type of variables being visualized.

### Core Data Terminology

**Variables**
- The column names in a dataset
- Can be categorized as dimensions or measures

**Values**
- A value seen inside a cell

**Observations**
- Rows in a table
- Individual data points or records

**Dimensions**
- Variables by which observations are divided or segmented
- Categorical variables that organize data (e.g., gender, occupation, region)

**Measures**
- Numeric values which are encoded in visual channels
- Quantitative data that can be measured and compared (e.g., income, unemployment rate)

**Domains**
- The context of who the users are and what concepts define their problem area
- Encompasses user background, expertise, and domain-specific terminology
- Helps center visualization design around user needs

**Tasks**
- The specific questions users are trying to answer
- The insights, comparisons, and patterns users need to identify
- Drives selection of appropriate visualization patterns based on user goals

## Visualization Patterns by Variable Count

The lecture systematically explores visualization options as data complexity increases from one variable to seven variables.

### 1 Variable Visualizations

**Standard Patterns:**
- **Histogram**: Shows distribution of a single numeric variable (e.g., night price distribution of Airbnb apartments)
- **Pie/Donut Chart**: Displays categorical proportions

**Hierarchy/Graph Patterns:**
- **Circular Graph**: Shows relationships within a single hierarchical or network variable
- Useful for displaying connections and structure

### 2 Variable Visualizations

**Standard Patterns:**
- **Scatter Plot**: Shows relationship between two continuous variables (e.g., ground living area vs. sale price of apartments)
- **Bar Chart**: Compares a measure across categories (e.g., weapon quantity by country)

**Hierarchy/Graph Patterns:**
- **Treemap**: Displays hierarchical data with nested rectangles sized by value (e.g., Singapore export products)
- **Sunburst Chart**: Radial hierarchical visualization
- **Chord Diagram**: Shows flows and relationships between entities
- **Arc Diagram**: Displays connections between nodes

### 3 Variable Visualizations

**Standard Patterns:**
- **Bubble Chart**: Scatter plot with third dimension encoded as size (e.g., population shown through bubble size)
- **Grouped/Stacked Bar Chart**: Compares measures across two categorical dimensions
- **Marimekko Chart**: Variable-width stacked bar chart showing multiple dimensions

**Hierarchy/Graph Patterns:**
- **Sankey Diagram**: Flow diagram showing quantities moving through a system (e.g., UK energy flows from sources to uses)
- **Enhanced Treemap**: Treemaps with color as additional encoding

### 4 Variable Visualizations

**Parallel Coordinates Plot**
- Multiple vertical axes representing different variables
- Lines connect values across axes for each observation
- Example: Iris dataset showing Petal.Length, Petal.Width, Sepal.Length, Sepal.Width colored by species (setosa, versicolor, virginica)

### Beyond 4 Variables: The Grammar is Limited

For higher density plots (5+ variables), traditional chart types become insufficient. Alternative approaches include:

- **Shared/Dual Axes**: Multiple measures sharing axis space
- **Novel Representations**: Custom visual encodings designed for specific data
- **Interactivity**: User-controlled filtering and exploration
- **Multiple Coordinated Views**: Separate but linked visualizations
- **Small Multiples**: Arrays of similar charts showing different slices

## Re-centering the User: Domains and Tasks

The lecture introduces a crucial shift from pattern selection to user-centered design through two key concepts:

### Domains

**Definition:** Who are the users and what are the concepts of the problem area you are working in?

**Key Questions:**
- What is the user's background and expertise?
- What domain-specific terminology do they use?
- What concepts are central to their work?

**Example:** For a Census data visualization:
- Users: Researchers studying economic inequality
- Domain concepts: median income, overall unemployment, occupation categories, demographic groups (gender, race)

### Tasks

**Definition:** What questions is the user trying to answer?

**Key Questions:**
- What insights are users seeking?
- What comparisons do they need to make?
- What patterns are they trying to identify?

**Example Tasks:**
- "Which group had the largest gender gap by income?"
- "Which occupation saw the largest unemployment?"
- "How did income inequality change over time?"

### Contextualizing Patterns Through Users

The same data can be visualized differently depending on user tasks. Rather than asking "Plot median income, unemployment, and number of people by occupation, gender, and race each year from 2015 to 2025," we should ask:

1. **Who needs this?** (Domain)
2. **Why do they need it?** (Tasks)
3. **How can visualization best support their work?** (Pattern selection)

This approach connects to Tamara Munzner's "What/Why/How" framework, which will be explored in greater depth in Lecture 14.

## Progressive Complexity Examples

The lecture walks through a series of increasingly complex visualization challenges:

1. **Example 1:** Plot median income by occupation (1 dimension, 1 measure)
   - Simple bar chart

2. **Example 2:** Plot median income by occupation and gender (2 dimensions, 1 measure)
   - Grouped or side-by-side bar chart

3. **Example 3:** Plot median income and unemployment by occupation and gender (2 dimensions, 2 measures)
   - Multiple charts, dual axes, or color encoding

4. **Example 4:** Plot median income, unemployment, and number of people by occupation and gender (2 dimensions, 3 measures)
   - Combination of size, color, and position encoding

5. **Example 5:** Plot median income, unemployment, and number of people by occupation, gender, and race (3 dimensions, 3 measures)
   - Small multiples, faceting, or interactive filtering

6. **Example 6:** Plot median income, unemployment, and number of people by occupation, gender, and race in 2015 vs 2025 (4 dimensions, 3 measures)
   - Temporal comparison requiring side-by-side views or animation

7. **Example 7:** Plot median income, unemployment, and number of people by occupation, gender, and race each year from 2015 to 2025 (4 dimensions including time, 3 measures)
   - Requires interactivity, animation, or highly sophisticated encoding strategies

## Activities
Continue your understanding of the material with supplemental reading and activities.

### Lecture Video
[Watch Lecture 12: Patterns on Vimeo](https://vimeo.com/1062955146)

### Group Activity
Students engaged in an in-class activity choosing appropriate visualization patterns for progressively complex problems, working through the examples listed above.

### Assignment
Continue the Census visualization started in the previous lecture. Previously, students visualized 4 or more variables. For this assignment:
- Visualize 6 or more variables from the Census dataset
- Consider which patterns best serve the user's tasks
- Optional reference: [Code example on GitHub](https://github.com/sampottinger/census-example-sketchingpy) (BSD-3-Clause license)
- Optional video walkthrough: [Vimeo walkthrough](https://vimeo.com/1064872882)

### Reading
Please take a look at a discussion of [Dear Data at Eyeo (2015)](https://vimeo.com/133608605). This reading explores how personal data can be represented through hand-drawn visualizations, connecting to themes of novel representations and the designer as author.

### Links
- [From Data to Viz](https://www.data-to-viz.com) - Comprehensive guide to chart types and when to use them

## Key Concepts and Terminology
Summarizing some terminology.

### Domains and Tasks
- **Domain**: The context of who the users are and what concepts define their problem area
- **Tasks**: The specific questions users are trying to answer with the visualization
- These user-centered concepts are essential for selecting appropriate visualization patterns
- Connects to Tamara Munzner's "What/Why/How" framework (explored further in Lecture 14)

### Tidy Data Structure
- Each variable forms a column
- Each observation forms a row
- Each type of observational unit forms a table
- Reference: Hadley Wickham's "Tidy Data" (2014)

### Tableau Terminology
- **Blue pills (Dimensions)**: Discrete fields that segment data
- **Green pills (Measures)**: Continuous numeric fields that are aggregated
- Common in business intelligence tools

### Data Density
- The amount of information packed into a visualization
- Higher density requires more sophisticated encoding strategies
- Balance between information richness and readability

## Citations

[1] Tableau, "Tableau Logo," Salesforce, 2024. Available: https://www.salesforce.com/news/tableau-from-salesforce-logo-color-1/

[2] H. Wickham, "Tidy Data," *Journal of Statistical Software*, 2014. Available: https://www.jstatsoft.org/article/view/v059i10

[3] Tableau, "Dimensions and Measures, Blue and Green," Salesforce. Available: https://help.tableau.com/current/pro/desktop/en-us/datafields_typesandroles.htm

[4] S. Carmody, "Mosaic Big," Wikimedia Foundation, 2009. Available: https://en.wikipedia.org/wiki/Mosaic_plot#/media/File:Mosaic-big.png

[5] G. Silvermanaz, "2012 Singapore Products Export Treemap," Wikimedia Foundation, 2014. Available: https://en.wikipedia.org/wiki/Treemapping#/media/File:2012_Singapore_Products_Export_Treemap.png

[6] S. Maskey, "Zoomable Sunburst with Labels Issue," StackOverflow, 2014. Available: https://stackoverflow.com/questions/24547620/zoomable-sunburst-with-labels-issue

[7] T. Munzner, "A Nested Model for Visualization Design and Validation," *IEEE Transactions on Visualization and Computer Graphics*, vol. 15, no. 6, pp. 921-928, Nov.-Dec. 2009, doi: 10.1109/TVCG.2009.111

[8] S. Zhang, "Canyon," OpenProcessing. Available: https://openprocessing.org/sketch/2552991

[9] Y. Holtz and C. Healy, "From Data to Viz," 2018. Available: https://www.data-to-viz.com
