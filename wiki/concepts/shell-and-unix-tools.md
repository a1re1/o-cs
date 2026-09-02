---
title: The shell, pipes, and the Unix tool philosophy
type: concept
section: "2.6"
level: 100
tags: [shell, bash, zsh, pipes, redirection, stdin, stdout, stderr, exit-codes, quoting, globbing, path, environment-variables, shell-scripting, job-control, signals, find, xargs, ssh, tmux, dotfiles, unix-philosophy]
sources: [missing-semester, tlcl-shotts]
summary: The shell is a programming environment whose primitives are programs — each reads stdin, writes stdout/stderr, returns an exit code, and is found via $PATH — glued by pipes and redirection; know quoting ('literal' vs "interpolated"), the special variables ($? $@ $1 $$), && / || on exit codes, command and process substitution, globbing, job control and signals, and the small-tools-composed philosophy behind grep/find/xargs/sort, plus the habits (shellcheck, set -euo pipefail, quoting variables) that make scripts safe.
---
# The shell and Unix tools

**In one sentence.** Small programs that do one thing, text streams as the universal interface, and
a shell that lets you compose them interactively or in scripts.

## The model
- A command line is split on whitespace; word 0 is looked up in `$PATH` (or is a builtin/keyword);
  the rest are `argv`. Quote to protect spaces/specials: `'…'` literal, `"…"` expands `$var`,
  `$(cmd)`, `\`. Globs `*`, `?`, `[a-z]`, `{a,b}` expand *before* the program runs.
- Every process has fd 0 stdin, 1 stdout, 2 stderr and returns an **exit code** (0 = success).
  Redirection: `< in`, `> out` (truncate), `>> out` (append), `2> err`, `2>&1`, `&>`, `| tee`.
  Pipes `a | b` connect stdout to stdin, running concurrently ([[processes-and-threads]]).
- Control by exit code: `a && b` (run b if a succeeded), `a || b`, `;` (always), `!`. `$?` is the last
  exit code. `set -e` (exit on error), `-u` (unset vars are errors), `-o pipefail` for scripts.
- Variables: `foo=bar` (no spaces), `$foo`/`${foo}`, `export` to pass to children; special: `$0`
  script name, `$1..$9`, `$@` all args (quote as `"$@"`), `$#`, `$$` pid, `!!` last command, `$_` last
  arg. Command substitution `$(…)`; process substitution `<(cmd)` gives a file name (`diff <(ls a)
  <(ls b)`); arithmetic `$(( ))`; `[[ ]]` tests; `case`, `for`, `while read -r line`; functions;
  here-docs `<<EOF`.
- Job control: `Ctrl-C` SIGINT, `Ctrl-Z` SIGSTOP → `bg`/`fg`/`jobs`, `&` background, `nohup`/`disown`
  survive SIGHUP, `kill -TERM/-KILL pid`; `trap` handlers in scripts.
- Environment: `~/.bashrc`/`.zshrc`, aliases, `$EDITOR`, dotfiles in a repo; `tmux` sessions →
  windows → panes for persistent remote work; `ssh` with keys, `~/.ssh/config`, `-L` port forwards,
  `rsync -a` for copying.
- Permissions: `rwx` for user/group/other, `chmod 755`, `sudo`; `/proc` and `/sys` expose the kernel
  as files ("everything is a file" — [[file-systems]]).

## The toolbox (compose them)
`ls -la`, `cd -`, `find dir -name '*.py' -mtime -1 -exec … {} \;`, `fd`, `grep -rn`/`rg`, `xargs -n1
-P4`, `sort | uniq -c | sort -rn | head`, `cut -d, -f2`, `tr`, `wc`, `head`/`tail -f`, `diff -u`,
`sed`, `awk`, `jq`, `curl`, `tar czf`, `time`, `watch`, `man`/`tldr`, `history | fzf`
([[text-processing-and-regex]]).

## Philosophy (McIlroy)
Write programs that do one thing well; expect the output of every program to become the input of
another (no chatty headers, text streams); build tools early; prototype in the shell before writing
a program. The same composition ideas as [[higher-order-functions]] and [[streams-and-lazy-evaluation]]
— pipes are lazy streams of lines.

## Pitfalls
- Unquoted variables (`rm -rf $dir/` with empty `dir`), spaces in filenames (`for f in $(ls)` —
  use globs or `find -print0 | xargs -0`), `cd` failing silently, parsing `ls` output.
- `foo = bar` (runs `foo`), `==` vs `=` in `[ ]`, bashisms in `sh` scripts. Run `shellcheck`.
- Pipelines hide failures (`false | true` succeeds) without `pipefail`.
- Scripts over ~100 lines or needing data structures: switch to Python/Rust.

## Related
- [[text-processing-and-regex]], [[git-data-model]], [[build-systems-and-make]], [[debugging]],
  [[processes-and-threads]], [[file-systems]].

## Sources
Missing Semester lectures 1, 2, 5; TLCL parts I, IV.
