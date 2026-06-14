---
id: security-sandbox-firejail
namespace: security:sandbox:firejail
name: firejail
description: SUID sandbox program that can escape confinement to spawn a privileged shell.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
  - security.sandbox.escape
platforms:
  - linux
risk_level: high
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - docker
  - nsenter
artifacts: []
workflow_edges:
  produces:
    - shell-access
  consumes: []
contract:
  inputs: []
  outputs:
    - type: process.output
      description: Shell output
  side_effects:
    - process_spawn
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
  - firejail
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "firejail {0}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell inside firejail sandbox (potentially break out)
    command: firejail /bin/sh
references:
  - label: "Firejail documentation"
    url: "https://firejail.wordpress.com/"
techniques:
  - privilege-escalation
  - execution
install:
    - method: apt
      package_name: "firejail"
      commands:
        - "apt-get install -y firejail"
---


# Firejail — SUID Sandbox

Firejail is a SUID sandbox program that restricts the environment of untrusted applications. When the binary itself is available via sudo, it can be used to spawn a shell — and depending on the configuration, potentially escape confinement.
