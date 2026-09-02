---
title: Access control and isolation — the access matrix and its two implementations (access control lists vs capabilities: list-oriented vs ticket-oriented, ambient authority and the confused deputy), discretionary vs mandatory access control (Bell–LaPadula, Biba, multilevel security, SELinux/AppArmor), role- and attribute-based models, Unix permissions/setuid and the reference monitor, privilege separation (OKWS, OpenSSH), sandboxing and isolation mechanisms compared (processes, chroot/namespaces/seccomp, containers, virtual machines, software fault isolation and WebAssembly, language-based isolation, hardware enclaves), the confinement problem and covert channels, capability systems (Capsicum, seL4, object capabilities), and platform security models (iOS/Android app sandboxes and permissions, browser site isolation)
type: concept
section: "8.1"
level: 400
tags: [access-control, access-matrix, lampson, acl, access-control-list, capabilities, capability-system, list-oriented, ticket-oriented, ambient-authority, confused-deputy, hardy, dac, discretionary, mac, mandatory, bell-lapadula, no-read-up, no-write-down, biba, multilevel-security, mls, selinux, apparmor, rbac, abac, unix-permissions, setuid, suid, reference-monitor, tcb, privilege-separation, okws, openssh, sandboxing, isolation, process-isolation, chroot, namespaces, seccomp, seccomp-bpf, containers, virtual-machines, hypervisor, gvisor, firecracker, software-fault-isolation, sfi, native-client, webassembly, wasm, language-based-security, memory-safe, enclaves, sgx, trustzone, confinement, covert-channels, side-channels, capsicum, sel4, object-capabilities, ocap, ios-sandbox, android-permissions, site-isolation, chrome-sandbox, hru-undecidability]
sources: [computer-security-texts-courses-and-seminal-papers]
summary: Access control answers "may this principal do this operation on this object?" — Lampson's access matrix records the answer for every (subject, object) pair, and Saltzer & Schroeder's two ways of storing it define the design space: access control lists keep, with each object, the list of authorized principals (list-oriented — easy to audit "who can read this file", needs authentication on every access and a name for every principal, hard to delegate and revoke narrowly) while capabilities give each principal unforgeable tickets naming an object plus rights (ticket-oriented — possession is authority, delegation is passing the ticket, no ambient authority, so the confused-deputy problem where a privileged program is tricked into using its own authority on an attacker's behalf cannot arise, but auditing and revocation are harder); Unix permissions, setuid and SELinux are ACL-flavoured, Capsicum/seL4/object-capability languages capability-flavoured, and browsers and mobile OSes mix both; discretionary control lets owners set policy, mandatory control imposes system-wide labels (Bell–LaPadula's no-read-up/no-write-down for confidentiality, Biba's dual for integrity, SELinux type enforcement), and RBAC/ABAC organize enterprise policy — with the caveat that the general safety question (can a right ever leak?) is undecidable (Harrison–Ruzzo–Ullman); enforcement needs a reference monitor and isolation, whose mechanisms trade strength for cost — processes with least privilege and privilege separation (OKWS's per-service daemons, OpenSSH's unprivileged child handling the network), chroot/namespaces/seccomp filters, containers (shared kernel — a kernel bug escapes), virtual machines and micro-VMs (gVisor, Firecracker — much smaller shared surface), software fault isolation (instrument or compile code so it cannot escape its region — Native Client, WebAssembly's verified linear memory and control flow), language-based isolation (memory-safe code with capability discipline), and hardware enclaves (SGX/TrustZone protect against a hostile OS but leak through side channels); Lampson's confinement problem — a borrowed program must not leak its caller's data — is unsolvable in full because of covert channels (timing, resource usage), so isolation is about bandwidth, not absolutes; and platform models put the theory in practice: iOS and Android sandbox every app, mediate hardware and data through runtime permissions, and sign code, while Chrome's site isolation puts each origin in its own process because the same-origin policy alone couldn't survive Spectre.
---
# Access control and isolation

