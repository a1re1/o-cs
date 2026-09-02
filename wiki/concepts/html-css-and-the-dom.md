---
title: HTML, CSS and the DOM — semantic HTML (document structure, elements as meaning, forms, media, the accessibility tree), the DOM as a live tree with events (bubbling and capturing, delegation), CSS fundamentals (selectors and specificity, the cascade and inheritance, the box model, units, positioning, flexbox and grid, responsive design and media queries, custom properties, transitions/animations), how the browser turns them into pixels (parse, style, layout, paint, composite), accessibility (WCAG, ARIA, keyboard, screen readers), and progressive enhancement
type: concept
section: "7.5"
level: 200
tags: [html, semantic-html, elements, attributes, document-structure, head, meta, forms, input-types, validation, media, images, responsive-images, srcset, picture, dom, document-object-model, nodes, tree, queryselector, events, event-bubbling, event-capturing, event-delegation, addeventlistener, preventdefault, css, selectors, specificity, cascade, inheritance, box-model, margin, padding, border, box-sizing, display, block, inline, units, rem, em, viewport-units, positioning, absolute, relative, fixed, sticky, z-index, stacking-context, flexbox, grid, responsive-design, media-queries, mobile-first, container-queries, custom-properties, css-variables, transitions, animations, transforms, rendering, style-calculation, layout, reflow, paint, composite, accessibility, a11y, wcag, aria, accessibility-tree, keyboard-navigation, focus, screen-readers, alt-text, color-contrast, progressive-enhancement, web-components, shadow-dom]
sources: [web-development-texts-courses-and-seminal-papers]
summary: HTML is a document language whose elements carry meaning (headings, sections, lists, tables, forms, figures, nav/main/article) that browsers, search engines and assistive technology all consume — so semantic markup is what makes a page accessible, indexable and styleable, while `div` soup discards it; the browser parses HTML into the DOM, a live tree of nodes that JavaScript reads and mutates and that dispatches events through capture and bubble phases (so one listener on a parent can handle events from many children — delegation); CSS attaches presentation by matching selectors to nodes, resolving conflicts by the cascade (origin and importance, then specificity, then source order) with inheritance for text properties, and laying out boxes (content, padding, border, margin — prefer `box-sizing: border-box`) as block or inline formatting contexts, positioned normally or by relative/absolute/fixed/sticky, and, for anything non-trivial, with flexbox (one-dimensional distribution) or grid (two-dimensional placement), made responsive with fluid units, media and container queries and a mobile-first approach, and parameterized by custom properties; the browser then computes styles, lays out (reflow), paints and composites layers, which is why animating `transform` and `opacity` is cheap and animating `width` or `top` is not; accessibility is a requirement, not a feature — WCAG's perceivable/operable/understandable/robust principles, native semantics first and ARIA only to fill gaps, full keyboard operability with visible focus, alt text, contrast, and testing with a screen reader — and progressive enhancement (working HTML, then CSS, then JS) is the design stance that keeps the page usable when any layer fails.
---
# HTML, CSS and the DOM

**In one sentence.** Write HTML that says what things *are*, let CSS decide how they
*look* through the cascade and layout systems, and treat the DOM as the live tree that
both scripts and assistive technologies read — then the page works for everyone and the
browser can render it fast.

## HTML: structure and meaning (MDN "Structuring content"; HTML Living Standard)
A document: `<!doctype html>`, `<html lang>`, `<head>` (`<meta charset>`, `<meta
name=viewport>`, `<title>`, `<link rel=stylesheet>`, `<script defer type=module>`),
`<body>`. **Semantic elements**: `header/nav/main/article/section/aside/footer`, `h1–h6`
(one logical outline), `p`, `ul/ol/li`, `dl`, `table/thead/tbody/th scope`, `figure/
figcaption`, `blockquote`, `time`, `code/pre`, `em/strong`, `button` (not a clickable
`div`), `a href` (navigation; not a click handler), `details/summary`, `dialog`.
Semantics feed the **accessibility tree** (role, name, state per element), search
engines, reader modes, and default styling/behaviour (a `<button>` is focusable and
activates with Enter/Space for free). **Forms**: `<form action method>`, `<label for>`,
`input type=` (text, email, number, date, file, checkbox, radio, range), `select`,
`textarea`, built-in **validation** (`required`, `pattern`, `min/max`, `:invalid`),
`autocomplete`, submission (GET query string vs POST body, `multipart/form-data` for files;
`FormData` in JS); forms work without JS. **Media**: `<img src alt width height>` (dimensions
prevent layout shift; `loading=lazy`; `srcset`/`sizes` and `<picture>` for **responsive
images** and formats — AVIF/WebP), `<video>`/`<audio>`, `<svg>` inline, `<canvas>`.
Attributes: global (`id`, `class`, `data-*`, `hidden`, `tabindex`, `aria-*`), boolean
attributes. **Web components**: custom elements (`class extends HTMLElement`, lifecycle
callbacks), **shadow DOM** (encapsulated subtree and styles), `<template>`/`<slot>`.

