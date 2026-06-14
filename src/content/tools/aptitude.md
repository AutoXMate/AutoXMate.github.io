---
id: package-apt-aptitude
namespace: package:apt:aptitude
name: aptitude
description: APT package manager with a text interface that can spawn a less pager to read files.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - system.package.install
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
  - apt
  - apt-get
artifacts: []
workflow_edges:
  produces:
    - file-content
  consumes: []
contract:
  inputs: []
  outputs:
    - type: process.output
      description: File content via pager
      mime: text/plain
  side_effects:
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 16
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: low
  disk_io: low
allowed-tools:
  - aptitude
  - Bash
  - execFile
parameters: []
features: []
execution:
  template: "aptitude {0}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read changelogs via less pager
    command: aptitude changelog aptitude
references:
  - label: "aptitude documentation"
    url: "https://wiki.debian.org/Aptitude"
techniques:
  - privilege-escalation
  - execution
install:
    - method: apt
      package_name: "aptitude"
      commands:
        - "apt-get install -y aptitude"
---


# aptitude — APT Package Manager Interface

aptitude is a text-based interface to the APT package management system. The `changelog` command opens a less pager, which can be used to read arbitrary files or escape to shell (`!command`) when the binary has elevated privileges.
