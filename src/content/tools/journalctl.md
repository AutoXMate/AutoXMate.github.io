---
id: system-service-journalctl
namespace: system:service:journalctl
name: journalctl
description: Query the systemd journal
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - system.service.journalctl
platforms:
  - linux
risk_level: medium
trust_level: verified
execution_policy: enabled
architectures:
  - amd64
  - arm64
features:
  - local
  - requires-root
techniques:
  - execution
  - persistence
parameters:
  - name: system
    type: string
    required: false
    description: "Show the system journal"
    aliases:
      - --system
  - name: user
    type: string
    required: false
    description: "Show the user journal for the current user"
    aliases:
      - --user
  - name: machine
    type: string
    required: false
    description: "Operate on local container"
    aliases:
      - -M
      - --machine
  - name: merge
    type: string
    required: false
    description: "Show entries from all available journals"
    aliases:
      - -m
      - --merge
  - name: directory
    type: file
    required: false
    description: "Show journal files from directory"
    aliases:
      - -D
      - --directory
  - name: file
    type: file
    required: false
    description: "Show journal file"
    aliases:
      - -i
      - --file
  - name: root
    type: file
    required: false
    description: "Operate on an alternate filesystem root"
    aliases:
      - --root
  - name: image
    type: file
    required: false
    description: "Operate on disk image as filesystem root"
    aliases:
      - --image
  - name: image-policy
    type: string
    required: false
    description: "Specify disk image dissection policy"
    aliases:
      - --image-policy
  - name: namespace
    type: string
    required: false
    description: "Show journal data from specified journal namespace"
    aliases:
      - --namespace
  - name: since
    type: string
    required: false
    description: "Show entries not older than the specified date"
    aliases:
      - -S
      - --since
  - name: until
    type: string
    required: false
    description: "Show entries not newer than the specified date"
    aliases:
      - -U
      - --until
  - name: cursor
    type: string
    required: false
    description: "Show entries starting at the specified cursor"
    aliases:
      - -c
      - --cursor
  - name: after-cursor
    type: string
    required: false
    description: "Show entries after the specified cursor"
    aliases:
      - --after-cursor
  - name: cursor-file
    type: file
    required: false
    description: "Show entries after cursor in FILE and update FILE"
    aliases:
      - --cursor-file
  - name: boot
    type: string
    required: false
    description: "Show current boot or the specified boot"
    aliases:
      - -b
      - --boot
  - name: unit
    type: string
    required: false
    description: "Show logs from the specified unit"
    aliases:
      - -u
      - --unit
  - name: user-unit
    type: string
    required: false
    description: "Show logs from the specified user unit"
    aliases:
      - --user-unit
  - name: invocation
    type: string
    required: false
    description: "Show logs from the matching invocation ID"
    aliases:
      - --invocation
  - name: identifier
    type: string
    required: false
    description: "Show entries with the specified syslog identifier"
    aliases:
      - -t
      - --identifier
  - name: exclude-identifier
    type: string
    required: false
    description: "Hide entries with the specified syslog identifier"
    aliases:
      - -T
      - --exclude-identifier
  - name: priority
    type: integer
    required: false
    description: "Show entries within the specified priority range"
    aliases:
      - -p
      - --priority
  - name: facility
    type: string
    required: false
    description: "Set the facility parameter"
    aliases:
      - --facility
  - name: grep
    type: string
    required: false
    description: "Show entries with MESSAGE matching PATTERN"
    aliases:
      - -g
      - --grep
  - name: case-sensitive
    type: string
    required: false
    description: "Set the case-sensitive parameter"
    aliases:
      - --case-sensitive
  - name: dmesg
    type: string
    required: false
    description: "Show kernel message log from the current boot"
    aliases:
      - -k
      - --dmesg
  - name: output
    type: string
    required: false
    description: "Change journal output mode (short, short-precise"
    aliases:
      - -o
      - --output
  - name: output-fields
    type: array
    required: false
    description: "Select fields to print in verbose/export/json modes"
    aliases:
      - --output-fields
  - name: lines
    type: integer
    required: false
    description: "Number of journal entries to show"
    aliases:
      - -n
      - --lines
  - name: reverse
    type: string
    required: false
    description: "Show the newest entries first"
    aliases:
      - -r
      - --reverse

  - name: all
    type: string
    required: false
    default: null
    description: "Show all fields, including long and unprintable"
    aliases:
      - "-a"
      - "--all"
  - name: catalog
    type: string
    required: false
    default: null
    description: "Add message explanations where available"
    aliases:
      - "-x"
      - "--catalog"
  - name: disk-usage
    type: string
    required: false
    default: null
    description: "Show total disk usage of all journal files"
    aliases:
      - "--disk-usage"
  - name: dump_catalog
    type: boolean
    required: false
    description: "Show entries in the message catalog"
    aliases:
      - "--dump-catalog"
  - name: field
    type: string
    required: false
    default: null
    description: "List all values that a specified field takes"
    aliases:
      - "-F"
      - "--field"
  - name: fields
    type: string
    required: false
    default: null
    description: "List all field names currently used"
    aliases:
      - "-N"
      - "--fields"
  - name: follow
    type: string
    required: false
    default: null
    description: "Follow the journal"
    aliases:
      - "-f"
      - "--follow"
  - name: force
    type: string
    required: false
    default: null
    description: "Override of the FSS key pair with --setup-keys"
    aliases:
      - "--force"
  - name: help
    type: string
    required: false
    default: null
    description: "Show this help text"
    aliases:
      - "-h"
      - "--help"
  - name: interval
    type: number
    required: false
    default: null
    description: "Time interval for changing the FSS sealing key"
    aliases:
      - "--interval"
  - name: list-boots
    type: string
    required: false
    default: null
    description: "Show terse information about recorded boots"
    aliases:
      - "--list-boots"
  - name: list-invocations
    type: string
    required: false
    default: null
    description: "Show invocation IDs of specified unit"
    aliases:
      - "--list-invocations"
  - name: list-namespaces
    type: array
    required: false
    default: null
    description: "Show list of journal namespaces"
    aliases:
      - "--list-namespaces"
  - name: list_catalog
    type: boolean
    required: false
    description: "Show all message IDs in the catalog"
    aliases:
      - "--list-catalog"
  - name: no-full
    type: string
    required: false
    default: null
    description: "Ellipsize fields"
    aliases:
      - "--no-full"
  - name: no-hostname
    type: string
    required: false
    default: null
    description: "Suppress output of hostname field"
    aliases:
      - "-W"
      - "--no-hostname"
  - name: no-pager
    type: string
    required: false
    default: null
    description: "Do not pipe output into a pager"
    aliases:
      - "--no-pager"
  - name: no-tail
    type: string
    required: false
    default: null
    description: "Show all lines, even in follow mode"
    aliases:
      - "--no-tail"
  - name: pager-end
    type: string
    required: false
    default: null
    description: "Immediately jump to the end in the pager"
    aliases:
      - "-e"
      - "--pager-end"
  - name: quiet
    type: string
    required: false
    default: null
    description: "Do not show info messages and privilege warning"
    aliases:
      - "-q"
      - "--quiet"
  - name: relinquish-var
    type: string
    required: false
    default: null
    description: "Stop logging to disk, log to temporary file system"
    aliases:
      - "--relinquish-var"
  - name: setup_keys
    type: boolean
    required: false
    description: "Generate a new FSS key pair"
    aliases:
      - "--setup-keys"
  - name: show-cursor
    type: string
    required: false
    default: null
    description: "Print the cursor after all the entries"
    aliases:
      - "--show-cursor"
  - name: smart-relinquish-var
    type: string
    required: false
    default: null
    description: "--flush Flush all journal data from /run into /var --rotate Request immediate rotation of the journal files --header Show journal header information --list-catalog Show all message IDs in the catalog --dump-catalog Show entries in the message catalog --update-catalog Update the message catalog database --setup-keys Generate a new FSS key pair"
    aliases:
      - "--smart-relinquish-var"
  - name: sync
    type: string
    required: false
    default: null
    description: "Synchronize unwritten journal messages to disk"
    aliases:
      - "--sync"
  - name: synchronize-on-exit
    type: string
    required: false
    default: null
    description: "Wait for Journal synchronization before exiting"
    aliases:
      - "--synchronize-on-exit"
  - name: truncate-newline
    type: string
    required: false
    default: null
    description: "Truncate entries by first newline character"
    aliases:
      - "--truncate-newline"
  - name: update_catalog
    type: boolean
    required: false
    description: "Update the message catalog database"
    aliases:
      - "--update-catalog"
  - name: utc
    type: string
    required: false
    default: null
    description: "Express time in Coordinated Universal Time (UTC)"
    aliases:
      - "--utc"
  - name: vacuum-files
    type: integer
    required: false
    default: null
    description: "Leave only the specified number of journal files"
    aliases:
      - "--vacuum-files"
  - name: vacuum-size
    type: integer
    required: false
    default: null
    description: "Reduce disk usage below specified size"
    aliases:
      - "--vacuum-size"
  - name: vacuum-time
    type: number
    required: false
    default: null
    description: "Remove journal files older than specified time"
    aliases:
      - "--vacuum-time"
  - name: verify
    type: string
    required: false
    default: null
    description: "Verify journal file consistency"
    aliases:
      - "--verify"
  - name: verify-key
    type: string
    required: false
    default: null
    description: "Specify FSS verification key"
    aliases:
      - "--verify-key"
  - name: version
    type: string
    required: false
    default: null
    description: "Show package version"
    aliases:
      - "--version"

execution:
  template: "journalctl --system {system} --user {user} -M {machine} -m {merge} -D
    {directory}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Basic usage with system"
    command: "journalctl ${system}"
  - description: "Display help message"
    command: "journalctl --help"
related_tools:
  - system-service-systemctl
install:
    - method: apt
      package_name: "systemd"
      commands:
        - "apt-get install -y systemd"
---


# journalctl — Query the systemd journal

## Overview

`journalctl` is a command-line utility for query the systemd journal.

## Usage

```
journalctl --system {system} --user {user} -M {machine} -m {merge} -D {directory}
```
