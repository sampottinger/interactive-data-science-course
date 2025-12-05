# Lecture 22: Accessibility

**Stat 198: Interactive Data Science and Visualization**
**Instructor:** A Samuel Pottinger
**Original Instruction Date:** April 15, 2025

## Description

Learn about the Web Content Accessibility Guidelines. Explore some common steps which you can take within your interactive data visualizations that can help improve access.

## Key Takeaways

This lecture introduces web accessibility standards and practices specifically tailored for interactive data visualizations, focusing on making visualizations usable by people with various disabilities.

### The Curb-Cut Effect

Accessibility improvements designed for people with disabilities often benefit everyone. This principle, known as the "curb-cut effect," demonstrates that laws and programs designed to benefit vulnerable groups often end up benefiting all of society.

### Web Content Accessibility Guidelines (WCAG)

WCAG provides clear, comprehensive guidelines for making web content accessible to people with disabilities. The standards cover WCAG 2.0, 2.1, and 2.2, offering a framework for accessible design.

## Visual Accessibility

For our purposes today, visual accessibility addresses three categories of visual impairment:

### 1. Color Deficiency

**Challenge:** Users may have difficulty distinguishing between certain colors.

**Solutions:**
- **Double Encoding (WCAG 1.4.1)**: Color should not be the only way elements are visually distinguished from each other. Use additional visual cues like:
  - Position
  - Shape
  - Patterns or textures
  - Labels
  - Size differences
- **Alternative Visualizations**: Offer different visualization modes that don't rely solely on color.
- **Semantic Association**: Be careful with color choices that have cultural or semantic meanings (e.g., red/green for bad/good).

**Example Applications:**
- Income Gaps visualization uses both color and position to distinguish gender categories.
- Global Plastics AI Policy Tool provides colorblind-friendly color scheme options.

### 2. Low Vision

**Challenge:** Users may use magnifiers, scaled resolutions, or have contrast sensitivity issues.

**Solutions:**

**Minimal Contrast (WCAG 1.4.3):**
- Ensure colors are sufficiently different from their backgrounds to be perceived.
- Maintain sufficient contrast between visual elements.
- Use contrast checking tools like WebAIM's Contrast Checker.
- Meet minimum contrast ratios (4.5:1 for normal text, 3:1 for large text).

**Resize Support (WCAG 1.4.4):**
- Applications should remain functional when zoomed to 200%.
- Use responsive design principles.
- Avoid fixed-size elements that break when magnified.
- Test visualizations at different zoom levels.

### 3. Blind or Partially Blind

**Challenge:** Users may rely on screen readers and keyboard-only navigation.

**Solutions:**

**Supporting Screen Readers (WCAG 1.1.1):**
- Provide non-visual alternatives to visualizations:
  - Data tables with the underlying data
  - Data download options
  - Textual descriptions of key findings
  - Alternative representations of the information
- Use semantic HTML elements properly.
- Add appropriate ARIA labels and roles.
- Ensure all interactive elements are accessible via keyboard.

## Motor Accessibility

Interactive visualizations present unique challenges for users with motor impairments:

### 1. Fine Motor Control

**Challenge:** Users may have difficulty with precise pointing or clicking.

**Solutions:**
- Make interactive targets large enough (minimum 44x44 pixels recommended).
- Provide adequate spacing between clickable elements.
- Support alternative input devices.
- Avoid interactions requiring precise hovering or dragging.

### 2. Timed Inputs

**Challenge:** Some users may require additional time to complete interactions.

**Solutions:**

**Adjustable Timing (WCAG 2.2.1):**
- Allow modification or pausing of timed actions.
- Provide options to extend time limits.
- Avoid auto-advancing content without user control.
- Include pause/play controls for animations.

**Example Applications:**
- Sketchingpy provides pause functionality for auto-shuffling animations.
- Climate simulation tools allow users to control the pace of exploration.

### 3. Keyboard-Only Navigation

**Challenge:** Users may not have access to a pointing device.

**Solutions:**

**Non-Keyboard Controls (WCAG 2.1.1):**
- Provide keyboard alternatives for all custom drawing interactions.
- Document keyboard shortcuts clearly.
- Ensure all functionality is accessible via keyboard.
- Follow logical tab order.

**Example Applications:**
- Climate maize loss visualization includes keyboard controls:
  - Esc: Exit visualization
  - y: Change year
  - c: Change coverage
  - v: Change vs historic or counterfactual
  - u: Change unit size

**Tab Order and Focus (WCAG 1.3.2):**
- Use proper tab order for navigation.
- Provide visible focus indicators.
- Ensure focus is never lost or trapped.
- Test keyboard navigation thoroughly.

**Example Applications:**
- Global Plastics AI Policy Tool uses standard HTML elements with proper tab order.
- Regional selection buttons follow logical left-to-right tab sequence.

## Group Activity

