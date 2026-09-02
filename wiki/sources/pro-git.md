---
title: Pro Git (Chacon & Straub, 2nd ed.)
type: source
section: "2.6"
level: 200
tags: [git, version-control, branching, merging, rebasing, remotes, distributed-workflows, git-internals, objects, refs, packfiles, reflog, hooks, submodules]
sources: []
authors: [Scott Chacon, Ben Straub]
year: 2014
institution: Apress / git-scm.com
url: https://git-scm.com/book/en/v2
license: CC-BY-NC-SA
format: html
summary: The free official Git book — getting started (snapshots not differences; the three states), basics (recording changes, viewing history, undoing, remotes, tagging, aliases), branching (branches are pointers; merging; branch management; workflows; remote branches; rebasing and its golden rule), Git on the server, distributed workflows and contributing, GitHub, tools (revision selection, interactive staging, stash, rewriting history, reset demystified, advanced merging, rerere, debugging with bisect/blame, submodules, bundling, replace, credential storage), customization and hooks, and Git internals (plumbing and porcelain, objects, references, packfiles, refspec, transfer protocols, maintenance).
---
# Pro Git

## What it is
Ch. 1 about version control — local, centralized, distributed; Git stores *snapshots* not
differences, nearly every operation is local, integrity by SHA-1, three states (modified, staged,
committed) and three areas (working tree, staging area/index, repository). Ch. 2 basics. Ch. 3
branching — a branch is a lightweight movable pointer to a commit, `HEAD` points to the current
branch; fast-forward vs three-way merge and conflicts; rebasing replays commits onto a new base —
"do not rebase commits that exist outside your repository". Ch. 7 tools — `reset` explained through
the three trees (`--soft` moves HEAD, `--mixed` also resets the index, `--hard` also the working
tree); `checkout` vs `reset`; `stash`, `rebase -i`, `filter-branch`, `bisect`, `rerere`. Ch. 10
internals — plumbing (`hash-object`, `cat-file`, `update-index`, `write-tree`, `commit-tree`), object
types blob/tree/commit/tag, refs and HEAD, packfiles and deltas, refspecs, dumb/smart protocols,
`gc`, `reflog` for data recovery.

## What it adds
The authoritative reference behind [[git-data-model]]; chapter 7's "reset demystified" and chapter
10 are the ones to read when Git behaves unexpectedly.