**In one sentence.** Store "who may do what to which object" either with the object
(ACLs) or with the principal (capabilities), enforce it through a reference monitor
that every access must pass, run each part of the system with only its own authority
in a compartment it cannot escape — and remember that no compartment is perfectly
tight, only tight enough.

## The access matrix, ACLs, and capabilities (Lampson 1971; Saltzer & Schroeder — read)
**Access matrix**: rows = **subjects/principals** (users, processes, roles), columns =
**objects** (files, sockets, devices, other processes), cells = rights (read, write,
execute, own, grant). Two storage strategies (S&S glossary): **list-oriented** — each object
carries an **access control list** of authorized principals (Unix mode bits + POSIX ACLs,
Windows DACLs, cloud IAM policies attached to resources): authenticate the principal,
look them up; audit is easy ("who can read /etc/shadow?"), revocation is editing a list,
delegation requires naming the delegate; **ticket-oriented** — each principal holds
**capabilities**: unforgeable tokens that name an object and confer rights (file
descriptors are capabilities: once `open()` succeeds you never re-check the path;
Kerberos tickets, signed URLs, bearer tokens, object references in ocap languages):
possession *is* authorization, delegation is handing over the ticket, there is no
**ambient authority** (a program can only touch what it was explicitly given), but
"who has access to X?" and selective **revocation** are hard (indirection/revocable
proxies, expiry). **Confused deputy** (Hardy 1988): a privileged program (compiler
writing a billing file, a web server fetching a URL, a CSRF-vulnerable site acting on
a cookie) is tricked into using *its* authority for the attacker's request — inherent
to ambient authority; capabilities fix it by making the requester supply authority for
every object it names. Real systems mix both (Unix: ACL-checked `open` returns a
capability). **Safety** — "can principal p ever obtain right r on object o under these
rules?" — is undecidable in general (HRU 1976), decidable for restricted models (take-
grant); this is why policies must be simple.

## Policies: DAC, MAC, RBAC, ABAC, and the Unix model (Bishop; CS161; Anderson ch. 6, 9)
**Discretionary (DAC)**: the object's owner sets permissions (Unix `chmod`, `chown`;
Windows). **Mandatory (MAC)**: the system enforces labels regardless of owners —
**Bell–LaPadula** (1973; confidentiality: subjects and objects have clearances/
classifications; **no read up** (simple security), **no write down** (★-property — a
process reading Top Secret cannot write to Unclassified, defeating Trojan leaks);
**multilevel security** with compartments (a lattice — Denning 1976); the tranquility
and declassification problems), **Biba** (integrity: no read down, no write up —
untrusted input cannot taint trusted data; Windows integrity levels, LOMAC), **Clark–
Wilson** (commercial integrity: well-formed transactions, separation of duty), **Chinese
Wall** (conflict-of-interest classes); **SELinux** type enforcement / **AppArmor** profiles
confine daemons by policy the admin, not the program, controls. **RBAC**: permissions
attached to roles, principals to roles (hierarchies, constraints — separation of duty);
**ABAC/policy engines**: rules over attributes of subject, object, action, environment
(XACML, OPA/Rego, AWS IAM condition keys, Zanzibar-style relationship-based for
"members of org X can edit docs shared with team Y" — [[web-backends-sessions-and-authentication]]
authorization). **Unix**: uid/gid, mode bits `rwx` for owner/group/other, root bypasses
all; **setuid** binaries run with the file owner's uid (`passwd` edits `/etc/shadow`) —
the classic privilege-escalation surface (env vars, `LD_PRELOAD`, races, argument
parsing); capabilities(7) split root into `CAP_NET_BIND_SERVICE` etc.; `sudo` as
audited delegation. Windows: SIDs, tokens, ACEs with inheritance, integrity levels, UAC.
Cloud IAM: identities, policies (allow/deny statements, resource + condition),
roles assumed with short-lived credentials — least privilege is a policy-authoring
problem ([[infrastructure-as-code-and-devops]]).