During the lecture, students explored the accessibility options at the Global Plastics AI Policy Tool (https://global-plastics-tool.org), examining:

### Layout Options
- Side-by-side vs linear layout
- Addresses different screen sizes and user preferences

### Color Options
- Default: Emphasizes color differences between series
- High contrast: Better for low vision users
- Helps both colorblind users and those with low vision

### Settings Persistence
- Settings saved to local file
- Supports consistent user experience across sessions
- Demonstrates adaptive technology support

## Case Studies
Let's look at some examples... 

### Income Gaps Visualization
- Demonstrates double encoding (color + position)
- Provides colorblind mode toggle
- Supports zoom to 200%
- Includes data download for screen reader users

### Global Plastics AI Policy Tool
- Comprehensive accessibility settings
- Multiple layout options
- High contrast color schemes
- Keyboard navigation support
- Detailed documentation of controls

### Climate Maize Loss Probability Tool
- Keyboard controls for custom visualizations
- Clear documentation of interaction methods
- Supports both mouse and keyboard interaction

### Sketchingpy Project
- Pause/play controls for animations
- Adjustable timing for auto-shuffle features
- Demonstrates accessible animation design

## Activities
To supplement our main content...

### Lecture Video
[Watch Lecture 22: Accessibility on Vimeo](https://vimeo.com/1075913765)

### Assignment
Though there is still some material left, this is a good opportunity to start on your final project to be refined over the next few lessons. See the course manual for recommended project ideas and datasets.

### Reading
Please continue our discussion by considering [motor accessibility](https://youtu.be/Ufe0i26DGiA) and [cognitive disability](https://www.youtube.com/watch?v=ObhvacfIOg0) over at Game Makers Toolkit.

### Additional Resources

Accessibility is a deep topic requiring ongoing learning and practice. Key resources include:

- [Making Games Better for Gamers with Colourblindness & Low Vision (video from slides)](https://youtu.be/xrqdU4cZaLw)
- [WCAG 2 Checklist](https://webaim.org/standards/wcag/checklist)
- [Contrast Checker tool](https://webaim.org/resources/contrastchecker/)
- [WCAG 2 Overview and official documentation](https://www.w3.org/WAI/standards-guidelines/wcag/)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/): Test color contrast ratios

## Citations

[1] A. Shatov, "White Digital Device at 12 00," Unsplash, 2021. Available: https://unsplash.com/photos/white-digital-device-at-12-00-DHl49oyrn7Y

[2] M. Brown, "Making Games Better for Gamers with Colourblindness & Low Vision | Designing for Disability," Game Maker's Toolkit, 2018. Available: https://www.youtube.com/watch?v=xrqdU4cZaLw

[3] WAI, "WCAG 2 Overview," W3C, 2025. Available: https://www.w3.org/WAI/standards-guidelines/wcag/

[4] A. Blackwell, "The Curb-Cut Effect," SSIR, 2017. Available: https://ssir.org/articles/entry/the_curb_cut_effect

[5] Larea, "Color," The Noun Project, 2024. Available: https://thenounproject.com/icon/color-7309833/

[6] Alvida, "Glasses," The Noun Project, 2025. Available: https://thenounproject.com/icon/glasses-7656753/

[7] R. Romadoni, "Blind," The Noun Project, 2025. Available: https://thenounproject.com/icon/blind-7616838/

[8] A. Pottinger, "Income Gaps." 2023. Available: https://incomegaps.com/

[9] A. Pottinger, R. Geyer, N. Biyani, C. Martinez, N. Nathan, M. Morse, M. de Bruyn, C. Boettiger, E. Baker, K. Koy, and D. McCauley, "Global Plastics AI Policy Tool," University of California, 2024. Available: https://global-plastics-tool.org/

[10] A. Pottinger, R. Geyer, N. Biyani, C. Martinez, N. Nathan, M, Morse, C. Liu, S. Hu, M. de Bruyn, C. Boettiger, E. Baker, and D. McCauley, "Pathways to reduce global plastic waste mismanagement and greenhouse gas emissions by 2050," *Science*, 2024. doi: 10.1126/science.adr3837

[11] WebAIM, "Contrast Checker," Utah State University. Available: https://webaim.org/resources/contrastchecker/

[12] A. Pottinger, L. Connor, B. Guzder-Williams, M. Weltman-Fahs, N. Gondek, and T. Bowles, "Climate-driven doubling of U.S. maize loss probability: Interactive simulation with neural network Monte Carlo," *JDSSV*, 2025. doi: 10.52933/jdssv.v5i3.134

[13] E. Purnomo, "Target," The Noun Project, 2022. Available: https://thenounproject.com/icon/target-4642615/

[14] P. Octaviani, "Keyboard," The Noun Project, 2023. Available: https://thenounproject.com/icon/keyboard-5600882/

[15] Alzam, "Speed," The Noun Project, 2022. Available: https://thenounproject.com/icon/speed-4573076/

[16] A. Pottinger and Sketchingpy Contributors, "Sketchingpy," Sketchingpy Project, 2025. Available: https://sketchingpy.org/

[17] WebAIM, "WebAIM's WCAG 2 Checklist," Utah State University. Available: https://webaim.org/standards/wcag/checklist
