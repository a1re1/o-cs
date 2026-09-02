---
title: The Missing Semester of Your CS Education (MIT)
type: source
section: "2.6"
level: 100
tags: [shell, bash, shell-scripting, editors, vim, data-wrangling, regex, sed, awk, command-line, dotfiles, ssh, tmux, git, debugging, profiling, metaprogramming, build-systems, make, security, cryptography]
sources: []
authors: [Anish Athalye, Jon Gjengset, Jose Javier Gonzalez Ortiz]
year: 2020
institution: MIT
url: https://missing.csail.mit.edu/
license: CC-BY-NC-SA
format: html
summary: Eleven one-hour lectures with notes, videos and exercises on the tools CS classes skip — the shell and scripting, editors (Vim), data wrangling with pipes/regex/sed/awk/jq, command-line environment (job control, tmux, aliases, dotfiles, ssh), version control with Git's data model explained from first principles, debugging and profiling (printf, loggers, pdb/gdb, strace, sampling profilers, flame graphs, resource monitors), metaprogramming (make, dependency management, CI, testing), security and cryptography, and potpourri.
---
# The Missing Semester of Your CS Education

## What it is
1 Course overview + the shell (`$PATH`, arguments and quoting, `cd`/`ls`/permissions,
redirection `< > >> |`, root and `sudo`, `/sys`); 2 shell tools and scripting (variables, quoting
`'` vs `"`, functions, `$0 $1 $@ $# $? $$ !! $_`, exit codes with `&&`/`||`, command substitution
`$(…)`, process substitution `<(…)`, globbing, shebang, shellcheck; finding things: `find`, `fd`,
`locate`, `grep -R`, `rg`, history, `fzf`, `tree`/`broot`); 3 editors — Vim modes, buffers/windows/
tabs, command-line, verbs+nouns grammar, counts, customization; 4 data wrangling (`sed`, regex,
`sort | uniq -c`, `awk`, `paste`, `bc`, `R`, `gnuplot`, `xargs`, binary data); 5 command-line
environment (job control — signals `SIGINT`/`SIGSTOP`/`SIGHUP`, `&`, `jobs`, `fg`, `nohup`; tmux
sessions/windows/panes; aliases; dotfiles; remote machines — ssh keys, `scp`/`rsync`, port
forwarding, config); 6 **version control (Git)** — the data model (blobs, trees, commits; content
addressing; references; staging area) before the interface, then basics, branching/merging,
remotes, advanced (`stash`, `bisect`, `blame`, `add -p`); 7 **debugging and profiling** — printf,
logging, third-party logs (`journalctl`), debuggers (`pdb`, `gdb`), specialized tools (`strace`,
`tcpdump`, Wireshark), static analysis and linters, profiling (`time`, real/user/sys; tracing vs
sampling profilers; `cProfile`, `line_profiler`, `memory_profiler`, `perf`, `valgrind`; flame
graphs, call graphs; `htop`, `iotop`, `lsof`, `ss`, `du`, `ncdu`); 8 metaprogramming (build systems
and `make`, dependency management and semantic versioning, lock files, continuous integration,
testing terminology); 9 security and cryptography (entropy, hash functions, KDFs, symmetric and
asymmetric encryption, case studies); 10 potpourri (keyboard remapping, daemons, FUSE, backups,
APIs, booting/live USBs, VMs, containers, VPNs, Markdown, Hammerspoon); 11 Q&A.

## Key ideas → pages
- The shell is a programming environment; everything is a program with stdin/stdout/exit code and
  pipes are the glue — [[shell-and-unix-tools]].
- Git = an immutable content-addressed DAG plus mutable references — [[git-data-model]].
- Debug with the cheapest tool that answers the question; profile before optimizing —
  [[debugging]], [[profiling-and-performance]].
- Build systems are DAGs of targets with dependencies and rules — [[build-systems-and-make]].

## What it adds
The practical glue for every later section; [[pro-git]] and [[tlcl-shotts]] provide depth.
