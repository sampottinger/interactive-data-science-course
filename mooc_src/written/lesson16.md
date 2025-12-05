# Lecture 16: The Reader as User

**Stat 198: Interactive Data Science and Visualization**
**Instructor:** A Samuel Pottinger
**Original Instruction Date:** March 19, 2025

## Description

The four waves of HCI and the ideas of Stuart Hall before briefly discussing how video games might fit into the data visualizations conversation.

## Key Takeaways

This lecture explores different conceptual frameworks for understanding the role of the user in data visualization, moving from mechanical interaction to co-creation of meaning. Understanding different ways of thinking about the role of the user provides lenses that can be used to understand design. Seeing visualizations from multiple perspectives helps pieces be more successful.

## Main Topics
Let's take a look at HCI and mediation.

### Audiences: Interrogating Our Lenses

The relationship between author and audience is mediated by the visualization itself. This relationship involves:

- **Assumptions, Focus, Language**: The choices authors make in how they present information
- **Stuart Hall's Reception Theory**: Three ways audiences interpret media:
  - **Dominant Reading**: Accepting the intended message as presented
  - **Oppositional Reading**: Rejecting the intended message entirely
  - **Negotiated Reading**: Partially accepting and partially rejecting the message

### Group Activity: Examining Interactive Data Visualization

Students examined "How Covid Shook the US: Eight Charts That Capture the Last Two Years" from The Guardian, analyzing it through the three reading positions (dominant, oppositional, and negotiated).

### The Three Waves of HCI

The lecture presents three paradigm shifts in how we conceptualize human-computer interaction:

#### Wave 1: Ergonomics
**The user as a robot interpreting through a mechanical system**

- Focus on physical interaction and ergonomic design
- Understanding how users mechanically interact with interfaces
- Examples include airplane cockpit design and door affordances
- Emphasis on making clear how a data visualization should be used
- Fine-tuning mechanisms through which a person "mechanically" interacts

**Key Example**: Fuel efficiency standards visualization showing data from 1978 to 1985

#### Wave 2: Information / Dialogue
**The user as engaged in conversation with a series of questions completing a task**

- Focus on information exchange and task completion
- User flows and supporting series of questions or tasks
- Multiple coordinated views and interactive exploration
- Examples include Windows 98 installation interface, Asana project management, and podcast visualization

**Key Considerations**:
- Think about the flow of a user (user loops)
- Support a series of questions or tasks
- Enable dialogue between user and system

#### Wave 3: Context
**The user as an entity with thought interpreting work through personal and cultural lenses within a social system**

- Recognition that users exist within social and cultural contexts
- Understanding how context interacts with the visualization
- Examples include Global Plastics AI Policy Tool
- Critically interrogating the context and how it may interact with the graphic

**Key Focus**: Understanding users as thinking beings embedded in cultural and social systems, not just task-completing entities.

### Something Else: Games and Media for Thought

Beyond the three waves, the lecture introduces two additional conceptual frameworks:

#### Media for Thought

Using mathematical notation and visual representations as tools for thinking. Historical example from Arabic mathematics demonstrates how notation itself shapes what we can think about.

**Key Example**: Ancient mathematical problem about finding a square, showing how mathematical notation (x² + 10x = 39) provides a more efficient medium for mathematical thought than prose description.

Interactive visualizations can serve as dynamic media for thought, allowing users to explore mathematical and data-driven concepts.

#### Games: The User as Co-Creator

**Reference**: Jesse Schell's "The Art of Game Design: A Book of Lenses"

Games represent a co-created experience between the player and the technology/designer. This perspective sees:

- Users as co-creators of meaning
- The work as a way to think new thoughts
- Creation of sometimes uniquely individual experiences
- Spaces that can be activated by users to see, feel, do, and think new things

**Key Quote from Will Wright**: Games enable players to build narratives and experiences that go beyond the designer's original intention.

## Summary: What Is the User Within Data Visualization?

The lecture presents four complementary ways of understanding users:

