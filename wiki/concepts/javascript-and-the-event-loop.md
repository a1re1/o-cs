---
title: JavaScript and the event loop — the language essentials (values and coercion, scope and closures, `this` and prototypes, classes as sugar, modules, iterators/generators, destructuring), why JavaScript is single-threaded and how the event loop schedules callbacks (call stack, task queue, microtasks for promises, rendering between tasks), callbacks → promises → async/await, error handling in async code, timers and `requestAnimationFrame`, Web Workers for parallelism, Node.js (libuv, streams, npm), TypeScript's structural type system and gradual typing, and the tooling (bundlers, transpilers, linters, package management)
type: concept
section: "7.5"
level: 200
tags: [javascript, ecmascript, es6, values, types, coercion, truthy-falsy, equality, scope, hoisting, let-const, closures, this, call-apply-bind, arrow-functions, prototypes, prototype-chain, classes, modules, esm, commonjs, import-export, iterators, generators, destructuring, spread, event-loop, single-threaded, call-stack, task-queue, macrotasks, microtasks, promise-jobs, rendering, run-to-completion, callbacks, callback-hell, promises, then-chaining, async-await, error-handling, try-catch, unhandled-rejection, settimeout, requestanimationframe, web-workers, workers, sharedarraybuffer, nodejs, libuv, streams, npm, package-json, typescript, structural-typing, gradual-typing, generics, type-narrowing, strict-mode, bundlers, vite, webpack, esbuild, transpilers, babel, eslint, prettier, deno, bun]
sources: [web-development-texts-courses-and-seminal-papers]
summary: JavaScript is a dynamically typed, prototype-based, first-class-functions language with a few things you must know cold — values are primitives (number, bigint, string, boolean, undefined, null, symbol) or objects (references), `==` coerces and `===` doesn't, `let`/`const` are block-scoped while `var` hoists, closures capture variables (not values) from their defining scope and are the mechanism behind callbacks, modules and private state, `this` is bound by how a function is called (method call, plain call, `call/apply/bind`, `new`) except arrow functions which inherit it lexically, objects delegate lookups up a prototype chain that `class` syntax merely sugars, and ES modules give static imports/exports — and one thing you must understand deeply: a JavaScript runtime executes on a single thread with a run-to-completion event loop that pops a task from the queue, runs it on the call stack to completion, drains all microtasks (promise reactions, queueMicrotask, MutationObserver) before doing anything else, and then may render, so a long synchronous task freezes the UI, a resolved promise's `.then` always runs after the current synchronous code but before any timer, and ordering puzzles (`setTimeout(…,0)` vs `Promise.resolve().then` vs `await`) resolve by asking "task or microtask?"; asynchronous code evolved from callbacks (inversion of control, the pyramid of doom) to promises (a value that will be available, chained with `then`, errors propagated to `catch`, combined with `all/allSettled/race/any`) to `async`/`await` (sequential-looking code that suspends at each `await` and resumes as a microtask; forgetting `await` or awaiting in a loop when you meant `Promise.all` are the classic bugs); real parallelism comes only from Web Workers/worker threads communicating by messages (and SharedArrayBuffer with Atomics); Node.js runs the same engine with libuv's event loop and thread pool for I/O, a stream API for backpressure, and npm's package ecosystem; TypeScript adds a structural, gradual static type system (interfaces, unions, generics, narrowing, `unknown` over `any`) that removes whole classes of bugs at compile time and is compiled away; and the toolchain — bundlers (Vite/esbuild/webpack), transpilers (Babel/tsc), linters and formatters (ESLint, Prettier), lockfiles — is what turns source into what ships.
---
# JavaScript and the event loop

**In one sentence.** JavaScript is a small, quirky, closure-and-prototype language whose
whole concurrency model is "one thread, one queue, run each task to completion, drain
microtasks, maybe render" — learn that loop and the async puzzles, the UI freezes, and
the ordering bugs all become predictable.

