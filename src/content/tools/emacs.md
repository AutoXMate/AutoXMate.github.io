---
id: editor-emacs
namespace: editor:text:emacs
name: emacs
description: Extensible text editor that can read, write files, and spawn interactive shells.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - system.file.read
  - system.file.write
  - security.privilege-escalation.shell
  - security.execution.command
platforms:
  - linux
  - macos
  - windows
  - cross-platform
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - vim
  - nano
  - vi
artifacts: []
workflow_edges:
  produces:
    - file-content
    - file-write
    - shell-access
  consumes:
    - input-file
contract:
  inputs:
    - type: system.file.path
      description: Path to file to edit
  outputs:
    - type: system.file.content
      description: File content displayed in editor
      mime: text/plain
  side_effects:
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 32
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 32
  network: low
  disk_io: low
allowed-tools:
  - emacs
  - Bash
  - execFile
parameters:
  - name: Q
    type: string
    required: false
    description: "Quick start (no init file)"
    aliases:
      - -Q
  - name: nw
    type: string
    required: false
    description: "No window system (terminal mode)"
    aliases:
      - -nw
  - name: eval
    type: string
    required: false
    description: "Evaluate Lisp expression"
    aliases:
      - --eval
features:
  - process-manip
execution:
  template: "emacs {Q} {nw} {eval}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read arbitrary file in emacs terminal interface
    command: emacs /path/to/input-file
  - description: Write arbitrary data to file in emacs
    command: |-
      emacs /path/to/output-file
      DATA
      C-x C-s
  - description: Spawn interactive shell inside emacs terminal
    command: emacs -Q -nw --eval '(term "/bin/sh")'
references:
  - label: "GNU Emacs documentation"
    url: "https://www.gnu.org/software/emacs/manual/"
techniques:
  - privilege-escalation
  - execution
  - collection
install:
    - method: apt
      package_name: "emacs"
      commands:
        - "apt-get install -y emacs"
---


# Emacs — Extensible Text Editor

Emacs is a highly extensible text editor. When used with sudo or elevated privileges, all functions operate within the Emacs terminal interface, allowing file read, file write, and shell spawning via `--eval '(term "/bin/sh")'`.
