---
title: Software engineering fundamentals — Software Engineering at Google (free), Fox & Patterson's Engineering Software as a Service, Brooks' The Mythical Man-Month, McConnell's Code Complete, The Pragmatic Programmer, Sommerville; Berkeley CS169, MIT 6.102, CMU 17-313, UW CSE403, Georgia Tech CS3300; Brooks "No Silver Bullet" (1986), Parnas (1972), Royce waterfall (1970), the Agile Manifesto (2001), Conway's law (1968), Lehman's laws (1980), Boehm's spiral model (1988), DeMarco & Lister's Peopleware
type: source
section: "7.1"
level: 300
tags: [software-engineering-at-google, swe-book, winters, manshreck, wright, fox-patterson, engineering-software-as-a-service, brooks, mythical-man-month, code-complete, mcconnell, pragmatic-programmer, hunt-thomas, sommerville, cs169, 6-102, 17-313, cse403, cs3300, no-silver-bullet, essence-accident, parnas, information-hiding, royce, waterfall, agile-manifesto, conway, conways-law, lehman, lehmans-laws, boehm, spiral-model, demarco-lister, peopleware, hyrums-law]
sources: []
authors: [Titus Winters, Tom Manshreck, Hyrum Wright, Armando Fox, David Patterson, Frederick Brooks, Steve McConnell, Andrew Hunt, David Thomas, Ian Sommerville, David Parnas, Winston Royce, Melvin Conway, Meir Lehman, Barry Boehm, Tom DeMarco, Timothy Lister]
year: 2020
institution: Google / Berkeley / MIT / CMU / UNC
url: https://abseil.io/resources/swe-book
license: mixed (SWE at Google free online; others commercial)
format: html
summary: Software Engineering at Google (Winters, Manshreck & Wright 2020; free; ToC read) defines the field as "programming integrated over time" — its thesis chapter covers time and change (Hyrum's law: with enough users every observable behaviour of an interface will be depended on; the hash-ordering example; why "nothing changes" isn't an option), scale and efficiency (policies that do and don't scale, the compiler-upgrade example, shifting left), trade-offs and costs (inputs to decisions, distributed builds, revisiting decisions) and software engineering versus programming — then culture (working well on teams: the genius myth, "hiding considered harmful", the bus factor; knowledge sharing; engineering for equity; leading teams; measuring engineering productivity), processes (style guides, code review, documentation, testing overview, unit/larger tests, deprecation) and tools (version control, code search, build systems, critique, static analysis, dependency management, large-scale changes, CI, CD, compute); Fox & Patterson teach agile/SaaS development with Rails and behaviour-driven tests; Brooks' Mythical Man-Month (1975) gives Brooks' law (adding people to a late project makes it later), the surgical team, conceptual integrity and the second-system effect; McConnell's Code Complete is the construction handbook; The Pragmatic Programmer the craft manual (DRY, orthogonality, tracer bullets); Sommerville the survey textbook; and the seminal papers are Brooks' "No Silver Bullet" (1986; read: essence — complexity, conformity, changeability, invisibility — vs accident, "no single development … promises even one order of magnitude improvement", and the prescriptions buy don't build, rapid prototyping, grow software organically, cultivate great designers), Parnas' criteria for decomposing systems into modules (1971/72; read: modularize around design decisions likely to change — information hiding — not around processing steps), Royce's waterfall paper (which actually argues for iteration), the Agile Manifesto and its twelve principles (read), Conway's law (organizations design systems that mirror their communication structures), Lehman's laws of software evolution (continuing change, increasing complexity), Boehm's spiral model (risk-driven iteration), and Peopleware (productivity is about people and environment).
---
# Software engineering fundamentals: sources

