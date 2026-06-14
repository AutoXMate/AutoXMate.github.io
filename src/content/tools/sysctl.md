---
id: system-kernel-sysctl
namespace: system:kernel:sysctl
name: sysctl
description: "Configure kernel parameters at runtime; can read and write files."
author: GTFOBins
version: 1.0.0
capabilities:
- security.execution.command
- system.file.read
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
- sysctl
parameters: []
features: []
execution:
  template: sysctl
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute arbitrary commands (sudo, suid)
  command: sysctl 'kernel.core_pattern=|/path/to/command'
- description: Read arbitrary files (sudo, suid, unprivileged)
  command: sysctl -n "/../../path/to/input-file"
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/sysctl/
techniques:
- execution
- collection
install:
- method: apt
  package_name: procps
  commands:
  - apt-get install -y procps
---


# sysctl

sysctl is a command-line utility. Configure kernel parameters at runtime; can also execute arbitrary commands, read arbitrary files.
