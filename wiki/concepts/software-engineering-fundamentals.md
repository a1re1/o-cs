---
title: Software engineering fundamentals — programming integrated over time (Hyrum's law, scale, trade-offs), essence vs accident and why there is no silver bullet, process models (waterfall as Royce actually wrote it, spiral, iterative/agile, Scrum/XP/Kanban, DevOps), requirements and specification, estimation and Brooks' law, conceptual integrity and the second-system effect, Conway's law, Lehman's laws, team practices (code review, style guides, documentation, knowledge sharing), and measuring engineering productivity
type: concept
section: "7.1"
level: 300
tags: [software-engineering, programming-over-time, hyrums-law, scale, trade-offs, essence-accident, no-silver-bullet, complexity, conformity, changeability, invisibility, process-models, waterfall, royce, spiral-model, boehm, iterative, incremental, agile, agile-manifesto, scrum, sprints, extreme-programming, xp, kanban, devops, continuous-delivery, requirements, user-stories, specification, acceptance-criteria, estimation, brooks-law, mythical-man-month, cocomo, planning-poker, conceptual-integrity, second-system-effect, conways-law, inverse-conway, lehmans-laws, team-practices, style-guides, code-review, documentation, knowledge-sharing, bus-factor, genius-myth, engineering-productivity, dora-metrics, peopleware, flow, sommerville, swe-at-google]
sources: [software-engineering-texts-courses-and-seminal-papers]
summary: Software engineering is programming integrated over time — the discipline of code that must keep working as requirements, dependencies, teams and platforms change (Hyrum's law: with enough users, every observable behaviour of your system will be depended on, so any change breaks someone), at a scale where policies must scale sublinearly with people and code, under trade-offs decided by evidence rather than taste; Brooks' "No Silver Bullet" explains why no tool gives an order-of-magnitude gain: the essential difficulties of software — complexity, conformity, changeability, invisibility — remain after every accidental one (languages, machines, environments) is removed, so the real levers are buying instead of building, rapid prototyping to discover requirements, growing systems incrementally, and great designers; process models organize the work — Royce's 1970 "waterfall" paper itself argued single-pass development fails and prescribed prototypes and iteration, Boehm's spiral makes risk drive each cycle, and the Agile Manifesto (individuals and interactions, working software, customer collaboration, responding to change; short iterations, sustainable pace, simplicity, reflection) became Scrum, XP and Kanban and then DevOps/continuous delivery; requirements are discovered not collected (user stories with acceptance criteria, prototypes, the cost of a late requirement); estimation is unreliable and Brooks' law says adding people to a late project makes it later (communication grows as n², ramp-up costs, indivisible tasks); design needs conceptual integrity (one mind or a small aristocracy of design) and beware the second-system effect; Conway's law says systems mirror the communication structure of the organizations that build them (so design the org for the architecture you want); Lehman's laws say a used system must change and, unless worked against, grows in complexity; and the practices that hold it together are code review, style guides, documentation, knowledge sharing (the bus factor, "hiding considered harmful"), and productivity measurement that looks at outcomes and flow (DORA metrics) rather than lines of code.
---
# Software engineering fundamentals

**In one sentence.** Software engineering is what programming becomes when the code has
to survive time, scale, and other people — so the discipline is mostly about managing
change (Hyrum's law, Lehman's laws), organizing humans (Brooks, Conway, Agile), and
attacking essential complexity, because the accidental kind has largely been solved.

## Programming integrated over time (SWE at Google ch. 1)
"Software engineering is programming integrated over time." Three axes: **time** — a program
written once and thrown away is different from one maintained for a decade; every
dependency, platform, and requirement will change, and **Hyrum's law** says that "with a
sufficient number of users of an API, it does not matter what you promise in the contract:
all observable behaviors of your system will be depended on by somebody" (the hash-
ordering example: code that relied on unspecified iteration order broke when the hash
changed) — so upgrades are inevitable and "nothing changes" isn't a policy; **scale** — as
engineers and code grow, human processes must scale sublinearly (a policy that needs one
person to approve everything doesn't; the compiler-upgrade example: the first upgrade of a
large codebase is agony, the tenth is routine once tests, tooling, and small-change
culture exist; **shift left** — find problems earlier where they're cheaper); **trade-offs** —
decisions by data and cost (engineering time, resources, opportunity, societal), not
"because I said so"; be willing to revisit decisions and admit mistakes. The rest of the
book is the practices (culture, process, tools) that make time and scale survivable —
[[technical-debt-and-maintenance]], [[code-review]], [[unit-testing]], [[build-systems-and-make]],
[[continuous-integration-and-delivery]].

## No silver bullet: essence and accident (Brooks 1986 — read)
"All software construction involves **essential** tasks, the fashioning of the complex
conceptual structures that compose the abstract software entity, and **accidental** tasks,
the representation of these abstract entities in programming languages and the mapping of
these onto machine languages." Past big gains (high-level languages, time-sharing,
integrated environments) removed accidental barriers; unless accidental work is > 9/10 of
the effort, shrinking it to zero can't give 10×. The essence is hard because of
**complexity** (no two parts alike — software has more states than any other artefact;
non-linear scaling; the source of unreliability, communication cost, and management
difficulty), **conformity** (to arbitrary human institutions and legacy interfaces),
**changeability** (software is pure thought-stuff embedded in a changing matrix of users,
laws, machines), and **invisibility** (no faithful geometric representation — hence design
is hard to visualize and communicate). The proposed bullets (Ada, OOP, AI/expert systems,
automatic programming, graphical programming, verification, environments, workstations)
each attack accidents. Attacks on the essence: **buy vs build** (the mass market — now
open source and cloud), **requirements refinement and rapid prototyping** ("the hardest
single part of building a software system is deciding precisely what to build"),
**incremental development — grow, don't build** (a running system at every stage; morale),
and **great designers** (nurture them as you would managers). Forty years on the diagnosis
holds; the "10× in a decade" claim is what to check any new tool against — including AI
coding assistants, which attack accidents (and some essence: requirements conversation).

## Process models (Royce 1970; Boehm 1988; Agile Manifesto 2001; Sommerville ch. 2–3)
**Waterfall**: requirements → design → implementation → verification → maintenance. Royce's
paper drew the diagram and then said it "is risky and invites failure" because testing
happens too late; he prescribed a preliminary design, **do it twice** (a pilot/prototype),
involving the customer, and documentation — the industry adopted the diagram and ignored
the text. Plan-and-document processes suit regulated/contractual work with stable
requirements. **Spiral** (Boehm): repeated cycles of determine objectives → identify and
resolve risks (prototype, simulate) → develop and verify → plan the next cycle — risk-
driven, the ancestor of iterative methods. **Iterative/incremental**: deliver working
increments, re-plan from feedback. **Agile** (2001): four values (individuals and
interactions over processes and tools; working software over comprehensive documentation;
customer collaboration over contract negotiation; responding to change over following a
plan — "while there is value in the items on the right, we value the items on the left
more") and twelve principles (early and continuous delivery; welcome changing requirements
even late; deliver frequently, weeks not months; business people and developers together
daily; motivated individuals, trusted; face-to-face conversation; working software as the
primary measure of progress; sustainable pace; technical excellence and good design;
simplicity — maximizing the work not done; self-organizing teams; regular reflection and
adjustment). Instances: **Scrum** (sprints of 1–4 weeks, product backlog, daily stand-up,
sprint review and retrospective, product owner / scrum master), **XP** (pair programming,
TDD, continuous integration, refactoring, small releases, collective ownership —
[[unit-testing]], [[refactoring]]), **Kanban** (flow, WIP limits, no fixed iterations), and
their degeneration into ritual ("agile theatre"); **DevOps** and continuous delivery extend
the loop to deployment and operations ([[continuous-integration-and-delivery]],
[[site-reliability-engineering]]). Choose by uncertainty: high requirement uncertainty →
short iterations and prototypes; high cost of failure → more up-front verification
([[program-verification]], safety standards).

## Requirements, specification, estimation (Sommerville ch. 4; Brooks MMM; Fox & Patterson ch. 7)
Requirements are **discovered**: elicitation (interviews, observation, prototypes,
scenarios), functional vs non-functional (performance, security, usability —
[[human-computer-interaction]]), and the cost curve — a requirement found in production
costs 10–100× one found in analysis (Boehm), which is agile's justification for frequent
feedback. **User stories** ("as a ⟨role⟩ I want ⟨goal⟩ so that ⟨benefit⟩") with **acceptance
criteria** (BDD: given/when/then — executable as tests), SMART/INVEST checklists, lo-fi
mockups, and **specifications** for interfaces and behaviour (preconditions/postconditions —
[[design-by-contract]]; formal specs where stakes justify — [[program-verification]]).
**Estimation**: notoriously poor (cone of uncertainty ±4× at inception); expert judgment,
analogy, decomposition, story points with **planning poker** and velocity, parametric
models (COCOMO: effort ∝ size^1.05–1.2 × cost drivers); schedule is not fungible with staff —
**Brooks' law**: "adding manpower to a late software project makes it later" — because of
ramp-up time, communication overhead (n(n−1)/2 channels), and tasks that are sequential
(nine women, one month); the **mythical man-month** is the assumption that they are
interchangeable. Prefer scope cuts, time-boxing, and delivering the most valuable slice.

## Design principles at the project level (Brooks MMM; Conway 1968; Lehman 1980)
**Conceptual integrity**: "it is better to have a system omit certain anomalous features
and improvements, but to reflect one set of design ideas" — achieved by one architect or a
small design team (the **surgical team**), with implementation separated from architecture;
the **second-system effect**: the designer's second system is over-engineered with every
idea deferred from the first — be vigilant on your second; "plan to throw one away; you
will, anyhow" (later retracted in favour of incremental growth). **Conway's law**: "any
organization that designs a system … will produce a design whose structure is a copy of the
organization's communication structure" — teams that don't talk produce interfaces that
don't fit; the **inverse Conway manoeuvre** shapes teams to get the architecture (two-pizza
teams ↔ microservices — [[software-architecture-and-system-design]]). **Lehman's laws** of
E-type (real-world) software: I continuing change (a used system must adapt or become
progressively less useful); II increasing complexity (unless work is done to reduce it);
III self-regulation; IV conservation of organizational stability (work rate is roughly
constant); V conservation of familiarity; VI continuing growth; VII declining quality
unless adapted; VIII feedback system — the empirical basis of [[technical-debt-and-maintenance]].
Modularity and information hiding as the design-level counterpart:
[[modularity-and-information-hiding]].

## Teams, culture, and productivity (SWE at Google ch. 2–7; Peopleware)
Software is a team endeavour: the **genius myth** (lone-inventor stories hide the team);
**hiding considered harmful** — working alone until it's perfect prevents early detection
of wrong directions, raises the **bus factor** (how many people can be hit by a bus before
the project dies), and slows the pace; humility, respect, trust as the three pillars;
blameless post-mortems ([[site-reliability-engineering]]); **knowledge sharing** (docs,
mailing lists, office hours, readability/mentorship — [[code-review]] as teaching);
psychological safety; **style guides** (consistency over personal preference; rules that
scale; automate enforcement — [[shell-and-unix-tools]], linters); **documentation** as code
(reviewed, versioned, owned; reference vs tutorial vs conceptual; design docs before
large work); leading teams (servant leadership, "always be deciding/leaving/scaling");
**engineering for equity** (who is harmed by defaults). **Measuring productivity**: not
lines of code or commits; GSM (goals → signals → metrics) and the QUANTS dimensions
(quality, attention, intellectual complexity, tempo/velocity, satisfaction); **DORA**
metrics — deployment frequency, lead time for changes, change failure rate, time to
restore — correlate with organizational performance (Accelerate, Forsgren et al.).
**Peopleware**: productivity varies 10× between individuals and teams; **flow** needs
uninterrupted time and quiet; open-plan offices and interruptions are measurable costs;
teams "jell" and management's job is removing obstacles, not adding pressure; overtime is
borrowed, not free.

## Pitfalls
- Adopting the waterfall diagram (or the agile rituals) without the underlying idea
  (iteration, feedback).
- Adding people to a late project; treating estimates as commitments; measuring
  productivity by output volume.
- Expecting a tool/language/AI to deliver 10× — check which of Brooks' essences it touches.
- Designing by committee (no conceptual integrity) or by org chart (Conway) without
  noticing.
- Ignoring Lehman: shipping and never budgeting for the change that use will demand.
- Hiding work until it's perfect; no docs, no review, bus factor of one.

## Related
- [[modularity-and-information-hiding]], [[technical-debt-and-maintenance]],
  [[code-review]], [[unit-testing]], [[refactoring]], [[debugging]],
  [[design-patterns-catalog]], [[git-data-model]], [[build-systems-and-make]],
  [[continuous-integration-and-delivery]], [[software-architecture-and-system-design]],
  [[site-reliability-engineering]], [[program-verification]], [[design-by-contract]],
  [[human-computer-interaction]].

## Sources
Winters, Manshreck & Wright 2020 ch. 1–7 (ToC read); Brooks 1986 (read), 1975/1995; Parnas 1972 (read); Royce 1970; Boehm 1988; Agile Manifesto and principles 2001 (read); Conway 1968; Lehman 1980; DeMarco & Lister 1987; Forsgren, Humble & Kim 2018 (*Accelerate*); Sommerville 10e ch. 1–4, 22–23; Fox & Patterson ch. 1, 7, 10.
