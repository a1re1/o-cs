---
title: Lexing and parsing — regular tokens, context-free grammars, recursive descent, Pratt parsing, LL and LR
type: concept
section: "4.3"
level: 300
tags: [lexing, scanning, tokens, maximal-munch, parsing, context-free-grammar, ambiguity, precedence, associativity, recursive-descent, pratt-parser, precedence-climbing, ll1, first-follow, lr-parsing, lalr, shift-reduce, yacc, bison, antlr, parser-combinators, peg, error-recovery, ast]
sources: [crafting-interpreters, dragon-book-and-compiler-texts, cs6120-and-compiler-courses, compiler-seminal-papers]
summary: A scanner turns characters into tokens with regular expressions compiled to a DFA (longest match wins), and a parser turns tokens into a syntax tree according to a context-free grammar whose ambiguities are resolved by precedence and associativity; hand-written recursive descent (one function per nonterminal, LL(1) lookahead, Pratt/precedence-climbing for expressions, panic-mode error recovery) is what most production compilers use, while generated LR/LALR parsers (yacc/bison; Knuth's shift–reduce automaton) handle more grammars declaratively, and PEG/parser combinators trade guarantees for convenience.
---
# Lexing and parsing

**In one sentence.** Two levels of grammar: regular for words, context-free for sentences — and
for real compilers, recursive descent with a Pratt expression parser is the pragmatic answer.

## Scanning (Crafting Interpreters ch. 4, Dragon Book ch. 3)
Token = type + lexeme + literal value + position. Each token type is a regular expression;
the union compiles (Thompson NFA → subset-construction DFA → minimization) into a table or
hand-written `switch` on the first character. **Maximal munch**: take the longest match
(`>=` not `>` `=`); keywords vs identifiers by lookup after matching; handle nested comments,
string escapes, numbers, and Unicode; track line/column for errors. Lexer generators: lex/
flex, re2c; hand-written scanners are common and fast ([[finite-automata-and-regular-languages]],
[[text-processing-and-regex]]).

## Grammars (ch. 5–6, Dragon ch. 4)
Context-free grammar: productions `expr → expr "+" term | term`; derivations build a parse
tree; the **AST** drops punctuation and keeps structure ([[context-free-grammars]]).
**Ambiguity** (`1 - 2 - 3`, dangling else) is removed by encoding **precedence** as grammar
levels (equality → comparison → term → factor → unary → primary) and **associativity** by left/
right recursion — or by an operator table.

## Top-down: recursive descent (ch. 6)
One function per rule; `match`/`peek` on the token stream; **LL(1)**: choose the production by
one token of lookahead using FIRST/FOLLOW sets; left recursion must be rewritten to iteration.
**Pratt / precedence climbing** (clox ch. 17): each token has prefix and infix parse functions
and a binding power; `parsePrecedence(p)` parses a prefix, then loops absorbing infix operators
with power ≥ p — elegant for expressions with many operators, mixfix and user-defined operators.
**Error recovery**: report, enter panic mode, synchronize at statement boundaries; ensure no
cascade errors; production parsers (clang, rustc) also produce partial ASTs for IDEs.
Hand-written parsers dominate (GCC, clang, Go, rustc, V8) for control over errors and speed.

## Bottom-up: LR parsing (Knuth 1965, Dragon 4.5–4.7)
Shift tokens onto a stack, reduce when a handle (right-hand side) is on top; a DFA over LR
items decides; LR(0) → SLR → LALR(1) (yacc/bison — compact tables) → canonical LR(1) (most
powerful, large tables). Handles left recursion natively and detects conflicts (shift/reduce,
reduce/reduce) statically — precedence declarations resolve them. GLR/Earley for ambiguous or
natural-language grammars (O(n³)); CYK for theory ([[context-free-grammars]]).

## Other approaches
**PEG** and packrat parsing (ordered choice, no ambiguity by definition, linear time with
memoization; left recursion needs care); **parser combinators** (Parsec, nom — parsers as
functions composed monadically, [[monads]]); ANTLR (ALL(*) adaptive LL). Tree-sitter (GLR,
incremental, error-tolerant) for editors. Lexerless/scannerless parsers for languages where
tokenization depends on context (C++'s `>>`, template angle brackets; Python's indentation
handled by INDENT/DEDENT tokens from the lexer).

## Pitfalls
- Left recursion in recursive descent (infinite loop); wrong associativity from the grammar
  shape.
- Grammar not LL(1) but forced through with backtracking (exponential time).
- Poor error messages: report the first error precisely, then synchronize.
- Lexer/parser mismatch on tricky tokens (`a<b>c` in generics vs comparison — the "lexer hack").

## Related
- [[context-free-grammars]], [[finite-automata-and-regular-languages]], [[compilers-overview]],
  [[interpreters-eval-apply]], [[monads]] (combinators), [[text-processing-and-regex]].

## Sources
Crafting Interpreters ch. 4–6, 16–17; Dragon Book ch. 3–4; Knuth 1965; CS143 lectures 4–9.
