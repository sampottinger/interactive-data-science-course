# Lesson 1: Overview
A look at four perspectives on data visualization.

## Objective
Introduce the four foundational perspectives on data visualization and establish core concepts that guide the course structure and learning outcomes.

## Outline
This lecture provides a broad overview of data visualization through four distinct perspectives, introducing students to the course structure and demonstrating how different approaches to visualization serve different purposes.

### Course overview
Building skills across design and implementation.

  - Build data visualizations and interactive experiences to share findings with others.
  - Tell impactful stories that engage readers emotionally through data.
  - Invite audiences in as co-creators to build new meaning alongside you in your work and collaborate with AI/ML to design solutions and make decisions.
  - Craft tools to explore data-heavy questions and uncover insights.
  - Incorporate ethics and accessibility into data visualization work.

### Course structure
Six sections combining conceptual understanding with technical skills.

  - Hello: Overview of data visualization (Creative Python).
  - Primitives: Perception and cognitive science for visualization (Sketchingpy, Matplotlib).
  - Combination: Data visualization within human-centered design (Geospatial and graph data).
  - Conversation: Game design (Alternative user inputs).
  - Context: Accessibility and ethics (Adaptive technologies).
  - Skills: Iterative process (including other technologies like JavaScript, D3, P5.js).

### Course activities
Multiple opportunities to engage with concepts through different modalities.

  - Weekly exercises.
  - Weekly reading assignments.
  - Interactive experience.
  - Final project with presentation.

### What we won't cover
Some limitations to the course scope.

  - Deep investigation of data manipulation and cleaning.
  - Full treatment of evaluative methods.
  - Server-side engineering.
  - Tableau, PowerBI, and similar tools.

### Data visualization as representation
How can data become visible?

  - Visual encoding: Mapping attributes of data to visual attributes.
  - Elementary perceptual tasks: Position, length, direction, angle, area, volume, curvature, shading, color saturation.
  - Understanding when some visual encodings may be better than others.

Example: Isle Royale wolf and moose populations

  - Demonstrate the premise that the human visual system is good at spotting patterns.
  - Progression from raw data table to color-coded table to bar charts reveals relationships between variables using increasingly effective encoding devices.

Why this perspective?

  - Offers flexibility beyond the chart wizard with principles to guide design decisions.
  - Returns later when learning more about the human visual system to understand when to use different chart types or encoding devices.

### Data visualization as task
How can users ask questions of data?

  - Visualizations are part of a broader user journey.
  - Structured way to think about the user in the context of data visualization.
  - Focus on domains, tasks, questions, and data.
  - Evidence-based understanding of user needs through a user-centered design or anthropology lens.

Rachel Binx at NASA (Vortex)

  - Looking at event records sent from spacecraft.
  - Interviewed users to understand how they worked with data previously (log files).
  - Users had never seen their data visually before and the periodicity of events was revelatory.
  - Boiled down into tasks the user executes and built user experiences to support those tasks.

Jigsaw

  - Multiple coordinated views supporting investigative analysis through interactive visualization.
  - Offers structured evidence-based understanding of the user to support them in their tasks.

Why this perspective

  - Orients around domains, tasks, questions, and data.
  - Fits within a broader modern user experience design dialogue building on Tamara Munzner's What/Why/How framework.
  - Returns later in discussion of how to use traditional design concepts employed in other forms of product and UX design as part of data visualization and interactive data experiences.

### Data visualization as message
How can data tell stories?

  - Forms given to data enable authors to convey a message to a reader.
  - How does the reader feel when going through a visualization?
  - Where is efficiency helpful but where does it conflict with the message of the piece?
  - How might we defy reader expectations or have them confront prior held beliefs?

U.S. Gun Killings (Periscopic)

  - Uses orange arcs to show stolen years (lives cut short) and gray arcs to show the years people could have lived.
  - Focuses on individual lives lost and potential futures.
  - Not the most efficient according to the cognitive science perspective and encoding devices but making it less efficient makes it more powerful by giving weight to the deaths.

Other examples

  - A Treaty to End Plastic Pollution (UC Berkeley/UCSB)
    - Combines approaches.
    - Logos (rational argument).
    - Pathos (emotional appeal).
  - You Draw It (New York Times) about family income and college attendance.
    - Reader draws their expectation on the chart before seeing the data.
    - Challenges assumptions and creates engagement making readers confront their prior beliefs.
    - Less efficient than a traditional approach but creates emotional investment in result.
    - Offers a way to convey messages with logos and pathos.

Why this perspective

  - How to invoke emotional response and challenge reader assumptions.
  - How to understand the process by which messages and meaning are interpreted.
  - Returns later with techniques we can borrow from art and design to guide and evoke an emotional response.

