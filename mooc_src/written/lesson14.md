# Lecture 14: Task / Domain

**Stat 198: Interactive Data Science and Visualization**
**Instructor:** A Samuel Pottinger
**Original Instruction Date:** March 12, 2025

## Description

Expand on the idea of domains and tasks with examples before looking at the What / Why / How framework from Munzner.

## Key Takeaways

This lecture deepens understanding of how to approach data visualization design through the lens of user tasks and domain contexts, introducing Tamara Munzner's What/Why/How framework as an optional structured approach.

### Core Concepts
- Understanding user domains and contexts
- Identifying and abstracting user tasks
- Applying the What/Why/How framework to visualization design
- Connecting tasks to encoding decisions

## Course Context
This lecture builds on the second perspective introduced in Lecture 1:

1. **Visualization as Representation** (covered)
2. **Visualization as Task** (current focus)
3. **Visualization as Narrative**
4. **Visualization as Dialogue**

## Understanding Domains and Tasks
Understanding the user's context is essential for effective visualization design. Key questions include:

### Who is the user?
- Identify the target audience for your visualization
- Consider their expertise level and background
- Understand their relationship to the data

### What social context is that user in?
- Professional environment
- Academic research setting
- Public consumption
- Decision-making context

### What are the concepts the user is interacting with?
- Domain-specific terminology
- Mental models users bring to the data
- Existing representations they're familiar with

### What prior knowledge or understanding might the user be interacting with?
- Assumptions about the data
- Previous exposure to similar visualizations
- Domain expertise or lack thereof

### How are the data produced?
- Data collection methods
- Measurement instruments
- Sampling strategies
- Data quality and limitations

## Methods for Understanding Domain/Context

The lecture emphasizes three fundamental approaches to understanding users:

1. **Talk to them** - User interviews and conversations
2. **Ask them to share their work with you** - Contextual inquiry
3. **Share prototypes with them** - Iterative feedback and testing

## Task / Questions
Understanding what users need to accomplish is critical for design decisions.

### Key Questions About Tasks
There are a few questions you can ask yourself when going through this process.

#### What questions are the users trying to answer or actions are they need to take?
- Specific queries they have about the data
- Decisions they need to make
- Insights they're seeking

#### What will the user do with that answer or action?
- How will insights be applied?
- What decisions will be made?
- Who else will be informed?

#### Why is the task important?
- Business value
- Scientific contribution
- Policy implications
- Personal goals

#### What information is needed to answer that question?
- Required data dimensions
- Level of detail needed
- Comparison requirements
- Temporal or spatial scope

### Connection to Encoding
Understanding tasks tells you what to encode and with what priority. The lecture emphasizes that task analysis directly informs:

- Which variables to visualize
- How to prioritize different encodings
- What interactions to support
- What level of detail to provide

## The What/Why/How Framework

This optional framework from Tamara Munzner provides a structured approach to visualization design through three iterative questions.

### Framework Overview

The framework operates in a nested, iterative manner where each cycle of What/Why/How can lead to deeper refinement and dependencies between decisions.

### What? - Data Abstraction

**Core Question:** What are we visualizing?

#### Datasets
Understanding data structure and types:

**Data Types:**
- Items (individual data points)
- Attributes (properties of items)
- Links (connections between items)
- Positions (spatial locations)
- Grids (regular spatial arrangements)

**Data and Dataset Types:**
- **Tables** - Items with attributes
- **Networks & Trees** - Items (nodes) with links and attributes
- **Fields** - Grids with positions and attributes
- **Geometry (Spatial)** - Items with positions
- **Clusters, Sets, Lists** - Items organized into groups

#### Attributes

**Attribute Types:**
- **Categorical** - Discrete, unordered categories
- **Ordered** - Can be ranked
  - Ordinal - Discrete ordered values
  - Quantitative - Continuous numerical values

**Ordering Direction:**
- Sequential - Progressive ordering
- Diverging - Two-way from center point
- Cyclic - Circular ordering pattern

#### Dataset Availability
- **Static** - Fixed dataset
- **Dynamic** - Changing over time

### Why? - Task Abstraction

**Core Question:** Why is the user examining these data?

#### Actions

**Analyze:**
- **Consume**
  - Discover - Find unknown patterns
  - Present - Communicate known information
  - Enjoy - Engage with data aesthetically
- **Produce**
  - Annotate - Add notes or markup
  - Record - Document findings
  - Derive - Create new data from existing

**Search:**
Understanding what users know and seek:

| Location Known | Location Unknown |
|---------------|------------------|
| **Target Known** | Lookup | Browse |
| **Target Unknown** | Locate | Explore |

**Query:**
- **Identify** - Find specific items
- **Compare** - Examine differences/similarities
- **Summarize** - Get overview or aggregate

#### Targets

**All Data:**
- **Trends** - Overall patterns over time or space
- **Outliers** - Exceptional or anomalous values
- **Features** - Distinctive characteristics

**Attributes:**
- **One**
  - Distribution - How values are spread
  - Extremes - Minimum and maximum values
- **Many**
  - Dependency - Relationships between attributes
  - Correlation - Statistical relationships
  - Similarity - How alike attributes are

**Network Data:**
- **Topology** - Overall structure
- **Paths** - Routes between nodes

