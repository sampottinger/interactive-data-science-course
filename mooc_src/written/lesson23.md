# Lecture 23: Ethics

**Stat 198: Interactive Data Science and Visualization**
**Instructor:** A Samuel Pottinger
**Original Instruction Date:** April 21, 2025

## Description

Explore some of the common issues that come up and how bias enters into our work. Critically examine the power we have as designers. Consider how exercising that power can lead to both positive and negative outcomes. Note that this lecture has multiple content warnings.

## Content Warning

This lecture addresses complex ethical questions and difficult topics that may be challenging. The material explores ethical issues in data visualization including representation, bias, and power dynamics in design.

## Key Takeaways

This lecture examines the ethical dimensions of data visualization through the lens of power, representation, and agency. It challenges students to critically examine their design choices and their impact on how people understand and interact with data. We are creating a "way of seeing" in which we necessarily must make decisions about:

- How others are represented.
- How users interact with an audience which may not be present.
- How our work mediates reality.

These questions extend beyond visual representation into the heart of technology, including AI.

## Conceptual Perspective
This gets a little philosophical but having this foundation motivateas the practical frameworks.

### 1. Lenses on the World

Data visualization is not neutral. As John Berger articulated in "Ways of Seeing," the way we see things is affected by what we know and what we believe. In data visualization, we are actively constructing ways of seeing. From Jones: "It is tempting to think of data and visualization as a neutral actor, with a single 'correct' set of design choices that 'truthfully' report the data. However, outside of egregious errors (e.g., when dates are sorted incorrectly or the y-axis is not scaled uniformly), we see that 'ground truth' in data is much more contextual and situated. Design choices we make give visualization a rhetorical power that influences what a reader concludes and remembers about the data, and blurs the line between persuasion and deception." We have a certain degree of power as designers. This power comes with responsibility for how we shape understanding and what narratives we enable or constrain.

### 2. Theoretical Foundations

**Michel Foucault and Discourse:**
- Discourses are produced by effects of power within a social order
- Power prescribes particular rules and categories which define the criteria for legitimating knowledge and truth
- Discourse masks its construction and capacity to produce knowledge and meaning
- Through reiteration in society, discourse fixes the meaning of statements

**Bret Victor - Media for Thinking the Unthinkable:**
- The medium changes what is possible to think altogether
- Our tools shape not just how we represent ideas, but what ideas are possible to conceive
- Data visualizations serve as cognitive tools that enable or constrain thinking

**Marian Wright Edelman:**
- "You can't be what you can't see"
- Representation matters - what we make visible (or invisible) shapes what people believe is possible
- Applied to data visualization: the choices we make about what to show and how to show it influence what people can imagine and understand

### 3. Encoding Choices and Ethics

**Cleveland and McGill's Hierarchy Revisited:**
Unlike earlier in the course where we used elementary perceptual tasks as a guide for "effective" visualization, we must now ask:

- What are the "most important" variables?
- What leads us to making that decision?
- Who decides what matters?

**Example: Income Gaps Visualization**
In visualizations showing economic data by gender, occupation, and other variables:

- Which variables receive the highest-accuracy encodings?
- What narrative does the encoding hierarchy tell?
- What comparisons are made easy versus difficult?

**Baseline Choices:**
Creating axes is a common place to have issues:

- Why is distance from zero the "standard" baseline?
- When is a broken axis appropriate or problematic?
- What implicit comparisons does our baseline choice enable or prevent?

### 4. Possibility Space (Action)

The possibility space defines what questions we can and cannot ask of data.

- What actions are allowed in our visualization?
- Why did we choose these specific interactions?
- What questions are made easy versus difficult or impossible?
- How does the interaction design shape user inquiry?

As example, the Global Plastics AI Policy Tool provides specific policy levers that users can adjust, defining:

- Which policy interventions are considered
- What metrics are used to measure success
- The range of futures that can be explored

These choices are unavoidable but shape what users can learn and imagine.

- How are we warping the possibility space through our accessibility choices?
- Who can access the full range of actions and information?
- What alternative representations might serve different accessibility needs?

### 5. Possibility Space (Narrative)

