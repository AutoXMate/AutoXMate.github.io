---
id: system-sync-rsync
namespace: system:sync:rsync
name: rsync
description: Fast, versatile file synchronization and transfer tool with delta encoding,
  compression, and remote sync over SSH.
author: Repository Maintainers
version: 1.0.0
techniques:
- exfiltration
- collection
capabilities:
- filesystem.sync.local
- filesystem.sync.remote
- filesystem.sync.incremental
- filesystem.sync.archive
- filesystem.transfer.delta
- filesystem.backup
platforms:
- linux
- macos
- cross-platform
risk_level: low
trust_level: verified
execution_policy: enabled
architectures:
- amd64
- arm64
- cross-platform
dependencies:
- ssh
related_tools:
- unison
- tar
- rclone
- scp
- network-remote-ssh
- network-transfer-scp
- network-transfer-sftp
artifacts:
- type: filesystem.directory.synced
  description: Destination directory after rsync operation
  trust_level: verified
- type: system.backup.archive
  description: Backup archive created via rsync
  trust_level: verified
workflow_edges:
  produces:
  - synced-directory
  - backup-archive
  consumes:
  - source-directory
  - destination-path
contract:
  inputs:
  - type: filesystem.directory.source
    description: Source directory or file path
  - type: filesystem.directory.destination
    description: Destination directory path
  outputs:
  - type: filesystem.directory.synced
    description: Synchronized destination directory
  side_effects:
  - filesystem_write
  resource_cost:
    cpu: low
    memory_mb: 32
    network: medium
    disk_io: high
resource_profile:
  cpu: low
  memory_mb: 32
  network: medium
  disk_io: high
allowed-tools:
- rsync
- Bash
- execFile
parameters:
- name: verbose
  type: string
  required: false
  description: increase verbosity
  aliases:
  - -v
  - --verbose
- name: info
  type: string
  required: false
  description: fine-grained informational verbosity
  aliases:
  - --info
- name: debug
  type: string
  required: false
  description: fine-grained debug verbosity
  aliases:
  - --debug
- name: stderr
  type: string
  required: false
  default_value: errors
  description: change stderr output mode
  aliases:
  - --stderr
- name: quiet
  type: string
  required: false
  description: suppress non-error messages
  aliases:
  - -q
  - --quiet
- name: no-motd
  type: string
  required: false
  description: suppress daemon-mode MOTD
  aliases:
  - --no-motd
- name: checksum
  type: string
  required: false
  description: skip based on checksum, not mod-time & size
  aliases:
  - -c
  - --checksum
- name: archive
  type: string
  required: false
  description: archive mode is -rlptgoD (no -A,-X,-U,-N,-H)
  aliases:
  - -a
  - --archive
  enum:
  - no -A
  - -X
  - -U
  - -N
  - -H
- name: no-OPTION
  template_key: no-option
  type: string
  required: false
  description: turn off an implied OPTION (e.g. --no-D)
  aliases:
  - --no-OPTION
- name: recursive
  type: string
  required: false
  description: recurse into directories
  aliases:
  - -r
  - --recursive
- name: relative
  type: string
  required: false
  description: use relative path names
  aliases:
  - -R
  - --relative
- name: no-implied-dirs
  type: string
  required: false
  description: don't send implied dirs with --relative
  aliases:
  - --no-implied-dirs
- name: backup
  type: string
  required: false
  description: make backups (see --suffix & --backup-dir)
  aliases:
  - -b
  - --backup
- name: backup-dir
  type: file
  required: false
  description: make backups into hierarchy based in DIR
  aliases:
  - --backup-dir
- name: suffix
  type: string
  required: false
  description: backup suffix (default ~ w/o --backup-dir)
  aliases:
  - --suffix
- name: update
  type: string
  required: false
  description: skip files that are newer on the receiver
  aliases:
  - -u
  - --update
- name: inplace
  type: string
  required: false
  description: update destination files in-place
  aliases:
  - --inplace
- name: append
  type: string
  required: false
  description: append data onto shorter files
  aliases:
  - --append
- name: append-verify
  type: string
  required: false
  description: --append w/old data in file checksum
  aliases:
  - --append-verify
