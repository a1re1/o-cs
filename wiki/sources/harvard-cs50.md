---
title: Harvard CS50 Introduction to Computer Science
type: source
section: "2.1"
level: 100
tags: [cs50, c, python, sql, memory, pointers, data-structures, web, javascript, html, flask]
sources: []
authors: [David J. Malan]
year: 2025
institution: Harvard
url: https://cs50.harvard.edu/x/
license: CC-BY-NC-SA
format: html
summary: The most-taken intro course (CS50x on edX; lectures, notes, problem sets, and an autograder all open) — Scratch, then C (types, control, arrays, algorithms, memory and pointers, data structures), then Python, SQL, HTML/CSS/JavaScript, Flask, cybersecurity — with sibling courses CS50P (Python), CS50 AI, CS50 Web, CS50 SQL, CS50 Cybersecurity.
---
# Harvard CS50

## What it is
Weeks: 0 Scratch; 1 C (compilation, types, loops, `printf`); 2 Arrays (strings, command-line args,
cryptography pset); 3 Algorithms (linear/binary search, bubble/selection/merge sort, big-O,
recursion); 4 Memory (hexadecimal, pointers, `malloc`, buffer overflows, file I/O, images pset);
5 Data structures (linked lists, trees, hash tables, tries — the speller pset); 6 Python; 7 SQL
(schemas, joins, indexes, race conditions); 8 HTML/CSS/JavaScript; 9 Flask (sessions, cookies);
10 Cybersecurity/ethics; final project. Everything is graded by `check50`/`submit50` in a browser IDE.

## Key ideas → pages
- Learning C first exposes what higher-level languages hide: memory layout, pointers, `malloc/free`,
  undefined behaviour — [[pointers-and-memory]] (§2.3).
- The algorithms week is the gentlest first exposure to [[asymptotic-notation]], [[sorting]] and
  [[binary-search]].
- Data structures week builds [[hash-tables]] and tries by hand for a spell checker.
- The Python/SQL/web weeks show the same ideas in a dynamic language — [[recursion-and-iteration]],
  [[relational-model]].

## What it adds
Breadth and a "C first, then Python" contrast; less depth than [[sicp]]/[[composing-programs]] on
abstraction, more on how the machine works. CS50P/CS50 SQL/CS50 AI are natural next steps.