## The language, minimum viable mental model (Eloquent JS ch. 1–6, 10–11; YDKJS)
**Values**: primitives — `number` (IEEE 754 double: `0.1 + 0.2 !== 0.3`, `NaN !== NaN`,
safe integers to 2⁵³ — [[floating-point]]), `bigint`, `string` (UTF-16 code units —
`'😀'.length === 2`), `boolean`, `undefined`, `null`, `symbol` — copied by value; objects
(incl. arrays, functions, Map/Set, Date) by reference. **Coercion**: `==` converts
(`'' == 0`, `null == undefined`, `[] == false`) — use `===`; truthy/falsy (`0 '' null
undefined NaN false` are falsy; `[]` and `{}` truthy); `+` concatenates if either side is a
string; `typeof null === 'object'` (historical bug). **Scope**: `let`/`const` block-scoped
with a temporal dead zone; `var` function-scoped and hoisted; functions hoisted whole;
use `'use strict'`/modules (strict by default) to forbid implicit globals. **Closures**:
a function keeps a live reference to the variables of the scope it was created in — the
`for (var i…) setTimeout(() => log(i))` bug prints the final `i` because one `i` is shared;
`let` makes one per iteration; closures implement private state, memoization, callbacks,
modules ([[higher-order-functions]]). **`this`**: determined at call time — `obj.m()` →
`obj`; plain `f()` → `undefined` in strict mode; `f.call(x)`/`bind`; `new F()` → the new
object; **arrow functions** have no own `this`/`arguments` (lexical) — so use arrows for
callbacks inside methods, and never as methods themselves. **Prototypes**: property lookup
walks `obj → Object.getPrototypeOf(obj) → …`; `class` syntax (constructor, methods on the
prototype, `extends`, `super`, `static`, `#private`) is sugar over this; prefer
composition and plain objects where a class adds nothing ([[inheritance-vs-composition]]).
**Modules** (ESM): `import {x} from './m.js'`, `export default`, static and hoisted,
live bindings, top-level `await`; CommonJS (`require`) in older Node. **Iteration**:
`for…of` over iterables (protocol: `[Symbol.iterator]()` → `{next()}`), generators
(`function*`, `yield`, lazy sequences — [[streams-and-lazy-evaluation]]), spread `...`,
destructuring `const {a, b: [c]} = o`, optional chaining `a?.b`, nullish `??`. Arrays:
`map/filter/reduce/find/some/flatMap`, sort is lexicographic by default (`[10,9].sort()`
→ `[10, 9]`), mutating vs non-mutating methods (`toSorted`). Regular expressions
([[text-processing-and-regex]]); `JSON.parse/stringify`; `Intl` for dates/numbers.

## The event loop: why is JavaScript single-threaded and what runs when? (HTML spec "event loops"; Eloquent JS ch. 11)
```
loop:
  task = taskQueue.dequeue()          # macrotask: script, event callback, setTimeout, I/O, message
  run(task)                           # on the call stack, to completion — nothing preempts it
  while microtaskQueue: run(microtaskQueue.dequeue())   # promise reactions, queueMicrotask, MutationObserver
  if time to render: run rAF callbacks; style; layout; paint   # ~60 Hz, only between tasks
```
Consequences: (1) **run-to-completion** — no data races within JS, but a 200 ms
synchronous loop freezes input and rendering (the 50 ms "long task" budget); (2)
**microtasks drain fully before the next task or render**, so a promise chain that keeps
enqueueing microtasks starves rendering just like a sync loop; (3) ordering:
`console.log(1); setTimeout(()=>log(2)); Promise.resolve().then(()=>log(3)); log(4)` →
`1 4 3 2`; an `await` splits the function — everything after it is a microtask
continuation; (4) `setTimeout(f, 0)` means "after the current task, microtasks, and
possibly a render, and clamped to ≥ 4 ms when nested" — not "immediately"; (5)
`requestAnimationFrame` runs before the next paint (use for visual updates), `requestIdleCallback`
in idle time, `setInterval` drifts; (6) `await` in a loop serializes (`for (const u of
urls) await fetch(u)`) — use `Promise.all(urls.map(fetch))` for concurrency, and
`allSettled` when failures shouldn't cancel. Node's loop (libuv) adds phases (timers →
pending I/O → poll → check `setImmediate` → close) and `process.nextTick` (before
microtasks). Real parallelism: **Web Workers** / Node `worker_threads` — separate
threads with their own loops, communicating by `postMessage` (structured clone) or
`SharedArrayBuffer` + `Atomics` ([[processes-and-threads]]); offload CPU work there;
service workers intercept network for offline/PWA ([[web-performance-and-browser-networking]]).

