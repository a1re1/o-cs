---
title: The Rust Programming Language (Klabnik & Nichols) and Stanford CS110L
type: source
section: "2.3"
level: 200
tags: [rust, ownership, borrowing, lifetimes, traits, generics, enums, pattern-matching, error-handling, smart-pointers, concurrency, memory-safety, unsafe]
sources: []
authors: [Steve Klabnik, Carol Nichols, Ryan Eberhardt, Armin Namavari]
year: 2024
institution: Rust Project / Stanford
url: https://doc.rust-lang.org/book/
license: MIT
format: html
summary: The official free Rust book — ownership, borrowing and slices; structs, enums and match; collections; Result/Option error handling; generics, traits and lifetimes; tests; closures and iterators; smart pointers (Box, Rc, RefCell); fearless concurrency; async; OOP features; patterns; advanced/unsafe — paired with Stanford CS110L "Safety in Systems Programming", which uses Rust to teach memory safety, error handling, multiprocessing, and networking pitfalls.
---
# The Rust Programming Language / CS110L

## What it is
Book chapters: 1 getting started; 2 guessing game; 3 common concepts; **4 ownership** (what is
ownership, references and borrowing, slices); 5 structs; 6 enums and pattern matching; 7 packages,
crates, modules; 8 collections (Vec, String, HashMap); 9 error handling (panic vs Result); 10 generic
types, traits, lifetimes; 11 tests; 12 a CLI project; 13 functional features (closures, iterators);
14 cargo; 15 smart pointers (Box, Deref, Drop, Rc, RefCell, reference cycles); 16 fearless concurrency
(threads, message passing, shared state, Send/Sync); 17 async; 18 OOP features (trait objects);
19 patterns; 20 advanced (unsafe, advanced traits/types/functions, macros); 21 a web server.
CS110L (Spring 2020, open lectures/notes): memory safety, error handling, object-oriented Rust,
traits and generics, smart pointers, pitfalls in multiprocessing, multithreading, channels, networking,
information security — motivated by how C programs fail.

## Key ideas → pages
- Ownership: each value has one owner; drop at scope end; move semantics; **borrowing rules** — any
  number of shared `&T` *or* one `&mut T`, never both, and references must not outlive their referent;
  the compiler enforces at zero runtime cost — [[ownership-and-borrowing]].
- Stack vs heap made explicit (the book's restaurant analogy): fixed-size values on the stack,
  `String`/`Vec` own heap buffers — [[memory-layout-stack-heap]].
- Enums + `match` as algebraic data types with exhaustiveness; `Option<T>` replaces null;
  `Result<T, E>` with `?` replaces exceptions — [[algebraic-data-types]], [[error-handling-strategies]].
- Traits (typeclasses) and generics with monomorphization; trait objects (`dyn`) for dynamic dispatch;
  lifetimes as the type-level form of "who outlives whom" — [[rust-traits-generics-lifetimes]].
- Smart pointers as ownership patterns: `Box` (heap), `Rc` (shared ownership), `RefCell` (runtime
  borrow checking, interior mutability), `Arc<Mutex<T>>` for threads; `Send`/`Sync` make data races a
  compile error — [[ownership-and-borrowing]], [[synchronization-primitives]].
- CS110L's framing: the classes of C bugs (dangling pointers, double free, buffer overflow, data race)
  map one-to-one onto Rust rules — [[memory-safety-and-buffer-overflows]], [[undefined-behavior]].

## What it adds
The "third approach" to memory management (neither GC nor manual) and the vocabulary for reasoning
about aliasing and lifetimes that transfers back to C/C++ ([[csapp-15-213]]).