## What they are
- **Software Engineering at Google** (ToC read): Thesis — *What is software engineering?*
  (time and change: **Hyrum's law**, hash ordering, why not aim for "nothing changes";
  scale and efficiency: policies that don't/do scale, compiler upgrade, shifting left;
  trade-offs and costs: markers, inputs to decision making, distributed builds, time vs
  scale, revisiting decisions and making mistakes; SE vs programming). Part II Culture —
  how to work well on teams (help me hide my code, the genius myth, hiding considered
  harmful — early detection, bus factor, pace; it's all about the team; humility, respect,
  trust), knowledge sharing, engineering for equity, how to lead a team, leading at scale,
  measuring engineering productivity. Part III Processes — style guides and rules, code
  review, documentation, testing overview, unit testing, test doubles, larger testing,
  deprecation. Part IV Tools — version control and branch management, code search, build
  systems and build philosophy, Critique (Google's code review tool), static analysis,
  dependency management, large-scale changes, continuous integration, continuous
  delivery, compute as a service. Its three axes: **time**, **scale**, **trade-offs**.
- **Fox & Patterson, Engineering Software as a Service** (Berkeley CS169): agile vs plan-
  and-document, SaaS architecture (3-tier, REST, MVC), Ruby/Rails, BDD with user stories
  and Cucumber, TDD with RSpec, legacy code, design patterns, DevOps and deployment,
  teamwork (Scrum, pair programming). **Brooks, The Mythical Man-Month** (1975/1995):
  the tar pit; **Brooks' law**; the surgical team; **conceptual integrity** (aristocracy of
  design); the **second-system effect**; plan to throw one away; "No Silver Bullet" and its
  "Refired" retrospective. **McConnell, Code Complete** (2e 2004): construction — design
  in construction, classes, routines, defensive programming, variables, statements, code
  improvements (testing, debugging, refactoring, tuning), system considerations, craft.
  **Hunt & Thomas, The Pragmatic Programmer** (1999/2019): DRY, orthogonality, tracer
  bullets, prototypes, estimation, the basic tools, pragmatic paranoia (design by
  contract, assertions), bend or break (decoupling), concurrency, while you are coding
  (refactoring, testing), before the project, pragmatic projects. **Sommerville, Software
  Engineering** (10e): processes, agile, requirements, modelling, architecture, design and
  implementation, testing, evolution, dependability and security, systems engineering,
  configuration management, project management, quality, planning.
- **Courses**: Berkeley **CS169** (SaaS, agile, open lectures); MIT **6.102** (Software
  Construction — safe from bugs, easy to understand, ready for change; specifications,
  testing, ADTs, immutability, concurrency, in TypeScript); CMU **17-313** (Foundations of
  SE — process, requirements, architecture, QA, teamwork, open-source projects; open);
  UW CSE403; Georgia Tech CS3300 (team project).
- **Seminal**: Brooks 1986 (**No Silver Bullet** — read: essential difficulties are
  **complexity** (no two parts alike; scaling up is non-linear), **conformity** (to arbitrary
  institutions and interfaces), **changeability** (software is embedded in a changing
  cultural matrix), **invisibility** (no geometric representation); past breakthroughs —
  high-level languages, time-sharing, unified environments — attacked accidents; hopes —
  Ada, OOP, AI, expert systems, automatic programming, graphical programming, verification,
  environments, workstations — each examined; attacks on essence: buy vs build, requirements
  refinement and rapid prototyping, incremental development "grow, don't build", great
  designers); Parnas 1971/72 (**On the criteria to be used in decomposing systems into
  modules** — read: the KWIC index example decomposed conventionally by processing step vs
  unconventionally by design decision; "the unconventional decompositions have distinct
  advantages"; each module hides a design decision likely to change — **information
  hiding**; the efficiency objection and its answer); Royce 1970 (the waterfall diagram —
  and the text explaining why it fails without iteration and prototypes); **Agile Manifesto**
  2001 (individuals and interactions, working software, customer collaboration,
  responding to change; twelve principles read: early and continuous delivery, welcome
  changing requirements, frequent delivery, daily collaboration, motivated individuals,
  face-to-face conversation, working software as the measure of progress, sustainable
  pace, technical excellence, simplicity, self-organizing teams, regular reflection);
  Conway 1968 (**Conway's law**); Lehman 1980 (**laws of software evolution**: continuing
  change, increasing complexity, self-regulation, conservation of organizational
  stability and familiarity, continuing growth, declining quality, feedback system);
  Boehm 1988 (**spiral model**: risk-driven cycles of objectives, alternatives, evaluation,
  planning; also COCOMO estimation); DeMarco & Lister 1987 (**Peopleware**: flow, office
  environment, team jelling, the "furniture police").

## Key ideas → pages
[[software-engineering-fundamentals]], [[modularity-and-information-hiding]],
[[technical-debt-and-maintenance]]; the Parnas paper has its own page [[parnas-1972-criteria]] (§2.5), as do [[solid-principles]], [[gof-design-patterns]] and [[fowler-refactoring]]; existing: [[code-review]], [[refactoring]],
[[unit-testing]], [[debugging]], [[design-patterns-catalog]], [[git-data-model]],
[[build-systems-and-make]].

## What they add
SWE at Google for the modern institutional view (time, scale, trade-offs; the tooling that
makes a monorepo of 2 B lines work); Brooks for the two papers everyone cites and few read
(the essence/accident distinction still sorts hype); Parnas for the one design idea that
matters most; the Agile principles as written rather than as practised; Lehman and Conway
for the sociological laws that explain why systems rot and mirror their org charts.