## Privilege separation and the reference monitor (OKWS; OpenSSH; 6.858 L4 — read)
The **reference monitor** (kernel, hypervisor, browser process broker) must be always
invoked, tamper-proof, and small enough to verify ([[security-principles]] complete
mediation, TCB). **Privilege separation** applies least privilege to program structure:
split a program into processes with distinct uids/capabilities so a bug in one yields
only its authority. **OKWS** (Krohn 2004; 6.858): each web service is a separate unprivileged
process in its own chroot, talking to the DB only through a **dbproxy** that exposes a
narrow RPC interface with its own credentials (SQL injection in a service can't read
other tables), a small privileged launcher, and a demux — compromise of one service is
contained. **OpenSSH** (Provos 2003): a privileged monitor forks an unprivileged child
(separate uid, chroot, later seccomp) that parses network input; only after
authentication does the monitor grant more. Browsers: **Chrome** runs the renderer
(HTML/JS/images — the risky parser) in a tightly sandboxed process; a broker process
mediates file and network access; **site isolation** (2018) gives each site its own
renderer because Spectre made in-process origin separation insufficient ([[web-security]]
same-origin policy). Systemd/service hardening options, `qmail`'s design, Postfix — the
pattern is: parse untrusted data with the least authority possible.

## How do I isolate untrusted third-party code in my application? Isolation mechanisms compared (6.858 L5–7 — read; Anderson ch. 6, 10)
| Mechanism | Boundary | Shared surface with attacker | Cost | Escape route |
|---|---|---|---|---|
| Process + uid | kernel | whole syscall API | ~free | any kernel bug; setuid/IPC misuse |
| chroot / **namespaces** + **seccomp-bpf** | kernel, filtered | syscall subset (seccomp allowlist) | low | allowed syscalls' bugs; ptrace; `/proc` |
| **Container** | kernel (namespaces, cgroups, caps) | full kernel unless seccomp/AppArmor | low | kernel exploits (Dirty COW/Pipe, runc CVE-2019-5736) — [[containers-and-kubernetes]] |
| **gVisor** | user-space kernel in Go | small host syscall set | medium | gVisor bugs; performance |
| **VM / micro-VM** (Firecracker, KVM) | hypervisor + virtual hardware | hypercalls, device emulation (QEMU is big) | medium–high | hypervisor/device bugs (VENOM), side channels — [[os-kernels-and-virtualization]] |
| **SFI** (Native Client) / **WebAssembly** | verified machine code | none but the host API you expose | low overhead (~10 %) | verifier bugs; host-API bugs; Spectre |
| Language-based (memory-safe + ocap) | type system | nothing but explicitly passed refs | free at runtime | unsafe code, FFI, runtime bugs |
| **Enclave** (SGX, TrustZone, SEV) | CPU-enforced memory encryption | OS is *untrusted* | high | side channels (controlled-channel, Foreshadow), microcode bugs |
**Software fault isolation** (Wahbe 1993): rewrite/verify code so every load, store and
jump stays within a sandbox region (masking addresses, guard pages, a verifier before
execution) — Native Client did it for x86; **WebAssembly** designs it in: linear memory
bounds-checked (or guard-page-checked), structured control flow, typed function
tables, no raw pointers to host memory, a small explicitly-imported API (WASI) —
isolation at near-native speed inside browsers, CDNs and plugin systems (6.858 L6);
**KSplit** (6.858 L7) isolates kernel drivers by splitting shared state automatically.
**Enclaves** invert the trust: code runs encrypted in memory the OS can't read; **remote
attestation** proves what code is running; but the OS still controls scheduling and
page tables, so **controlled-channel attacks** (Xu 2015 — page faults leak access
patterns) and cache side channels leak secrets ([[software-exploitation-and-mitigations]]).
Choose by threat model: hostile multi-tenant code → VM/micro-VM; plugins/user code in
your process → Wasm; your own services → processes + seccomp + least privilege.

