---
id: system-kernel-dmesg
namespace: system:kernel:dmesg
name: dmesg
description: Print kernel ring buffer messages, can read files via raw format flag
  and spawn less pager.
author: Repository Maintainers
version: 1.0.0
capabilities:
- system.file.read
- system.kernel.log
- security.privilege-escalation.shell
platforms:
- linux
risk_level: low
trust_level: community
execution_policy: enabled
architectures:
- amd64
- arm64
dependencies: []
related_tools:
- journalctl
- less
artifacts:
- type: system.kernel.log
  description: Kernel ring buffer messages
  mime: text/plain
  trust_level: community
workflow_edges:
  produces:
  - kernel-log
  - file-content
  consumes: []
contract:
  inputs:
  - type: system.file.path
    description: Path to file read via -rF flag
  outputs:
  - type: system.kernel.log
    description: Kernel log or file content
    mime: text/plain
  side_effects: []
  resource_cost:
    cpu: low
    memory_mb: 4
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 4
  network: low
  disk_io: low
allowed-tools:
- dmesg
- Bash
- execFile
parameters:
- name: rF
  type: file
  required: false
  description: Read raw log from file
  aliases:
  - -rF
- name: H
  type: string
  required: false
  description: Human readable output
  aliases:
  - -H
features:
- file-system
- interactive
- local
- pipes-stdout
- process-manip
- requires-root
execution:
  template: dmesg {rF} {H}
  sandbox: execFile
  timeout_seconds: 10
  shell: false
global_vars: {}
examples:
- description: Read arbitrary file via raw format flag
  command: dmesg -rF /path/to/input-file
- description: Spawn less pager via human-readable output
  command: dmesg -H
references:
- label: dmesg man page
  url: https://man7.org/linux/man-pages/man1/dmesg.1.html
techniques:
- collection
- privilege-escalation
install:
- method: apt
  package_name: util-linux
  commands:
  - apt-get install -y util-linux
---

# dmesg — Kernel Ring Buffer

dmesg prints kernel ring buffer messages. The `-rF` flag reads from a file as raw log data, useful for file read. The `-H` flag spawns a less pager for interactive browsing, which can be escaped to shell.
