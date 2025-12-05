# Lecture 1: Hello Visualization

**Stat 198: Interactive Data Science and Visualization**
**Instructor:** A Samuel Pottinger
**Original Instruction Date:** January 22, 2025

## Description

An overview of the course, what you will learn, and what we will be doing together. We look at 4 different perspectives on data visualization in order to paint a landscape of ideas that will be revisited and expanded upon throughout the rest of the semester.

## Key Takeaways

This lecture introduces the four foundational perspectives on data visualization and establishes the core concepts that will guide the course.

### Visual Encoding Devices
From Cleveland and McGill's research on elementary perceptual tasks:
- Position on common scale (most accurate).
- Position on non-aligned scales.
- Length, direction, angle.
- Area.
- Volume.
- Curvature.
- Shading.
- Color saturation (least accurate).

### The Premise of Data Visualization
The human visual system is good at spotting patterns. We can leverage this capability to make data more understandable and actionable.

## Course Overview
We start with a discussion of the broader structure of the course.

### What You Will Learn
- **Build data visualizations and interactive experiences** to share your findings with others.
- **Tell impactful stories** that engage your readers emotionally through data.
- **Invite your audience in as co-creators** to build new meaning alongside you in your work and collaborate with AI/ML to design solutions and make decisions.
- **Craft tools to explore data-heavy questions** and uncover insights.
- **Incorporate ethics and accessibility** into your data visualization work.

### Course Structure
You can think of the course as being broken into a series of chapters.

- **Hello**: Overview of data visualization (Creative Python).
- **Primitives**: Perception/cognitive science for visualization (Sketchingpy, Matplotlib).
- **Combination**: Data visualization within human-centered design (Geospatial and graph data).
- **Conversation**: Game design (Alternative user inputs).
- **Context**: Accessibility and ethics (Adaptive technologies).
- **Skills**: Iterative process (JavaScript, D3, P5.js).

Across the course, you will have an opportunity to engage with concepts through:

- Weekly exercises
- Weekly reading assignments
- Interactive experience
- Final project with presentation

### What We Won't Cover
There are some limitations to our time together. If these are essential to you, it might be best to find another course:

- Deep investigation of data manipulation/cleaning
- Full treatment of evaluative methods
- Server-side engineering
- Tableau, PowerBI, and similar tools

## Four Perspectives on Data Visualization
Thematically, our time together will be broken into 4 perspectives. These represent different ways of thinking about data visualization and guide design in different ways.

### 1. Data Visualization as Representation

**Core Question:** How can data become visible?

**Key Concepts:**
- **Visual encoding**: Mapping attributes of data to visual attributes.
- **Elementary perceptual tasks**: Position, length, direction, angle, area, volume, curvature, shading, color saturation.
- Understanding when some visual encodings may be better than others.
- A first look at visualization and accessibility.

**Example: Isle Royale Wolf and Moose Populations**
- A look at populations of wolf and moose and their relationship.
- Demonstrated the premise that the human visual system is good at spotting patterns.
- Showed progression from raw data table → color-coded table → bar charts → revealing relationships between variables. Each of these take advantage of increasingly useful "encoding devices" for this example dataset.

**What This Perspective Offers:**
- Flexibility beyond the "chart wizard" but principles to guide us.
- Basic building blocks for how humans process visual information.
- Freedom to use that understanding in many different ways.

**Where This Comes Back:** Learning more about the human visual system to understand when to use different chart types or encoding devices.

### 2. Data Visualization as Task

**Core Question:** How can users ask questions of data?

**Key Concepts:**
- Visualizations are part of a broader user journey.
- Structured way to think about the user in the context of data visualization.
- Focus on domains, tasks, questions, and data.
- Evidence-based understanding of user needs more through a user-centered design or anthropology lens.

**Example: Rachel Binx at NASA (Vortex)**
- Looking at "event records" sent from spacecraft to NASA.
- Interviewed users to figure out how they worked with data previously (log files).
- Users had never seen their data visually before.
- Periodicity of events was revelatory.
- Boiled down into "tasks" the user executes and built user experiences to support those tasks.

**Example Visualization Tool: Jigsaw**
- Multiple coordinated views (List View, Graph View, Scatter Plot View, Text View).
- Supporting investigative analysis through interactive visualization.
- Follows a user through a series of questions or tasks, not just efficiency of conveying info.

**What This Perspective Offers:**
- Structured evidence-based understanding of the user to support them in their tasks.
- Orients around domains, tasks, questions, and data.
- Fits within a broader modern user experience design dialogue.
- Builds on Tamara Munzner's "What/Why/How" framework.

