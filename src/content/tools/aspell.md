---
id: text-aspell
namespace: text:spell:aspell
name: aspell
description: Interactive spell checker that can read arbitrary files via its TUI or
  config file parsing.
author: Repository Maintainers
version: 1.0.0
capabilities:
- system.file.read
- text.spellcheck
platforms:
- linux
- macos
- cross-platform
risk_level: low
trust_level: community
execution_policy: enabled
architectures:
- amd64
- arm64
dependencies: []
related_tools:
- ispell
artifacts: []
workflow_edges:
  produces:
  - file-content
  consumes:
  - input-file
contract:
  inputs:
  - type: system.file.path
    description: Path to file to spell-check
  outputs:
  - type: system.file.content
    description: File content displayed in TUI or as error
    mime: text/plain
  side_effects: []
  resource_cost:
    cpu: low
    memory_mb: 8
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 8
  network: low
  disk_io: low
allowed-tools:
- aspell
- Bash
- execFile
parameters:
- name: c
  type: file
  required: false
  description: Check a file in interactive mode
  aliases:
  - -c
- name: conf
  type: file
  required: false
  description: Config file path
  aliases:
  - --conf
features:
- file-system
- interactive
- local
execution:
  template: aspell {c} {conf}
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Open a file in the interactive spell checker TUI
  command: aspell -c /path/to/input-file
- description: Leak file content through config parsing error message
  command: aspell --conf /path/to/input-file
references:
- label: aspell man page
  url: https://man7.org/linux/man-pages/man1/aspell.1.html
techniques:
- collection
install:
- method: apt
  package_name: aspell
  commands:
  - apt-get install -y aspell
---

# aspell — Interactive Spell Checker

aspell is an interactive spell checker. The `-c` flag opens a file in the spell checker TUI, useful for reading files when used with elevated privileges. The `--conf` flag leaks file contents through error messages.