- name: dirs
  type: string
  required: false
  description: transfer directories without recursing
  aliases:
  - -d
  - --dirs
- name: old-dirs
  type: string
  required: false
  description: works like --dirs when talking to old rsync
  aliases:
  - --old-dirs
  - --old-d
- name: mkpath
  type: string
  required: false
  description: create destination's missing path components
  aliases:
  - --mkpath
- name: links
  type: string
  required: false
  description: copy symlinks as symlinks
  aliases:
  - -l
  - --links
- name: copy-links
  type: string
  required: false
  description: transform symlink into referent file/dir
  aliases:
  - -L
  - --copy-links
- name: copy-unsafe-links
  type: string
  required: false
  description: only "unsafe" symlinks are transformed
  aliases:
  - --copy-unsafe-links
- name: safe-links
  type: string
  required: false
  description: ignore symlinks that point outside the tree
  aliases:
  - --safe-links
- name: munge-links
  type: string
  required: false
  description: munge symlinks to make them safe & unusable
  aliases:
  - --munge-links
- name: copy-dirlinks
  type: string
  required: false
  description: transform symlink to dir into referent dir
  aliases:
  - -k
  - --copy-dirlinks
- name: keep-dirlinks
  type: string
  required: false
  description: treat symlinked dir on receiver as dir
  aliases:
  - -K
  - --keep-dirlinks
- name: hard-links
  type: string
  required: false
  description: preserve hard links
  aliases:
  - -H
  - --hard-links

- name: perms
  type: string
  required: false
  default: null
  description: "preserve permissions"
  aliases:
    - "-p"
    - "--perms"
- name: executability
  type: string
  required: false
  default: null
  description: "preserve executability"
  aliases:
    - "-E"
    - "--executability"
- name: chmod
  type: file
  required: false
  default: null
  description: "affect file and/or directory permissions"
  aliases:
    - "--chmod"
- name: acls
  type: string
  required: false
  default: null
  description: "preserve ACLs (implies --perms)"
  aliases:
    - "-A"
    - "--acls"
- name: xattrs
  type: string
  required: false
  default: null
  description: "preserve extended attributes"
  aliases:
    - "-X"
    - "--xattrs"
- name: owner
  type: string
  required: false
  default: null
  description: "preserve owner (super-user only)"
  aliases:
    - "-o"
    - "--owner"
- name: group
  type: string
  required: false
  default: null
  description: "preserve group"
  aliases:
    - "-g"
    - "--group"
- name: devices
  type: string
  required: false
  default: null
  description: "preserve device files (super-user only)"
  aliases:
    - "--devices"
- name: copy-devices
  type: string
  required: false
  default: null
  description: "copy device contents as a regular file"
  aliases:
    - "--copy-devices"
- name: write-devices
  type: string
  required: false
  default: null
  description: "write to devices as files (implies --inplace)"
  aliases:
    - "--write-devices"
- name: specials
  type: string
  required: false
  default: null
  description: "preserve special files"
  aliases:
    - "--specials"
- name: times
  type: string
  required: false
  default: null
  description: "preserve modification times"
  aliases:
    - "-t"
    - "--times"
- name: atimes
  type: string
  required: false
  default: null
  description: "preserve access (use) times"
  aliases:
    - "-U"
    - "--atimes"
- name: open-noatime
  type: string
  required: false
  default: null
  description: "avoid changing the atime on opened files"
  aliases:
    - "--open-noatime"
- name: crtimes
  type: string
  required: false
  default: null
  description: "preserve create times (newness)"
  aliases:
    - "-N"
    - "--crtimes"
- name: omit-dir-times
  type: string
  required: false
  default: null
  description: "omit directories from --times"
  aliases:
    - "-O"
    - "--omit-dir-times"
- name: omit-link-times
  type: string
  required: false
  default: null
  description: "omit symlinks from --times"
  aliases:
    - "-J"
    - "--omit-link-times"
- name: super
  type: string
  required: false
  default: null
  description: "receiver attempts super-user activities"
  aliases:
    - "--super"
