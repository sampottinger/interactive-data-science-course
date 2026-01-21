# AI Basics for Data Visualization

Welcome to Skills Lab 6! In this tutorial, we will explore how to use AI assistants to help create data visualizations. Rather than writing every line of code from scratch, we can collaborate with AI to build visualizations more quickly while still applying our design knowledge and critical thinking skills.

**Contents**
- [Motivation](#motivation)
- [Prepare](#prepare)
- [Initial Request](#initial-request)
- [First Iteration](#first-iteration)
- [Refining Labels](#refining-labels)
- [Final Polish](#final-polish)
- [Reflection](#reflection)
- [Next](#next)

## Motivation

Throughout this course, you have been building data visualizations through a combination of pre-built charting libraries and custom drawing with Sketchingpy. You've learned about visual encoding, task-oriented design, accessibility, and data-ink ratio. These skills remain critical even as we introduce a new tool: AI assistants.

AI assistants like Claude, ChatGPT, or other language models can help generate visualization code quickly. However, they work best when you bring your visualization expertise to the conversation. You need to:

- Know what kind of visualization will best serve your data and purpose
- Recognize when a visualization has issues with readability, accessibility, or design
- Provide specific feedback to improve the output
- Iterate towards a better result

Think of an AI assistant as a collaborator who can write code quickly but needs your design eye and domain knowledge to guide the work. This tutorial will walk you through a real example of this iterative process.

**Important note**: The exact output you get from an AI assistant may differ slightly from what's shown here. That's completely normal and expected. The key learning goal is to experience the process of iteration: making a request, reviewing the output, identifying what to improve, and refining your prompts accordingly.

## Prepare

For this tutorial, you'll need access to an AI assistant that can generate Python code for data visualization. Some options include:

- **Claude** (claude.ai)
- **ChatGPT** (chat.openai.com)
- **GitHub Copilot** (if you have access)
- Other language model services

You'll also need a Python environment where you can run the generated code. This could be:

- A Jupyter notebook
- Google Colab
- Your local Python installation
- Any environment where you can install and use matplotlib

For this example, we'll be using matplotlib to create a visualization of predator-prey dynamics between wolves and moose populations at Isle Royale National Park. You don't need to download the data yourself - we'll ask the AI assistant to fetch it for us.

Make sure you have matplotlib installed in your environment. If you're using a Jupyter notebook or Colab, it's likely already available. If not, you can install it with:

```
pip install matplotlib
```

Once you're set up, open your AI assistant in one window and your Python environment in another so you can easily test the code as you go.

## Initial Request

Let's start by making our first request to the AI assistant. The goal here is to create a split bar plot showing both wolf and moose populations over time, with wolves extending to the left and moose extending to the right.

Try copying this prompt into your AI assistant:

```
Hello! Can you please use matplotlib to generate a graph of wolves vs moose
populations as a split bar plot (one going to the left and the other going
to the right) where the axes have different colors to correspond to the bar
colors for the two series? Please have the left facing axis for wolves go
from 0 to 50 and the right facing axis for moose go from 0 to 2500. See
https://www.nps.gov/isro/learn/nature/wolf-moose-populations.htm for data.
```

**Check the work**: Run the code provided by the AI assistant. You should see a visualization with:

- Blue bars extending to the left representing wolf populations
- Orange (or similar color) bars extending to the right representing moose populations
- A timeline showing years (likely 1980-2019 or similar range)
- Color-coordinated axes with scales from 0-50 for wolves and 0-2500 for moose

Take a moment to examine the output. What do you notice? Can you see the predator-prey relationship in the data?

**What to look for**: The classic predator-prey oscillation pattern should be visible, but the wolf data might appear compressed because the scale is much smaller (0-50) compared to moose (0-2500). This brings us to our first iteration.

## First Iteration

Looking at the initial visualization, you might notice that the wolf population changes are hard to see because they're compressed into a narrow space compared to the moose. The wolves vary from about 0 to 50, while moose vary from about 500 to 2500, so the wolf variations look subtle.

Let's improve this by giving wolves more horizontal space. This will make the harmonic relationship between the two populations easier to see.

Try this prompt:

```
This is great but the wolves are too compressed. Let's have the split at
roughly half way across the plot. This means that there is more horizontal
space per wolf than per moose. However, this will show the harmonic
relationship better.
```

**Check the work**: Run the updated code. Now you should see:

- Wolves taking up approximately half the plot width (left side)
- Moose taking up approximately half the plot width (right side)
- Much more visible oscillations in the wolf population
- The predator-prey relationship should be much clearer

**What improved**: By allocating equal horizontal space to both scales, we've effectively "zoomed in" on the wolf data. Now you can see how when wolves are high, moose populations tend to be lower, and when wolves crash (especially around 2015-2018 in the data), moose populations surge.

This is an excellent example of how your visualization knowledge guides the AI. The assistant gave you a technically correct chart, but you recognized that the visual encoding wasn't optimal for showing the relationship you wanted to highlight.

## Refining Labels

The visualization is getting better, but you might notice that the axis labels could be clearer. Specifically, there might be overlapping text where the colored "Wolves" and "Moose" labels compete with a black axis title.

Let's clean this up and make the labels more descriptive. Try this prompt:

```
Perfect! We have the colored wolves and moose labels overlapping with the
black axis title. Let's set the black axis title to empty and then let's
make the colors for both series darker so that it is easy to read wolves
and moose. Finally, let's say "Number of Wolves" and "Number of Moose" in
that colored text.
```

**Check the work**: Run the code and verify:

- The black axis title is now gone, eliminating the overlap
- The blue and orange colors are darker and easier to read
- The labels now say "Number of Wolves" and "Number of Moose" instead of just "Wolves" and "Moose"
- The visualization should feel cleaner and more professional

**Design thinking**: Notice how this iteration focused on reducing visual clutter and improving readability. This connects to Tufte's concepts of reducing chartjunk and maximizing the data-ink ratio. You're making intentional design choices to improve the final product.

## Final Polish

There's one more improvement we can make. Right now, the numerical labels along the horizontal axis (the tick marks showing the actual population numbers) are all in black. Let's make them match their respective data series for maximum clarity.

Try this final prompt:

```
Doing really well. One last thing. The labels for the count (along the
bottom horizontal axis). Can you please make those the same color as the
series they describe (so one color on left and a different color on right)?
```

**Check the work**: Run the final version. You should now see:

- Blue tick labels on the left side (for wolf counts)
- Orange tick labels on the right side (for moose counts)
- The tick marks themselves are also color-coded
- The entire visualization now uses color consistently to distinguish the two data series

**The result**: You now have a polished visualization that clearly shows the predator-prey dynamics between wolves and moose. Every visual element is intentionally designed to support the viewer's understanding of the data.

## Reflection

Let's step back and think about what we just accomplished and what it teaches us about working with AI assistants for data visualization.

**The iterative process**: Notice that we didn't get a perfect visualization in one shot. We went through several rounds:

1. Initial request with basic requirements
2. Adjusting the spatial allocation to better show the data
3. Cleaning up labels and improving readability
4. Fine-tuning color coding for consistency

This is exactly how you should work with AI assistants. Start with the core requirements, then iteratively refine based on your design knowledge and what you observe in the output.

**Your expertise matters**: At each step, you brought your knowledge from this course to bear:

- You recognized that the compressed wolf data wasn't showing the pattern effectively
- You identified overlapping labels as visual clutter
- You applied color coding principles to improve clarity

The AI assistant can write code quickly, but it needed your design eye to reach the optimal result. Without your guidance, the first version would have been technically correct but visually suboptimal.

**Specificity in feedback**: Notice how each prompt was specific about what to change and why. Vague feedback like "make it better" is less effective than "give wolves more horizontal space to show the oscillations better." The more precisely you can articulate what you want, the better results you'll get.

**Verification is essential**: After each change, we ran the code and examined the output. Don't skip this step. AI assistants can make mistakes, and you need to verify that the changes match your intentions.

**When to use AI assistance**: AI assistants are particularly valuable when:

- You need to quickly prototype a visualization
- You're working with standard chart types (bar plots, scatter plots, line charts, etc.)
- You want to explore different design options rapidly
- You know what you want but need help with implementation details

However, for highly custom visualizations or when you need pixel-perfect control, you might still prefer to write the code yourself using tools like Sketchingpy.

**Limitations to keep in mind**: AI assistants have some limitations:

- They may not always make optimal design choices without guidance
- Their output can vary - you might get different results on different runs
- They might not be familiar with the latest library versions or features
- Complex visualizations may require multiple rounds of refinement

This is why your visualization knowledge from this course remains essential. You're not replacing your skills with AI - you're augmenting them with a powerful tool that can accelerate your work when properly directed.

**Compare to previous work**: Think back to the visualizations you've built from scratch using Sketchingpy. There, you had complete control over every pixel and could create highly customized designs. Here, you're trading some of that control for speed and convenience. Both approaches have their place in your toolkit.

The key is knowing when to use each approach and how to work effectively with AI when you choose that path.

## Next

Congratulations! You've experienced the process of collaborating with an AI assistant to create a data visualization. You started with a basic request, reviewed the output critically, and iteratively refined it using your visualization knowledge.

As you continue working with AI assistants for data visualization, remember:

- Always review the output - don't blindly trust generated code
- Apply your design knowledge to identify improvements
- Be specific in your feedback and requests
- Iterate towards better results
- Verify that the visualization accurately represents the data

In future work, you might combine AI-generated code with manual refinements, or use AI to scaffold a visualization that you then customize further. The possibilities are extensive when you pair AI capabilities with human expertise.

**Citations**

- National Park Service, "Wolf and Moose Populations," Isle Royale National Park, 2025. [Online]. Available: https://www.nps.gov/isro/learn/nature/wolf-moose-populations.htm
- J. Hunter, et al., "Matplotlib: Visualization with Python," Matplotlib Development Team, 2025. [Online]. Available: https://matplotlib.org
- E. Tufte, "The Visual Display of Quantitative Information," Graphics Press, 2001.
- Anthropic, "Claude," Anthropic PBC, 2025. [Online]. Available: https://claude.ai
- OpenAI, "ChatGPT," OpenAI, 2025. [Online]. Available: https://chat.openai.com
