---
title: Design Patterns: Elements of Reusable Object-Oriented Software (Gamma, Helm, Johnson, Vlissides) and Head First Design Patterns
type: source
section: "2.5"
level: 300
tags: [design-patterns, gof, creational, structural, behavioral, strategy, observer, decorator, factory, singleton, command, adapter, facade, composite, iterator, state, visitor, template-method, proxy]
sources: []
authors: [Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides, Eric Freeman, Elisabeth Robson]
year: 1994
institution: IBM / Taligent / UIUC
url: https://en.wikipedia.org/wiki/Design_Patterns
license: proprietary
format: book
summary: The catalogue of 23 object-oriented patterns in three families (creational, structural, behavioral), each documented as intent/motivation/applicability/structure/participants/consequences, built on two principles — program to an interface, not an implementation; favor object composition over class inheritance — with Head First as the friendlier tutorial (Strategy, Observer, Decorator, Factory, Singleton, Command, Adapter/Facade, Template Method, Iterator/Composite, State, Proxy, Compound, MVC).
---
# Design Patterns (GoF) / Head First Design Patterns

## What it is
GoF ch. 1 introduction: what a pattern is (name, problem, solution, consequences); the catalogue;
how patterns solve design problems — finding appropriate objects, determining granularity,
specifying interfaces, *program to an interface not an implementation*, inheritance vs
composition ("favor object composition"), delegation, parameterized types, designing for change
(the causes of redesign each pattern addresses). Ch. 2 a case study (Lexi document editor).
Ch. 3 **creational**: Abstract Factory, Builder, Factory Method, Prototype, Singleton. Ch. 4
**structural**: Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy. Ch. 5
**behavioral**: Chain of Responsibility, Command, Interpreter, Iterator, Mediator, Memento,
Observer, State, Strategy, Template Method, Visitor. Head First adds the "design principles" as
slogans: encapsulate what varies; favor composition; program to interfaces; loosely coupled designs
(Observer); open for extension, closed for modification (Decorator); depend on abstractions
(Factory); principle of least knowledge (Facade); Hollywood principle (Template Method); single
responsibility (Iterator).

## What it adds
[[design-patterns-catalog]] (when each pattern earns its keep and what replaces it in FP/modern
languages), [[inheritance-vs-composition]], [[polymorphism-and-dispatch]] (Visitor = double
dispatch; Strategy = first-class function), [[solid-principles]].
