# Interactive Data Science and Visualization
Formal curriculum and syllabus which is completed by the [course manual](/course_wide/manual.html) with practical guidance on either taking the course as a learner or providing / adapting it as an instructor.

**Other formats:** [HTML version](syllabus.html) | [Markdown version](syllabus.md) (you are here) | [PDF version](syllabus.pdf) (from UC Berkeley Spring 2025 teaching)

## Motivation
Before getting into a detailed breakdown of the material, let’s explore how this course can help.

### Why take this class?
Data are essential to how we experience and understand the world. The way we interact with tools, analyses, and simulations all change the insights we learn, the stories we tell, the actions we take, who is included, and what is left out. This course combines traditional user experience and information design with interactive storytelling and video game design. We will emphasize practical techniques and technical skills needed to make both word-class data visualizations and interactive data science tools. More info online at [https://interactivedatascience.courses](https://interactivedatascience.courses).

### Who is this for?
Scientists, engineers, designers, artists, journalists, and anyone else who wants to explore new methods for interactively and visually understanding, experiencing, and communicating data.

### What we will do together?
We have three pillars of our time together:

- Explore data visualization theory and fundamentals before studying cutting edge work in interactive data science.
- Learn practical career-building technologies for building both static and interactive data experiences through hands-on portfolio-building activities.
- Examine existing powerful and informative interactive experiences including data visualizations and other interactive media like video games.

### What you will be able to do after?
After completing the course, you should be able to:

- Build data visualizations and other interactive experiences to share your data findings with others.
- Invite your audience in as co-creators to build new meaning alongside you in your work.
- Craft digital tools which help both you and your users navigate data-heavy tasks and uncover insights.
- Tell impactful stories that engage your readers emotionally through data.
- Incorporate ethics and accessibility into your work.

## Basics
Next, let’s explore the logistics and basic information of the class together. This section offers fundamental information about the course as required to consider its place within a personal learning journey or for instructors to consider its role within a broader degree plan.

### Instructor
Hello! My name is Sam Pottinger. I am a Senior Research Software Engineer / Data Scientist at UC Berkeley's Schmidt Center for Data Science and Environment. I've previously worked at Google, Apple, two start ups, and global design firm IDEO. I offer over a decade of data visualization / interactive science experience. My research at Berkeley blends information design, video game design, and ML / AI, and public policy for environment.

### Schedule and credit
This course can be adapted to meet different learning criteria and formats. However, in teaching it in person at the University of California Berkeley, we met twice weekly for an hour with an additional hour of office hours online. It was completed in a semester-based schedule. Additionally, this was originally offered for 2 credit hours though conversion of optional aspects of the course to required may meet criteria to teach for 3 credit hours instead. In either case, this was comprised of hands-on activities, final mastery project, original lectures, discussion, hands-on skills labs, and guest lectures over 7 short modules.

### Prerequisites
Recommended but not required that learners have had prior introduction to Python or JavaScript (course or self-taught). Recommended at the graduate level or for undergrad at sophomore or later.

### Skills taught
In considering how this course may layer into broader degree requirements or personal learning objectives:

 - **Technical Skills Taught**: [Sketchingpy](https://sketchingpy.org/) (Pottinger 2024), [P5](https://p5js.org/) (P5js Contributors 2026), and [D3](https://d3js.org/) (Bostock et al 2011). Will also provide optional brief Python and JavaScript / HTML / CSS instruction.
 - **Theoretical Skills Taught**: Information design, video game design, evaluative methods, human visual perception, accessibility.

### Grading
Given each lecture as described below. 54% small projects, 12% interactive experience reflection, 35% final project intended to build mastery. Originally taught as pass / fail. Scores provided for each small project, final project, and the interactive experience reflection.

### Additional Resources
Includes complementary short reading / videos and supportive technology skills labs. The interactive experience will be your choice of either a video game or interactive data visualization.
  
## Course sections
The course is designed across 7 major sections expected to be taken in order.

### 1. Hello
Begin with an initial exploration of key ideas.

We start our journey together by motivating why data visualization is useful, what interactive science can offer, and take an early look at some of the foundational ideas that we will explore together throughout the rest of the course. We will also make sure everyone has what they need to do some upcoming activities with two optional skills labs.

| Day | Reading / Watching | Classroom Material                    | Activity             |
| --- | ------------------ | ------------------------------------- | -------------------- |
| 1   | None               | 4 perspectives on data visualization. | Async introductions. |
| 2 | [Media for Thinking the Unthinkable (Victor 2013)](https://vimeo.com/67076984) | Trying out the 4 perspectives on 4 examples. | Example visualization 1 |
| 3 | [Dealing with Open Source Licenses (Winslow 2019)](https://docs.google.com/presentation/d/1qF9MHkp0p6THLU1bXPV7snaKTMYwYWH0RqxL7v0bJ8Y/edit?usp=sharing) | Skills lab on creative coding in Python with basic concepts introduced. | Revisit example from the 4 perspectives lens. |
| 4 | [A Byte of Python (Swaroop 2023)](https://python.swaroopch.com) | Skills lab on software architecture for creative coding in Python. | None. |
  
### 2. Primitives
Study of the essential building blocks for data visualization.

We transition to the foundational building blocks of data visualization and explore the cognitive science underpinnings behind effective information design. Using what many call the grammar of graphics, we will also have our first small projects that begin to offer hands-on experiences to build custom graphics with code.

| Day | Reading / Watching | Classroom Material | Activity |
|-----|-------------------|-------------------|----------|
| 5 | [Review of Tufte's "The Visual Display of Quantitative Information" (LeRoy 2018)](https://benjaminleroy.github.io/pages/blog/public/post/2018/05/16/review-of-tufte-s-the-visual-display-of-quantitative-information/) | Examples of problematic graphs (Tufte 2013), Chart junk (Tufte 2013), Tuftean axes (Tufte 2013), [After Tufte (Elliot 2016)](https://medium.com/@kennelliott/39-studies-about-human-perception-in-30-minutes-4728f9e31a73) | Example visualization 2. |
| 6 | [Preattentive Attributes in Visualization (Kesavan 2016)](https://daydreamingnumbers.com/blog/preattentive-attributes-example/) | Visual processing stages, working memory, pre-attention features (Ware 2021). Gestalt / neg space (Portnow 2018) | Job satisfaction. |
| 7 | [Inventing on Principle (Victor 2012)](https://www.youtube.com/watch?v=PUv66718DII) | Color (Ware 2021), Gestalt / neg space (Portnow 2018) | Job satisfaction remix. |
| 8/9 | [Genuary](https://genuary.art/) | Stroke, fill, primitive shapes, options for input, fonts. | Responsive art 1. |
| 10 | [All Maps are Wrong (Harris 2016)](https://www.youtube.com/watch?v=kIID5FDi2JQ) | Events, user loops, and data manipulation. | Responsive art 2. |
| 11 | [How William Cleveland Turned Data Visualization Into a Science (Pricenomics 2016)](https://priceonomics.com/how-william-cleveland-turned-data-visualization/) | Cleveland and McGill (1984), grammar (Wilkinson 2005), shared axes / direct label (Tufte 2013). Chartjunk 2. | Census 1 / Income inequality with 4 variables. |


### 3. Combination
Understand common patterns and methods for making new ones.

Having built up the primitives used in data visualization, we pick up the pace to build sophisticated data graphics. After using existing chart types, we will venture into the great unknown by looking at how these lego pieces enable us to build completely new visual representations and how to test if novel approaches are successful.

| Day | Reading / Watching | Classroom Material | Activity |
|-----|-------------------|-------------------|----------|
| 12 | [From Data to Viz (Holtz 2018)](https://www.data-to-viz.com/) | Taxonomy of common graphs ([Hess 2022](https://www.datylon.com/blog/types-of-charts-graphs-examples-data-visualization)). [Developer happiness (Pottinger 2019)](https://towardsdatascience.com/what-are-the-happiest-jobs-in-tech-4c4d33e065f0), task / domain (Munzner). | Census 2 / Income inequality with 6 variables. |
| 13 | [Lupi and Posavec (2015)](https://vimeo.com/channels/eyeo2015/133608605) | Movements ([Harris and Kamvar 2015](http://www.wefeelfine.org); [Pottinger 2015](https://gleap.org/content/ted_visualization)). Levels ([Fry 2015](https://vimeo.com/133608686)). Networks. Geographic data formats, projections. A look at [Gephi](https://gephi.org/) and [QGIS](https://qgis.org/). | Draw your last 5 years and your next 5 years by hand. |
| 14 | [15 Views on a Node Link Graph (Munzner 2007)](https://www.youtube.com/watch?v=WOBKnRlOAes) | Task / domain (Munzner). | BART 1 |
| 15 | [Designing for Realtime Spacecraft Operations (Binx 2016)](https://www.youtube.com/watch?v=HiGd-JJ94QA) | Inquiry (Munzner 2014), thinking-aloud (Lewis 1982), diary studies (Shniderman and Plaisant 2006), participatory desig ([IxDF 2023](https://www.interaction-design.org/literature/topics/participatory-design)), generalizable knoweldge vs quality assurance. | Think-Aloud of [Pyafscgap](https://pyafscgap.org/) ([Pottinger and Zarpellon 2023](https://joss.theoj.org/papers/10.21105/joss.05593)). |


### 4. Conversation  
Consider and design for the reader's dialogue with your work.

Just short of half way through the course, you are already an expert at choosing from existing chart types and constructing your own novel visual representations. Next we look critically at the role of the reader to construct media which enable the reader to explore more freely and become a co-creator of knowledge.

| Day | Reading / Watching | Classroom Material | Activity |
|-----|-------------------|-------------------|----------|
| 16 | [It's Not You, Bad Doors are Everywhere (Posner et al 2016)](https://www.youtube.com/watch?v=yY96hTb8WgI) | History of HCI (Duarte and Baranauskas 2016). Affordances (Norman 2013), working memory (Ware 2021), social actors (Nass et al 1994) | BART 2 |
| 17 | [The Role of the Player (Portnow 2011)](https://www.youtube.com/watch?v=ulm7bcB2xvY), [Explorable Explanations (Victor 2011)](https://worrydream.com/ExplorableExplanations/) | Why game design and its role, thinking and play, PLATO system (Bitzer et al). Ethos, pathos, logos. | Game or interactive viz analysis part 1. |
| 18 | [The Last Guardian and the Language of Games (Brown 2017)](https://www.youtube.com/watch?v=Qot5_rMB8Jc) | [Bussed out visualization (Bremer and Wu 2017)](https://www.theguardian.com/us-news/ng-interactive/2017/dec/20/bussed-out-america-moves-homeless-people-country-study), [Gun Deaths (Rees 2013)](https://guns.periscopic.com/), [Parable of the Polygons (Hart and Case 2014)](https://ncase.me/polygons/). | Game or interactive viz analysis part 2. |
| 19 | [Super Mario Bros: Level 1-1 (Edmonds and Portnow 2014)](https://www.youtube.com/watch?v=ZH2wGpEZVgE), [Triangle Design (Brown 2023)](https://www.youtube.com/watch?v=CZzcVs8tNfE&themeRefresh=1). | [Loops (Brazie 2024)](https://gamedesignskills.com/game-design/core-loops-in-gameplay/), [Hayashida level design](https://youtu.be/dBmIkEvEBtA) ([Pottinger and Zarpellon 2023](https://joss.theoj.org/papers/10.21105/joss.05593)), [Plastics (Pottinger et al 2024)](https://doi.org/10.48550/ARXIV.2312.11359) | Game or interactive viz analysis part 3*. |

### 5. Context
Expand our understanding of the reader.

Now that we have a deeper understanding of how to think about the reader within our designs, we next zoom out to understand users as within a broader social and physical context. We will also consider visualization in a broader sense-making context.

| Day | Reading / Watching | Classroom Material | Activity |
|-----|-------------------|-------------------|----------|
| 20 | None | Interactive Experience graded activity. | Interactive Visualization |
| 21 | [Storytelling with Verbs (Tremblay 2020)](https://www.youtube.com/watch?v=ontNUxSLhb8). [Spore, birth of a game (Wright 2007)](https://www.ted.com/talks/will_wright_spore_birth_of_a_game?language=en) | [Possibility space (Wright 2003)](https://www.computerhistory.org/revolution/computer-games/16/201/2309). [Diegesis (Dassler and Portnow 2019)](https://www.youtube.com/watch?v=-auyB19Mc6U). APH visualization (Pottinger et al 2024). | None |
| 22 | [Games are for Everyone (Brown 2018)](https://www.youtube.com/watch?v=xrqdU4cZaLw) | [WCAG (MDN 2024)](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Understanding_WCAG), common patterns, non-visual strategies. | [Final] Choose topic. |
| 23 | [Here's What Ethical AI Really Means (Thorne 2023)](https://www.youtube.com/watch?v=AaU6tI2pb3M) or [Sasha Costanza-Chock (2019)](https://vimeo.com/354276956) | [User Centered Machine Learning (Pottinger 2019)](https://www.slideshare.net/Samnsparky/user-centered-data-science-135680883). | [Final] Initial designs. |
| 24 | [The World Design of Metroid 1 and Zero Mission (Brown 2018)](https://www.youtube.com/watch?v=kUT60DKaEGc) | [Inquiry-based design (Hayes 2023)](https://stamen.com/data-visualization-for-education-when-asking-questions-is-the-answer/), overview of datasets, journey mapping. | [Final] Initial design ideas. |

### 6. Skills
Grow your implementation tool chest.

You have gotten through some of the most important concepts in data visualization and interactive science. Now, we will explore different technical skills as you work on your final project. Note that guest lectures may move.

| Day | Reading / Watching | Classroom Material | Activity |
|-----|-------------------|-------------------|----------|
| 25 | None | Logistics for the final, preparing for larger or non-notebook code. Git, architecture patterns, iterative process. | [Final] Sketch in code. |
| 26.1 | None | P5 introduction. | [Final] Iterate for final. |
| 26.2 | Lecture 25.2 is reading for Lecture 26. | D3 introduction. | [Final] Iterate for final. |

### 7. Build
Contribute to your portfolio.

The course ends with sharing final projects and a celebration of our time together.

| Day | Reading / Watching | Classroom Material | Activity |
|-----|-------------------|-------------------|----------|
| 27 | Final reading (see appendix) | Final projects and celebration. | [Final] Feedback |

## Details
Ready to take or teach the class? Here’s some additional information that might help.

### Welcoming and Supportive Environment
I love this topic and I hope you will love it too! I am dedicated to your success within this course. All activities and projects should be an engaging avenue for collaboration focused on refinement of ideas in a hands-on but low pressure setting. We will be discussing big topics through design and artistic expression. By participating, we collectively promise to generously create a welcoming and supportive environment for exploration. Lectures will be hands-on so laptops and discussion encouraged. Class time ensures successful outcomes in the course and will provide key information about assignments. However, things happen. I trust you to use your time well so attendance will not be taken. There are no textbook or service fees and free options are available for the interactive experience if you do not wish to purchase a copy of a game.

### How to Succeed and Pass the Course
Except day 1, each instruction day has an outside activity essential to course objectives and complementary to that day's discussion. I am excited to provide written individual feedback to help complement other course resources. Numerical scoring is not a focus of this course. However, for the purposes of pass / fail, each instructional day has an activity worth 10 points with two instruction days per week. 14 days have small projects which are generally short to complete, the interactive experience analysis spans 3 days, and the final project spans 9 days. For each 10 point grading, 3 points are given for completeness, 3 for reflecting course materials, 2 for technical correctness, and 2 for exploration / expression. For those at UC Berkeley, 70% overall grade is required to pass (course is pass / fail).

### Timely Response and Late Assignments
For those in the UC Berkeley community, being able to share timely feedback on activities enables projects to serve an important role in ensuring you get the most out of your time in the course. Therefore, activities are due at 5pm 2 days after their assignment except the final which is due altogether. Submissions must be made by May 1 if you want to receive pre-final feedback. Please talk to me if personal circumstances arise. Note that, automatically, there are no points deducted for 7 calendar days after assignment. However, 20% will be deducted each calendar day for late assignments starting at 5pm on the 8th day after assignment. All times are given in PT.

### Student Feedback
At UC Berkeley, student feedback will be solicited at the end of each module to ensure the course is meeting its goals. Grades and submissions through university-provided LMS.

### Contact
I work at Wellman Hall #201. Contact options available at interactivedatascience.courses. Originally taught as a small course without a TA.

### Lab / Discussion
To fit the 2 credit hour format, labs will take place during course instruction time as indicated in the schedule. For those attempting a 3 credit version of the course, the lab and discussion sections can expand class time.

### Paid resources
Reading to be provided. Students encouraged to purchase the interactive experience but alternatives provided. Otherwise, all materials are intended to be free to access.

---

## See Also

For additional course materials, please see:

- [Course Manual](/course_wide/manual.html) - Detailed guidance for students and instructors
- [Grading Rubric](/course_wide/rubric.html) - Detailed grading criteria for code projects

## Works Cited
Bitzer, D., P. Braunfeld, and W. Lichtenberger. "PLATO: An Automatic Teaching Device." IRE Transactions on Education 4, no. 4 (December 1961): 157–61. https://doi.org/10.1109/TE.1961.4322215.

Bostock, Mike, Vadim Ogievetsky, and Jeffrey Heer. "D3: Data-Driven Documents." IEEE Transactions on Visualization and Computer Graphics 17, no. 12 (December 2011): 2301-2309. https://doi.org/10.1109/TVCG.2011.185. See also https://d3js.org/.

Brazie, Alexander. "Designing The Core Gameplay Loop: A Beginner's Guide." Game Design Skills, March 19, 2024. https://gamedesignskills.com/game-design/core-loops-in-gameplay/.

Bremer, Nadieh, and Shirely Wu. "Bussed out: How America Moves Its Homeless (Visualization)." The Guardian, December 20, 2017. https://www.theguardian.com/us-news/ng-interactive/2017/dec/20/bussed-out-america-moves-homeless-people-country-study.

Binx, Rachel. "Designing for Realtime Spacecraft Operations." BocoupLLC, April 2016. https://www.youtube.com/watch?v=HuYKhSHcRSQ.

Brown, Mark. "Designing for Disability." Game Maker's Toolkit, 2018. https://www.youtube.com/watch?v=xrqdU4cZaLw.

———. "How Nintendo Solved Zelda's Open World Problem." Game Makers Toolkit, May 9, 2023. https://www.youtube.com/watch?v=CZzcVs8tNfE&themeRefresh=1.

———. "The Last Guardian and the Language of Games." Game Maker's Toolkit, January 9, 2017. https://www.youtube.com/watch?v=Qot5_rMB8Jc.

———. "The World Design of Metroid 1 and Zero Mission." Game Maker's Toolkit, July 31, 2018. https://www.youtube.com/watch?v=kUT60DKaEGc.

Cleveland, William S., and Robert McGill. "Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods." Journal of the American Statistical Association 79, no. 387 (September 1984): 531–54. https://doi.org/10.1080/01621459.1984.10478080.

Dassler, Sam, and James Portnow. "Diegetic UI - Realistic, or Distracting?" Extra Credits, August 14, 2019. https://www.youtube.com/watch?v=-auyB19Mc6U.

Duarte, Emanuel Felipe, and M. Cecília C. Baranauskas. "Revisiting the Three HCI Waves: A Preliminary Discussion on Philosophy of Science and Research Paradigms." In Proceedings of the 15th Brazilian Symposium on Human Factors in Computing Systems, 1–4. São Paulo Brazil: ACM, 2016. https://doi.org/10.1145/3033701.3033740.

Elliot, Kennedy. "39 Studies about Human Perception in 30 Minutes." OpenVisConf, 2016. https://medium.com/@kennelliott/39-studies-about-human-perception-in-30-minutes-4728f9e31a73.

Emmons, Dan, and James Portnow. "Super Mario Bros: Level 1-1 - How Super Mario Mastered Level Design." Extra Credits, June 5, 2014. https://www.youtube.com/watch?v=ZH2wGpEZVgE.

Fry, Ben. "Audience & Context." Eyeo, 2015. https://vimeo.com/133608686.

Genuary. "Genuary Creative Coding Prompts." Genuary, 2025. https://genuary.art/.

Gephi Consortium. "Gephi - The Open Graph Viz Platform." Gephi, 2024. https://gephi.org/.

Harris, Johnathan. "The Web's Secret Stories." TED Conference, 2007. https://www.ted.com/talks/jonathan_harris_the_web_s_secret_stories?language=en.

———, and Sep Kamvar. "We Feel Fine." We Feel Fine, 2006. http://www.wefeelfine.org.

Harris, Johnny, Gina Barton, Alvin Chang, and Phil Edwards. "Why All World Maps Are Wrong." Vox Media, December 2, 2016. https://www.youtube.com/watch?v=kIID5FDi2JQ.

Hart, Vi, and Nicky Case. "Parable of the Polygons," November 7, 2014. https://ncase.me/polygons/.

Hayes, Nicolette. "Data Visualization for Education: When Asking Questions Is the Answer." Stamen Design, April 26, 2023. https://stamen.com/data-visualization-for-education-when-asking-questions-is-the-answer/.

Hess, Kosma. "80 Types of Charts and Graphs," May 30, 2022. https://www.datylon.com/blog/types-of-charts-graphs-examples-data-visualization.

IxDF. "What Is Participatory Design?" Interaction Design Foundation, March 17, 2023. https://www.interaction-design.org/literature/topics/participatory-design.

Kesavan, Vidya. "Preattentive Attributes in Visualization – An Example," November 17, 2016. https://daydreamingnumbers.com/blog/preattentive-attributes-example/.

LeRoy, Benjamin. "Review of Tufte's 'The Visual Display of Quantitative Information,'" May 16, 2018. https://benjaminleroy.github.io/pages/blog/public/post/2018/05/16/review-of-tufte-s-the-visual-display-of-quantitative-information/.

Lewis, Clayton. "Using the 'Thinking-Aloud' Method in Cognitive Interface Design." IBM Research, 1982. https://dominoweb.draco.res.ibm.com/2513e349e05372cc852574ec0051eea4.html.

Luipi, Georigia, and Stefanie Posavec. "Dear Data." Eyeo, 2015. https://vimeo.com/channels/eyeo2015/133608605.

MDN Contributors. "Understanding the Web Content Accessibility Guidelines." Mozilla Corporation, 2024. https://developer.mozilla.org/en-US/docs/Web/Accessibility/Understanding_WCAG.

Munzner, Tamara. "15 Views of a Node Link Graph." Google, October 8, 2007. https://www.youtube.com/watch?v=WOBKnRlOAes.

———. Visualization Analysis and Design. A.K. Peters Visualization Series. Boca Raton: CRC Press, Taylor & Francis Group, CRC Press is an imprint of the Taylor & Francis Group, an informa business, 2015.

Nass, Clifford, Jonathan Steuer, and Ellen R. Tauber. "Computers Are Social Actors," 204. Boston, Massachusetts, United States: ACM Press, 1994. https://doi.org/10.1145/259963.260288.

Norman, Donald A. The Design of Everyday Things. Revised and Expanded editions. Cambridge, MA London: The MIT Press, 2013.

Portnow, James. "Gestalt and Parts of the Whole." Extra Credits, 2018. https://www.youtube.com/watch?v=TcMO1xhjKTg.

———. "The Role of the Player - The Fundamental Difference between Games and Every Other Art Form." Extra Credits, October 12, 2011. https://www.youtube.com/watch?v=ulm7bcB2xvY.

Posner, Joe, Roman Mars, Don Norman, and Gina Barton. "It's Not You. Bad Doors Are Everywhere." Vox Media, February 26, 2016. https://www.youtube.com/watch?v=yY96hTb8WgI.

Pottinger, A. "Sketchingpy." UC Berkeley, 2024. sketchingpy.org.

———. "TED Visualization." Gleap, 2012. https://gleap.org/content/ted_visualization.

———. "User Centered Machine Learning," March 11, 2019. https://www.slideshare.net/Samnsparky/user-centered-data-science-135680883.

———. "What Are the Happiest Jobs in Tech?" Towards Data Science, August 19, 2019. https://towardsdatascience.com/what-are-the-happiest-jobs-in-tech-4c4d33e065f0.

Pottinger, A Samuel, Nivedita Biyani, Roland Geyer, Douglas J McCauley, Magali de Bruyn, Molly R Morse, Neil Nathan, Kevin Koy, and Ciera Martinez. "Combining Game Design and Data Visualization to Inform Plastics Policy: Fostering Collaboration between Science, Decision-Makers, and Artificial Intelligence," 2023. https://doi.org/10.48550/ARXIV.2312.11359.

Pottinger, A., and G. Zarpellon. "Pyafscgap.org: Open Source Multi-Modal Python-Based Tools for NOAA AFSC RACE GAP." JOSS 8, no. 86 (2023): 5593. https://doi.org/10.21105/joss.05593.

P5js Contributors. "P5js." Processing Foundation, 2026. [Online]. Available: https://p5js.org/.

Pricenomics. "How William Cleveland Turned Data Visualization Into a Science." Udemy, January 6, 2016. https://priceonomics.com/how-william-cleveland-turned-data-visualization/.

QGIS Development Team. "QGIS Geographic Information System." QGIS Association, 2024. https://qgis.org/.

Rees, Kim. "U.S. Gun Deaths." Perisocopic, 2018. https://guns.periscopic.com/.

Sasha, Costanza-Chock. "Eyeo 2019 - Sasha Costanza-Chock." Eyeo Festival, 2019. https://vimeo.com/354276956.

Shneiderman, Ben, and Catherine Plaisant. "Strategies for Evaluating Information Visualization Tools: Multi-Dimensional in-Depth Long-Term Case Studies." In Proceedings of the 2006 AVI Workshop on BEyond Time and Errors: Novel Evaluation Methods for Information Visualization, 1–7. Venice Italy: ACM, 2006. https://doi.org/10.1145/1168149.1168158.

Swaroop, CH. "A Byte of Python," 2023. https://python.swaroopch.com.

Thorne, Abigail. "Here's What Ethical AI Really Means." Philosophy Tube, October 13, 2023. https://www.youtube.com/watch?v=AaU6tI2pb3M.

Tremblay, Kaitlin. "Storytelling with Verbs: Integrating Gameplay and Narrative." GDC, March 17, 2020. https://www.youtube.com/watch?v=ontNUxSLhb8.

Tufte, Edward R. The Visual Display of Quantitative Information. 2nd ed., 8th print. Cheshire, Conn: Graphics Press, 2013.

Victor, Bret. "Explorable Explanations." Bret Victor, 2011. https://worrydream.com/ExplorableExplanations/.

———. "Inventing on Principle." CUSEC, 2012. https://www.youtube.com/watch?v=PUv66718DII.

———. "Media for Thinking the Unthinkable." MIT Media Lab, April 4, 2013. https://vimeo.com/67076984.

Ware, Colin. Information Visualization: Perception for Design. Fourth edition. Cambridge, MA: Morgan Kaufmann, Inc, 2021.

Wilkinson, Leland. The Grammar of Graphics. Second edition. Statistics and Computing. New York, NY: Springer, 2005.

Winslow, Steve. Dealing with Open Source Licenses. Nerd Summit. 2019.

Wright, Will. "Probability Space, Possibility Space." Computer History Museum, n.d. https://www.computerhistory.org/revolution/computer-games/16/201/2309.

———. "Spore, Birth of a Game." TED Conference, March 2007. https://www.ted.com/talks/will_wright_spore_birth_of_a_game?language=en.

Y. Holtz, "From Data to Viz." Data to Viz, 2018. [Online]. Available: https://www.data-to-viz.com/

**Interactive Experience:**

Brier, Wren, Tim Dawson, Kip Bunyea, and Erika Olsen. "Unpacking," November 2, 2021.

Deconstructteam. "The Cosmic Wheel Sisterhood," August 16, 2023. https://cosmicwheel.com/.

Ma, Justin, and Matthew Davis. "FTL: Faster Than Light," September 14, 2012. https://subsetgames.com/ftl.html.

"Papers, Please," February 12, 2014. https://papersplea.se.

Thunder Lotus Games. "Spiritfarer," August 18, 2020. https://thunderlotusgames.com/spiritfarer/.

---

## License
Provided under the [CC-BY International 4.0 License](https://creativecommons.org/licenses/by/4.0/).