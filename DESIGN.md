---
name: WsprryPi Documentation
description: A restrained technical reference for installing, configuring, and operating WsprryPi.
colors:
  content-background: "#ffffff"
  content-surface: "#fdfeff"
  heading: "#223345"
  body-text: "#243746"
  muted-text: "#5c6f80"
  link: "#355774"
  link-hover: "#28445c"
  navigation: "#405e7a"
  navigation-text: "#ecf1f6"
  code-text: "#16344a"
  active: "#c8a85d"
typography:
  display:
    fontFamily: "Barlow Semi Condensed, Segoe UI, sans-serif"
    fontWeight: 600
    lineHeight: 1.12
    letterSpacing: "0.012em"
  body:
    fontFamily: "Source Sans 3, Segoe UI, sans-serif"
    fontSize: "1rem"
    lineHeight: 1.6
  code:
    fontFamily: "SFMono-Regular, Consolas, Liberation Mono, monospace"
    fontSize: "0.92rem"
    lineHeight: 1.55
rounded:
  inline-code: "0.2rem"
  focus: "0.25rem"
  container: "0.75rem"
spacing:
  compact: "0.35rem"
  body: "1rem"
  section: "2.25rem"
components:
  navigation:
    backgroundColor: "{colors.navigation}"
    textColor: "{colors.navigation-text}"
  code-block:
    backgroundColor: "{colors.content-surface}"
    textColor: "{colors.code-text}"
    typography: "{typography.code}"
    rounded: "{rounded.container}"
    padding: "1rem 1.1rem"
  table:
    backgroundColor: "{colors.content-surface}"
    textColor: "{colors.body-text}"
    rounded: "{rounded.container}"
---

# Design System: WsprryPi Documentation

## 1. Overview

**Creative North Star: "The Operator's Bench Manual"**

The documentation is a practical technical companion for amateur radio operators configuring a Raspberry Pi transmitter. It should feel precise, calm, and trustworthy: dense enough to answer operational questions without becoming an implementation reference. The established Read the Docs shell, persistent navigation, restrained blue-gray palette, and readable content column are part of that dependable character.

Organize content around reader tasks: learn, install, configure, operate, troubleshoot, and reference. Preserve familiar Sphinx and Read the Docs behavior instead of inventing navigation or presentation patterns. New material should fit the existing hierarchy and should not introduce a marketing voice, ornamental layout, or application-dashboard styling.

Key characteristics:

- Technical, direct, and operator-focused.
- Stable navigation with descriptive page and section names.
- Short paragraphs, scannable subsections, and copyable examples.
- Precise separation between user-visible behavior and implementation detail.

## 2. Colors

The palette is a restrained blue-gray system: white content surfaces, dark slate text, and a muted blue navigation shell.

### Primary

- **Navigation Blue** (`#405e7a`): Read the Docs sidebar, search header, and mobile navigation chrome.
- **Operational Link Blue** (`#355774`): links within documentation content; use `#28445c` for hover and focus emphasis.

### Neutral

- **Content White** (`#ffffff`): primary reading background.
- **Quiet Surface** (`#fdfeff`): code blocks, tables, and admonition surfaces.
- **Heading Slate** (`#223345`): page and section headings.
- **Body Slate** (`#243746`): primary prose.
- **Muted Slate** (`#5c6f80`): secondary explanatory text where contrast remains sufficient.
- **Navigation Text** (`#ecf1f6`): text and icons on Navigation Blue.

### Named Rules

**The Functional Color Rule.** Use color to identify navigation, links, focus, status, and active state. Do not add decorative accent colors to documentation content.

## 3. Typography

**Display Font:** Barlow Semi Condensed (with Segoe UI and sans-serif fallbacks)  
**Body Font:** Source Sans 3 (with Segoe UI and sans-serif fallbacks)  
**Label/Mono Font:** the Read the Docs/Pygments monospace stack

**Character:** Compact technical headings pair with a neutral, highly readable body face. Typography should help readers scan configuration names and procedures without making the documentation feel promotional.

### Hierarchy