1. **A robot** which interprets through a mechanical system (Wave 1)
2. **A conversational partner** with a series of questions for which a series of learnings complete a task (Wave 2)
3. **An entity with thought** interpreting the work through a series of personal and cultural lenses within a social system (Wave 3)
4. **A co-creator of meaning**, using the work as a way to think new thoughts and create sometimes uniquely individual experiences (Games/Media for Thought)

## Practical Implications for Design

Understanding these different conceptualizations of the user suggests designers should:

- Make it clear how a data visualization should be used and fine-tune the mechanisms through which a person "mechanically" interacts (Wave 1)
- Think about the flow of a user (user loops) and how we support a series of questions or tasks (Wave 2)
- Critically interrogate the context of this visualization and how it may interact with the graphic (Wave 3)
- Create spaces that can be activated by the user to see, feel, do, and think new things (Games/Media)

## Activities
To supplement the main content...

### Lecture Video
[Watch Lecture 16: The Reader as User on Vimeo](https://vimeo.com/1067524875)

### Assignment
In this exercise, we will visualize the BART ridership dataset. For this activity, please visualize 4 variables.

Note that this project invites you to do geospatial visualization in that stations have latitudes and longitudes. However, it is not required. If you want to go this route, see the geospatial examples on the Sketchingpy examples page. To support you, please see this geojson which has the outline of the Bay Area: bayarea.geojson. If you do geospatial visualization, latitude counts for one variable and longitude counts for another. The geojson is under Public Domain.

Regardless, please use the BART 2024 ridership data I preprocessed for you or the upstream official dataset.

### Reading
I have selected a fairly short video for you to review digging deeper into the idea of affordances through bad doors.

### Links
- [Example linked in slides: How Covid Shook the US](https://www.theguardian.com/us-news/2022/mar/13/how-covid-shook-the-us-charts-graphs)
- [BART ridership data (preprocessed)](/support/bart.xlsx)
- [BART official dataset](https://www.bart.gov/about/reports/ridership)
- [Bay Area GeoJSON](/support/bayarea.geojson)
- [Bad doors video](https://www.vox.com/2016/2/26/11120236/bad-doors-human-centered-design)

## Citations

[1] M. Hoekstra, "MacPaint," Geek Technique, 2007. Available: https://www.geektechnique.org/blog/786/mac-paint.html

[2] "Reception Theory," Revision World. Available: https://revisionworld.com/a2-level-level-revision/media-studies-level-revision/reception-theory#google_vignette

[3] J. Tong, "Diagrammatic thinking and audience reading of COVID-19 data visualisations: A UK case study," *Convergence*, 2024. doi: 10.1177/13548565241309886.

[4] "Stuart Hall," Wikimedia Foundation, 2025. Available: https://en.wikipedia.org/wiki/Stuart_Hall_(cultural_theorist)

[5] E. Berger and A. Witherspoon, "How Covid shook the US: eight charts that capture the last two years," The Guardian, 2022. Available: https://www.theguardian.com/us-news/2022/mar/13/how-covid-shook-the-us-charts-graphs

[6] S. Harrison, P. Sengers, and D. Tatar, "The Three Paradigms of HCI," CHI 2007, 2007.

[7] "Understanding Projects," Asana. Available: https://help.asana.com/s/article/understanding-projects?language=en_US

[8] Schell, Jesse. *The Art of Game Design: A Book of Lenses*. CRC Press, Taylor & Francis Group, 2020.

[9] Wright, Will. "Spore, Birth of a Game." TED, Ted Conferences, 2007, https://www.ted.com/talks/will_wright_spore_birth_of_a_game.

[10] S. Dale. "Back wooden 4-Panel Door Closed," Unsplash, 2018. Available: https://unsplash.com/photos/black-wooden-4-panel-door-closed-dJycgkec2p0

[11] L. Parren, "Pilot Driving Plane During Daytime," Unsplash, 2018. Available: https://unsplash.com/photos/pilot-driving-plane-during-daytime-S3xxiedz0hE

[12] F Bezies, "Installation MS-Windows 98," Flickr, 2013. Available: https://www.flickr.com/photos/fredbezies/9136730422/