- name: fake-super
  type: string
  required: false
  default: null
  description: "store/recover privileged attrs using xattrs"
  aliases:
    - "--fake-super"
- name: sparse
  type: string
  required: false
  default: null
  description: "turn sequences of nulls into sparse blocks"
  aliases:
    - "-S"
    - "--sparse"
- name: preallocate
  type: string
  required: false
  default: null
  description: "allocate dest files before writing them"
  aliases:
    - "--preallocate"
- name: dry-run
  type: string
  required: false
  default: null
  description: "perform a trial run with no changes made"
  aliases:
    - "-n"
    - "--dry-run"
- name: whole-file
  type: string
  required: false
  default: null
  description: "copy files whole (w/o delta-xfer algorithm)"
  aliases:
    - "-W"
    - "--whole-file"
- name: checksum-choice
  type: string
  required: false
  default: null
  description: "choose the checksum algorithm (aka --cc)"
  aliases:
    - "--checksum-choice"
- name: one-file-system
  type: string
  required: false
  default: null
  description: "don't cross filesystem boundaries"
  aliases:
    - "-x"
    - "--one-file-system"
- name: block-size
  type: integer
  required: false
  default: null
  description: "force a fixed checksum block-size"
  aliases:
    - "-B"
    - "--block-size"
- name: rsh
  type: string
  required: false
  default: null
  description: "specify the remote shell to use"
  aliases:
    - "-e"
    - "--rsh"
- name: rsync-path
  type: string
  required: false
  default: null
  description: "specify the rsync to run on remote machine"
  aliases:
    - "--rsync-path"
- name: existing
  type: string
  required: false
  default: null
  description: "skip creating new files on receiver"
  aliases:
    - "--existing"
- name: ignore-existing
  type: string
  required: false
  default: null
  description: "skip updating files that exist on receiver"
  aliases:
    - "--ignore-existing"
- name: remove-source-files
  type: string
  required: false
  default: null
  description: "sender removes synchronized files (non-dir)"
  aliases:
    - "--remove-source-files"
- name: del
  type: string
  required: false
  default: null
  description: "an alias for --delete-during"
  aliases:
    - "--del"
- name: delete
  type: string
  required: false
  default: null
  description: "delete extraneous files from dest dirs"
  aliases:
    - "--delete"
- name: delete-before
  type: string
  required: false
  default: null
  description: "receiver deletes before xfer, not during"
  aliases:
    - "--delete-before"
- name: delete-during
  type: string
  required: false
  default: null
  description: "receiver deletes during the transfer"
  aliases:
    - "--delete-during"
- name: delete-delay
  type: string
  required: false
  default: null
  description: "find deletions during, delete after"
  aliases:
    - "--delete-delay"
- name: delete-after
  type: string
  required: false
  default: null
  description: "receiver deletes after transfer, not during"
  aliases:
    - "--delete-after"
- name: delete-excluded
  type: string
  required: false
  default: null
  description: "also delete excluded files from dest dirs"
  aliases:
    - "--delete-excluded"
- name: ignore-missing-args
  type: string
  required: false
  default: null
  description: "ignore missing source args without error"
  aliases:
    - "--ignore-missing-args"
- name: delete-missing-args
  type: string
  required: false
  default: null
  description: "delete missing source args from destination"
  aliases:
    - "--delete-missing-args"
- name: ignore-errors
  type: string
  required: false
  default: null
  description: "delete even if there are I/O errors"
  aliases:
    - "--ignore-errors"
- name: force
  type: string
  required: false
  default: null
  description: "force deletion of dirs even if not empty"
  aliases:
    - "--force"
- name: max-delete
  type: integer
  required: false
  default: null
  description: "don't delete more than NUM files"
  aliases:
    - "--max-delete"
- name: max-size
  type: integer
  required: false
  default: null
  description: "don't transfer any file larger than SIZE"
  aliases:
    - "--max-size"
- name: min-size
  type: integer
  required: false
  default: null
  description: "don't transfer any file smaller than SIZE"
  aliases:
    - "--min-size"
- name: max-alloc
  type: integer
  required: false
  default: null
  description: "change a limit relating to memory alloc"
  aliases:
    - "--max-alloc"
