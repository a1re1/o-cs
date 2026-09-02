---
title: Design patterns — the GoF catalogue and when each earns its keep
type: concept
section: "2.5"
level: 300
tags: [design-patterns, strategy, observer, decorator, factory-method, abstract-factory, builder, singleton, adapter, facade, composite, proxy, command, iterator, state, visitor, template-method, mediator, memento, dependency-injection, anti-patterns]
sources: [gof-design-patterns, fowler-refactoring, cs3110-ocaml]
summary: A pattern is a named, reusable solution to a recurring design problem with known trade-offs; the GoF 23 split into creational (how objects are made), structural (how they are composed) and behavioral (how they interact), most of them are ways to vary one thing without touching the rest, and many collapse into a first-class function, a closure, an enum or a module in languages that have those — so know the intent, not just the class diagram.
---
# Design patterns

**In one sentence.** Patterns are vocabulary for "encapsulate what varies": each one isolates an
axis of change (algorithm, object creation, structure, notification) behind an interface.

## The catalogue, by intent
| Family | Pattern | Varies / hides | Modern equivalent |
|---|---|---|---|
| Creational | Factory Method / Abstract Factory | which concrete class is instantiated | a function returning an interface; DI container |
| | Builder | step-by-step construction of complex objects | fluent builders, keyword args, `Default` + struct update |
| | Prototype | cloning configured instances | `clone` |
| | Singleton | one instance, global access | module-level value; *usually an anti-pattern* (hidden global, hard to test) |
| Structural | Adapter | incompatible interface | wrapper / trait impl for foreign type |
| | Bridge | abstraction and implementation vary independently | interface + injected impl |
| | Composite | tree of parts treated uniformly | recursive [[algebraic-data-types]] |
| | Decorator | add responsibility dynamically | wrapper implementing same interface; middleware; higher-order function |
| | Facade | simplify a subsystem | a deep module ([[managing-complexity-in-software-design]]) |
| | Flyweight | share many fine-grained objects | interning |
| | Proxy | control access (lazy, remote, protected) | smart pointers, RPC stubs |
| Behavioral | Strategy | interchangeable algorithm | pass a function ([[higher-order-functions]]) |
| | Observer | notify dependents of change | events, callbacks, channels, reactive streams |
| | Command | request as an object (undo, queue, log) | closures; message types |
| | Template Method | skeleton with overridable steps | higher-order function with hooks |
| | Iterator | sequential access without exposing structure | language iterators/generators ([[streams-and-lazy-evaluation]]) |
| | State | behaviour changes with state | enum + match; typestate |
| | Visitor | new operation over a fixed class hierarchy (double dispatch) | pattern matching on an ADT ([[polymorphism-and-dispatch]]) |
| | Chain of Responsibility | handler chosen at runtime | middleware pipeline |
| | Mediator / Memento / Interpreter | centralize interaction / snapshot state / evaluate a language | event bus / persistent snapshot / [[interpreters-eval-apply]] |

## Principles behind them (GoF ch. 1, Head First)
Program to an interface, not an implementation; favor composition over inheritance
([[inheritance-vs-composition]]); encapsulate what varies; open for extension, closed for
modification ([[solid-principles]]). Every pattern names the *cause of redesign* it prevents:
creating an object by class name, dependence on specific operations/platform/representation,
algorithmic dependencies, tight coupling, extending by subclassing, inability to alter classes
conveniently.

## Using them well
- Start from the smell or the change you expect; introduce the pattern by refactoring toward it,
  not up front ([[refactoring]] "Replace Conditional with Polymorphism", "Replace Type Code with
  Subclasses/Strategy").
- Name the pattern in code (`XStrategy`, `YObserver`) only when it clarifies intent.
- In languages with closures, ADTs and modules, prefer the language feature — Peter Norvig's
  observation that 16 of the 23 are invisible or simpler in dynamic/functional languages.
- Anti-patterns: Singleton-as-global, pattern fever (AbstractFactoryFactory), Visitor when the set of
  cases changes more often than the operations (the [[data-abstraction]] expression problem).

## Related
- [[inheritance-vs-composition]], [[polymorphism-and-dispatch]], [[solid-principles]], [[refactoring]],
  [[higher-order-functions]], [[algebraic-data-types]], [[objects-and-classes]].

## Sources
GoF ch. 1, 3–5; Head First Design Patterns; CS3110 (variants replace Visitor).
