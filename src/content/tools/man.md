---
id: system-documentation-man
namespace: system:documentation:man
name: man
description: Display system manual pages, can read files and spawn shells via pager or groff.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - system.file.read
  - security.privilege-escalation.shell
platforms:
  - linux
  - macos
  - cross-platform
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - less
  - groff
  - info
artifacts: []
workflow_edges:
  produces:
    - file-content
    - shell-access
  consumes:
    - input-file
contract:
  inputs:
    - type: system.file.path
      description: Path to file display as man page
  outputs:
    - type: system.file.content
      description: Formatted file content in pager
      mime: text/plain
  side_effects:
    - process_spawn
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
  - man
  - Bash
  - execFile
parameters:
  - name: H
    type: string
    required: false
    description: "HTML browser command"
    aliases:
      - -H
features:
  - process-manip
execution:
  template: "man {H}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read arbitrary file formatted as man page in pager
    command: man /path/to/input-file
  - description: Spawn shell via -H browser option with GNU troff
    command: man '-H/bin/sh #' man
  - description: Open man page in less pager (can escape to shell)
    command: man man
references:
  - label: "man man page"
    url: "https://man7.org/linux/man-pages/man1/man.1.html"
techniques:
  - privilege-escalation
  - execution
  - collection
install:
    - method: apt
      package_name: "man-db"
      commands:
        - "apt-get install -y man-db"
---


# man — Manual Page Displayer

man displays system manual pages. It can read arbitrary files by passing a path as an argument (the file is formatted and shown in the pager). The `-H` option with GNU troff can execute commands, and the default pager (less) can be escaped to shell.