**Spatial Data:**
- **Shape** - Geographic or spatial form

### How? - Visual Encoding and Interaction

**Core Question:** How does the visualization help achieve goals?

#### Encode - Arrange

**Express:**
- Convey data directly through visual marks

**Separate:**
- Distinguish different data elements clearly

**Order:**
- Arrange according to meaningful sequence

**Align:**
- Position elements for comparison

**Use:**
- Employ marks effectively for the task

#### Map - From Categorical and Ordered Attributes

**Color:**
- **Hue** - Color type (red, blue, green, etc.)
- **Saturation** - Color intensity
- **Luminance** - Brightness

**Size, Angle, Curvature** - Various visual dimensions

**Shape** - Different glyphs or marks (circle, square, triangle, etc.)

**Motion:**
- Direction
- Rate
- Frequency

#### Manipulate

**Change:**
- Adjust viewpoint or parameters

**Select:**
- Choose specific items or regions

**Navigate:**
- Move through data space

#### Facet

**Juxtapose:**
- Place multiple views side-by-side

**Partition:**
- Divide data into separate regions

**Superimpose:**
- Overlay multiple representations

#### Reduce

**Filter:**
- Remove unwanted data from view

**Aggregate:**
- Group and summarize data

**Embed:**
- Integrate into other contexts

## Example Applications
Let's apply these ideas to two different examples.

### Case Study 1: NASA Spacecraft Operations (Rachel Binx - Vortex)
Users had never seen their data visually before, and the periodicity of events was revelatory.

**Domain/Context:**
- Users: NASA spacecraft operators
- Context: Real-time spacecraft monitoring
- Prior work: Manual review of log files
- Data: Event records from spacecraft

**Tasks:**
- Monitor spacecraft status
- Identify anomalies
- Understand event patterns
- Track periodic events

**Design Decisions:**
- Visual representation of temporal patterns
- Support for identifying rhythms in event data
- Multiple coordinated views

### Case Study 2: Jigsaw - Visual Analytics Tool
Let's revisit our video demonstration.

**Domain/Context:**
- Users: Intelligence analysts, researchers
- Context: Investigative analysis
- Task: Make sense of large document collections

**Tasks:**
- Explore connections between entities
- Identify patterns across documents
- Compare different data views
- Generate and test hypotheses

**Design Features:**
- Multiple coordinated views (List View, Graph View, Scatter Plot View, Text View)
- Interactive linking between views
- Support for iterative exploration
- Focus on user journey through questions, not just information efficiency

## Group Activity

The lecture included an in-class group activity where students:

1. Revisited visualizations from earlier in the course
2. Identified the domain and context
3. Analyzed the tasks being supported
4. Applied the What/Why/How framework (optional)

This reinforced concepts by applying the framework to familiar examples.

## Looking Forward
Let's look at next steps through the lens of material and activity.

### Materials

**User Research:**
- Methods for understanding users
- Design research techniques
- User interviews
- Contextual inquiry
- Think-Aloud Protocol

**Measurement and Evaluation:**
- How to assess visualization effectiveness
- User testing approaches
- Evaluation frameworks

**The Player:**
- User as co-creator
- Interactive experiences
- Game design concepts

### Interactive Experience Assignment

The lecture announced details about an upcoming interactive experience assignment with two options:

**Option 1: Video Game**
- Well-behaved games (violent or non-violent options)
- Short duration
- Can be inexpensive ($7) and played on phone
- Two formats:
  - 1.1: In-class discussion with grade
  - 1.2: Zoom discussion with grade (Friday 3pm)

**Option 2: Essay**
- Engage with 4 different interactive visualizations
- Write 4-sentence response to each prompt
- No cost, browser-only access required

## Activities
For this lecture, consider the following to supplement your review of this material.

### Lecture Video
[Watch Lecture 14: Task / Domain on Vimeo](https://vimeo.com/1064129940)

### Reading
An overview of what / why / how at [Visualisation Analysis & Design by Tamara Munzner or the What-Why-How of data viz](https://www.datarocks.co.nz/post/data-viz-bookshelf_visualization-analysis-design-tamara-munzner).

### Links
- [Video 1 from lecture - Jigsaw Visual Analytics](https://www.youtube.com/watch?v=2CMw4i9DiaM)
- [Video 2 from lecture - Designing for Realtime Spacecraft Operations](https://www.youtube.com/watch?v=HuYKhSHcRSQ)

## Citations

[1] T. Munzner, "Visualization Analysis & Design," University of British Columbia, 2021. Available: https://www.youtube.com/watch?v=pHljd-cgICY

[2] T. Romanowski, "Visualisation Analysis & Design by Tamara Munzner or the What-Why-How of data viz," Datarocks, 2023. Available: https://www.datarocks.co.nz/post/data-viz-bookshelf_visualization-analysis-design-tamara-munzner

[3] J. Stasko, C. Gorg, Z. Liu, and K. Singhal, "Jigsaw – Visual Analytics," Georgia Institute of Technology, 2009. Available at: https://youtu.be/2CMw4i9DiaM?feature=shared

[4] R. Binx, "Designing for Realtime Spacecraft Operations," OpenVisConf, 2016. Available at: https://youtu.be/HuYKhSHcRSQ?feature=shared