Beyond what actions are possible, we must consider what narratives are possible.

**Propaganda Games (Extra Credits):**
Games (and interactive visualizations) can be designed to promote particular viewpoints through mechanics, not just content.

**Parable of the Polygons:**
- Uses simple geometric shapes to explore complex social dynamics
- What is gained through abstraction? (accessibility, clarity, universal applicability)
- What is lost through abstraction? (specificity, individual experiences, historical context)

**Three Treatments of Gun Deaths:**
The lecture compares three visualizations of firearm mortality:
1. **Periscopic Gun Deaths**: Emotional, individual focus with stolen years shown as arcs
2. **Rand Longitudinal Study**: State-by-state trends showing policy impacts
3. **MDSR Book**: Statistical presentation focused on data accuracy

**Question:** Which is most ethical? There is no single answer, but each makes different choices about:
- Emotional versus analytical framing
- Individual versus aggregate perspective
- Policy implications versus human impact

### 6. Agency and Representation
Consider how your actions change agency and how that influences representation:

- How are we choosing what is good and what is bad?
- How are we choosing what is visible and what is invisible?
- How are we choosing what is possible to think?
- How would those we are representing feel about that representation?

Unlike some other forms of technology, these choices in data visualization are often more explicit. We have outlined the steps in which these choices are made:

- Encoding devices
- User actions
- Ludonarrative
- Possibility space

However, we are choosing reality. We are choosing representation. These choices require critical thought and there is no formula to get to a right answer.

## Resources and Frameworks
Let's turn to practical places where we can apply these ideas or examples we can learn from:

### Design Justice Network Principles

