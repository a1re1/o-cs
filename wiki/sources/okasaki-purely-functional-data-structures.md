---
title: Purely Functional Data Structures (Okasaki, 1996 thesis / 1998 book)
type: source
section: "2.4"
level: 400
tags: [persistent-data-structures, functional-data-structures, amortized-analysis, bankers-method, physicists-method, lazy-evaluation, queues, deques, real-time, scheduling, lazy-rebuilding, numerical-representations, red-black-trees, leftist-heaps, binomial-heaps]
sources: []
authors: [Chris Okasaki]
year: 1996
institution: Carnegie Mellon
url: https://www.cs.cmu.edu/~rwh/students/okasaki.pdf
license: open-access
format: pdf
summary: Shows that efficient data structures need not be imperative — functional data structures are automatically persistent (old versions survive updates), amortized bounds break under persistence ("multiple futures") but can be restored with lazy evaluation and memoization, analyzed by the banker's and physicist's methods; scheduling makes bounds worst-case; plus lazy rebuilding, numerical representations, and bootstrapping.
---
# Purely Functional Data Structures

## What it is
Chapters: 1 introduction (functional vs imperative data structures — no destructive update, so all
versions persist; strict vs lazy evaluation); 2 lazy evaluation and `$`-notation (streams);
3 **amortization and persistence via lazy evaluation** — traditional amortization (banker's and
physicist's methods, batched queues with front/rear lists), the problem of multiple futures (an
expensive operation can be repeated on the same old version, breaking the credit argument), and
the reconciliation: suspend the expensive work with lazy evaluation and *memoize* it so every
future pays once; 4 eliminating amortization — scheduling forces suspensions incrementally
(real-time queues, worst-case O(1)); 5 lazy rebuilding (batched → global → lazy; deques); 6 numerical
representations (binary random-access lists, binomial heaps, skew binary numbers); 7 data-structural
bootstrapping; 8 implicit recursive slowdown; 9 conclusions. The book (1998) adds leftist heaps,
red-black trees, splay heaps, and Standard ML/Haskell code.

## Notable claims
- "Functional data structures are persistent for free" — but the classic amortized ones are *not*
  efficient under persistence until redesigned.
- Lazy evaluation + memoization is the essential ingredient for amortized functional structures;
  strict languages need explicit suspensions.
- Many imperative structures (queues, deques, heaps, random-access lists) have functional versions
  with the same asymptotics; arrays and union–find remain the hard cases.

## What it adds
[[persistent-data-structures]] and the persistence-aware [[amortized-analysis]]; the design
vocabulary behind immutable collections in Clojure, Scala, Haskell and Rust's `im`.
