---
id: shell-csh-tcsh
namespace: shell:csh:tcsh
name: tcsh
description: "Enhanced C shell; can execute commands, read/write files, and spawn shells."
author: GTFOBins
version: 1.0.0
capabilities:
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
- tcsh
parameters: []
features: []
execution:
  template: tcsh
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Write to arbitrary files (sudo, suid, unprivileged)
  command: tcsh -c 'echo DATA >/path/to/output-file'
- description: Spawn an interactive shell (sudo, suid, unprivileged)
  command: tcsh
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/tcsh/
techniques:
- collection
- exfiltration
- privilege-escalation
- execution
install:
- method: apt
  package_name: tcsh
  commands:
  - apt-get install -y tcsh
---


# tcsh

tcsh is a command-line utility. Enhanced C shell with file completion and editing; can also write to arbitrary files, spawn an interactive shell.
