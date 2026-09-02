---
title: Linking and loading — object files, symbols, relocation, static vs dynamic linking, shared libraries, and ABI
type: concept
section: "4.3"
level: 300
tags: [linking, loading, linker, loader, object-files, elf, mach-o, symbols, symbol-resolution, relocation, static-linking, dynamic-linking, shared-libraries, plt, got, pic, lazy-binding, ld_preload, lto, abi, name-mangling, one-definition-rule, dwarf]
sources: [csapp-15-213, patterson-hennessy-cod, compilers-overview]
summary: The linker combines relocatable object files (ELF/Mach-O/PE sections: .text, .data, .bss, symbol table, relocation entries) into an executable by resolving symbol references (globals, functions; strong vs weak; static archives searched in order) and patching addresses via relocation records; static linking copies library code in, dynamic linking defers it to load time through shared objects with position-independent code, the GOT and PLT (lazy binding), and a dynamic loader that maps libraries and resolves symbols (with interposition via LD_PRELOAD); the ABI (calling convention, type layout, name mangling) is the contract that makes separately compiled code interoperate.
---
# Linking and loading

**In one sentence.** Separate compilation produces pieces with holes; the linker fills the
holes with addresses, either at build time (static) or at load/run time (dynamic).

## Object files (CSAPP ch. 7)
Relocatable objects contain **sections**: `.text` (code), `.rodata`, `.data` (initialized
globals), `.bss` (zero-initialized, no file space), `.symtab` (symbols: name, section, value,
size, binding local/global/weak), `.rel.text`/`.rela.data` (**relocation entries**: where a
symbol's address must be patched and how — PC-relative for calls, absolute for pointers),
`.debug_*` (DWARF), `.strtab`. Formats: ELF (Linux), Mach-O (macOS), PE/COFF (Windows). Tools:
`nm`, `objdump -d/-t/-r`, `readelf`, `ldd`, `otool`.

## Symbol resolution
Each object defines and references symbols. Rules (C): multiple **strong** definitions → error;
strong + weak → strong wins; multiple weak → any (source of silent bugs: two `int x;` in different
files merged; `-fno-common`). **Static libraries** (`.a` archives) are scanned in command-line
order and only members resolving currently-undefined symbols are pulled in — so put libraries
after the objects that use them, and order libraries by dependency. C++ **name mangling** encodes
namespaces/types into symbol names (overloading); `extern "C"` to interoperate. The **one
definition rule** and inline functions (weak/COMDAT sections). LTO ships IR in objects and
optimizes across them at link time ([[compiler-optimizations]]).

## Relocation
The linker assigns final addresses to merged sections, then applies each relocation:
`R_X86_64_PC32` for `call foo` (target − (place + 4)), `R_X86_64_64` for absolute pointers,
GOT/PLT-relative kinds for shared code. Link maps and linker scripts control layout (embedded
systems).

## Static vs dynamic linking
- **Static**: everything copied into one executable — self-contained, fast startup, larger
  binaries, no shared updates (Go's default; `-static`).
- **Dynamic**: **shared objects** (`.so`/`.dylib`/`.dll`) mapped into each process at load time
  by the dynamic loader (`ld-linux.so`, `dyld`), one physical copy in the page cache shared by all
  ([[virtual-memory]]). Code must be **position-independent** (PIC/PIE): globals accessed via the
  **GOT** (global offset table, patched by the loader), functions called through the **PLT**
  (procedure linkage table) with **lazy binding** on first call (or eager with `LD_BIND_NOW`/
  RELRO for security). Symbol lookup order, versioned symbols (`GLIBC_2.34`), `RPATH`/`RUNPATH`,
  `LD_LIBRARY_PATH`. **Interposition**: `LD_PRELOAD` overrides symbols (malloc debuggers,
  fault injection). `dlopen`/`dlsym` for plugins at run time.
- Trade-offs: memory sharing and security updates vs "DLL hell"/ABI drift; startup relocation
  cost; container images that vendor everything.

## Loading and the ABI
The loader (`execve` → ELF program headers) maps segments (code R-X, data RW, bss), sets up the
stack with argv/envp/auxv, runs the dynamic linker, then constructors, then `_start` → `main`
([[processes-and-threads]], [[memory-layout-stack-heap]]). The **ABI** fixes the calling
convention, register usage, type sizes/alignment, struct layout, name mangling, exception
unwinding, and symbol versioning — so binaries compiled by different compilers/languages link
([[calling-conventions-and-the-stack]]); breaking it silently is worse than a compile error
(stable C ABI as lingua franca; Swift/Rust ABI stability efforts).

## Pitfalls
- Undefined reference errors from library order; duplicate weak symbols merging silently.
- Mismatched compile flags/ABI across objects (struct layout, `-fPIC`, exception models).
- Dynamic symbol resolution picking an unexpected library (LD_LIBRARY_PATH, versioning).
- Assuming static linking removes all runtime dependencies (glibc NSS, dlopen'd plugins).

## Related
- [[calling-conventions-and-the-stack]], [[isa-and-assembly]], [[memory-layout-stack-heap]],
  [[virtual-memory]], [[compilers-overview]], [[build-systems-and-make]], [[register-allocation-and-code-generation]].

## Sources
CSAPP ch. 7; COD 2.12; Levine *Linkers and Loaders*; Drepper "How to Write Shared Libraries".
