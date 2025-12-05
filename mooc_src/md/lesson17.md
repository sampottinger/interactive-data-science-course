# Lecture 17: The Reader as Player

**Stat 198: Interactive Data Science and Visualization**
**Instructor:** A Samuel Pottinger
**Original Instruction Date:** March 31, 2025

## Description

Go deep into interactivity with affordances, kinesthetic projection, and common patterns in data visualization. This is setting up our final ingredient for data visualizations that you need for the final!

## Key Takeaways

This lecture explores the bridge between user interaction and data visualization, introducing common interaction patterns and formalizing the concept of affordances to create more intuitive and engaging interactive experiences.

### Acting Through Tools

Understanding how users interact with digital interfaces requires examining the relationship between action and tool:
- Users act through interfaces rather than on them
- The concept of kinesthetic projection: how physical movement translates to digital action
- Tools should feel like extensions of the user's intent

### Common Interaction Patterns in Data Visualization

The lecture introduces five fundamental interaction patterns that recur throughout interactive data visualization:

#### 1. Details Disclosure
- Revealing additional information on demand
- Progressive disclosure of complexity
- Example: Podcast Anthropology visualization showing episode details by year
- Allows overview first, details on demand approach

#### 2. Coordinated Scrubbing
- Synchronized navigation across multiple views
- Time-based or parameter-based coordination
- Example: TED visualization showing coordinated exploration of talks
- Enables pattern discovery across dimensions

#### 3. Madlibs
- Structured query interface using dropdown menus and selections
- Fill-in-the-blank approach to data exploration
- Provides guidance while maintaining flexibility
- Reduces cognitive load by constraining options

#### 4. Coordinated Filtering
- Filtering in one view affects all linked views
- Multiple coordinated views responding to same filter
- Example: Global Plastics AI Policy Tool showing end of life outcomes by region
- Enables multi-faceted data exploration

#### 5. Configuration Panel
- Dedicated control interface for simulation or visualization parameters
- Multiple input types (sliders, buttons, radio buttons)
- Example: Hypothetical Rates Simulator showing agricultural subsidy scenarios
- Separates controls from visualization for clarity

#### 6. Direct Manipulation
- Users interact directly with visual elements
- Click, drag, or tap on data representations themselves
- Example: FoodSim San Francisco allowing users to place buildings directly on map
- Provides intuitive, spatial interaction model

## Formalizing Affordances
Affordances have come up in conversation before but let's give this a formal definition.

### Action + Target Framework

The lecture introduces a formal way to think about interaction design:
- **Action**: What the user does (click, hover, drag, type, etc.)
- **Target**: What the user acts upon (data point, axis, filter, button, etc.)

This framework helps designers:
- Systematically consider all possible interactions
- Ensure affordances are clear and discoverable
- Design consistent interaction patterns
- Communicate design intentions clearly

### Principles

- Affordances should be discoverable without instruction
- The design should suggest its own use
- Feedback should be immediate and clear
- Interactions should feel natural and intuitive

## Group Activity

The lecture included a group activity where students imagined potential interactions for the Census visualization:

- What actions could enhance data exploration?
- How could multiple views be coordinated?
- What filters or configurations would be useful?
- How can direct manipulation reveal insights?

## Road to the Final

The lecture concluded with discussion of how these concepts prepare students for their final projects:

- Interaction patterns as building blocks
- Combining multiple patterns for rich experiences
- Balancing guidance with freedom
- Designing for both exploration and explanation

## Activities
As always, some additional materials to consider...

### Lecture Video
[Watch Lecture 17: The Reader as Player on Vimeo](https://vimeo.com/1071192794)

### Assignment
We will start our interactive experience. There are different video games for you to choose from within the course manual. See "experience" section. After you have selected your choice, lookup the game specific instructions. You can space out your game play over the next few lectures. There will be an additional question asked of all games later in lesson 20 when it would be good to be done.

### Reading
Please watch a fantastic discussion regarding the role of the player from Extra Credits.

### Links
- [First video from slides: Kinect Disconnect - Watch 1:30 to 3:10 for Kinesthetic Projection discussion](https://www.youtube.com/watch?v=ijcezUy3ZzY)
- [Second video from slides: Affordances - How Design Teaches Us Without Words](https://www.youtube.com/watch?v=QCSXEKHL6fc)

## Citations

[1] M. Hoekstra, "MacPaint," Geek Technique, 2007. Available: https://www.geektechnique.org/blog/786/mac-paint.html

[2] J. Portnow, "Kinect Disconnect - How NOT to do Motion Control," Extra Credits, 2012. Available: https://www.youtube.com/watch?v=ijcezUy3ZzY

[3] A. Pottinger, "Podcast Anthropology," Gleap, 2015. Available: https://gleap.org/static/special/podcast_viz/index.html

[4] A. Pottinger, "Ted Viz 2," Gleap, 2013. Available: https://gleap.org/content/ted_visualization_2

[5] A. Pottinger, "Montreal Policy Simulator," University of California, 2025. Available: https://mlf-policy-explorer.org/

[6] A. Pottinger, R. Geyer, N. Biyani, C. Martinez, N. Nathan, M. Morse, M. de Bruyn, C. Boettiger, E. Baker, K. Koy, and D. McCauley, "Global Plastics AI Policy Tool," University of California, 2024. Available: https://global-plastics-tool.org/

[7] A. Pottinger, R. Geyer, N. Biyani, C. Martinez, N. Nathan, M, Morse, C. Liu, S. Hu, M. de Bruyn, C. Boettiger, E. Baker, and D. McCauley, "Pathways to reduce global plastic waste mismanagement and greenhouse gas emissions by 2050," *Science*, 2024. doi: 10.1126/science.adr3837

[8] A. Pottinger, "FoodSim: San Francisco." 2023. Available: https://foodsimsf.com/

[9] J. Portnow, "Affordances - How Design Teaches Us Without Words," Extra Credits, 2014. Available: https://www.youtube.com/watch?v=QCSXEKHL6fc

[10] A. Pottinger, L. Connor, B. Guzder-Williams, M. Weltman-Fahs, N. Gondek, and T. Bowles, "Climate-driven doubling of U.S. maize loss probability: Interactive simulation with neural network Monte Carlo," *JDSSV*, 2025. doi: 10.52933/jdssv.v5i3.134
