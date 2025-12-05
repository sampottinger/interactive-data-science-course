# Lecture 19: Architecture

**Stat 198: Interactive Data Science and Visualization**
**Instructor:** A Samuel Pottinger
**Original Instruction Date:** April 7, 2025

## Description

Look at level design and how it help us teach users about how to use and navigate through our data visualizations. Explore Meeks, Hayashida Level Design, and Triangle Design.

## Key Takeaways

This lecture explores how game design principles, specifically level design and architectural patterns, can be applied to data visualization to guide users through complex information spaces and teach them how to interact with visualizations effectively.

Architecture in data visualization refers to how we structure and organize the user's journey through information. Just as game levels guide players through experiences while teaching mechanics, visualization architectures guide users through data while teaching interaction patterns.

## Course Timeline Update

The lecture begins with an overview of the remaining course schedule:

- **Wednesday (with makeup on Friday)**: Interactive experience discussions
- **Friday**: BART visualization assignment
- **Monday**: Interactive visualization extension (assigned today)
- **End**: Final project (to be assigned on Wednesday)

## Three Architectural Patterns from Game Design

The lecture introduces three key architectural approaches borrowed from game design that can be applied to data visualization:

### Architecture 1: Levels

**Definition**: Modulate what is visible to the user at any given moment in time, offer hints towards other areas.

**Key Concepts**:
- Control information visibility to prevent overwhelming users
- Provide progressive disclosure of complexity
- Use hints and breadcrumbs to suggest additional content
- Think of dashboards as spaces with artifacts rather than just charts

**Metaphor**: Dashboard as game level
- Viewing a dashboard as having **space** and **artifacts**
- Users can be thought of as **moving through** a complex world
- Designers can optimize how players navigate and **collect insights**
- Map user movement through the dashboard to better design navigation

**Example**: Illinois Soil Health Tool
- Demonstrates controlled information revelation
- Users progress through levels of detail
- Available at: https://illinois-soil-health-tool.org/

**Application**: Choose Your Own Adventure vs Interactive Fiction
- Reimagining data dashboards through narrative structures
- Zork-style interaction with data
- Users explore data spaces like game environments

### Architecture 2: Hayashida Level Design

**Definition**: A four-step progressive learning pattern for introducing mechanics and complexity.

**The Four Steps**:
1. **Introduction**: Show information about the tool with pre-filled controls for minor modifications
2. **Development**: Use mechanics introduced previously, invite users to make changes and compare
3. **Twist**: Enable overlays for the same display, allowing users to leverage previously learned mechanics in more complex interfaces
4. **Conclusion**: Invite users to demonstrate acquired skills in a new problem context

**Example**: AFSC GAP Visualization
- Implements Hayashida design for teaching Pacific cod data analysis
- Progressive introduction of controls and complexity
- Users build skills incrementally through structured sequence
- Tool available at: https://app.pyafscgap.org/

**Key Insight**: This pattern tutorializes users through a "real" analysis, gradually building their confidence and capability with the visualization tool.

### Architecture 3: Triangle Design

**Definition**: Valleys and hills - modulate what is visible to the user at any given moment in time, offer hints towards other areas through landmark-based navigation.

**Three Components**:
1. **Valley**: Current region shows deep detail with local landmarks - users are immersed in specific data
2. **Over the hill**: Landmarks support quick insights and navigation - overview elements help orient users
3. **Mechanics impact whole world**: Global effects of user actions are visible - users understand system-wide implications

**Key Principles**:
- Balance between detail (valley) and overview (hill)
- Use landmarks for orientation and navigation
- Show both local and global impacts of user interactions
- Create rhythm between focused analysis and broad understanding

**Examples**:
- **Global Plastics AI Policy Tool**: https://global-plastics-tool.org
  - Valley view shows detailed policy scenarios
  - Hill view provides global impact metrics
  - Mechanics (policy adjustments) affect entire system

- **No Ceilings**: http://www.noceilings.org
  - Clinton Foundation data visualization project
  - Demonstrates effective use of landmarks for navigation
  - Balances detail and overview throughout user journey

## Case Studies
Let's consider some prior work to contextualize these ideas...

### AFSC GAP Visualization Revisited

The lecture revisits the AFSC GAP (Alaska Fisheries Science Center Groundfish Assessment Program) visualization as a detailed example of Hayashida Level Design implementation:

