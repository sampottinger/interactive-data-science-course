# Lesson 22
Briefly introducing web accessibility standards.

## Objective
Learn about the Web Content Accessibility Guidelines and explore common steps to improve access within interactive data visualizations.

## Outline
This lecture introduces web accessibility standards and practices specifically tailored for interactive data visualizations, focusing on making visualizations usable by people with various disabilities. Starting with WCAG guidelines and the curb-cut effect, we explore visual accessibility considerations including color deficiency, low vision, and screen reader support before examining motor accessibility concerns like keyboard navigation and timing controls.

### Introduction to WCAG
Web accessibility standards provide clear guidelines for creating inclusive experiences.

- WCAG provides comprehensive guidelines for making web content accessible to people with disabilities.
- Standards cover WCAG 2.0, 2.1, and 2.2.
- Accessibility improvements designed for people with disabilities often benefit everyone through the curb-cut effect.
- Laws and programs designed to benefit vulnerable groups often end up benefiting all of society.

### Visual accessibility
Visual accessibility addresses three categories of visual impairment with specific solutions for each.

- Color deficiency: Users may have difficulty distinguishing between certain colors.
- Low vision: Users may use magnifiers, scaled resolution, or have contrast sensitivity issues.
- Blind or partially blind: Users may rely on screen readers and keyboard-only navigation.

### Color deficiency solutions
Double encoding and alternative visualizations help address color blindness.

- WCAG 1.4.1: Color should not be the only way elements are visually distinguished from each other.
- Use additional visual cues like position, shape, patterns, textures, labels, or size differences.
- Offer alternative visualizations that don't rely solely on color.
- Be careful with semantic association in color choices like red/green for bad/good.
- Example: Income Gaps visualization uses both color and position to distinguish gender categories.
- Example: Global Plastics AI Policy Tool provides colorblind-friendly color scheme options.

### Low vision solutions
Contrast and resize support ensure visualizations remain accessible at different scales.

- WCAG 1.4.3: Ensure colors are sufficiently different from their backgrounds to be perceived.
- Maintain sufficient contrast between visual elements using tools like WebAIM's Contrast Checker.
- Meet minimum contrast ratios of 4.5:1 for normal text and 3:1 for large text.
- WCAG 1.4.4: Applications should remain functional when zoomed to 200%.
- Use responsive design principles and avoid fixed-size elements that break when magnified.
- Test visualizations at different zoom levels.

### Screen reader support
Providing non-visual alternatives ensures content is accessible to blind users.

- WCAG 1.1.1: Provide non-visual alternatives to visualizations.
- Offer data tables with the underlying data.
- Provide data download options.
- Include textual descriptions of key findings.
- Use semantic HTML elements properly with appropriate ARIA labels and roles.
- Ensure all interactive elements are accessible via keyboard.

### Motor accessibility
Interactive visualizations present unique challenges for users with motor impairments.

- Fine motor control: Users may have difficulty with precise pointing or clicking.
- Timed inputs: Some users may require additional time to complete interactions.
- Keyboard-only navigation: Users may not have access to a pointing device.

### Fine motor control solutions
Making interactive targets large enough helps users with motor impairments.

- Make interactive targets large enough with minimum 44x44 pixels recommended.
- Provide adequate spacing between clickable elements.
- Support alternative input devices.
- Avoid interactions requiring precise hovering or dragging.

### Keyboard navigation
Providing keyboard alternatives ensures access for users without pointing devices.

- WCAG 2.1.1: Provide keyboard alternatives for all custom drawing interactions.
- Document keyboard shortcuts clearly and ensure all functionality is accessible via keyboard.
- Follow logical tab order with visible focus indicators.
- WCAG 1.3.2: Use proper tab order for navigation and ensure focus is never lost or trapped.
- Example: Climate maize loss visualization includes keyboard controls for Esc, y, c, v, and u.
- Example: Global Plastics AI Policy Tool uses standard HTML elements with proper left-to-right tab sequence.

### Timing controls
Adjustable timing supports users who need more time to interact.

- WCAG 2.2.1: Allow modification or pausing of timed actions.
- Provide options to extend time limits.
- Avoid auto-advancing content without user control.
- Include pause/play controls for animations.
- Example: Sketchingpy provides pause functionality for auto-shuffling animations.
- Example: Climate simulation tools allow users to control the pace of exploration.

## Take Aways
Accessibility is good for everyone, and making visualizations accessible requires attention to visual and motor considerations while following established guidelines.

- Accessibility improvements designed for people with disabilities often benefit all users through the curb-cut effect.
- WCAG provides clear, actionable guidelines for making interactive visualizations accessible.
- Visual accessibility requires addressing color deficiency through double encoding, low vision through contrast and resize support, and blindness through screen reader alternatives.
- Motor accessibility requires keyboard navigation support, appropriately sized interactive targets, and adjustable timing controls.
- Accessibility is a deep topic requiring ongoing learning and practice with resources like WebAIM and W3C.

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
