---
title: Objects, classes, inheritance, and dispatch (basics)
type: concept
section: "2.1"
level: 100
tags: [objects, classes, oop, inheritance, dispatch, methods, attributes, polymorphism, composition, dispatch-dictionaries, self, dunder-methods]
sources: [composing-programs, sicp]
summary: An object bundles state with the operations on it and dispatches by name; classes are templates and inheritance shares behaviour; Composing Programs builds the whole system from dictionaries and closures to show that "object" is message passing plus local state — with composition, generic functions, and the rule to prefer interfaces over inheritance.
---
# Objects and classes (basics)

**In one sentence.** An object is local state ([[assignment-state-and-environments]]) plus a
dispatcher from message names to procedures (SICP's message passing); a class is the shared part of
that dispatcher; inheritance chains dispatchers.

## Mechanics (Composing Programs 2.5–2.7)
- Class statement creates a class object; calling it makes an instance and runs `__init__`.
- Attribute lookup: instance dict → class → superclasses (method resolution order). Methods are
  functions whose first parameter is bound to the instance (`self`); `obj.method(x)` is
  `Class.method(obj, x)`.
- Class attributes are shared; assigning `self.x` creates an instance attribute that shadows.
- Inheritance: `class B(A)` — B's namespace falls back to A's; `super()` continues the lookup.
  Multiple inheritance uses C3 linearization.
- Everything above can be built from dispatch dictionaries and closures — DeNero implements
  `make_class`, `make_instance`, `bind_method` — proving objects are a *pattern*, not magic.
- Dunder methods (`__repr__`, `__eq__`, `__add__`, `__iter__`) hook objects into the language's
  generic functions — Python's version of SICP's generic operations table ([[data-abstraction]]).

## Design guidance (previewing §2.5)
- **Composition over inheritance**: a `Stack` that *has* a list, not one that *is* a list.
- Inherit only for "is-a" with substitutable behaviour ([[liskov-substitution]]); otherwise use
  interfaces/protocols/duck typing.
- Keep state private-ish; expose operations. Small classes with one responsibility.
- Identity vs equality: define `__eq__`/`__hash__` together for value objects; leave identity semantics
  for entities.

## Pitfalls
- Mutable class attributes shared by all instances (`items = []` at class level).
- Deep inheritance hierarchies where behaviour is scattered across five files.
- Forgetting `self`; calling a method on the class without an instance.
- Overriding `__eq__` without `__hash__` makes objects unhashable.

## Related
- [[data-abstraction]], [[assignment-state-and-environments]], [[design-patterns]],
  [[liskov-substitution]], [[specifications-and-invariants]].

## Sources
Composing Programs 2.5–2.7, 2.9; SICP 2.4.3 (message passing), 3.1.