### Data visualization as dialogue
How can data help us think?

  - Data as humane dynamic media.
  - The designer creates media for thought.
  - Elevating the reader to an author of tools and co-creator of meaning.
  - Creating tools which afford users an opportunity to find their own narratives instead of prescribing one.
  - Ghost train ride vs open world (It's a Small World vs Star Wars: Galaxy's Edge).

Global Plastics AI Policy Tool

  - Layered experience where users can simulate different policies.
  - Shows multiple outcome metrics (Mismanaged Waste, Incinerated Waste, Landfill Waste, Gross GHG).
  - Users can adjust policy levers and see projected impacts.
  - Invitation to build outside the original designer's intention.
  - Supports exploration and hypothesis testing.

En-ROADS Climate Simulator

  - Interactive sliders for various climate and energy policies.
  - Real-time feedback on impact and users can test their own policy scenarios supporting collaborative decision-making.

Why this perspective?

  - Offers co-creation and user agency often leaning on game design concepts.
  - How to teach with/without tutorializing.
  - How to create spaces to interrogate assumptions and build media to be repurposed.
  - How to design experiences where the user is co-author.
  - Returns later when employing interaction and game design to create digital spaces where users can explore data more freely and go beyond your own narrative.

## Take Aways
Data visualization encompasses multiple perspectives that serve different purposes and audiences.

  - Four perspectives (representation, task, message, dialogue) offer different lenses for understanding and creating visualizations.
  - Visual encoding builds on how the human visual system processes information with some encodings being more effective than others.
  - User-centered design approaches help create visualizations that support specific tasks and domains.
  - Message-focused visualizations can combine rational argument with emotional appeal to create impact.
  - Interactive tools can elevate users to co-creators allowing them to explore data and find their own meaning.
  - The course will develop both implementation skills (primarily Python with some JavaScript) and design understanding grounded in evidence and literature.

## Citations

[1] G. Aisch, A. Cox, and K. Quealy, "You Draw It: How Family Income Predicts Children's College Chances." The New York Times Company, May 28, 2015. Available: https://www.nytimes.com/interactive/2015/05/28/upshot/you-draw-it-how-family-income-affects-childrens-college-chances.html

[2] R. Binx, "Vortex." 2015. Available: https://rachelbinx.com/data-visualization/vortex

[3] R. Binx, "Designing for Realtime Spacecraft Operations." BocoupLLC, Apr. 2016. Available: https://www.youtube.com/watch?v=HuYKhSHcRSQ

[4] J. Harris, "We Feel Fine." TED Conference, Dec. 2009. Available: https://www.youtube.com/watch?v=vi8WrnWNSzU

[5] W. S. Cleveland and R. McGill, "Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods," *Journal of the American Statistical Association*, vol. 79, no. 387, pp. 531–554, Sep. 1984, doi: 10.1080/01621459.1984.10478080.

[6] Flipflops, "I feel… everything." Flipflops.org, Oct. 2007. Available: https://www.flipflops.org/category/thoughtful/page/2/

[7] V. Hart and N. Case, "Parable of the Polygons." Nicky Case, 2022. Available: https://ncase.me/polygons/

[8] Isle Royale National Park Michigan, "Wolf & Moose Populations." National Parks Service, Mar. 29, 2024. Available: https://www.nps.gov/isro/learn/nature/wolf-moose-populations.htm

[9] S. D. Kamvar and J. Harris, "We feel fine and searching the emotional web," in *Proceedings of the fourth ACM international conference on Web search and data mining*, Hong Kong China: ACM, Feb. 2011, pp. 117–126. doi: 10.1145/1935826.1935854.

[10] A. KIRK, *DATA VISUALISATION: a handbook for data driven design*. S.l.: SAGE PUBLICATIONS, 2024.

[11] A. Kirk, "Visualizing Data." Visualising Data Ltd, 2024. Available: https://visualisingdata.com/

[12] T. Munzner, "A Nested Model for Visualization Design and Validation," *IEEE Trans. Visual. Comput. Graphics*, vol. 15, no. 6, pp. 921–928, Nov. 2009, doi: 10.1109/TVCG.2009.111.

[13] T. Munzner, "Visualization Analysis and Design." AK Peters Visualization Series, 2014. Available: https://books.apple.com/us/book/visualization-analysis-and-design/id1567434451

[14] T. Munzner, *Visualization analysis and design*. in A.K. Peters visualization series. Boca Raton: CRC Press, Taylor & Francis Group, 2015.

[15] T. Munzner, "Task Abstraction (Ch 3), Visualization Analysis & Design, 2021." YouTube, 2021. Available: https://www.youtube.com/watch?v=pHljd-cgICY

[16] M. Nix, *Visual simplexity: die Darstellung großer Datenmengen*. Frankfurt am Main: entwickler.press, 2013.

[17] K. Rees and Periscopic, "U.S. Gun Deaths." Periscopic, 2018. Available: https://guns.periscopic.com/

[18] A. Pottinger, "FoodSim: San Francisco." 2023. Available: https://foodsimsf.com/

