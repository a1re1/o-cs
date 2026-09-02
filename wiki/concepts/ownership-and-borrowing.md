---
title: Ownership, borrowing, and lifetimes (Rust's memory model)
type: concept
section: "2.3"
level: 300
tags: [ownership, borrowing, borrow-checker, lifetimes, move-semantics, references, mutable-aliasing, raii, drop, smart-pointers, box, rc, refcell, arc, mutex, interior-mutability, send-sync, memory-safety]
sources: [rust-book, csapp-15-213]
summary: Every value has exactly one owner and is dropped when the owner goes out of scope; assignment moves (or copies for Copy types); you may hold many shared references or one mutable reference, never both, and no reference may outlive its referent — rules the compiler checks statically, eliminating use-after-free, double free, dangling pointers and data races at zero runtime cost; Box/Rc/RefCell/Arc/Mutex are the escape hatches that keep the guarantees.
---
# Ownership and borrowing

**In one sentence.** Rust replaces "remember to free, and never alias a mutable buffer" with three
compiler-checked rules: one owner, drop at scope end, and *aliasing XOR mutability*.

## Ownership (Rust Book ch. 4.1)
- Each value has one owner variable; when the owner leaves scope, `drop` runs (RAII: files close,
  locks release, memory frees) — deterministic, no GC, no manual `free`.
- `let b = a;` **moves** heap-owning values (`String`, `Vec`, `Box`): `a` is invalid afterwards
  (compile error to use it — the C double-free becomes impossible). `Copy` types (integers, `&T`,
  small plain structs) are duplicated instead. `.clone()` for an explicit deep copy.
- Passing to a function moves (or copies); returning transfers ownership back. Design consequence:
  functions borrow unless they need to own.

## Borrowing (ch. 4.2–4.3)
- `&T` shared reference: read-only, any number at once. `&mut T`: exactly one, no `&T` alive
  concurrently. The borrow ends at the last use (non-lexical lifetimes).
- References are never null and never dangle: the compiler rejects returning `&local` or holding a
  reference into a `Vec` across a `push` (which may reallocate) — the iterator-invalidation bug class.
- Slices `&s[a..b]`, `&[T]`, `&str` are (pointer, length) borrows — bounds-checked views.
- **Lifetimes** `'a` name how long a borrow lasts; mostly inferred (elision rules); written when a
  function returns a reference derived from one of several inputs (`fn longest<'a>(x: &'a str, y: &'a
  str) -> &'a str`) or when a struct holds a reference. `'static` = whole program. Lifetimes are
  *checked*, never affect codegen.

## Escape hatches that keep safety (ch. 15–16)
| Type | Gives you | Cost |
|---|---|---|
| `Box<T>` | heap allocation, recursive types, trait objects | one allocation |
| `Rc<T>` | shared ownership (refcount) in one thread | count inc/dec; cycles leak (use `Weak`) |
| `RefCell<T>` / `Cell<T>` | interior mutability with **runtime** borrow checking (panic on violation) | flag check |
| `Arc<T>` | thread-safe shared ownership | atomic refcount |
| `Mutex<T>` / `RwLock<T>` | mutation across threads; the data lives *inside* the lock, so you can't forget to lock | lock |
| `unsafe` | raw pointers, FFI, hand-verified invariants | you carry the proof ([[undefined-behavior]]) |
`Send`/`Sync` marker traits make "this type may cross threads" part of the type; data races are
compile errors ("fearless concurrency" — [[synchronization-primitives]]).

## How to think when the borrow checker complains
1. Who owns this data, and for how long? Often the fix is to own (`String` not `&str` in a struct) or to
   return owned values.
2. Am I trying to mutate while iterating/holding a view? Collect indices, or split borrows
   (`split_at_mut`), or restructure.
3. Do two parts of a struct need independent mutable access? Borrow fields separately, not `&mut self`.
4. Shared mutable state across owners? `Rc<RefCell<T>>` (single thread) or `Arc<Mutex<T>>`.
5. Lifetime error on a returned reference: the output can only live as long as the shortest input it
   comes from — or clone.

## Why it matters beyond Rust
The rules are the *correct discipline* for C/C++ too (a single owner per allocation, no mutable
aliasing) — Rust just enforces it; C++ approximates with `unique_ptr`/`shared_ptr`/RAII and
guidelines ([[pointers-and-memory]], [[memory-layout-stack-heap]]). Linear/affine types are the
theory ([[type-systems]]).

## Related
- [[memory-layout-stack-heap]], [[undefined-behavior]], [[memory-safety-and-buffer-overflows]],
  [[rust-traits-generics-lifetimes]], [[synchronization-primitives]], [[type-systems]].

## Sources
Rust Book ch. 4, 10.3, 15, 16; CS110L lectures 2, 6.