## Confinement, covert channels, capabilities in practice (Lampson 1973; Capsicum; seL4)
**Confinement problem**: can you run a borrowed program on your data and be sure it
doesn't leak the data to its author? Lampson: block explicit channels (files, network,
IPC — the sandbox), **legitimate** channels that carry information (a bill's amount),
and **covert channels** — resource usage (CPU time, disk space, page faults, cache
timing) modulated to signal bits; the latter cannot be fully closed, only reduced in
bandwidth (noise, quotas, fixed-time scheduling) — the theoretical root of side-channel
defence. **Capsicum** (FreeBSD/Linux patches): a process enters *capability mode*, loses
global namespaces (no `open` by path), and may only use the descriptors it holds, with
per-descriptor rights masks — retrofit ocap onto Unix (used by tcpdump, dhclient).
**seL4**: a formally verified capability-based microkernel — every kernel object is
reachable only via capabilities, and the proof shows the kernel enforces them
([[program-verification]]). **Object-capability languages/patterns** (E, Pony, Caja;
"capability discipline" in JS/Rust APIs): authority flows only along references —
a module without a reference to the file system cannot touch it, which also makes
supply-chain compromise less powerful ([[software-supply-chain-security]]).
**Platform models** (6.858 L8–9): **iOS** — every app in a sandbox with an entitlement
list, hardware-mediated permissions with user prompts, code signing and the Secure
Enclave for keys, data protection classes tied to the passcode; **Android** — each app
its own Linux uid (the sandbox), SELinux policy, install/runtime permissions with a
permission-usage UI, scoped storage, verified boot, Play signing and Google Play
Protect; both treat the *app* as the principal and the user as the policy setter
([[mobile-development-and-cross-platform]]). Browsers apply the same idea to origins
([[web-security]]).

## Pitfalls
- Ambient authority in a privileged deputy (setuid helpers, CI runners, web hooks).
- Checking a path then opening it (TOCTTOU); caching authorization across a
  permission change.
- Assuming a container is a VM; running hostile code in-process without SFI.
- Enclaves as a silver bullet — side channels; "encrypted memory" ≠ "no leaks".
- Root for convenience; wildcard IAM; broad cross-service database credentials (the
  thing OKWS was built to prevent).

## Related
- [[security-principles]], [[software-exploitation-and-mitigations]], [[web-security]],
  [[containers-and-kubernetes]], [[os-kernels-and-virtualization]],
  [[web-backends-sessions-and-authentication]], [[infrastructure-as-code-and-devops]],
  [[software-supply-chain-security]], [[mobile-development-and-cross-platform]],
  [[program-verification]] (seL4), [[processes-and-threads]], [[file-systems]].

## Sources
Saltzer & Schroeder 1975 (read: glossary; §II); Lampson 1971 ("Protection"), 1973 (confinement); Harrison, Ruzzo & Ullman 1976; Bell & LaPadula 1973; Biba 1977; Denning 1976; Hardy 1988 (confused deputy); Krohn et al. 2004 (OKWS; 6.858 L4 read: schedule); Provos, Friedl & Honeyman 2003 (OpenSSH privsep); Wahbe et al. 1993 (SFI); Yee et al. 2009 (Native Client); Haas et al. 2017 (WebAssembly; 6.858 L6); Watson et al. 2010 (Capsicum); Klein et al. 2009 (seL4); Xu, Cui & Peinado 2015 (controlled-channel); Reis et al. 2019 (site isolation); Mayrhofer et al. 2021 (Android platform security model); Apple Platform Security guide; Anderson 2020 ch. 6, 9–10; Bishop 2018 ch. 2–8; CS161 textbook ch. 1 (read).
