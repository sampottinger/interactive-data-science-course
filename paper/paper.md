---
title: 'Interactive Data Science and Visualization: Multi-disciplinary Open Educational Resources for Building Modern Data Experiences'
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
These open educational resources offer hands-on instruction in crafting digital experiences enabling users to interactively engage with data and computation through visualization. Taught at the University of California, Berkeley [@Catalogue] and in guest lectures / workshops across multiple schools and programs [@PottingerTeaching], these labs and lessons provide a multi-disciplinary approach. Specifically, these open source materials begin with traditional information design [@Munzner] and perception science [@Ware]. Then, instruction extends to media studies [@Hall], human-centered computing [@Harrison], user research [@Shneiderman], and game design [@Schell]. Meanwhile, skills labs and guided practical projects explore software engineering alongside these diverse ideas, inviting scientists, engineers, journalists, designers, and others to 1) critically consider the role of those constructing interfaces to information and 2) act on the unique possibilities of digital media [@VictorDead; @Portnow]. Historically situated [@Plato] but embracing modern tools like AI, these reusable resources support instructors and learners in creating "media for thinking the unthinkable" [@VictorMedia].

# Statement of Need
Existing open data visualization instruction often takes a perception science [@StahmerReynolds] and user-centered design approach [@MunznerYoutube] but may lean on reusable charts or static drawing [@Cairo]. Some valuable resources choose not to center creating new bespoke experiences possible only with custom programming [@MarcusWu]. In response to current open offerings and experience lecturing within existing curricula [@PottingerTeaching], these educational materials instead assume some programming capability enabling the creation of new custom interactive graphical forms. Honoring classical principles [@ClevelandMcGill] but considering them flexibly in novel structures [@PottingerTools], this approach reaches beyond standard charts towards giving students the capacity to build pieces similar to the custom interactive experiences which often light up the classroom but which also often remain out of reach for students to actually construct [@Harris; @Rees]. This embrace of software engineering to augment information design enables teachers and learners to update traditional data visualization instruction such as in supporting science-informed policymaking [@Enroads; @PottingerPlasticsTool] and interactive science [@VictorExplorable], meeting new opportunities from computers' ever-growing capacity to react to the user [@VictorDead]. In total, these adaptable modular resources seek to empower learning blending evidence-based information design and programming's expressiveness.

# Objective, Design, and Content
Through hands-on projects^[Taught in Python, adaptable to other languages.], these open source educational materials aim to both empower students to critically design digital media and give them the capability to build rich bespoke interactive data experiences. In addition to discussing ethics and accessibility, modular resources explore different "perspectives" on data visualization as:

 - *Representation*: traditional perception science approach to information design [@Ware].
 - *Task*: modern user-centered design [@Munzner; @Harrison].
 - *Message*: consideration of sociology, anthropology, and media studies [@DiagrammaticCovid; @Hall].
 - *Dialogue*: unique capabilities of digital interactivity [@VictorDead] with audiences as co-creators of meaning, including through game design [@Portnow; @PottingerAfscgap].

This mix of traditional lecture content with hands-on labs and projects^[Each entry includes its own citations which may extend beyond those listed here.] also often include supplementary captioned videos and PDFs. Altogether, these offer the experience of programming to not just learn interactive information design but to feel and understand the role of human iteration, concluding with critical but applied consideration of AI in visualization.

# Use
Supporting blended design and engineering instruction, materials are compiled from markdown and YAML to HTML at https://mooc.interactivedatascience.courses/ via Python. All materials are available under a Creative Commons license with open source code. Using modern technologies like WebAssembly, one may complete all instruction without installing local software beyond a modern web browser.

These materials were taught as a full course^[Original offering was for 2 credit hours upper-division undergraduate or graduate. Use of some optional materials may allow for use in a 3 credit hour setting.] at the University of California, Berkeley in 2025 [@Catalogue] and served different programs and universities as components in other instruction or as workshops [@PottingerTeaching]. Individual lessons may provide topic-specific supplement to other instruction, modules may offer a treatment of a topical area for learning, and the class as a whole may allow for an approximate semester of hybrid hands-on and lecture-based exploration.

# Acknowledgements
**Thanks** to Fernando Pérez for guidance / sponsoring Stat 198 and Joanne Chung for the wisdom behind many guest lectures at this course's nucleus. **Funded** by the Schmidt Center for Data and Environment at the University of California, Berkeley with support from the UC Berkeley Fung Institute for Engineering Leadership. Carefully directed **AI** aided in the HTML rendering system [@Claude]. With the exception of the AI skills lab which generated some content based on demo chat history, all lessons and labs were first written manually. Unless trivial, AI-assisted edits (including proofreading and formatting) marked in git through co-author. **Dedicated** to my grandmother who taught me of the unique expressiveness of digital media and a love of teaching.

# References