## The DOM and events (Eloquent JS ch. 14–15; DOM Standard)
The parser builds a tree of `Node`s (`Document` → `Element`s → `Text`); the DOM API is
the live, mutable view: `document.querySelector(All)`, `el.textContent`/`innerHTML`
(HTML injection risk — [[web-security]]), `createElement`/`append`/`remove`,
`classList`, `dataset`, `getAttribute`, `getBoundingClientRect` (forces layout),
`MutationObserver`, `IntersectionObserver`, `ResizeObserver`. **Events**: `el.addEventListener
(type, handler, {capture, once, passive})`; dispatch runs the **capture** phase (window →
target), **target**, then **bubble** (target → window) for most events; `event.target` vs
`currentTarget`; `preventDefault()` (cancel the default action: link navigation, form
submit, checkbox toggle), `stopPropagation()`; **event delegation** — one listener on a
container handling events from many (present or future) descendants by checking
`target.closest(selector)`; input events (`click`, `input` vs `change`, `keydown`,
pointer events unify mouse/touch/pen), `submit`, `DOMContentLoaded` vs `load`,
`scroll`/`resize` (throttle; `passive: true`), custom events (`new CustomEvent`). The
DOM is the boundary where JavaScript meets the page ([[javascript-and-the-event-loop]])
and what frameworks abstract ([[frontend-frameworks-and-state-management]]).

## CSS: selectors, the cascade, the box model (MDN "CSS styling basics"; CSS specs)
**Selectors**: type, `.class`, `#id`, attribute `[type=email]`, combinators (descendant
` `, child `>`, sibling `+ ~`), pseudo-classes (`:hover :focus-visible :nth-child()
:not() :is() :has()`), pseudo-elements (`::before ::after ::marker`). **Specificity**
(id, class/attr/pseudo-class, type) compared lexicographically; **cascade** order:
origin and importance (user-agent < user < author; `!important` reverses), then **cascade
layers** (`@layer`), then specificity, then source order; **inheritance** for text
properties (`color`, `font`, `line-height`) not box properties; `inherit/initial/unset/
revert`; custom properties `--brand: #123; color: var(--brand, fallback)` inherit and
can be set per element/theme (`prefers-color-scheme`). **Box model**: content + padding +
border + margin; `box-sizing: border-box` (width includes padding/border — set it
globally); margins collapse vertically between blocks; `display`: `block`, `inline`,
`inline-block`, `none` (removes from tree), `flex`, `grid`, `contents`; formatting
contexts; **units**: `px`, `rem` (root font-size — use for type and spacing scales),
`em` (parent font-size), `%`, `vw/vh/dvh`, `ch`, `fr` (grid), `min()/max()/clamp()` for
fluid sizes. **Positioning**: `static` (normal flow), `relative` (offset, keeps space),
`absolute` (out of flow, relative to nearest positioned ancestor), `fixed` (viewport),
`sticky` (relative until a threshold); `z-index` works within a **stacking context**
(created by positioned + z-index, `opacity < 1`, `transform`, etc. — the classic
"z-index doesn't work" bug). `overflow`, `object-fit`, `aspect-ratio`.

## Layout: flexbox, grid, responsive design (MDN "CSS layout")
**Flexbox** (one axis): container `display: flex; flex-direction; justify-content (main
axis); align-items (cross axis); gap; flex-wrap`; items `flex: grow shrink basis`,
`align-self`, `order`; use for toolbars, nav, centering, distributing space. **Grid** (two
axes): `display: grid; grid-template-columns: repeat(auto-fit, minmax(16rem, 1fr));
grid-template-areas; gap`; items placed by line numbers or areas; `auto-fill/auto-fit`
for responsive card grids without media queries; subgrid. **Responsive design**: fluid
layouts, `<meta viewport>`, **mobile-first** `@media (min-width: 48rem)` breakpoints based
on content, **container queries** (`@container (min-width: …)` — component-level
responsiveness), responsive images, `prefers-reduced-motion`, logical properties
(`margin-inline`) for RTL. Typography: system font stacks, `font-display`, scale via
`clamp()`, `line-height ~1.5`, measure ~60–75 ch. **Transitions/animations**:
`transition: transform .2s`, `@keyframes` + `animation`, `transform` and `opacity` are
compositor-only (cheap, off main thread); `will-change` sparingly; View Transitions API.
Methodologies: BEM naming, utility classes (Tailwind), CSS Modules/scoped styles in
frameworks, design tokens as custom properties ([[human-computer-interaction]] for the
design side).