- name: partial
  type: string
  required: false
  default: null
  description: "keep partially transferred files"
  aliases:
    - "--partial"
- name: partial-dir
  type: file
  required: false
  default: null
  description: "put a partially transferred file into DIR"
  aliases:
    - "--partial-dir"
- name: delay-updates
  type: string
  required: false
  default: null
  description: "put all updated files into place at end"
  aliases:
    - "--delay-updates"
- name: prune-empty-dirs
  type: file
  required: false
  default: null
  description: "prune empty directory chains from file-list"
  aliases:
    - "-m"
    - "--prune-empty-dirs"
- name: numeric-ids
  type: string
  required: false
  default: null
  description: "don't map uid/gid values by user/group name"
  aliases:
    - "--numeric-ids"
- name: usermap
  type: string
  required: false
  default: null
  description: "custom username mapping"
  aliases:
    - "--usermap"
- name: groupmap
  type: string
  required: false
  default: null
  description: "custom groupname mapping"
  aliases:
    - "--groupmap"
- name: chown
  type: string
  required: false
  default: null
  description: "simple username/groupname mapping"
  aliases:
    - "--chown"
- name: timeout
  type: integer
  required: false
  default: null
  description: "set I/O timeout in seconds"
  aliases:
    - "--timeout"
- name: contimeout
  type: integer
  required: false
  default: null
  description: "set daemon connection timeout in seconds"
  aliases:
    - "--contimeout"
- name: ignore-times
  type: string
  required: false
  default: null
  description: "don't skip files that match size and time"
  aliases:
    - "-I"
    - "--ignore-times"
- name: size-only
  type: string
  required: false
  default: null
  description: "skip files that match in size"
  aliases:
    - "--size-only"
- name: modify-window
  type: integer
  required: false
  default: null
  description: ""
  aliases:
    - "-t"
    - "--modify-window"
- name: temp-dir
  type: file
  required: false
  default: null
  description: "create temporary files in directory DIR"
  aliases:
    - "-T"
    - "--temp-dir"
- name: fuzzy
  type: string
  required: false
  default: null
  description: "find similar file for basis if no dest file"
  aliases:
    - "-y"
    - "--fuzzy"
- name: compare-dest
  type: file
  required: false
  default: null
  description: "also compare destination files relative to DIR"
  aliases:
    - "--compare-dest"
- name: copy-dest
  type: file
  required: false
  default: null
  description: "and include copies of unchanged files"
  aliases:
    - "--copy-dest"
- name: link-dest
  type: file
  required: false
  default: null
  description: "hardlink to files in DIR when unchanged"
  aliases:
    - "--link-dest"
- name: compress
  type: string
  required: false
  default: null
  description: "compress file data during the transfer"
  aliases:
    - "-z"
    - "--compress"
- name: compress-choice
  type: string
  required: false
  default: null
  description: "choose the compression algorithm (aka --zc)"
  aliases:
    - "--compress-choice"
- name: compress-level
  type: integer
  required: false
  default: null
  description: "explicitly set compression level (aka --zl)"
  aliases:
    - "--compress-level"
- name: skip-compress
  type: array
  required: false
  default: null
  description: "skip compressing files with suffix in LIST"
  aliases:
    - "--skip-compress"
- name: cvs-exclude
  type: string
  required: false
  default: null
  description: "auto-ignore files in the same way CVS does"
  aliases:
    - "-C"
    - "--cvs-exclude"
- name: filter
  type: string
  required: false
  default: null
  description: "add a file-filtering RULE"
  aliases:
    - "-f"
    - "--filter"
- name: exclude
  type: string
  required: false
  default: null
  description: "exclude files matching PATTERN"
  aliases:
    - "--exclude"
- name: exclude-from
  type: file
  required: false
  default: null
  description: "read exclude patterns from FILE"
  aliases:
    - "--exclude-from"
- name: include
  type: string
  required: false
  default: null
  description: "don't exclude files matching PATTERN"
  aliases:
    - "--include"
