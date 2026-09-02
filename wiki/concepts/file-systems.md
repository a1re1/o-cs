---
title: File systems — files, directories, inodes, allocation, the buffer cache, FFS locality, journaling, LFS, and flash
type: concept
section: "4.2"
level: 300
tags: [file-systems, files, directories, inodes, file-descriptors, hard-links, symbolic-links, block-allocation, indirect-blocks, extents, bitmaps, buffer-cache, page-cache, ffs, cylinder-groups, crash-consistency, fsck, journaling, write-ahead-log, lfs, copy-on-write, ssd, ftl, wear-leveling, fsync, raid, data-integrity, checksums]
sources: [ostep, xv6-and-6-1810, os-seminal-papers]
summary: A file is a named, persistent array of bytes reached through inodes (metadata + block pointers, direct/indirect or extents) and directories (name → inode number tables that are themselves files), accessed via descriptors with read/write/lseek and made durable only by fsync; on disk, bitmaps track free blocks, the superblock describes layout, and the buffer/page cache absorbs reads and writes; FFS placed related data in cylinder groups for locality, crash consistency moved from fsck to journaling (write-ahead logging of metadata or data) and copy-on-write trees, LFS turned all writes into a sequential log with cleaning — the design SSDs' flash translation layers and LSM-tree databases reuse — and RAID and checksums address device failure and silent corruption.
---
# File systems

**In one sentence.** Map names to bytes on a block device such that reads are fast, writes are
durable, and a crash halfway through an update leaves something sane.

## The interface (OSTEP ch. 39; Ritchie & Thompson)
Files as unstructured byte streams; `open` (flags, permissions) → **file descriptor** (a per-process
index into an open-file table holding the offset — shared by `fork`/`dup`, which is how
redirection works); `read`/`write`/`lseek`; `fsync` (data reaches stable storage — without it,
writes sit in the cache), `rename` (atomic replace: write temp, fsync, rename), `link` (hard
links: one inode, several names; `rm` is `unlink`; reference count), symbolic links (a file
containing a path — can dangle), `mkdir`, `stat`, permissions (rwx, uid/gid, setuid), `mount`
(graft another FS at a directory), the special files for devices and pipes (everything is a
file — [[shell-and-unix-tools]]).

## On-disk structure (OSTEP ch. 40, xv6 ch. 8)
Superblock | inode bitmap | data bitmap | inode table | data blocks. **Inode**: type, size, links,
timestamps, owner, and block pointers — direct (12), single/double/triple **indirect** (a
multi-level tree; large files pay extra reads) or **extents** (start, length; ext4, XFS).
**Directory** = list of (name, inode number) entries (hashed/B-tree indexed in ext4/XFS/btrfs).
Access path: `/foo/bar` walks root inode → dir data → foo inode → … (each hop a read; the
**dentry** cache avoids it). Reads/writes go through the **buffer/page cache** (write-back with
periodic flush; the FS is mostly a cache manager). Free space via bitmaps or free lists.

## Locality: FFS (McKusick 1984)
Original Unix FS treated the disk as a random-access array → 2% of bandwidth. FFS: **cylinder
groups** (block groups today) each with its own inodes/bitmaps/data; place a file's inode and
data in the same group, a directory's files together, spread directories; larger blocks (4 KB)
with **fragments** for small files; rotationally aware layout; long names, symlinks, locking.
Every modern FS inherits "keep related things near".

## Crash consistency (OSTEP ch. 42)
An append touches inode, bitmap, data block; a crash between writes yields inconsistency
(garbage pointer, space leak). **fsck** scans everything after a crash (slow, fixes only
consistency, not lost data). **Journaling / write-ahead logging** (ext3/4, NTFS, XFS): write a
transaction (TxB, metadata, data, TxE) to the log, wait, then checkpoint to final locations; on
recovery replay committed transactions. Modes: data journaling (safe, writes twice) vs **ordered
metadata journaling** (write data first, then journal metadata — the default); checksums to
avoid the TxE ordering wait; batching; circular log. **Copy-on-write** trees (ZFS, btrfs, APFS):
never overwrite in place; atomically flip the root — free snapshots. **Soft updates** order
writes carefully instead.

## Log-structured FS (Rosenblum & Ousterhout 1992)
Buffer everything in memory and write it as one sequential segment (data, inodes, an **inode
map** whose location the checkpoint region holds); reads use the inode map; old versions are
garbage → **segment cleaning** (cost–benefit: prefer cold, mostly empty segments); crash
recovery via checkpoint + roll-forward. Slow to reach mainstream for disks, but exactly the
right shape for **SSDs** (flash pages can't be overwritten; erase blocks; the **FTL** maps
logical → physical, does wear leveling and garbage collection — a log-structured FS in firmware,
OSTEP ch. 44) and for LSM-tree storage engines ([[storage-engines-and-indexes]]).

## Devices and integrity (OSTEP ch. 37–38, 45)
Disks: seek + rotation + transfer (ms), so sequential ≫ random; scheduling (SSTF, SCAN, deadline).
**RAID** levels: 0 stripe, 1 mirror, 4/5 parity (small-write problem), 6 double parity,
10; capacity/performance/reliability trade-offs. Latent sector errors and silent corruption →
per-block **checksums** (ZFS, btrfs), scrubbing, end-to-end verification (Lampson's end-to-end
hint); redundancy across machines for real durability ([[replication-and-partitioning]]).

## Pitfalls
- Assuming `write` is durable (it isn't until `fsync` of file *and* directory); fsync ordering
  bugs ("fsyncgate" in PostgreSQL).
- Many small files/directories with millions of entries on old FSs; deep indirect trees.
- Filling disks (allocators degrade); deleting open files (space freed only on close).
- Treating SSDs like disks (TRIM, write amplification, random writes of small sizes).

## Related
- [[virtual-memory]] (page cache, mmap), [[io-and-device-drivers]], [[storage-engines-and-indexes]],
  [[transactions-and-concurrency-control]] (WAL again), [[replication-and-partitioning]],
  [[shell-and-unix-tools]], [[git-data-model]] (content-addressed storage as a file system idea).

## Sources
OSTEP ch. 36–45; xv6 book ch. 8; Ritchie & Thompson 1974; McKusick et al. 1984; Rosenblum & Ousterhout 1992.
