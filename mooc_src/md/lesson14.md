# Lesson 14: Tasks and Domains
Understanding tasks and domains, drawing information design to user centered design.

## Objective
Deepen understanding of how to approach data visualization design through the lens of user tasks and domain contexts, introducing Tamara Munzner's What/Why/How framework as an optional structured approach.

## Outline
This lecture expands on the idea of domains and tasks with examples before looking at the What / Why / How framework from Munzner. It provides more information on the second perspective introduced in Lecture 1, focusing on visualization as task alongside representation, narrative, and dialogue perspectives.

### Understanding domains and contexts
Understanding the user's context is essential for effective visualization design.

  - Who is the user and what is their expertise level?
  - What social context is that user in (professional, academic, public)?
  - What are the concepts the user is interacting with and their mental models?
  - What prior knowledge or understanding might the user be interacting with?
  - How are the data produced (collection methods, measurement instruments, sampling)?

### Methods for understanding users
Three fundamental approaches to understanding users and their needs.

  - Talk to them through user interviews and conversations.
  - Ask them to share their work with you through contextual inquiry.
  - Share prototypes with them for iterative feedback and testing.

There are structured appraoches but these act as general principles.

### Understanding tasks and questions
What users need to accomplish is critical for design decisions.

  - What questions are the users trying to answer or actions they need to take?
  - What will the user do with that answer or action?
  - Why is the task important (business value, scientific contribution, policy implications)?
  - What information is needed to answer that question?
  - Understanding tasks tells you what to encode and with what priority.

### The What / Why / How framework
This framework from Tamara Munzner provides a structured approach to visualization design through three iterative questions operating in a nested manner.

  - What (data abstraction): datasets, attributes, dataset availability.
  - Why (task abstraction): actions (analyze, search, query) and targets (trends, outliers, features).
  - How (visual encoding and interaction): encode, map, manipulate, facet, reduce.

Note that this can be a useful framework but is optional in your projects for the course. 

### Data abstraction
Understanding what we are visualizing through data structure and types.

  - Data types: items, attributes, links, positions, grids.
  - Dataset types: tables, networks and trees, fields, geometry (spatial), clusters, sets, lists.
  - Attribute types: categorical, ordered (ordinal, quantitative).
  - Ordering direction: sequential, diverging, cyclic.
  - Dataset availability: static or dynamic.

### Task abstraction
Understanding why users examine data through actions and targets.

  - Analyze actions: consume (discover, present, enjoy) or produce (annotate, record, derive).
  - Search understanding: lookup, browse, locate, explore based on what is known.
  - Query actions: identify, compare, summarize.
  - Targets for all data: trends, outliers, features.
  - Targets for attributes: distribution, extremes, dependency, correlation, similarity.
  - Targets for networks and spatial: topology, paths, shape.

### Visual encoding and interaction
How the visualization helps achieve goals through arrangement and manipulation.

  - Encode and arrange: express, separate, order, align, use marks effectively.
  - Map from categorical and ordered attributes: color (hue, saturation, luminance), size, angle, curvature, shape, motion.
  - Manipulate: change viewpoint or parameters, select items or regions, navigate through data space.
  - Facet: juxtapose (side-by-side), partition (divide), superimpose (overlay).
  - Reduce: filter unwanted data, aggregate and summarize, embed into other contexts.

### Case study: NASA spacecraft operations
Rachel Binx's Vortex project revealed periodicity of events users had never seen visually before.

  - Domain: NASA spacecraft operators monitoring real-time spacecraft with prior work of manual log review.
  - Tasks: monitor spacecraft status, identify anomalies, understand event patterns, track periodic events.
  - Design: visual representation of temporal patterns supporting identification of rhythms through multiple coordinated views.

### Case study: Jigsaw visual analytics
An intelligence analysis tool for making sense of large document collections.

  - Domain: intelligence analysts and researchers in investigative analysis contexts.
  - Tasks: explore connections between entities, identify patterns across documents, compare different data views, generate and test hypotheses.
  - Design: multiple coordinated views (list, graph, scatter plot, text), interactive linking, iterative exploration, focus on user journey through questions.

## Take Aways
Effective visualization design requires understanding both the user's domain context and their specific tasks, with the What/Why/How framework offering an optional structured approach to design decisions.

  - Talk to users, share work with them, and prototype iteratively to understand domain and context.
  - Understanding tasks directly informs what to encode and with what priority.
  - The What/Why/How framework provides a nested, iterative approach through data abstraction, task abstraction, and visual encoding.
  - Apply these concepts to familiar examples through analysis of domain, context, and tasks.

## Note
This outline was expanded after the video was recorded and may include additional details.

## Citations

[1] T. Munzner, "Visualization Analysis & Design," University of British Columbia, 2021. Available: https://www.youtube.com/watch?v=pHljd-cgICY

[2] T. Romanowski, "Visualisation Analysis & Design by Tamara Munzner or the What-Why-How of data viz," Datarocks, 2023. Available: https://www.datarocks.co.nz/post/data-viz-bookshelf_visualization-analysis-design-tamara-munzner

[3] J. Stasko, C. Gorg, Z. Liu, and K. Singhal, "Jigsaw – Visual Analytics," Georgia Institute of Technology, 2009. Available at: https://youtu.be/2CMw4i9DiaM?feature=shared

[4] R. Binx, "Designing for Realtime Spacecraft Operations," OpenVisConf, 2016. Available at: https://youtu.be/HuYKhSHcRSQ?feature=shared