- name: include-from
  type: file
  required: false
  default: null
  description: "read include patterns from FILE"
  aliases:
    - "--include-from"
- name: files-from
  type: file
  required: false
  default: null
  description: "read list of source-file names from FILE"
  aliases:
    - "--files-from"
- name: from0
  type: array
  required: false
  default: null
  description: "all *-from/filter files are delimited by 0s"
  aliases:
    - "-0"
    - "--from0"
- name: old-args
  type: string
  required: false
  default: null
  description: "disable the modern arg-protection idiom"
  aliases:
    - "--old-args"
- name: secluded-args
  type: string
  required: false
  default: null
  description: "use the protocol to safely send the args"
  aliases:
    - "-s"
    - "--secluded-args"
- name: trust-sender
  type: string
  required: false
  default: null
  description: "trust the remote sender's file list"
  aliases:
    - "--trust-sender"
- name: copy-as
  type: string
  required: false
  default: null
  description: "specify user & optional group for the copy"
  aliases:
    - "--copy-as"
- name: address
  type: string
  required: false
  default: null
  description: "bind address for outgoing socket to daemon"
  aliases:
    - "--address"
- name: port
  type: integer
  required: false
  default: null
  description: "specify double-colon alternate port number"
  aliases:
    - "--port"
- name: sockopts
  type: string
  required: false
  default: null
  description: "specify custom TCP options"
  aliases:
    - "--sockopts"
- name: blocking-io
  type: string
  required: false
  default: null
  description: "use blocking I/O for the remote shell"
  aliases:
    - "--blocking-io"
- name: outbuf
  type: integer
  required: false
  default: null
  description: "set out buffering to None, Line, or Block"
  aliases:
    - "--outbuf"
- name: stats
  type: string
  required: false
  default: null
  description: "give some file-transfer stats"
  aliases:
    - "--stats"
- name: flag-8
  type: string
  required: false
  default: null
  description: "leave high-bit chars unescaped in output"
  aliases:
    - "-8"
    - "--8-bit-output"
- name: human-readable
  type: string
  required: false
  default: null
  description: "output numbers in a human-readable format"
  aliases:
    - "-h"
    - "--human-readable"
- name: progress
  type: string
  required: false
  default: null
  description: "show progress during transfer"
  aliases:
    - "--progress"
- name: itemize-changes
  type: string
  required: false
  default: null
  description: "output a change-summary for all updates"
  aliases:
    - "-i"
    - "--itemize-changes"
- name: remote-option
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "-M"
    - "--remote-option"
- name: out-format
  type: string
  required: false
  default: null
  description: "output updates using the specified FORMAT"
  aliases:
    - "--out-format"
- name: log-file
  type: file
  required: false
  default: null
  description: "log what we're doing to the specified FILE"
  aliases:
    - "--log-file"
- name: log-file-format
  type: string
  required: false
  default: null
  description: "log updates using the specified FMT"
  aliases:
    - "--log-file-format"
- name: password-file
  type: file
  required: false
  default: null
  description: "read daemon-access password from FILE"
  aliases:
    - "--password-file"
- name: early-input
  type: file
  required: false
  default: null
  description: "use FILE for daemon's early exec input"
  aliases:
    - "--early-input"
- name: list-only
  type: string
  required: false
  default: null
  description: "list the files instead of copying them"
  aliases:
    - "--list-only"
- name: bwlimit
  type: number
  required: false
  default: null
  description: "limit socket I/O bandwidth"
  aliases:
    - "--bwlimit"
- name: stop-after
  type: string
  required: false
  default: null
  description: "Stop rsync after MINS minutes have elapsed"
  aliases:
    - "--stop-after"
- name: stop-at
  type: string
  required: false
  default: null
  description: "Stop rsync at the specified point in time"
  aliases:
    - "-m"
    - "-d"
    - "--stop-at"
- name: fsync
  type: string
  required: false
  default: null
  description: "fsync every written file"
  aliases:
    - "--fsync"
- name: write-batch
  type: file
  required: false
  default: null
  description: "write a batched update to FILE"
  aliases:
    - "--write-batch"
