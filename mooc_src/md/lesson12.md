# Lesson 12
Briefly exploring visualization patterns and user tasks.

## Objective
Introduce common visualization patterns organized by variable count, establish core data terminology, and explore how user domains and tasks should guide pattern selection.

## Outline
This lecture provides a tour through common chart types used for different situations as well as common terminology. It also offers a brief introductory mention of domains and tasks as a way to contextualize visualization patterns by understanding users.

### Data terminology
Understanding the language used to describe data structures.

- Variables are the column names in a dataset.
- Values are seen inside individual cells.
- Observations are rows in a table.
- Dimensions are variables by which observations are divided or segmented.
- Measures are numeric values which are encoded in visual channels.

### Visualization patterns by variable count
The lecture systematically explores visualization options as data complexity increases from one variable to seven variables.

- 1 variable: histogram, pie chart, donut chart, circular graph.
- 2 variables: scatter plot, bar chart, treemap, sunburst chart, chord diagram, arc diagram.
- 3 variables: bubble chart, grouped bar chart, stacked bar chart, Marimekko chart, Sankey diagram.
- 4 variables: parallel coordinates plot.
- Beyond 4 variables: shared axes, dual axes, novel representations, interactivity, multiple coordinated views, small multiples.

### The grammar is limited
For higher density plots, traditional chart types become insufficient.

- Standard visualization patterns struggle with 5 or more variables.
- Alternative approaches include shared axes, novel representations, and interactivity.
- Multiple coordinated views and small multiples help manage complexity.

### Re-centering the user
Moving from pattern selection to user-centered design through domains and tasks.

- Domains define who the users are and what concepts matter in their problem area.
- Tasks identify what questions users are trying to answer.
- The same data can be visualized differently depending on user needs.
- This approach connects to Tamara Munzner's "What/Why/How" framework explored in Lecture 14.

## Take Aways
Visualization pattern selection should be driven by both data complexity and user needs, not just variable count alone.

- Learn core data terminology: variables, values, observations, dimensions, and measures.
- Understand common visualization patterns and their appropriate use cases.
- Recognize that traditional patterns struggle beyond 4 variables.
- Center design around user domains (who they are and their concepts) and tasks (questions they need to answer).
- The same dataset may require different visualizations depending on user goals.

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