[19] A. Pottinger, "Income Gaps." 2023. Available: https://incomegaps.com/

[20] A. Pottinger, "Interactive Data Science." 2024. Available: https://mooc.interactivedatascience.courses/

[21] A. S. Pottinger et al., "Combining Game Design and Data Visualization to Inform Plastics Policy: Fostering Collaboration between Science, Decision-Makers, and Artificial Intelligence," 2023, arXiv. doi: 10.48550/ARXIV.2312.11359.

[22] A. Pottinger, L. Connor, B. Guzder-Williams, M. Weltman-Fahs, N. Gondek, and T. Bowles, "Climate-driven doubling of U.S. maize loss probability: Interactive simulation with neural network Monte Carlo," *JDSSV*, 2025. doi: 10.52933/jdssv.v5i3.134

[23] A. S. Pottinger and G. Zarpellon, "Pyafscgap.org: Open source multi-modal Python-basedtools for NOAA AFSC RACE GAP," *JOSS*, vol. 8, no. 86, p. 5593, Jun. 2023, doi: 10.21105/joss.05593.

[24] J. N. Rooney-Varga, F. Kapmeier, J. D. Sterman, A. P. Jones, M. Putko, and K. Rath, "The Climate Action Simulation," *Simulation & Gaming*, vol. 51, no. 2, pp. 114–140, Apr. 2020, doi: 10.1177/1046878119890643.

[25] J. Schell, *The art of game design: a book of lenses*, Third edition. Boca Raton: CRC Press/Taylor & Francis Group, 2020.

[26] J. Snow, *On the mode of communication of cholera*. London: John Churchill, 1855. Available: https://archive.org/details/b28985266/page/n57/mode/2up

[27] J. Stasko, C. Gorg, Z. Liu, and K. Singhal, "Jigsaw: Supporting Investigative Analysis through Interactive Visualization," in *2007 IEEE Symposium on Visual Analytics Science and Technology*, Sacramento, CA, USA: IEEE, Oct. 2007, pp. 131–138. doi: 10.1109/VAST.2007.4389006.

[28] The Document Foundation, *LibreOffice*. (2024). The Document Foundation.

[29] ThoughtLab, The Wendy and Eric Schmidt Center for Data Science and Environment, and Benioff Ocean Science Laboratory, "A Treaty to End Plastic Pollution. Forever." University of California, 2023. Available: https://plasticstreaty.berkeley.edu/

[30] B. Victor, "Inventing on Principle." CUSEC, 2012. Available: https://www.youtube.com/watch?v=PUv66718DII

[31] B. Victor, "Media for Thinking the Unthinkable." MIT Media Lab, Apr. 04, 2013. Available: https://vimeo.com/67076984

[32] Visual Computing BLOG, "Tamara Munzner discussed quantification in terms of a nested model of visualization design and evaluation." Transregional Collaborative Research Center. Available: https://www.visual-computing.org/2018/10/17/computerscienceconferenceweek/201810_conferenceweek_munzner-2/

[33] C. Ware, "Colin Ware | The Data Visualzation Research Lab." University of New Hampshire. Available: https://ccom.unh.edu/vislab/people/colin_ware/

[34] C. Ware, *Information visualization: perception for design*, Fourth edition. Cambridge, MA: Morgan Kaufmann, 2021.

[35] Wikipedia Contributors, "Snow-cholera-map-1.jpg." Wikimedia Foundation, Inc., 2020. Available: https://en.wikipedia.org/wiki/File:Snow-cholera-map-1.jpg

[36] Wikipedia Contributors, "Bret Victor." Wikimedia Foundation, Inc., Jun. 22, 2023. Available: https://en.wikipedia.org/wiki/Bret_Victor

[37] Wikipedia Contributors, "Star Wars: Galaxy's Edge." Wikimedia Foundation, Inc., Sep. 21, 2024. Available: https://en.wikipedia.org/wiki/Star_Wars:_Galaxy%27s_Edge

[38] Wikipedia Contributors, "It's a Small World." Wikimedia Foundation, Inc., Sep. 24, 2024. Available: https://en.wikipedia.org/wiki/It%27s_a_Small_World

[39] N. Yee, "Motivations for Play in Online Games," *CyberPsychology & Behavior*, vol. 9, no. 6, pp. 772–775, Dec. 2006, doi: 10.1089/cpb.2006.9.772.

[40] J. Harris and S. Kavar, "We Feel Fine." We Feel Fine., 2006. Available: http://www.wefeelfine.org and https://jjh.org/we-feel-fine.

[41] J. Harris, "The Web's Secret Stories." TED Conference., 2007. Available: https://youtu.be/zAvNlh2Z0GI?feature=shared.

[42] Thanks to https://unsplash.com/photos/DHl49oyrn7Y

## License

This lesson is part of [Interactive Data Science and Visualization](https://mooc.interactivedatascience.courses/) and is released under a [CC-BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/deed.en) license.
