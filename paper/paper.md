---
title: 'Interactive Data Science and Visualization: Multi-Disciplinary Open Educational Resources for Building Modern Data Experiences'
tags:
  - Python
  - Design
  - Visualization
  - HCI
  - Interactivity
authors:
  - name: A Samuel Pottinger
    orcid: 0000-0002-0458-4985
    affiliation: 1
affiliations:
  - name: Eric and Wendy Schmidt Center for Data Science and Environment at the University of California, Berkeley
    index: 1
date: 2025-02-04
bibliography: paper.bib
---
# Summary
These open educational resources offer hands-on instruction in crafting digital experiences enabling users to interactively engage with data and computation through visualization. Taught at the University of California, Berkeley [@Catalogue] and in guest lectures / workshops across multiple schools and programs [@PottingerTeaching], these labs and lessons begin with traditional information design [@Munzner] and perception science [@Ware]. Then, instruction extends to media studies [@Hall], human-centered computing [@Harrison], user research [@Shneiderman], and game design [@Schell]. Meanwhile, skills labs and guided practical projects explore the software engineering aspects of this multidisciplinary work, inviting scientists, engineers, journalists, designers, and others with programming foundation to build within applied exercises utilizing the unique possibilities of interactive digital media for understanding data [@VictorDead; @Portnow]. Historically situated [@Plato] but embracing modern tools like AI, these reusable resources support instructors and learners in creating "media for thinking the unthinkable" [@VictorMedia].

# Statement of Need
Through hands-on projects, these open source educational materials aim to empower students to critically design interactive digital media for interrogating data. However, going beyond traditional introductory information design instruction, these resources also explore the implementation of these rich bespoke interactive computational experiences as made possible through custom programming^[Taught in Python, adaptable to other languages.]. Altogether, this educational contribution situtates design techniques within engineering instruction as necessary for building media for thought [@VictorMedia].

## State of the field
Existing open data visualization instruction often takes a perception science [@StahmerReynolds] and user-centered design approach [@MunznerYoutube]. These materials may primarily focus on reusable charts or static drawing [@Cairo]. While these valuable resources offer a robust introduction to traditional information design, many existing options choose not to center creating new bespoke experiences possible only with custom programming [@MarcusWu].

## Research impact statement
In response to current open offerings and experience lecturing within existing curricula [@PottingerTeaching], these educational materials instead assume some programming capability enabling the creation of new custom interactive graphical forms. Honoring classical principles [@ClevelandMcGill] but considering them flexibly in novel structures [@PottingerTools], this approach reaches beyond standard charts towards giving students the capacity to build pieces similar to the custom interactive experiences which often light up the classroom but which also often remain out of reach for students to actually construct [@Harris; @Rees]. This embrace of software engineering to augment and reach new design topics enables teachers and learners to update traditional data visualization instruction such as in supporting science-informed policymaking [@Enroads; @PottingerPlasticsTool] and interactive science [@VictorExplorable], meeting new opportunities from computers' ever-growing capacity to react to the user [@VictorDead]. In total, these adaptable modular resources seek to empower learning blending evidence-based design and programming's expressiveness.

# Design
In addition to discussing ethics and accessibility, modular resources explore different perspectives within data visualization. These lessons and projects are designed to be completed with minimal local software configuration.

## Instructional design
The course is organized into ways of understanding data visualization and interactive data science:

 - *Representation*: traditional perception science approach to information design [@Ware].
 - *Task*: modern user-centered design [@Munzner; @Harrison].
 - *Message*: consideration of sociology, anthropology, and media studies [@DiagrammaticCovid; @Hall].
 - *Dialogue*: unique capabilities of digital interactivity [@VictorDead] with audiences as co-creators of meaning, including through game design [@Portnow; @PottingerAfscgap].

This mix of traditional lecture content with hands-on labs and projects^[Each entry includes its own citations which may extend beyond those listed here.] also often include supplementary captioned videos and PDFs. Altogether, these offer the experience of programming to not just learn interactive information design but to feel and understand the role of human iteration. This set of lessons concludes with critical but applied consideration of AI in visualization.

## Software design
Supporting blended design and engineering instruction, materials are compiled from markdown and YAML to HTML at https://mooc.interactivedatascience.courses/ via Python. All instructional materials are available under a Creative Commons license with open source code under a BSD-3-Clause license. Using modern technologies like WebAssembly, one may complete all instruction without installing local software beyond a modern web browser.

## Integration
These materials were taught as a full course^[Original offering was for 2 credit hours upper-division undergraduate or graduate. Use of some optional materials may allow for use in a 3 credit hour setting.] at the University of California, Berkeley in 2025 [@Catalogue] and served different programs and universities as components in other instruction or as workshops [@PottingerTeaching]. Individual lessons may provide topic-specific supplement to other instruction, modules may offer a treatment of a topical area for learning, and the class as a whole may allow for an approximate semester of hybrid hands-on and lecture-based exploration.

# Acknowledgements
Taught under the DeCal program with thanks to Fernando Pérez for guidance / sponsoring Stat 198 and Joanne Chung for the wisdom behind many guest lectures at this course's nucleus. Dedicated to my grandmother who taught me of the unique expressiveness of digital media and a love of teaching.

## Funding
Funded by the Schmidt Center for Data and Environment at the University of California, Berkeley with support from the UC Berkeley Fung Institute for Engineering Leadership.

## AI usage disclosure
Carefully directed AI aided in the HTML rendering system [@Claude]. With the exception of the AI skills lab which generated some content based on demo chat history, all written materials including lessons and labs were first written manually but may have been proofread by AI. Unless trivial "mechanical" edits, AI-assisted changes (including proofreading and formatting) marked in git through co-author.

# References
