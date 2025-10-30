# Doc Pages Styling Guide - Quick Reference

## 🎨 Visual Style Guide for Chapter Pages

This guide provides a quick reference for the premium styling features applied to all ebook chapter/doc pages.

---

## 📖 Typography

### Headings

#### H1 - Main Chapter Title
- **Style:** Gradient text effect (Deep Navy → #003366)
- **Size:** 2.75rem (44px)
- **Effect:** Decorative underline (80px × 4px)
- **Dark Mode:** Light Gray → White gradient

```markdown
# Chapter Title: The Hook
```

#### H2 - Major Sections
- **Style:** Accent underline with gradient
- **Size:** 2rem (32px)
- **Effect:** Bottom border + 60px gradient accent
- **Spacing:** 3rem top margin

```markdown
## Major Section Title
```

#### H3 - Subsections
- **Style:** Left border accent (4px gradient)
- **Size:** 1.5rem (24px)
- **Effect:** Padding left with colored border
- **Spacing:** 2.5rem top margin

```markdown
### Subsection Title
```

### Body Text
- **Line Height:** 1.8 (optimal readability)
- **Font Size:** 1.0625rem (17px)
- **Max Width:** 75ch (optimal line length)
- **Spacing:** 1.5rem between paragraphs

---

## 🔗 Links

**Appearance:**
- Colored text (Deep Navy / Medium Gray)
- Bottom border underline
- Hover: Background highlight + darker text

```markdown
[Link Text](https://example.com)
```

---

## 📝 Lists

### Unordered Lists (Bullets)
- **Custom Bullet:** ▸ (colored triangle)
- **Color:** Theme primary color
- **Spacing:** 0.75rem between items

```markdown
- First item
- Second item
  - Nested item
- Third item
```

### Ordered Lists (Numbers)
- **Style:** Bold numbers with theme color
- **Alignment:** Right-aligned
- **Spacing:** 0.75rem between items

```markdown
1. First step
2. Second step
3. Third step
```

---

## 💬 Blockquotes

**Features:**
- Gradient background (theme-tinted)
- 4px left border (theme color)
- Decorative quote mark (4rem)
- Box shadow for depth
- Rounded corners (0 8px 8px 0)

```markdown
> This is a blockquote with premium styling.
> It has a gradient background and decorative elements.
```

**Result:**
- Beautiful gradient background
- Clear visual separation
- Professional appearance

---

## 💻 Code

### Inline Code
- **Background:** Theme-tinted (8% opacity)
- **Border:** 1px solid with theme color
- **Padding:** 0.2em 0.5em
- **Font:** SF Mono, Monaco, Cascadia Code

```markdown
Use `inline code` for commands or code snippets.
```

### Code Blocks
- **Margins:** 2rem top and bottom
- **Border Radius:** 8px
- **Shadow:** Enhanced depth effect
- **Padding:** 1.5rem

````markdown
```python
def hello_world():
    print("Hello, World!")
```
````

---

## 📊 Tables

**Features:**
- Gradient header (Deep Navy → darker)
- Zebra striping (alternating row colors)
- Hover effects on rows
- Rounded corners (8px)
- Box shadow for elevation

```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Data 1   | Data 2   | Data 3   |
| Data 4   | Data 5   | Data 6   |
```

---

## 🎯 Admonitions / Callouts

### Available Types

#### 📘 Note (Blue)
```markdown
:::note
This is important information to remember.
:::
```

#### 💡 Tip (Green)
```markdown
:::tip
Here's a helpful tip for better results.
:::
```

#### ⚠️ Warning (Orange)
```markdown
:::warning
Be careful with this approach.
:::
```

#### 🚨 Danger (Red)
```markdown
:::danger
This is critical information - pay attention!
:::
```

#### ℹ️ Info (Cyan)
```markdown
:::info
Additional context and information.
:::
```

**Styling:**
- 4px left border (type-specific color)
- Gradient background (subtle)
- Box shadow
- Rounded corners (8px)
- Proper padding and spacing

---

## 🖼️ Images

**Effects:**
- Rounded corners (8px)
- Box shadow for depth
- Hover: Lifts up (translateY -4px)
- Enhanced shadow on hover
- Smooth transitions

```markdown
![Alt text](image-path.png)
```

---

## ➖ Horizontal Rules

**Style:**
- Gradient line (center-focused)
- Transparent edges (fade effect)
- 1px height
- 3rem spacing top and bottom

```markdown
---
```

**Result:**
- Elegant section dividers
- Theme-aware colors
- Subtle and professional

---

## 📱 Responsive Behavior

### Desktop (1920px+)
- Full-size typography
- Optimal line length (75ch)
- All effects enabled

### Tablet (768px)
- Slightly reduced font sizes
- Maintained spacing
- Compact tables
- All effects preserved

### Mobile (480px)
- Optimized typography
- Reduced padding
- Stacked layouts
- Touch-friendly spacing

---

## 🌓 Dark Mode

**Automatic Theme Support:**
- ✅ All elements adapt to dark theme
- ✅ Proper contrast ratios
- ✅ Adjusted gradients and shadows
- ✅ Color palette shifts automatically
- ✅ Maintains visual hierarchy

**Dark Mode Colors:**
- Primary: #AAAAAA (Medium Gray)
- Text: #d0d0d0 (Light Gray)
- Backgrounds: #111111, #1a1a1a
- Gradients: Lighter variants for contrast

---

## 🎨 Color Reference

### Light Mode
```
Primary:     #001f3f (Deep Navy)
Secondary:   #003366 (Navy)
Text:        #2c3e50 (Dark Gray)
Links:       #001f3f (Deep Navy)
Borders:     rgba(0, 31, 63, 0.15)
```

### Dark Mode
```
Primary:     #AAAAAA (Medium Gray)
Secondary:   #DDDDDD (Light Gray)
Text:        #d0d0d0 (Light Gray)
Links:       #AAAAAA (Medium Gray)
Borders:     rgba(170, 170, 170, 0.2)
```

---

## ⚡ Interactive Elements

### Hover Effects
- Links: Background highlight
- Buttons: Lift and shadow
- Images: Lift and enhanced shadow
- Table rows: Background change
- Cards: Border and transform

### Transitions
- Duration: 0.2s - 0.3s
- Easing: cubic-bezier(0.4, 0, 0.2, 1)
- Properties: color, background, transform, box-shadow

---

## 📐 Spacing System

### Margins
```
Small:   0.75rem - 1rem
Medium:  1.5rem - 2rem
Large:   2.5rem - 3rem
XLarge:  4rem
```

### Padding
```
Compact: 0.5rem - 1rem
Normal:  1rem - 1.5rem
Relaxed: 1.5rem - 2rem
```

---

## 🎯 Best Practices

### Writing Content

1. **Use Headings Hierarchically**
   - H1 for chapter title (once per page)
   - H2 for major sections
   - H3 for subsections
   - Don't skip levels

2. **Break Up Long Paragraphs**
   - Keep paragraphs focused
   - Use spacing effectively
   - Add visual breaks with HR

3. **Use Lists for Clarity**
   - Bullet points for items
   - Numbered lists for sequences
   - Nested lists for sub-items

4. **Highlight Important Content**
   - Use blockquotes for key takeaways
   - Use admonitions for special notes
   - Use **bold** for emphasis
   - Use *italics* for subtle emphasis

5. **Code Examples**
   - Inline code for short snippets
   - Code blocks for multi-line examples
   - Include language identifier for syntax highlighting

6. **Visual Elements**
   - Add images to break up text
   - Use tables for structured data
   - Use HR for section dividers

---

## ✅ What's Styled Automatically

Everything in your markdown gets premium styling:
- ✅ All heading levels (H1-H6)
- ✅ Paragraphs with optimal spacing
- ✅ Links with hover effects
- ✅ Lists (ordered, unordered, nested)
- ✅ Blockquotes with decorations
- ✅ Code (inline and blocks)
- ✅ Tables with zebra striping
- ✅ Images with hover effects
- ✅ Horizontal rules
- ✅ Strong and emphasis text
- ✅ Admonitions (if using Docusaurus syntax)

---

## 🚀 Zero Configuration

**Just write markdown as usual!**

The styling system automatically:
- Applies premium styles to all elements
- Adapts to light/dark theme
- Responds to screen size
- Maintains accessibility
- Provides smooth interactions

**No special classes or tags needed** - just write clean, semantic markdown and the styles handle the rest!

---

## 📚 Example Chapter Structure

```markdown
# Chapter Title: Introduction to AI Development

Brief introduction paragraph explaining what this chapter covers.

## Learning Objectives

By the end of this chapter, you will:

1. Understand core concepts
2. Apply practical techniques
3. Build real projects

---

## Main Concept

This is where the main content begins. Each paragraph is properly spaced
for optimal readability with a line height of 1.8.

### Subsection

More detailed information here with proper visual hierarchy.

> **Key Takeaway:** Important information stands out in blockquotes
> with premium styling and decorative elements.

:::tip
Here's a practical tip for better results!
:::

### Code Example

Here's how to implement this:

```python
def example_function():
    """Premium code styling with syntax highlighting"""
    return "Beautiful code blocks"
```

## Summary

Final thoughts and recap with proper spacing and styling.

---

**Next Chapter:** [Chapter 2: Advanced Topics →](next-chapter.md)
```

---

## 🎨 Result

With these styling improvements, your doc pages now have:

✨ **Professional appearance** matching the homepage  
📖 **Optimal readability** with enhanced typography  
🎯 **Clear hierarchy** guiding readers naturally  
🌈 **Consistent branding** with Polar Night theme  
💫 **Smooth interactions** with subtle animations  
🌓 **Perfect dark mode** experience  
📱 **Fully responsive** across all devices  

---

**Happy Writing! Your content now looks as good as it reads.** 🎉