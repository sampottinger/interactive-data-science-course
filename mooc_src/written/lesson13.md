# Lecture 13: Building New Languages

**Stat 198: Interactive Data Science and Visualization**
**Instructor:** A Samuel Pottinger
**Original Instruction Date:** March 10, 2025

## Description

Exploration of how to make new visual representations through the use of visual encoding mappings as well as two new patterns for fitting in more variables: movements and levels. Finally, a look at data formats and a discussion of advice for geospatial visualization.

## Key Takeaways

This lecture focuses on building custom visual languages beyond traditional chart types, introduces techniques for managing complexity in visualizations, and provides practical guidance for working with geospatial data.

### Charts Without Names

Instead of relying on predefined chart types (bar chart, scatter plot, etc.), think in terms of:
- **Dimensions and Measures**: What are the categorical vs. quantitative variables?
- **Encoding Devices**: How can these be mapped to visual attributes?
- **Visual Encoding Flexibility**: Move beyond the "chart wizard" to create custom representations.

### Two New Techniques for Complexity

**Movements** (inspired by Jonathan Harris):
- Reuse visual motifs or graphical representations across multiple plots to create a story between them
- Creates visual continuity and narrative flow across different views
- Example: Podcast Anthropology visualization

**Levels** (inspired by Ben Fry):
- Start with very simple graphics
- As the user spends more time interacting, add in more sophistication
- Progressive disclosure of complexity
- Example: Global Plastics AI Policy Tool with layered detail levels

## Novel Representations
Do all charts have a name? What about structures we've never seen before?

### Moving Beyond Chart Types
- Traditional approach: selecting from predefined chart types (bar, line, pie, etc.)
- New approach: thinking in terms of encodings and mappings
- Focus on dimensions, measures, and how to map them to visual channels

### Historical Examples
- **Marey's Train Schedule**: Complex time-space visualization showing train movements
- **Nicholas Felton's Annual Reports**: Creative personal data visualizations combining multiple encoding strategies
- **Minard's Napoleon Map**: Classic example of multivariate flow map
- **NYT Election Visualization**: Small multiples showing voter change across geography
- **Fathom's Connected China**: Network visualization of social and political connections

### Key Questions to Ask
- What are the dimensions and measures in the data?
- What encoding devices are available?
- How can variables be mapped to these devices effectively?

## Tips for Managing Complexity
If we leave the default chart names behind, what tools do we have?

### Movements: Creating Visual Continuity
- **Definition**: Reusing visual motifs across multiple related visualizations
- **Purpose**: Creates narrative connection between different data views
- **Example Analysis**: Podcast Anthropology
  - Consistent visual encoding for episodes across different views
  - Color, shape, and position create continuity
  - Allows readers to track elements across transformations

### Levels: Progressive Complexity
- **Definition**: Starting simple and adding sophistication as users engage deeper
- **Purpose**: Prevents overwhelming users while allowing detailed exploration
- **Example Analysis**: Global Plastics AI Policy Tool
  - Overview level: Simple end-of-life metrics
  - Details level: Breakdowns by policy interventions
  - Deep dive: Country-specific impacts and assumptions
  - Each level reveals more granularity

### When to Use These Techniques
- **Movements**: When showing the same data from multiple perspectives or over time
- **Levels**: When users have varying levels of expertise or interest in detail

## Group Activity: Assignment 11
In class, we did assignment 11 together but you can do it at home!

- Draw (by hand with a pen, no code) your last five years and your next five years
- Inspired by the Dear Data project
- Focus on personal data representation
- Emphasizes the creative and expressive side of data visualization

### Complex Data Formats
A brief look at different data formats.

### Text-Based Formats
- **CSV**: Simple tabular data, rows and columns
- **JSON**: Hierarchical data with nested structures
- **YAML**: Human-readable configuration and structured data
- **GeoJSON**: Geographic features with properties in JSON format

### Binary Formats
- **Protobuf**: Protocol buffers for efficient serialization
- **Avro**: Row-oriented data serialization
- **Arrow**: Columnar in-memory data format
- **Geotiff**: Raster geospatial data
- **Geobuf**: Compact binary encoding of GeoJSON
- **GeoArrow**: Columnar geospatial data
- **COG (Cloud Optimized GeoTIFF)**: Efficient cloud-based raster access
- **NetCDF**: Multidimensional scientific data

### Working with GeoJSON
- Standard format for geospatial vector data
- JSON structure with geometry and properties
- Tools: geojson.io for visualization and editing
- Integration with mapping libraries (Mapbox, OpenStreetMap)

### Advice for Geospatial Visualization
With these formats in mind, finishing with geospatial data.

### Technical Challenges
- **Large File Sizes**: Geospatial datasets often run into many gigabytes
- **Multiple Formats**: Need to work with various text and binary formats
- **Basemap Size**: The background map itself is often very large
- **Performance**: Rendering and interaction performance becomes critical

### Design Challenges

**Challenge 1: Loss of Best Encoding Device**
- Position (horizontal and vertical) is immediately consumed by geographic coordinates
- This is typically the most accurate encoding device according to Cleveland & McGill
- Forces reliance on secondary encoding channels (color, size, shape)

**Challenge 2: Visual Complexity of Basemaps**
- Basemaps include substantial visual elements (roads, labels, terrain)
- These can occlude or interfere with data glyphs overlaid on top
- Creates figure/ground separation challenges

### Design Strategies for Maps

