---
id: build-compiler-gcc
namespace: build:compiler:gcc
name: gcc
description: GNU C compiler that can read files, delete files, and spawn shells via wrapper/plugin options.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - system.file.read
  - system.file.write
  - security.privilege-escalation.shell
  - build.compile.c
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
  - g++
  - as
  - ld
artifacts:
  - type: build.compiled.binary
    description: Compiled executable
    mime: application/x-executable
    trust_level: community
workflow_edges:
  produces:
    - compiled-binary
    - file-content
    - shell-access
  consumes:
    - source-file
contract:
  inputs:
    - type: system.file.path
      description: Path to source file
  outputs:
    - type: build.compiled.binary
      description: Compiled output
      mime: application/x-executable
  side_effects:
    - process_spawn
  resource_cost:
    cpu: high
    memory_mb: 128
    network: low
    disk_io: medium
resource_profile:
  cpu: high
  memory_mb: 128
  network: low
  disk_io: medium
allowed-tools:
  - gcc
  - Bash
  - execFile
parameters:
  - name: x
    type: string
    required: false
    description: "Specify language"
    aliases:
      - -x
  - name: E
    type: string
    required: false
    description: "Preprocess only"
    aliases:
      - -E
  - name: at-file
    type: file
    required: false
    description: "Read options from file"
    template_key: file
    aliases:
      - "@"
  - name: o
    type: file
    required: false
    description: "Output file"
    aliases:
      - -o
  - name: wrapper
    type: string
    required: false
    description: "Invoke command with wrapper"
    aliases:
      - -wrapper
features:
  - process-manip
execution:
  template: "gcc {x} {E} {o} {wrapper}"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Read arbitrary file via C preprocessing
    command: gcc -x c -E /path/to/input-file
  - description: Read file via @file directive leaked as error messages
    command: gcc @/path/to/input-file
  - description: Spawn interactive shell via wrapper
    command: gcc -wrapper /bin/sh,-s x
references:
  - label: "gcc man page"
    url: "https://man7.org/linux/man-pages/man1/gcc.1.html"
techniques:
  - privilege-escalation
  - execution
  - collection
install:
    - method: apt
      package_name: "gcc"
      commands:
        - "apt-get install -y gcc"
---


# gcc — GNU C Compiler

gcc is the GNU C compiler. When available via sudo, it can read arbitrary files through preprocessing (`-x c -E`) or the `@file` directive, delete files, and spawn shells via the `-wrapper` option.
