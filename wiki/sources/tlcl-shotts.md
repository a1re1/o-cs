---
title: The Linux Command Line (Shotts), GNU Make manual, and Debugging (Agans)
type: source
section: "2.6"
level: 100
tags: [linux, command-line, bash, shell-scripting, permissions, processes, redirection, text-processing, make, makefile, debugging-rules]
sources: []
authors: [William Shotts, Richard Stallman, Roland McGrath, Paul D. Smith, David J. Agans]
year: 2019
institution: No Starch / GNU / AMACOM
url: https://linuxcommand.org/tlcl.php
license: CC-BY-NC-ND
format: pdf
summary: Shotts's free TLCL walks from navigation, files, redirection, permissions, processes and the environment through text processing (grep, sed, awk, sort, cut, diff, regex), archiving, networking and package management to a full course in bash scripting (variables, flow control, arrays, positional parameters, functions, here documents); the GNU Make manual defines rules, targets, prerequisites, variables, pattern rules, automatic variables and phony targets; Agans's Debugging gives nine rules (understand the system, make it fail, quit thinking and look, divide and conquer, change one thing at a time, keep an audit trail, check the plug, get a fresh view, if you didn't fix it it ain't fixed).
---
# The Linux Command Line / GNU Make / Debugging

## What it is
**TLCL** parts: I learning the shell (navigation, exploring the system, manipulating files and
directories, working with commands, redirection — `>`, `>>`, `2>`, `&>`, `|`, `tee`; seeing the
world as the shell sees it — expansion and quoting; keyboard tricks; permissions — `chmod`, `umask`,
`su`/`sudo`; processes — `ps`, `top`, `kill`, signals, job control); II configuration and the
environment (environment variables, startup files, vi, prompt); III common tasks and essential
tools (package management, storage media, networking — `ssh`, `scp`, `wget`; searching for files —
`locate`, `find` with tests/actions/`-exec`/`xargs`; archiving and backup — `tar`, `gzip`, `rsync`;
regular expressions; text processing — `cat`, `sort`, `uniq`, `cut`, `paste`, `join`, `comm`,
`diff`/`patch`, `tr`, `sed`, `aspell`; formatting; printing; compiling programs); IV shell scripts
(writing, starting a project, top-down design, flow control with `if`/`test`/`[[ ]]`, reading
keyboard input, `while`/`until`, troubleshooting, `case`, positional parameters, `for`, strings and
numbers, arrays, exotica — group commands, subshells, process substitution, traps, `wait`,
asynchronous execution, named pipes).
**GNU Make**: rules `target: prerequisites` + tab-indented recipe; make rebuilds a target when any
prerequisite is newer; variables (`:=` vs `=`), automatic variables (`$@ $< $^`), pattern rules
(`%.o: %.c`), `.PHONY`, implicit rules, functions (`wildcard`, `patsubst`), `-j` parallel builds,
recursive make considered harmful.
**Agans**: the nine rules with war stories; "make it fail" (reproduce, then automate the repro) and
"quit thinking and look" (instrument, don't guess) are the ones engineers most often skip.

## What it adds
Depth for [[shell-and-unix-tools]] and [[build-systems-and-make]]; Agans's rules are folded into
[[debugging]].
