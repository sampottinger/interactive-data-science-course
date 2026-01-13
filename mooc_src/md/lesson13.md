# Lesson 13: New Languages and Complex Types
Using what we've learend to build new visual languages.

## Objective
Explore how to create custom visual languages through novel representations and advice for more complex data types which often require some creativity in encoding.

## Outline
This lecture moves beyond traditional chart types to explore building custom visual languages through understanding dimensions, measures, and encoding devices. It introduces movements and levels as techniques for managing visual complexity, provides a brief survey of complex data formats, and offers design strategies specifically for geospatial data visualization.

### Charts without names
Think in terms of encodings rather than predefined chart types.

  - Instead of selecting from chart wizards, ask what are the dimensions and measures.
  - Map variables to encoding devices directly rather than choosing named chart types.
  - Focus on the fundamental questions:
    - How can variables be mapped to available encoding devices?
    - Whare the most important aspects, what are the most valued encoding devices?

Historical examples include Marey's train schedule, Felton's annual reports, Minard's Napoleon map, NYT election visualizations, and Fathom's Connected China.

### Two techniques for managing complexity
Movements and levels offer approaches for handling visual sophistication.

  - Movements
    - Reuse visual motifs or graphical representations across multiple plots to create a story between them
    - See Jonathan Harris.
    - Example of movements: Podcast Anthropology uses consistent visual encoding across different views to create narrative continuity.
  - Levels
    - Start with very simple graphics but, as the user spends more time interacting, add in more sophistication.
    - See Ben Fry.
    - Example of levels: Global Plastics AI Policy Tool reveals progressively more detail as users engage deeper.

Use movements when showing the same data from multiple perspectives or over time, and levels when users have varying expertise or interest in detail.

### In-class activity
Dear Data inspired exercise completed during the lecture. Draw by hand (pen, no code) your last five years and your next five years.

### Complex data formats
Brief look at different data formats beyond CSV.

  - Text formats: CSV for simple tabular data, JSON for hierarchical data, YAML for human-readable configuration, and GeoJSON for geographic features.
  - Binary formats
    - Protobuf for efficient serialization
    - Avro for row-oriented data, Arrow for columnar format
    - Geotiff for raster geospatial data
    - Geobuf for compact binary GeoJSON
    - GeoArrow for columnar geospatial data
    - COG (Cloud Optimized GeoTIFF) for efficient cloud-based raster access
    - NetCDF for multidimensional (often scientific) data.
  - Working with GeoJSON:
    - Standard format for geospatial vector data with JSON structure containing geometry and properties.
    - Tools like geojson.io for visualization and editing.
    - Integration with tools like Mapbox.

### Geospatial visualization challenges
Maps present unique technical and design challenges.

  - Technical challenges: Large file sizes often running into many gigabytes, multiple formats to work with, very large basemaps, and performance considerations for rendering and interaction.
  - Design challenge 1: Loss of best encoding device as position (horizontal and vertical). Immediately consumed by geographic coordinates, forcing reliance on secondary encoding channels.
  - Design challenge 2: Visual complexity of basemaps which include substantial visual elements like roads, labels, and terrain that can occlude or interfere with data glyphs.

### Design strategies for maps
Apply the first perspective to navigate map design.

  - Focus on preattentive features: Emphasize shape, form, and color that will pop against the background, use high contrast to create clear figure/ground separation.
  - Strategic use of encoding devices: Consider area for depicting small details that might be lost with other encodings, consider color for things where there are very large differences in values.
  - Quantitative color scales: Focus on contrast against background, create strong figure/ground relationships, importance of perceptually uniform color spaces.
  - Keep visual channels clear: Minimize clutter and overlapping elements.
  - Focus on user and task: Not all data may be relevant for specific use cases, focus based on user needs, task-driven design reduces unnecessary complexity.

## Take Aways
Custom visual languages built on encoding principles enable more expressive data visualization, while movements and levels provide systematic approaches to managing complexity.

  - Think in encodings (dimensions, measures, and devices) rather than chart names to create novel representations.
  - Use movements to create visual continuity across multiple views and levels to progressively disclose complexity.
  - Various data formats beyond CSV include GeoJSON for geospatial work.
  - When working with maps, focus on preattentive features, clear visual channels, and task-driven design to overcome the challenges of losing position encoding and basemap complexity.
  - For networks and other complex data types, see the assigned reading on "15 Views on a Node-Link Graph."

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

[19] T. Munzner, "15 Views on a Node-Link Graph," YouTube video. Available: https://youtu.be/WOBKnRlOAes

[20] Dear Data Project, "Dear Data," 2015. Available: https://www.dear-data.com/theproject