**Where This Comes Back:** Discussion of how to use more traditional design concepts including those employed in other forms of product and UX design as part of data visualization and interactive data experiences.

### 3. Data Visualization as Message

**Core Question:** How can data tell stories?

**Key Concepts:**
- Forms given to data enable authors to convey a message to a reader.
- How does the reader feel when going through a visualization?
- Where is efficiency helpful but where does it conflict with the message of the piece?
- How might we defy reader expectations or have them confront prior held beliefs?

**Example: U.S. Gun Killings (Periscopic)**
- Uses orange arcs to show stolen years (lives cut short).
- Gray arcs show the years people could have lived.
- Focuses on individual lives lost and potential futures.
- Not the most "efficient" according to the cognitive science perspective and encoding devices but making it less "efficient" makes it more powerful by giving weight to the deaths.

**Example: A Treaty to End Plastic Pollution (UC Berkeley/UCSB)**
- Similar to gun deaths visualization, not the most efficient according to encoding devices.
- Combines logos (rational argument) with pathos (emotional appeal).

**Example: "You Draw It" (New York Times)**
- Interactive piece about family income and college attendance.
- Reader draws their expectation on the chart before seeing the data.
- Challenges assumptions and creates engagement.
- Makes readers confront their prior beliefs.
- Less "efficient" than a more traditional approach but creates an emotional investment in result.

**What This Perspective Offers:**
- A way to convey messages with logos and pathos.
- How to invoke emotional response.
- How to challenge reader assumptions.
- How to understand the process by which messages and meaning are interpreted.

**Where This Comes Back:** Techniques we can borrow from art and design to guide and evoke an emotional response.

### 4. Data Visualization as Dialogue

**Core Question:** How can data help us think?

**Key Concepts:**
- Data as humane dynamic media.
- The designer creates media for thought.
- Elevating the reader to an author of tools and co-creator of meaning.
- Creating tools which afford users an opporutnity to find their own narratives instead of prescribing one.
- "Ghost train ride" vs "open world" metaphors (It's a Small World vs Star Wars: Galaxy's Edge).

**Example: Global Plastics AI Policy Tool**
- Layered experience where users can simulate different policies.
- Shows multiple outcome metrics (Mismanaged Waste, Incinerated Waste, Landfill Waste, Gross GHG).
- Users can adjust policy levers and see projected impacts.
- Invitation to build outside the original designer's intention.
- Supports exploration and hypothesis testing.

**Example: En-ROADS Climate Simulator**
- Interactive sliders for various climate and energy policies.
- Real-time feedback on impact.
- Users can test their own policy scenarios.
- Supports collaborative decision-making.

**What This Perspective Offers:**
- Co-creation and user agency.
- Often leaning on game design concepts.
- How to teach with/without tutorializing.
- How to create spaces to interrogate assumptions.
- How to build media to be repurposed.
- How to design experiences where the user is co-author.

**Where This Comes Back:** How to employ interaction and game design to create digital spaces where users can explore data more freely and go beyond your own narrative.

## Key Examples and Case Studies

### Historical Example: John Snow's Cholera Map (1854)
- Classic example of data visualization as representation
- Mapped cholera deaths in London
- Revealed the Broad Street pump as the source
- Data → Graphic transformation that saved lives

### Isle Royale Wolf and Moose Populations
- Demonstrated the power of visual encoding
- Showed relationship between predator and prey populations over time
- Year 1994 saw the most moose (1800)
- Inverse relationship visible in visualization

### We Feel Fine
- Harvested emotional statements from blogs
- Created an artistic, interactive exploration of human emotion
- Combined data visualization with emotional storytelling

## Activities
Like many lectures, we will ahve an assignment and reading. In addition to this outline, you can continue your engagement through videos.

### Lecture Video
- [Watch Lecture 1: Hello Visualization on Vimeo](https://vimeo.com/1047306328)

### Assignment
For getting warmed up, please write about 4 sentences reflecting on what you are hoping to gain from the course. If you feel comfortable and want to engage with other learners, post your response online!

### Reading
We will learn more about how tools change the way we think. Please watch the very excellent [Media for Thinking the Unthinkable lecture](https://vimeo.com/67076984) delivered by Bret Victor at the MIT Media Lab. A question for you to consider is what kinds of representations of thought do you use every day?

### Links
- [Video for the section on data visualization as task](https://youtu.be/2CMw4i9DiaM?t=112&feature=shared)
- [Sam's teaching homepage](https://interactivedatascience.courses)

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

[20] A. Pottinger, "Interactive Data Science." 2024. Available: https://interactivedatascience.courses/

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
