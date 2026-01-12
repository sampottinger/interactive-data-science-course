# Lesson 19: Architecture
Applying game design to visualization to offer structure.

## Objective
Explore how game design principles, specifically level design and architectural patterns, can be applied to data visualization. This can help guide users through complex information spaces and teach them how to interact with visualizations effectively.

## Outline
Architecture in data visualization refers to how we structure and organize the user's journey through information. Just as game levels guide players through experiences while teaching mechanics, visualization architectures guide users through data while teaching interaction patterns. This lecture examines three architectural approaches borrowed from game design that can be applied to data visualization.

### Three architectural patterns
Game design offers structured frameworks for guiding users through complex experiences. We will look at three:

- Levels: Modulate visibility and offer hints toward other areas.
- Hayashida Level Design: Four-step progressive learning pattern.
- Triangle Design: Valleys and hills with landmark-based navigation.

#### Levels
Modulate what is visible to the user at any given moment in time, offer hints towards other areas.

- Control information visibility to prevent overwhelming users.
- Provide progressive disclosure of complexity.
- Use hints and breadcrumbs to suggest additional content.
- Think of dashboards as spaces with artifacts rather than just charts.
- View dashboards as having space where users move through a complex world collecting insights.
- Example: Illinois Soil Health Tool demonstrates controlled information revelation.
- Application: Reimagine data dashboards through narrative structures like Choose Your Own Adventure or interactive fiction.

#### Hayashida Level Design
A four-step progressive learning pattern for introducing mechanics and complexity.

- Introduction: Show information about the tool with pre-filled controls for minor modifications.
- Development: Use mechanics introduced previously, invite users to make changes and compare.
- Twist: Enable overlays for the same display, allowing users to leverage previously learned mechanics in more complex interfaces.
- Conclusion: Invite users to demonstrate acquired skills in a new problem context.
- Example: AFSC GAP Visualization implements Hayashida design for teaching Pacific cod data analysis.
- This pattern tutorializes users through a real analysis, gradually building confidence and capability.

#### Triangle Design
Valleys and hills: modulate what is visible to the user at any given moment in time, offer hints towards other areas through landmark-based navigation.

- Valley: Current region shows deep detail with local landmarks where users are immersed in specific data.
- Over the hill: Landmarks support quick insights and navigation with overview elements to orient users.
- Mechanics impact whole world: Global effects of user actions are visible so users understand system-wide implications.
- Balance between detail (valley) and overview (hill).
- Use landmarks for orientation and navigation.
- Create rhythm between focused analysis and broad understanding.
- Examples: Global Plastics AI Policy Tool and No Ceilings demonstrate effective landmark-based navigation.

### Case Studies
Note that we looked at AFSC GAP in class (https://app.pyafscgap.org/) and then watched a video disecting Mario Level 1-1 (https://www.youtube.com/watch?v=ZH2wGpEZVgE).

#### Case study: AFSC GAP Visualization
The AFSC GAP (Alaska Fisheries Science Center Groundfish Assessment Program) visualization demonstrates Hayashida Level Design implementation.

- Tool visualizes Pacific cod population data with analysis capabilities.
- Introduction phase: Pre-configured analysis with simple modifications.
- Development phase: Users modify parameters using learned controls.
- Twist phase: Overlays and additional complexity build on existing knowledge.
- Conclusion phase: Users apply skills to new analytical questions.
- Users progressively learn data analysis capabilities without overwhelming initial tutorials.

#### Case study: Mario Level 1-1
Super Mario Bros. Level 1-1 teaches without words with principles directly applicable to data visualization onboarding.

- Teaches all core game mechanics without explicit tutorial.
- Users learn through guided exploration.
- Architecture naturally leads to skill acquisition.
- Progressive difficulty with safe experimentation.
- Design entry points that teach basic interactions naturally.
- Use visual design to suggest actions (affordances).
- Allow safe experimentation without consequences.
- Build complexity gradually based on demonstrated competence.

### Practical applications
Elijah Meeks' work on "Designing a Data Visualization Dashboard Like It was a Game" provides frameworks for implementation.

- Think spatially about dashboard organization.
- Consider user movement patterns through information.
- Create natural pathways and decision points.
- Use landmarks for orientation.
- Design for exploration and discovery.
- Apply patterns for onboarding users to complex visualizations.
- Implement progressive disclosure of analytical capabilities.
- Design spatial organization of dashboard elements and navigation through multi-view systems.

## Take Aways
Game design principles provide powerful frameworks for structuring data visualization experiences that teach users how to interact with and explore complex information.

- Architecture in visualization guides users through information spaces just as game levels guide players through experiences.
- Three key patterns: Levels (controlled visibility), Hayashida Design (four-step learning), and Triangle Design (valleys and hills).
- Dashboard design benefits from spatial thinking where users move through space collecting insights.
- Progressive disclosure and tutorialization help users build skills without overwhelming them.
- Visual affordances and environmental cues can teach interaction patterns without explicit instructions.
- Landmark-based navigation helps users orient themselves between detail and overview.

## Citations

[1] G. Nicoli, "Spiritfarer: la morte felice," Ludica, 2020. Available: https://www.ludicamag.com/spiritfarer-la-morte-felice/

[2] M. Brown, "Super Mario 3D World's 4 Step Level Design," Game Maker's Toolkit, 2015. Available: https://www.youtube.com/watch?v=dBmIkEvEBtA

[3] A. Pottinger and G. Zarpellon, "Pyafscgap.org: Open source multi-modal Python-based tools for NOAA AFSC RACE GAP," *JOSS*, 2023. doi: 10.21105/joss.05593.

[4] D. Emmons and J. Portnow, "Design Club - Super Mario Bros: Level 1-1," Extra Credits, 2014. Available: https://www.youtube.com/watch?v=ZH2wGpEZVgE

[5] "Illinois Soil Health," University of California, 2023. Available: https://illinois-soil-health-tool.org/

[6] E. Meeks, "Designing a Data Visualization Dashboard Like It was a Game," Nightingale, 2018. Available: https://medium.com/nightingale/designing-a-data-visualization-dashboard-like-it-was-a-game-b347858c1bce

[7] A. Pottinger, N. Biyani, R. Geyer, D. J. McCauley, M. de Bruyn, M. R. Morse, N. Nathan, K. Koy, and C. Martinez, "Combining Game Design and Data Visualization to Inform Plastics Policy: Fostering Collaboration between Science, Decision-Makers, and Artificial Intelligence," Arxiv, 2023. Available: https://arxiv.org/abs/2312.11359.

[8] Fathom Information Design, "No Ceilings," The Clinton Foundation, 2015. Available: http://www.noceilings.org/