## From markup to pixels (MDN "Critical rendering path" — read)
HTML bytes → tokens → nodes → **DOM**; CSS → **CSSOM** (render-blocking: the browser
won't paint until CSSOM is built, so CSS in `<head>`, minimal and inlined critical CSS);
`<script>` without `defer/async` **blocks the parser** (it may `document.write`) and
waits for CSSOM (it may read styles); DOM + CSSOM → **render tree** (visible nodes with
computed styles) → **layout/reflow** (geometry) → **paint** (rasterize into layers) →
**composite** (GPU stacks layers). Costs: changing geometry (`width`, `top`, font size)
triggers layout for subtrees; reading layout properties after writing styles forces
**synchronous layout** (layout thrashing — batch reads then writes; `requestAnimationFrame`);
`transform`/`opacity` skip layout and paint. Aim for 60 fps (16 ms per frame) and no
jank; measure with DevTools Performance panel and the Performance APIs
([[web-performance-and-browser-networking]]).

## Accessibility (WCAG 2.2; WAI-ARIA; MDN "Accessibility")
**POUR**: perceivable (text alternatives — `alt` that describes purpose; captions;
contrast ≥ 4.5:1; don't convey meaning by colour alone), operable (everything works by
**keyboard** — Tab order follows DOM order, visible `:focus-visible`, no traps, skip
links; enough time; no seizure-inducing flashes), understandable (language `lang`,
predictable navigation, labelled inputs with error messages), robust (valid markup,
correct semantics/ARIA). **Native first**: a `<button>` beats `<div role=button
tabindex=0 onkeydown=…>`; **ARIA** only for what HTML lacks (`role=tablist`, `aria-expanded`,
`aria-live` regions for dynamic updates, `aria-label`/`aria-labelledby` for names) —
"no ARIA is better than bad ARIA"; hidden content: `hidden`/`display:none` (removed from
tree) vs visually-hidden CSS (kept for screen readers) vs `aria-hidden`. Test with
keyboard only, a screen reader (VoiceOver/NVDA), zoom 200 %, automated checks (axe,
Lighthouse) which catch ~30 % of issues. Legal and moral baseline; also better SEO and
UX for everyone. **Progressive enhancement**: HTML works (links, forms), CSS enhances
(`@supports`), JS enhances (hydrate, validate, animate); the reverse ("graceful
degradation") ships broken pages when JS fails — which it does (blocked, errored,
slow networks).

## Pitfalls
- `div`/`span` for everything; click handlers on non-interactive elements; missing
  labels/alt; removing focus outlines.
- Fighting specificity with `!important` and ids; global resets that break inheritance;
  `z-index: 9999` wars without understanding stacking contexts.
- Fixed pixel layouts; desktop-first breakpoints; images without dimensions (layout shift).
- Animating layout properties; layout thrashing in scroll handlers.
- Render-blocking scripts in `<head>` without `defer`; huge inline SVG/CSS per page.

## Related
- [[javascript-and-the-event-loop]], [[frontend-frameworks-and-state-management]],
  [[web-performance-and-browser-networking]], [[web-backends-sessions-and-authentication]],
  [[dns-http-and-the-web-stack]], [[web-security]], [[human-computer-interaction]],
  [[text-processing-and-regex]] (parsing), [[api-design]].

## Sources
MDN Web Docs: "Structuring content with HTML", "CSS styling basics", "CSS layout", "Critical rendering path" (read), "Accessibility"; WHATWG HTML and DOM Living Standards; W3C CSS Cascade 5, Flexbox, Grid, WCAG 2.2, WAI-ARIA 1.2; Haverbeke 2024 ch. 14–15, 18; Grigorik 2013 (rendering pipeline talks); Frost 2013 (atomic design); Champeon & Finck 2003 (progressive enhancement).
