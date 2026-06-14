---
id: build-assembler-as
namespace: build:assembler:as
name: as
description: GNU assembler that can read files via the @file directive, leaking lines as error messages.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - system.file.read
  - build.compile.assembly
platforms:
  - linux
  - cross-platform
risk_level: low
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - gcc
  - ld
artifacts: []
workflow_edges:
  produces:
    - file-content
  consumes:
    - input-file
contract:
  inputs:
    - type: system.file.path
      description: Path to file read via @file directive
  outputs:
    - type: system.file.content
      description: File content leaked as error messages
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
  - as
  - Bash
  - execFile
parameters:
  - name: at-file
    type: file
    required: false
    description: "Read options from file using @ prefix"
    template_key: file
    aliases:
      - "@"
features: []
execution:
  template: "as {at-file}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read arbitrary file via @file directive, leaked as error messages
    command: as @/path/to/input-file
references:
  - label: "as man page"
    url: "https://man7.org/linux/man-pages/man1/as.1.html"
techniques:
  - collection
install:
    - method: apt
      package_name: "binutils"
      commands:
        - "apt-get install -y binutils"
---


# as — GNU Assembler

The GNU assembler converts assembly source code to object code. The `@file` directive reads options from a file, which can be abused to leak arbitrary file contents through error messages when used with elevated privileges.
