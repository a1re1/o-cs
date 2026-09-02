---
title: Git's data model — content-addressed objects, references, the staging area, and the commands on top
type: concept
section: "2.6"
level: 200
tags: [git, version-control, commits, blobs, trees, dag, content-addressing, sha1, merkle-tree, references, head, staging-area, index, branches, merge, rebase, reset, reflog, bisect, workflows]
sources: [missing-semester, pro-git]
summary: A Git repository is a set of immutable objects (blobs = file contents, trees = directories, commits = parents + metadata + root tree) addressed by the hash of their content, plus mutable references (branches, tags, HEAD) pointing at commits; every command adds objects or moves refs, the staging area chooses what the next snapshot contains, merges create commits with two parents, rebase rewrites new commits with different parents (never for shared history), reset moves HEAD/index/worktree, and the reflog makes almost everything recoverable.
---
# Git's data model

**In one sentence.** History is a DAG of snapshots stored in a content-addressed object store; a
branch is just a name for one node; learn the graph and every command becomes "add objects" or
"move a pointer".

## Objects (Missing Semester lecture 6, Pro Git ch. 10)
```
blob   = bytes                                   // a file's contents
tree   = map<name, blob | tree>                  // a directory (mode, type, hash, name)
commit = { parents: [commit], author, committer, message, snapshot: tree }
id(obj) = sha1(type + size + content)            // content addressing
```
Objects never change; the same content anywhere has the same id (dedup for free). Trees reference
children by hash, so a commit's hash covers the whole snapshot and all history — a **Merkle DAG**
([[hash-functions-and-integrity]]). Loose objects live in `.git/objects/ab/cdef…`, later packed
into delta-compressed packfiles (`git gc`). Snapshots, not diffs: diffs are computed on demand.

## References
`refs/heads/main` → commit hash; `refs/tags/v1`; `refs/remotes/origin/main`; `HEAD` → usually a
branch name (symbolic), or a commit ("detached"). A branch is a 41-byte file; creating one is free.
`git log` walks parents from a ref; a commit is "on" a branch if reachable from it. Unreachable
objects are garbage-collected after the **reflog** (`git reflog`, per-ref history of where it
pointed) expires — this is why "lost" commits are recoverable.

## The three trees and the staging area (Pro Git 7.7)
Working tree (files) → **index/staging area** (proposed next tree) → HEAD (last commit).
`add` copies working → index (`add -p` for hunks); `commit` writes the index as a tree + a commit
whose parent is HEAD and moves the branch. `reset <commit>`: `--soft` moves HEAD only, `--mixed`
(default) also resets the index, `--hard` also the working tree; `reset -- file` un-stages;
`checkout`/`restore` copy from a commit into the working tree without moving the branch;
`stash` is a commit on a side ref.

## Combining histories
- **Merge**: fast-forward if the target is an ancestor (just move the pointer); otherwise a
  three-way merge against the common ancestor produces a commit with two parents; conflicts are
  hunks both sides changed. `rerere` remembers resolutions.
- **Rebase**: replay your commits onto a new base, creating *new* commits (new hashes); linear
  history, but the **golden rule**: never rebase commits others may have; `rebase -i` to squash,
  reorder, edit; `cherry-pick` moves one commit; `bisect` binary-searches history for a regression
  ([[debugging]]); `blame` attributes lines.
- Remotes: `fetch` downloads objects and updates `refs/remotes/*`; `pull` = fetch + merge/rebase;
  `push` updates a remote ref (refused if not fast-forward unless `--force-with-lease`).
  Workflows: centralized, feature-branch + PR, fork-based, trunk-based with short branches.

## Good habits
Small focused commits with imperative messages; commit often locally, tidy before sharing;
`.gitignore` build artifacts; never commit secrets (history remembers — `filter-repo` to purge);
tags for releases; hooks for lint/tests ([[code-review]]).

## Pitfalls
- Detached HEAD commits vanish from view (recover via reflog).
- `reset --hard`/`checkout -- file` discard uncommitted work irreversibly.
- Force-pushing shared branches; rebasing merge commits; huge binaries in history (use LFS).

## Related
- [[shell-and-unix-tools]], [[dags-and-partial-orders]], [[hash-functions-and-integrity]],
  [[code-review]], [[debugging]], [[build-systems-and-make]].

## Sources
Missing Semester lecture 6; Pro Git ch. 1–3, 7, 10.