- **Display** (600, `2rem` to `2.5rem`, 1.12): one page title.
- **Headline** (600, `1.5rem` to `2rem`, 1.12): major task or reference sections.
- **Title** (600, approximately `1.2rem` to `1.25rem`, 1.12): focused subsections.
- **Body** (400, `1rem`, 1.6): prose capped near `68ch` where the theme permits.
- **Code** (`0.92rem`, 1.55): commands, INI examples, and literal values.

### Named Rules

**The Exact Label Rule.** Match UI labels and configuration keys exactly, including spacing and capitalization. Use code styling for keys, values, paths, and commands; use plain text or bold only when referring to a visible field label.

## 4. Elevation

The documentation is flat by default. Structure comes from the navigation/content split, whitespace, borders, and quiet surface changes. Existing code blocks, tables, and admonitions may use the theme's subtle `0 1px 2px rgba(20, 27, 35, 0.04)` shadow, but shadows must never become decorative cards or compete with content hierarchy.

### Shadow Vocabulary

- **Quiet separation** (`0 1px 2px rgba(20, 27, 35, 0.04)`): existing code blocks, tables, and admonitions only.

### Named Rules

**The Flat-by-Default Rule.** Prefer whitespace and a thin neutral border. Do not introduce elevated card grids or nested containers.

## 5. Components

### Navigation

- Preserve the Read the Docs sidebar, search field, breadcrumbs, next/previous links, sticky behavior, and mobile menu.
- Keep top-level navigation task-oriented: Start Here, Operate WsprryPi, and Reference.
- Place new detail on the narrowest relevant existing page; add a page only when the material represents a distinct reader task.

### Configuration Tables and Examples

- Use tables for compact key/default/meaning comparisons when cells remain short.
- Keep units explicit and defaults formatted as literal values.
- For INI examples, preserve exact section and key names and comment enough context to distinguish mode-specific settings.
- Never imply that a text field is numeric merely because an example contains digits.
- Avoid long explanatory paragraphs inside table cells; place nuance immediately below the table or example.

### Command Snippets

- Use fenced code blocks with an explicit language such as `bash`, `ini`, `json`, or `text`.
- Make commands copyable and show `cd` when the working directory matters.
- State prerequisites immediately before the command and describe the expected purpose, not internal test mechanics.
- Do not include a shell prompt unless distinguishing privileged and unprivileged commands is necessary.

### Screenshots and Rendered Examples

- Use screenshots only when they clarify location, state, or a sequence that prose cannot explain as quickly.
- Keep captions descriptive and alt text meaningful; do not rely on a screenshot as the only record of labels or defaults.
- Update or replace screenshots when visible labels or control groupings materially change. Do not add decorative product imagery.

### Markdown and Sphinx Content

- Use one `#` page title followed by a consistent heading hierarchy.
- Use `-` for unordered lists, blank lines around lists and fences, and a language on every fenced block.
- Keep heading text concise and descriptive. Avoid emphasis used as a heading.
- Preserve MyST toctrees and existing internal navigation conventions.
- Treat generated HTML as validation output; never edit files under `docs/_build`.

## 6. Do's and Don'ts

### Do:

- **Do** write in direct, restrained language for technically capable radio operators.
- **Do** distinguish WSPR, QRSS, FSKCW, and DFCW behavior wherever shared terminology could mislead.
- **Do** pair every configuration default with its units and applicable mode.
- **Do** keep UI descriptions synchronized with visible labels and conditional control states.
- **Do** explain what a setting changes for the operator and where it appears.
- **Do** validate navigation, tables, lists, code blocks, images, and terminology in rendered HTML.

### Don't:

- **Don't** expose exception classes, source guards, regression assertions, serialization internals, or implementation planning as user documentation.
- **Don't** turn a fixed defect into a standalone user-guide topic; use an existing changelog or release-notes page if one is available.
- **Don't** copy application UI CSS into the documentation or disrupt Read the Docs sidebar, search, and mobile behavior.
- **Don't** invent a marketing visual direction, decorative motion, ornamental cards, or dashboard-like controls.
- **Don't** duplicate the same explanation across UI, CLI, and configuration pages; adapt each reference to its reader task and cross-link when useful.
- **Don't** use screenshots to hide missing textual explanations of controls, accepted values, defaults, or mode-specific behavior.
