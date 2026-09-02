---
title: Frontend frameworks and state management — why frameworks (imperative DOM mutation vs declarative UI = f(state)), React's model (components, JSX, props down/events up, virtual DOM and reconciliation with keys, hooks — useState/useEffect/useMemo — and the rules behind them, controlled inputs, lifting state), alternatives (Vue's reactivity, Svelte/SolidJS compiled fine-grained signals, Angular), state management (local vs server vs URL vs global; Redux/Flux, context, stores, React Query/SWR and caching server state), routing and SPA vs MPA, server-side rendering, hydration, islands and server components, forms and data fetching, testing components, and choosing a framework
type: concept
section: "7.5"
level: 300
tags: [frontend-frameworks, react, jsx, components, props, state, unidirectional-data-flow, declarative-ui, ui-equals-f-of-state, virtual-dom, reconciliation, diffing, keys, hooks, usestate, useeffect, usememo, usecallback, useref, rules-of-hooks, effects, dependencies, stale-closures, controlled-components, lifting-state-up, composition, render-props, context, redux, flux, reducers, actions, immutability, zustand, mobx, signals, solidjs, svelte, vue, reactivity, angular, server-state, react-query, tanstack-query, swr, caching, stale-while-revalidate, url-state, routing, client-side-routing, react-router, spa, mpa, ssr, server-side-rendering, ssg, hydration, islands, astro, server-components, rsc, nextjs, remix, forms, data-fetching, suspense, testing-library, playwright, bundle-size, choosing-a-framework, htmx, web-components]
sources: [web-development-texts-courses-and-seminal-papers]
summary: Frameworks exist because keeping a hand-mutated DOM consistent with application state does not scale — the declarative alternative is UI = f(state): describe what the screen should look like for a given state, and let the framework compute the minimal DOM changes when state changes; React does this with components (functions from props to a tree of elements written in JSX), unidirectional data flow (props down, callbacks up), a virtual DOM that is diffed against the previous render — reconciliation, which needs stable keys on lists to match elements across renders — and hooks that give function components state (useState), side effects synchronized with rendering (useEffect with a dependency array, cleanup on unmount, the source of most React bugs via stale closures and missing deps), memoization (useMemo/useCallback for expensive work or referential stability), and refs (escape hatches to DOM nodes and mutable values), under the rule that hooks are called unconditionally in the same order; Vue, Svelte and SolidJS achieve the same declarative model with fine-grained reactivity (signals that track which computations read them, so updates skip diffing) and Svelte compiles components to direct DOM code; state is best classified before choosing a tool — local UI state stays in components, server state (data from APIs) belongs in a cache with stale-while-revalidate and invalidation (React Query/SWR), URL state in the router, and only genuinely global client state in a store (Redux with reducers over immutable state, or lighter stores like Zustand, or React context for rarely changing values); rendering strategy is its own axis — client-side SPA (fast navigation, empty first paint, SEO and JS-weight costs), multi-page apps and server-side rendering (HTML first, then hydration to attach handlers — expensive when the whole page hydrates), static generation, islands (hydrate only interactive parts) and React Server Components (components that run only on the server, shipping no JS) as the current synthesis in Next.js/Remix/Astro; forms, data fetching with Suspense, client routing, component testing (Testing Library for behaviour, Playwright end-to-end) round out the stack; and the honest framework choice weighs team knowledge, ecosystem, bundle size and how much interactivity the page really has — a content site may want no framework at all.
---
# Frontend frameworks and state management

**In one sentence.** Stop mutating the DOM by hand: express the UI as a function of
state, let the framework reconcile the difference when state changes, keep each kind of
state where it belongs (component, server cache, URL, store), and pick a rendering
strategy — client, server, static, islands — by what the page actually needs.

## Why frameworks: UI = f(state) (React docs "Thinking in React"; Garrett 2005)
Ajax made pages into applications ([[javascript-and-the-event-loop]]); jQuery-era code
updated the DOM imperatively from many event handlers, and state lived in the DOM —
every new feature multiplied the transitions to keep consistent. **Declarative UI**: the
view is a pure function of state; on change, re-render conceptually from scratch and let
the framework apply the minimal mutations. Benefits: one source of truth, testable
render logic, composition of **components** (self-contained units with props, local
state, and a rendered subtree), predictable data flow. React (2013), Vue (2014),
Angular (2016 rewrite), Svelte (2016), SolidJS (2021) all share this; they differ in
how change is detected (virtual-DOM diffing vs compiled fine-grained reactivity) and how
much they prescribe.

