---
id: security-capabilities-capsh
namespace: security:capabilities:capsh
name: capsh
description: Linux capability shell wrapper that can spawn a privileged shell by dropping or manipulating capabilities.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
  - security.capabilities.manage
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
  - setcap
  - getcap
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
    memory_mb: 4
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 4
  network: low
  disk_io: low
allowed-tools:
  - capsh
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "capsh {0}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell with current capabilities
    command: capsh --
  - description: Spawn a root shell with SUID (set gid and uid to 0)
    command: capsh --gid=0 --uid=0 --
references:
  - label: "capsh man page"
    url: "https://man7.org/linux/man-pages/man1/capsh.1.html"
techniques:
  - privilege-escalation
  - execution
install:
    - method: apt
      package_name: "libcap2-bin"
      commands:
        - "apt-get install -y libcap2-bin"
---


# capsh — Capability Shell

capsh is a wrapper for manipulating Linux capabilities and spawning shells. When installed with SUID, it can spawn a root shell by setting gid and uid to 0.