**Tool Purpose**: Visualize Pacific cod population data with analysis capabilities

**Design Implementation**:
- **Introduction phase**: Pre-configured analysis with simple modifications
- **Development phase**: Users modify parameters using learned controls
- **Twist phase**: Overlays and additional complexity build on existing knowledge
- **Conclusion phase**: Users apply skills to new analytical questions

**Learning Outcomes**: Users progressively learn data analysis capabilities without overwhelming initial tutorials.

### Mario Level 1-1

The lecture examines Super Mario Bros. Level 1-1 as a masterclass in teaching without words - principles directly applicable to data visualization onboarding.

**Why Mario 1-1 Matters**:
- Teaches all core game mechanics without explicit tutorial
- Users learn through guided exploration
- Architecture naturally leads to skill acquisition
- Progressive difficulty with safe experimentation

**Transferable Principles for Data Visualization**:
- Design entry points that teach basic interactions naturally
- Use visual design to suggest actions (affordances)
- Allow safe experimentation without consequences
- Build complexity gradually based on demonstrated competence
- Use environmental cues rather than text instructions

## Practical Applications

Let's turn next to how you can put these ideas into practice.

### Designing Data Visualization Dashboards Like Games

Referenced work by Elijah Meeks: "Designing a Data Visualization Dashboard Like It was a Game"

- Think spatially about dashboard organization
- Consider user movement patterns through information
- Create natural pathways and decision points
- Use landmarks for orientation
- Design for exploration and discovery

### Use of Patterns

The architectural patterns provide frameworks for:

- **Onboarding users** to complex visualizations
- **Progressive disclosure** of analytical capabilities
- **Spatial organization** of dashboard elements
- **Navigation design** through multi-view systems
- **Teaching interaction patterns** without explicit tutorials

## Activities
Additional related materials and activities...

### Lecture Video
[Watch Lecture 19: Architecture on Vimeo](https://vimeo.com/1073368650)

### Assignment
The goal for this exercise is to take one of your prior visualizations from the class (Stack Overflow Developer Survey, Census, or BART) and make it interactive with at least one user action.

### Reading
Please watch this closer look at [Triangle Design in Zelda](https://youtu.be/CZzcVs8tNfE).

### Links
- [Hayashida Level Design](https://youtu.be/dBmIkEvEBtA) - Super Mario 3D World's 4 Step Level Design
- [AFSC GAP visualization](https://app.pyafscgap.org/)
- [Mario Level 1-1](https://youtu.be/ZH2wGpEZVgE) - Design Club breakdown

## Citations

[1] G. Nicoli, "Spiritfarer: la morte felice," Ludica, 2020. Available: https://www.ludicamag.com/spiritfarer-la-morte-felice/

[2] M. Brown, "Super Mario 3D World's 4 Step Level Design," Game Maker's Toolkit, 2015. Available: https://www.youtube.com/watch?v=dBmIkEvEBtA

[3] A. Pottinger and G. Zarpellon, "Pyafscgap.org: Open source multi-modal Python-based tools for NOAA AFSC RACE GAP," *JOSS*, 2023. doi: 10.21105/joss.05593.

[4] D. Emmons and J. Portnow, "Design Club - Super Mario Bros: Level 1-1," Extra Credits, 2014. Available: https://www.youtube.com/watch?v=ZH2wGpEZVgE

[5] "Illinois Soil Health," University of California, 2023. Available: https://illinois-soil-health-tool.org/

[6] E. Meeks, "Designing a Data Visualization Dashboard Like It was a Game," Nightingale, 2018. Available: https://medium.com/nightingale/designing-a-data-visualization-dashboard-like-it-was-a-game-b347858c1bce

[7] A. Pottinger, N. Biyani, R. Geyer, D. J. McCauley, M. de Bruyn, M. R. Morse, N. Nathan, K. Koy, and C. Martinez, "Combining Game Design and Data Visualization to Inform Plastics Policy: Fostering Collaboration between Science, Decision-Makers, and Artificial Intelligence," Arxiv, 2023. Available: https://arxiv.org/abs/2312.11359.

[8] Fathom Information Design, "No Ceilings," The Clinton Foundation, 2015. Available: http://www.noceilings.org/