The lecture references the Design Justice Network (https://designjustice.org/read-the-principles) as a framework for ethical design practice that centers the voices of those directly impacted by design decisions.

### Income Gaps Visualization
Shows economic disparities across occupation, gender, race, and other demographics. Demonstrates how encoding choices emphasize certain comparisons and patterns.

### Global Plastics AI Policy Tool
Interactive simulation that allows users to explore policy scenarios and their projected impacts on plastic waste. The choice of available policies and metrics shapes what futures users can imagine.

### Parable of the Polygons
Interactive exploration of segregation dynamics using abstract shapes. Demonstrates the tradeoffs between abstraction and specificity in ethical communication.

### Gun Death Visualizations
Multiple approaches to visualizing firearm mortality demonstrate how different design choices (emotional vs. analytical, individual vs. aggregate) serve different purposes and have different ethical implications.

## Activities
Building on today's materials...

### Lecture Video
[Watch Lecture 23: Ethics on Vimeo](https://vimeo.com/1077298223)

### Reading
Sasha Costanza-Chock (Eyeo 2019) digging deeper into Design Justice at https://vimeo.com/354276956.

### Links
- [Video 1: AI is an Ethical Nightmare by Philosophy Tube](https://www.youtube.com/watch?v=AaU6tI2pb3M) (recommend watching 11:30 to 20:30)
- [Video 2: Propaganda Games - Ethical Game Design by Extra Credits](https://www.youtube.com/watch?v=UP4_bMhZ4gA)
- [Income Gaps](https://incomegaps.com/)
- [Periscopic Gun Deaths](https://guns.periscopic.com/)
- [Rand Firearm Mortality](https://www.rand.org/research/gun-policy/longitudinal-firearm-mortality.html)
- [MDSR Book Gun Deaths](https://mdsr-book.github.io/mdsr2e/ch-ethics.html)
- [Parable of the Polygons](https://ncase.me/polygons/)

## Moving Forward: A Positive Framework

This lecture doesn't need to be purely negative or paralyzing. Instead, it offers guidance:

1. **Broaden the perspective of who is an author** - Consider co-creation and participatory design
2. **These choices are essential, make them wisely** - Acknowledge the responsibility that comes with design power
3. **Think about which narratives are elevated or diminished** - Be intentional about perspective
4. **There is no formula to get to a right or wrong answer** - We have to think critically. We have to do the work.

The goal is not to avoid making choices, but to make them thoughtfully with awareness of their implications.

## Citations

[1] A. Shatov, "White Digital Device at 12 00," Unsplash, 2021. Available: https://unsplash.com/photos/white-digital-device-at-12-00-DHl49oyrn7Y

[2] J. Berger, *Ways of Seeing*, Penguin Books, 1972.

[3] R. Jones, "Deceptive by Design: Data Visualization and The Ethics of Representation," MIT. Available: https://technologist.mit.edu/deceptive-by-design-data-visualization-and-the-ethics-of-representation/

[4] Wikipedia Contributors, "Ciclo de conferências do filósofo francês Michel Foucault, no Hospital das Clínicas da Universidade do Estado da Guanabara (UEG)," Wikimedia Foundation. Available: https://en.wikipedia.org/wiki/Michel_Foucault#/media/File:Michel_Foucault_1974_Brasil.jpg

[5] W. Pragher, "Photograph of Martin Heidegger," Wikimedia Foundation. Available: https://en.wikipedia.org/wiki/Martin_Heidegger#/media/File:Heidegger_2_(1960).jpg

[6] R. Adams, "Michel Foucault: Discourse," Critical Legal Thinking, 2017. Available: https://criticallegalthinking.com/2017/11/17/michel-foucault-discourse/

[7] Wikipedia Contributors, "Bret Victor." Wikimedia Foundation, Inc., Jun. 22, 2023. Available: https://en.wikipedia.org/wiki/Bret_Victor

[8] B. Victor, "Media for Thinking The Unthinkable," MIT Media Lab, 2013. Available: https://vimeo.com/67076984

[9] CDC, "Marian Write Edelman," Wikimedia Foundation. Available: https://en.wikipedia.org/wiki/Marian_Wright_Edelman#/media/File:Marian_Wright_Edelman_01.jpg

[10] M. Edelman, "You can't be what you can't see," Goodreads. Available: https://www.goodreads.com/quotes/536048-you-can-t-be-what-you-can-t-see

[11] A. Thorn, "AI is an Ethical Nightmare," Philosophy Tube, 2023. Available: https://www.youtube.com/watch?v=AaU6tI2pb3M

[12] W. S. Cleveland and R. McGill, "Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods," *Journal of the American Statistical Association*, vol. 79, no. 387, pp. 531–554, Sep. 1984, doi: 10.1080/01621459.1984.10478080.

[13] A. Pottinger, "Income Gaps." 2023. Available: https://incomegaps.com/

[14] A. Tierney, "Median annual earnings of full-time workers in the United States in 2023, by gender," Statista, 2024. Available: https://www.statista.com/statistics/1186135/us-median-annual-worker-earnings-by-gender/

[15] B. Baumer, D. Kaplan, and N. Horton, *Modern Data Science with R*, 2nd Ed, CRC Press, 2021.

[16] K. Rees and Periscopic, "U.S. Gun Deaths." Periscopic, 2018. Available: https://guns.periscopic.com/

[17] K. Sumah, L. Floyd, and H. McCracken, "Changes in State Firearm Mortality," Rand Corporation, 2024. Available: https://www.rand.org/research/gun-policy/longitudinal-firearm-mortality.html

[18] A. Pottinger, R. Geyer, N. Biyani, C. Martinez, N. Nathan, M. Morse, M. de Bruyn, C. Boettiger, E. Baker, K. Koy, and D. McCauley, "Global Plastics AI Policy Tool," University of California, 2024. Available: https://global-plastics-tool.org/

[19] A. Pottinger, R. Geyer, N. Biyani, C. Martinez, N. Nathan, M, Morse, C. Liu, S. Hu, M. de Bruyn, C. Boettiger, E. Baker, and D. McCauley, "Pathways to reduce global plastic waste mismanagement and greenhouse gas emissions by 2050," *Science*, 2024. doi: 10.1126/science.adr3837

[20] J. Portnow, "Propaganda Games - Ethical Game Design," Extra Credits, 2012. Available: https://www.youtube.com/watch?v=UP4_bMhZ4gA

[21] V. Hart and N. Case, "Parable of the Polygons," Nicky Case, 2022. Available: https://ncase.me/polygons/

[22] Design Justice Network, "Design Justice Network Principles," Design Justice Network, 2018. Available: https://designjustice.org/read-the-principles
