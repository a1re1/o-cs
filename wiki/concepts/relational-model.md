---
title: The relational model, relational algebra, SQL, and normalization
type: concept
section: "4.5"
level: 300
tags: [relational-model, relations, tuples, attributes, keys, primary-key, foreign-key, data-independence, relational-algebra, selection, projection, join, sql, ddl, dml, group-by, aggregation, subqueries, window-functions, ctes, views, constraints, normalization, functional-dependencies, 1nf, 2nf, 3nf, bcnf, denormalization, er-model, schema-design, nulls, three-valued-logic]
sources: [cmu-15-445, database-textbooks, database-seminal-papers]
summary: Codd's relational model stores data as sets of tuples over typed attributes (relations/tables) identified by keys and connected by foreign keys, and the point is data independence — programs express what they want in a declarative language grounded in first-order logic, not how to navigate pointers or which index or ordering exists; relational algebra (select, project, join, union, difference, rename, plus aggregation) is the operator language that SQL compiles to and optimizers rewrite; SQL adds DDL, constraints, NULLs with three-valued logic, grouping, subqueries, window functions, CTEs and views; and normalization (functional dependencies → 3NF/BCNF) removes redundancy so a fact is stored once, while deliberate denormalization trades that for read speed.
---
# The relational model and SQL

**In one sentence.** Describe the data by its natural structure only — relations — and let the
system, not the program, decide how it is stored and reached.

## Codd's model (1970; 15-445 L01)
A **relation** is a set of tuples over a fixed set of attributes with domains; no order, no
duplicates in the theory (SQL uses bags). **Keys**: superkey → candidate key → primary key;
**foreign keys** reference other relations' keys (referential integrity). Codd's motivation was
**data independence** — existing systems bound programs to ordering (records assumed in
address order), indexing (programs written for particular indexes), and access paths (network/
hierarchical pointers: "the connection trap" — deriving relations by following links you
happened to store). The normal form (no repeating groups, atomic values) made a uniform
representation possible; the "data sublanguage" was to be declarative and based on predicate
calculus — realized as SQL (via System R/SEQUEL) and QUEL.

## Relational algebra
σ (selection), π (projection), × (product), ⋈ (join — natural, theta, equi, outer, semi, anti),
∪, −, ∩, ρ (rename), ÷ (division), plus extended operators: γ (grouping/aggregation), sort,
duplicate elimination. Every SQL query is a tree of these; equivalences (push selections
down, reorder joins, projections early) drive [[query-optimization]]. Relational calculus
(tuple/domain) is the declarative equivalent (Codd's theorem: equally expressive); Datalog adds
recursion.

## SQL (15-445 L02)
DDL (`CREATE TABLE` with types, `PRIMARY KEY`, `FOREIGN KEY … ON DELETE CASCADE`, `UNIQUE`,
`CHECK`, indexes), DML (`INSERT`/`UPDATE`/`DELETE`), queries: `SELECT … FROM … WHERE … GROUP BY
… HAVING … ORDER BY … LIMIT`; joins (`INNER`/`LEFT`/`FULL`/`CROSS`, `LATERAL`); subqueries
(scalar, `IN`, `EXISTS`, correlated); set ops; **window functions** (`ROW_NUMBER() OVER
(PARTITION BY … ORDER BY …)`, running sums, `LAG`); **CTEs** (`WITH`, recursive for trees/
graphs); views and materialized views; `NULL` and three-valued logic (`NULL = NULL` is unknown;
`IS NULL`); transactions (`BEGIN`/`COMMIT`/`ROLLBACK`, isolation levels); prepared statements
(and SQL injection when you don't — [[security-principles]]). Dialects differ (Postgres vs
MySQL vs SQLite); JSON columns blur relational/document.

## Design and normalization
E-R modelling → tables. **Functional dependency** X → Y; anomalies from redundancy (update,
insert, delete). Normal forms: 1NF atomic; 2NF no partial dependency on a composite key; **3NF**
no transitive dependency (every non-key attribute depends on the key, the whole key, and
nothing but the key); **BCNF** every determinant is a superkey (may lose dependency
preservation); 4NF multivalued. Decompose losslessly along dependencies. **Denormalize**
deliberately for read-heavy/analytic workloads (star schemas, materialized aggregates) and
document stores — knowing what invariants you now maintain by hand. Surrogate vs natural keys;
indexing follows query patterns ([[storage-engines-and-indexes]]).

## Pitfalls
- Treating SQL as procedural; row-by-row loops in application code instead of set operations
  (N+1 queries) — [[query-optimization]].
- NULL semantics (`NOT IN` with NULLs returns nothing; aggregates skip NULLs).
- Mistaking bags for sets (duplicates after joins); `GROUP BY` with non-aggregated columns.
- Over-normalizing analytics or under-normalizing OLTP; entity-attribute-value tables.
- ORMs hiding joins and transactions.

## Related
- [[storage-engines-and-indexes]], [[query-optimization]], [[transactions-and-concurrency-control]],
  [[distributed-databases-and-nosql]], [[predicate-logic]], [[sets-relations-functions]].

## Sources
Codd 1970; 15-445 L01–02; Silberschatz ch. 1–7; DDIA ch. 2.