- name: only-write-batch
  type: file
  required: false
  default: null
  description: ""
  aliases:
    - "--only-write-batch"
    - "--write-batch"
- name: read-batch
  type: file
  required: false
  default: null
  description: "read a batched update from FILE"
  aliases:
    - "--read-batch"
- name: protocol
  type: integer
  required: false
  default: null
  description: "force an older protocol version to be used"
  aliases:
    - "--protocol"
- name: iconv
  type: file
  required: false
  default: null
  description: "request charset conversion of filenames"
  aliases:
    - "--iconv"
- name: checksum-seed
  type: integer
  required: false
  default: null
  description: "set block/file checksum seed (advanced)"
  aliases:
    - "--checksum-seed"
- name: ipv4
  type: string
  required: false
  default: null
  description: "prefer IPv4"
  aliases:
    - "-4"
    - "--ipv4"
- name: ipv6
  type: string
  required: false
  default: null
  description: "prefer IPv6"
  aliases:
    - "-6"
    - "--ipv6"
- name: version
  type: string
  required: false
  default: null
  description: "print the version + other info and exit"
  aliases:
    - "-V"
    - "--version"
- name: help
  type: string
  required: false
  default: null
  description: "show this help (* -h is help only on its own)"
  aliases:
    - "-h"
    - "--help"

execution:
  template: rsync {verbose} {info} {debug} {stderr} {quiet}
  sandbox: execFile
  timeout_seconds: 600
  shell: false
global_vars:
  target: ip
  user: user
  port: port
examples:
- description: Local directory sync
  command: rsync -av /source/dir/ /backup/dir/
- description: Remote sync over SSH
  command: rsync -avz /local/dir/ user@remote:/backup/dir/
- description: Pull remote directory to local
  command: rsync -avz user@remote:/source/dir/ /local/dir/
- description: Incremental backup with hardlinks
  command: rsync -av --link-dest=../previous /source/ /backup/current/
- description: Dry run to preview changes
  command: rsync -avn /source/ /destination/
- description: Sync with exclusions
  command: rsync -av --exclude='node_modules' --exclude='.git' /project/ /backup/
references:
- label: Rsync documentation
  url: https://rsync.samba.org/documentation.html
- label: Rsync tips and tricks
  url: https://linux.die.net/man/1/rsync
install:
- method: apt
  package_name: rsync
  commands:
  - apt-get install -y rsync
features:
- compression
- file-system
- local
- network-intensive
- remote
---

# Rsync — File Synchronization

Rsync is a fast, versatile file synchronization tool that transfers only the differences between source and destination (delta encoding), making repeated transfers extremely efficient.

## How It Works

1. **Scan** — Rsync examines source and destination files
2. **Delta** — Only the changed parts of files are transferred
3. **Apply** — Changes are written to the destination

## Key Features

| Feature | Description |
|---------|-------------|
| **Delta transfer** | Only transfers differences, not entire files |
| **Compression** | Optional `-z` flag for network-efficient transfer |
| **Preservation** | Maintains permissions, ownership, timestamps |
| **Remote sync** | Built-in SSH support for secure remote sync |
| **Incremental** | Hard-link based snapshots for backup rotation |

## Backup Strategies

### Simple Backup
```bash
rsync -av /home/user/ /backup/daily/
```

### Rotating Snapshots
```bash
# Create hardlink-based incremental backup
rsync -av --link-dest=../monday /source/ /backup/tuesday/

# Next day
rsync -av --link-dest=../tuesday /source/ /backup/wednesday/
```

### Remote Backup
```bash
# Push to remote
rsync -avz --delete /data/ user@backup-server:/backup/

# Pull from remote
rsync -avz user@server:/data/ /local/backup/
```

## Important Trailing Slash

```bash
# Copies the directory itself
rsync -av /source /destination  # → /destination/source/

# Copies the contents
rsync -av /source/ /destination  # → /destination/file1, ...
```

## Related Tools

- **[scp](../../remote/scp.md)** — Simple secure copy (simpler, no delta)
- **[rclone](../../sync/rclone.md)** — Cloud storage sync
- **[tar](../../archive/tar.md)** — Archive creation for offline transfer