## Async patterns: callbacks → promises → async/await (Eloquent JS ch. 11)
**Callbacks** (`fs.readFile(p, (err, data) => …)`, Node's error-first convention): invert
control, nest into the pyramid of doom, and make error handling ad hoc. **Promise**: an
object in state pending → fulfilled(value) | rejected(reason), settled once; `p.then(onF,
onR)` returns a new promise (chain; return a value or a promise from `then`);
`catch` = `then(undefined, onR)`; `finally`; rejections propagate down the chain until
caught; `Promise.all` (fail-fast), `allSettled`, `race` (first settles — timeouts),
`any` (first fulfils); create with `new Promise((resolve, reject) => …)` only to wrap
callback APIs (`util.promisify`); never nest `then` inside `then`. **`async` functions**
always return a promise; `await` suspends, unwraps or throws; use `try/catch/finally`
around awaits; **unhandled rejections** crash Node ≥ 15 and are logged in browsers —
always terminate chains with a handler; **forgotten `await`** → the promise is created,
the error escapes, and the code continues (lint rule `no-floating-promises`).
**Cancellation**: `AbortController` + `signal` for `fetch` and custom async work;
timeouts via `AbortSignal.timeout(ms)`. **Async iteration**: `for await (const chunk of
stream)`; async generators. Streams (Node `Readable/Writable/Transform`, Web Streams)
carry **backpressure** — `pipe`/`pipeline` handle it; don't buffer whole files. `fetch`
returns after headers (`await res.json()` for the body); check `res.ok` (4xx/5xx don't
reject) — [[dns-http-and-the-web-stack]].

## Node.js, TypeScript, tooling (Full Stack Open parts 3, 9; Node docs; TS handbook)
**Node**: V8 + libuv (event loop, thread pool for fs/DNS/crypto), non-blocking I/O suits
I/O-bound servers; `http`, `fs/promises`, `path`, `events`, `stream`, `child_process`;
Express/Fastify/Hono for HTTP ([[web-backends-sessions-and-authentication]]); `npm`/`pnpm`
with `package.json` (dependencies vs devDependencies, semver ranges `^1.2.3`), **lockfiles**
for reproducibility, `npm audit` and supply-chain caution (typosquatting, install scripts —
[[security-principles]]); Deno and Bun as alternative runtimes (TS-native, permissions).
**TypeScript**: a superset compiled to JS; **structural** typing (shape compatibility, not
nominal), type inference, `interface`/`type`, union `A | B` and literal types, **narrowing**
by `typeof`/`in`/discriminated unions (`kind: 'circle'`), generics `<T>` with constraints,
utility types (`Partial`, `Pick`, `Record`), `unknown` (must narrow) vs `any` (opts out —
avoid), `strict: true`, `readonly`, template literal types; types are erased — validate
external data at runtime (zod/valibot) since a type is not a check
([[type-systems]] — gradual typing). **Toolchain**: bundlers (**Vite** — dev server with
native ESM, Rollup/esbuild for production; webpack; esbuild; Parcel) resolve modules,
tree-shake, code-split, hash filenames; transpilers (Babel/`tsc`/SWC) for syntax
targets; **ESLint** (+ typescript-eslint; catch floating promises, unused vars) and
**Prettier**; test runners (Vitest/Jest, Playwright — [[unit-testing]]); source maps;
`browserslist` targets and polyfills. Language evolution via TC39 stages (ES2015+ yearly).

## Pitfalls
- `==`, `var`, `this` in a detached method (`const f = obj.m; f()`), arrow methods.
- Sync CPU work on the main thread; microtask storms; `await` in loops.
- Floating promises; `catch` that swallows; throwing non-`Error`s.
- Trusting TypeScript types for data from the network; `any` everywhere.
- `Array.sort` without a comparator; mutating shared arrays/objects passed by reference;
  `parseInt` without a radix (mostly fixed) and `Number('')` → 0.

## Related
- [[html-css-and-the-dom]], [[frontend-frameworks-and-state-management]],
  [[web-backends-sessions-and-authentication]], [[web-performance-and-browser-networking]],
  [[higher-order-functions]], [[streams-and-lazy-evaluation]], [[type-systems]],
  [[processes-and-threads]], [[floating-point]], [[text-processing-and-regex]],
  [[inheritance-vs-composition]], [[dns-http-and-the-web-stack]], [[unit-testing]].

## Sources
Haverbeke 2024 (Eloquent JS 4e; contents read) ch. 1–6, 10–11, 13, 20; Simpson, *You Don't Know JS Yet* (Scope & Closures; Objects & Classes; Sync & Async); WHATWG HTML Standard §8.1 "Event loops"; Roberts 2014 ("What the heck is the event loop anyway?"); Archibald 2015 ("Tasks, microtasks, queues and schedules"); Node.js documentation ("The Node.js Event Loop"); Full Stack Open parts 3, 9 (read: outline); TypeScript Handbook; Ecma-262 (ES2024).
