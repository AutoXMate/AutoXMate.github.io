---
id: audio-oss-aoss
namespace: audio:oss:aoss
name: aoss
description: OSS sound wrapper that can spawn a shell by wrapping /bin/sh.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
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
related_tools: []
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
    memory_mb: 2
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 2
  network: low
  disk_io: low
allowed-tools:
  - aoss
  - Bash
  - execFile
parameters: []
features: []
execution:
  template: "aoss {0}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn interactive shell via OSS sound wrapper
    command: aoss /bin/sh
references:
  - label: "aoss man page"
    url: "https://man7.org/linux/man-pages/man1/aoss.1.html"
techniques:
  - privilege-escalation
  - execution
install:
    - method: apt
      package_name: "oss-compat"
      commands:
        - "apt-get install -y oss-compat"
---


# aoss — OSS Sound Wrapper

aoss is used to run programs with OSS sound support. When installed with SUID or available via sudo, it can spawn a shell by wrapping `/bin/sh`.