## React's model (React docs; Full Stack Open parts 1, 2, 5)
- **Components and JSX**: `function Card({title, children}) { return <section
  className="card"><h2>{title}</h2>{children}</section> }` — JSX compiles to
  `createElement` calls producing **elements** (plain objects); components must be pure
  in render (no side effects, same output for same props/state).
- **Data flow**: **props down, events up** — a parent passes data and callbacks; a child
  calls `onChange(value)`; to share state between siblings, **lift it up** to the common
  ancestor; **composition** (`children`, slots) over inheritance; **context** for values
  many descendants need (theme, auth user) — not for high-frequency updates.
- **State**: `const [count, setCount] = useState(0)`; setting state schedules a
  re-render (batched); state is **immutable** — create new objects/arrays
  (`setItems([...items, x])`), never mutate; updater form `setCount(c => c + 1)` when
  depending on the previous value; derive, don't duplicate (compute `total` from `items`
  in render rather than storing both).
- **Reconciliation**: the virtual DOM is diffed with heuristics — different element type
  → rebuild subtree; same type → update props; lists matched by **`key`** (stable ids,
  never array index for reorderable lists — wrong keys cause state to stick to the wrong
  item). Re-render cost is the tree walk, not DOM mutation; optimize with `memo`,
  `useMemo`, `useCallback` only when measured (React Compiler automates much of this).