**1. Focus on Preattentive Features**
- Emphasize shape, form, and color that will "pop" against the background
- Use high contrast to create clear figure/ground separation
- Example visualizations showing effective use of distinct shapes and colors

**2. Strategic Use of Encoding Devices**
- **Area**: Good for depicting small details that might be lost with other encodings
- **Color**: Effective when there are very large differences in values
- Consider both approaches shown in climate adaptation visualizations

**3. Quantitative Color Scales**
- Focus on contrast against background
- Create strong figure/ground relationships
- Examples showing effective vs. ineffective color choices
- Importance of perceptually uniform color spaces

**4. Keep Visual Channels Clear**
- Minimize clutter and overlapping elements
- Strategic use of simplification and aggregation
- Examples showing progression from cluttered to clean designs
- Consider different zoom levels or detail levels

**5. Focus on User and Task**
- Not all data may be relevant for specific use cases
- Filter and focus based on user needs
- Task-driven design reduces unnecessary complexity
- Teaser for next lecture on domain/task analysis

## Activities
This was a big lecture! Here are some resources to supplement.

### Lecture Video
[Watch Lecture 13: Building New Languages on Vimeo](https://vimeo.com/1064101038)

### Assignment
Please draw some representation of your last 5 years and what you hope your next 5 years will look like. You can use whatever tools and materials you like other than code. For inspiration see [Dear Data](https://www.dear-data.com/theproject).

### Reading
Please watch [15 Views on a Node-Link Graph](https://youtu.be/WOBKnRlOAes) by Tamara Munzner.

## References

### Text
- Munzner, Tamara. *Visualization Analysis and Design*. CRC Press, 2015.
  - Relevant chapters on visual encoding and marks/channels

### Assignment
- Assignment 12: Dear Data exercise (draw last 5 years and next 5 years by hand)

### Reading
- Munzner, Tamara. "15 Views on a Node-Link Graph." YouTube video. Available: https://youtu.be/WOBKnRlOAes

### Links
- [Dear Data Project](https://www.dear-data.com/theproject)
- [Geojson.io](https://geojson.io/) - Interactive GeoJSON editor

## Citations

[1] B. Adhikari, "Marey's train schedule," University of Missouri Saint Louis, 2021. Available: https://badriadhikari.github.io/data-viz-workshop-2021/minards/

[2] N. Felton, "2012 Annual Report," Feltron, 2013. Available: https://feltron.com/FAR12.html

[3] J. Cheng, "Analyzing Minard's Visualization Of Napoleon's 1812 March," ThoughtBot, 2014. Available: https://thoughtbot.com/blog/analyzing-minards-visualization-of-napoleons-1812-march

[4] A. Wu, L. Gamio, R. Gebeloff, E. Shao, and M. Bender, "Key to Trump's Win: Heavy Losses for Harris Across the Map," *New York Times Company*, 2024. Available: https://www.nytimes.com/interactive/2024/11/19/us/politics/voter-turnout-election-trump-harris.html

[5] Fathom Information Design, "Connected China," Thomson Reuters. Available: https://fathom.info/china/

[6] D. Ling, "Introduction to Statistics Using LibreOffice.org Calc, Apache OpenOffice.org Calc, and Gnumeric," Comfsm. Available: http://www.comfsm.fm/~dleeling/statistics/text5.html

[7] Fathom Information Design, "No Ceilings", The Clinton Foundation and The Bill and Melinda Gates Foundation. Available: https://noceilings.org/

[8] A. Pottinger, "Podcast Anthropology," Gleap, 2025. Available: http://podcastanthropology.com/

[9] B. Fry, "Audience & Context," Eyeo, 2015. Available: https://vimeo.com/133608686?embedded=true&source=vimeo_logo&owner=8053320

[10] Geojson.io, "Geojson.io," Mapbox. Available: https://geojson.io/

[11] A. Pottinger, L. Connor, B. Guzder-Williams, M. Weltman-Fahs, N. Gondek, and T. Bowles, "Climate-driven doubling of U.S. maize loss probability: Interactive simulation with neural network Monte Carlo," *JDSSV*, 2025. doi: 10.52933/jdssv.v5i3.134

[12] A. Pottinger, "SF AirBnB Analysis," Towards Data Science. Available: https://gleap.org/content/airbnb

[13] A. Pottinger, "California Crop Shift Simulation," University of California, 2024. Available: https://crop-shift-sampottinger3-2860.replit.app/

[14] A. Pottinger, "Food Sim SF," Gleap, 2024. Available: https://foodsimsf.com/

[15] S. Kamvar and J. Harris, "We Feel Fine and Searching the Emotional Web," *Proceedings of the fourth ACM international conference on Web search and data mining*, 2011. Available: https://www.wefeelfine.org/wefeelfine.pdf

[16] A. Pottinger, "TED Visualization," Gleap, 2012. Available: https://gleap.org/content/ted_visualization

[17] A. Pottinger, R. Geyer, N. Biyani, C. Martinez, N. Nathan, M. Morse, M. de Bruyn, C. Boettiger, E. Baker, K. Koy, and D. McCauley, "Global Plastics AI Policy Tool," University of California, 2024. Available: https://global-plastics-tool.org/

[18] A. Pottinger, R. Geyer, N. Biyani, C. Martinez, N. Nathan, M. Morse, C. Liu, S. Hu, M. de Bruyn, C. Boettiger, E. Baker, and D. McCauley, "Pathways to reduce global plastic waste mismanagement and greenhouse gas emissions by 2050," *Science*, 2024. doi: 10.1126/science.adr3837
