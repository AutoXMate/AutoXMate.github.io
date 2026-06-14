---
id: shell-yash-yash
namespace: shell:yash:yash
name: yash
description: "POSIX-compliant shell; can execute commands, read/write files, and spawn shells."
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
- yash
parameters: []
features: []
execution:
  template: yash
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Spawn an interactive shell (sudo, suid, unprivileged)
  command: yash
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/yash/
techniques:
- privilege-escalation
- execution
install:
- method: apt
  package_name: yash
  commands:
  - apt-get install -y yash
---


# yash

yash is a command-line utility. Yet another shell (POSIX-compliant); can also spawn an interactive shell.