- **Effects**: `useEffect(() => { const id = subscribe(); return () => unsubscribe(id) },
  [dep])` synchronizes with external systems (subscriptions, timers, manual DOM,
  logging) after paint; the dependency array must list every reactive value used
  (**stale closure** bugs when it doesn't; `eslint-plugin-react-hooks` enforces); cleanup
  runs before re-run and on unmount; Strict Mode double-invokes in dev to expose impure
  effects. Effects are **not** for deriving state or handling events — "you might not need
  an effect". Data fetching in effects needs cancellation/race handling; prefer a data
  library (below) or framework loaders.
- **Rules of hooks**: call at the top level, same order every render, only from
  components/custom hooks — because hooks are stored by call index. **Custom hooks**
  (`useLocalStorage`, `useDebounce`) extract stateful logic. `useRef` for mutable values
  that don't trigger renders and for DOM nodes; `useReducer` for complex local state
  transitions; `useId`, `useTransition`/`useDeferredValue` for concurrent rendering
  (keep input responsive while a heavy render proceeds); **Suspense** for loading states
  of lazy components and data.
- **Controlled inputs**: `value={text} onChange={e => setText(e.target.value)}` — state is
  the source of truth; uncontrolled (`defaultValue` + ref) for simple forms; form
  libraries (React Hook Form) and schema validation (zod) for real ones.

## Alternatives: reactivity and compilation (Vue, Svelte, SolidJS, Angular)
**Fine-grained reactivity / signals**: `const count = signal(0)`; a computation that reads
`count()` is subscribed; setting `count` re-runs only those computations and updates
only those DOM nodes — no diff, no component re-render (SolidJS, Vue's `ref/reactive`
via proxies, Preact Signals, Angular signals, Svelte 5 runes); the trade-off is that
reactivity must track reads (proxies/compilation) and components run once. **Svelte**
compiles components to imperative DOM updates (small bundles, no runtime VDOM). **Vue**
offers templates + SFCs with a gentle curve and both Options/Composition APIs.
**Angular**: batteries-included (DI, router, forms, RxJS), TypeScript-first, suited to
large enterprise teams. **htmx**/Hotwire: server renders HTML fragments, attributes
declare swaps — the "HTML over the wire" counter-movement for CRUD apps. **Web components**
([[html-css-and-the-dom]]) for framework-agnostic design systems (Lit). Bundle cost:
React+ReactDOM ~45 kB gz, Preact ~4 kB, Svelte/Solid apps often smallest; measure
against your interactivity needs.

## State management: classify before you choose (Redux docs; TanStack Query)
1. **Local/UI state** (open/closed, input text): component state.
2. **Server state** (users, orders — owned by the backend, shared, async, stale):
   a **cache**, not a store — **React Query/TanStack Query** or **SWR**: `useQuery({queryKey:
   ['todos', id], queryFn})` handles loading/error, dedup, **stale-while-revalidate**,
   refetch on focus/reconnect, retries, pagination/infinite queries, **mutations** with
   invalidation or optimistic updates ([[scalable-system-design]] caching applied to
   the client). Most "global state" pain was server state in the wrong container.
3. **URL state** (page, filters, selected item): the router — shareable, back-button-
   friendly, survives reload.
4. **Global client state** (auth session, theme, cart draft, cross-cutting UI): a store —
   **Redux** (Flux: single immutable state tree; `dispatch(action)` → pure `reducer(state,
   action)` → new state; middleware/thunks/sagas for async; Redux Toolkit removes
   boilerplate; DevTools time-travel — predictable, verbose), **Zustand**/**Jotai**/**MobX**
   (smaller, less ceremony; MobX observable proxies), or **context + reducer** for small
   apps. Keep stores normalized (entities by id — [[relational-model]]), select
   minimal slices to avoid re-renders, and don't put server data in Redux unless you
   need offline/complex sync (then consider RTK Query or an offline-first sync engine —
   [[mobile-development-and-cross-platform]]).
Forms are their own state category (dirty/validation/submission); machines (XState) for
genuinely stateful flows (wizards, media players — [[finite-automata-and-regular-languages]]).

## Rendering strategies: SPA, SSR, SSG, islands, server components (Next.js/Remix/Astro docs)
- **SPA (client-side rendering)**: one HTML shell + JS bundle; client **router** swaps
  views without reloads (History API; nested routes, loaders, code-splitting per route);
  fast in-app navigation, offline-capable; costs: blank first paint until JS loads,
  SEO/social previews need extra work, large bundles, every user pays JS parse/execute
  ([[web-performance-and-browser-networking]]).
- **MPA / SSR**: server renders HTML per request (templates, or React `renderToString`/
  streaming); fast first paint and SEO; with a framework the client then **hydrates** —
  downloads the same components and attaches event handlers, re-running render on the
  client; hydration cost ≈ a full client render, and the page is visible but inert
  until it completes ("uncanny valley"); streaming SSR + selective hydration (React 18)
  mitigate.
- **SSG / ISR**: pre-render at build time (docs, marketing, blogs); revalidate
  incrementally.
- **Islands** (Astro, Fresh, Qwik's resumability): ship static HTML, hydrate only the
  interactive components (`client:visible`).
- **React Server Components** (Next.js App Router): components that run only on the
  server (direct DB/API access, no bundle cost), stream a serialized tree; `'use
  client'` marks interactive leaves; server actions for mutations; the current answer to
  "SSR + SPA without double data fetching", at the price of a new mental model (which
  code runs where) and framework lock-in. **Remix**/React Router: loaders/actions per
  route, progressive enhancement of forms (works without JS).
Choose: content-heavy → SSG/islands; app-like behind login → SPA or SSR+hydration;
mixed → RSC/Remix. Deploy edge/CDN for static, servers/serverless for SSR
([[cloud-and-serverless]], [[continuous-integration-and-delivery]]).

## Fetching, forms, testing
Data fetching: colocate with routes/components via loaders or query hooks; handle
loading, error, empty, and stale states explicitly (Suspense boundaries + error
boundaries); avoid waterfalls (fetch in parallel, prefetch on hover/route match);
optimistic UI with rollback; auth tokens via HttpOnly cookies rather than JS-readable
storage ([[web-backends-sessions-and-authentication]]). Testing: **Testing Library** (query
by role/label like a user; avoid testing implementation details), component tests in
Vitest/JSDOM or browser mode, **Playwright** for E2E, visual regression (Storybook +
Chromatic), MSW for API mocking ([[software-testing-fundamentals]]). Accessibility in
components: semantic elements, focus management on route change/modal open, ARIA only
as needed ([[html-css-and-the-dom]]).

## Pitfalls
- Index keys on reorderable lists; mutating state; deriving state into `useState` and
  syncing with effects; missing effect deps or disabling the lint rule.
- Server data in a global store with hand-rolled caching; global state for local UI.
- SPA for a content site (SEO, weight); full hydration of a mostly static page.
- Effects for data fetching without cancellation → race conditions on fast navigation.
- Premature `useMemo`/`useCallback` everywhere; or none and re-rendering the world.

## Related
- [[javascript-and-the-event-loop]], [[html-css-and-the-dom]],
  [[web-performance-and-browser-networking]], [[web-backends-sessions-and-authentication]],
  [[api-design]] (GraphQL/REST from the client), [[scalable-system-design]] (caching),
  [[mobile-development-and-cross-platform]] (React Native, offline-first),
  [[software-testing-fundamentals]], [[finite-automata-and-regular-languages]],
  [[relational-model]], [[cloud-and-serverless]], [[human-computer-interaction]].

## Sources
React documentation (react.dev: "Thinking in React", "You Might Not Need an Effect", "Rules of Hooks", "Reconciliation"); Full Stack Open parts 1–2, 5–7, 14 (read: outline); Garrett 2005; Abramov 2015–19 (Redux docs; "A Complete Guide to useEffect"); TanStack Query docs; Vue, Svelte, SolidJS docs (signals); Next.js App Router and React Server Components RFC (2020–23); Astro docs (islands); Miller 2020 ("Islands architecture"); Osmani 2019 ("Rendering on the Web").
