---
title: Human-Computer Interaction
type: concept
section: "9.1"
level: 300
tags: [hci, usability, affordance, mental-model, user-centered-design]
sources: [hci-texts-courses-and-seminal-papers]
summary: The design and study of interactive systems from the human's side — affordances, mental models, the gulfs of execution and evaluation, and iterative user-centered design.
---

# Human-Computer Interaction
**In one sentence.** HCI is the discipline of designing, building, and evaluating
interfaces so that the *human's* goals, perception, and cognition — not the
machine's convenience — drive how the system behaves.

## Why it matters
Most software failures that users experience are not crashes; they are the
interface making the wrong thing easy and the right thing hard. HCI gives the
vocabulary and methods to design against that, and it is the theory behind every
front end, [[data-visualization]], and accessibility requirement. A correct system
with an unusable interface is, from the user's chair, a broken system.

## How it works
**Norman's cognitive model.** A user acts across two gaps:
- **Gulf of execution** — the distance between the user's intention and the
  actions the system allows. Narrowed by good *affordances* and *signifiers*.
- **Gulf of evaluation** — the distance between the system's state and the user's
  ability to perceive it. Narrowed by good *feedback*.

**Norman's design principles:**
- **Affordance** — what an object lets you do (a handle affords pulling). The
  digital version is often only a *signifier* — a visible cue (a button's shading)
  that advertises the affordance.
- **Signifiers** — perceivable signals of where to act.
- **Mapping** — the correspondence between controls and effects (stove knobs laid
  out like the burners they control).
- **Feedback** — immediate, informative response to every action.
- **Constraints** — physical, logical, cultural limits that prevent error.
- **Conceptual model** — the simplified story the user builds of how the system
  works; the designer's job is to make the *system image* teach a correct one.

**Mental models.** Users act on their model of the system, not the system. When the
model and the system image diverge, errors follow. Good design makes the system
image reveal an accurate, simple model.

**User-centered / iterative design.** Study real users and their tasks
(*needfinding*), prototype cheaply, test, and revise — repeatedly. Fidelity rises
only as confidence rises; see [[usability-evaluation-and-user-research]].

## Historical spine
- **Bush's memex (1945)** — associative trails; the ancestor of hypertext.
- **Sutherland's Sketchpad (1963)** — direct manipulation.
- **Engelbart (1968)** — mouse, windows, hypertext, collaboration in one demo.
- **Xerox PARC / the desktop GUI** — WIMP (windows, icons, menus, pointer).
- **Card/Moran/Newell (1983)** — the quantitative turn; see
  [[interaction-design-and-cognitive-models]].

## Pitfalls & gotchas
- **Designing for yourself.** You are not the user; your expertise hides problems.
- **Dark patterns.** Interfaces engineered to exploit cognition (roach motels,
  confirm-shaming) — an ethics failure; see [[computing-ethics-and-professional-responsibility]].
- **Feature creep** erases the conceptual model users had learned.
- **Ignoring accessibility** designs out users with disabilities; it is also a
  legal obligation in many jurisdictions.

## Worked example
A "Norman door" — a flat plate (afford *push*) on a door that must be *pulled* —
is a mapping/signifier failure: the signifier contradicts the required action, so
users fail even though the task is trivial. The fix is not a "PULL" label (a
patch over bad design) but a handle that affords pulling.

## Related
- [[usability-evaluation-and-user-research]] — how HCI measures whether a design works.
- [[interaction-design-and-cognitive-models]] — the quantitative models (Fitts, GOMS).
- [[data-visualization]] — perceptual HCI applied to data.
- [[frontend-frameworks-and-state-management]] — HCI made concrete in the browser.
- [[computing-ethics-and-professional-responsibility]] — dark patterns, consent, accessibility.

## Sources
Distilled from [[hci-texts-courses-and-seminal-papers]] (Norman *DOET*; Bush 1945;
Engelbart 1962/1968; Sutherland 1963).
