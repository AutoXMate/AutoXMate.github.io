---
id: system-resolve-systemd-resolve
namespace: system:resolve:systemd-resolve
name: systemd-resolve
description: DNS resolver from systemd; can read arbitrary files.
author: GTFOBins
version: 1.0.0
capabilities:
- security.execution.command
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
- systemd-resolve
parameters: []
features:
- file-system
- local
- pipes-stdin
execution:
  template: systemd-resolve
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Leverage less capabilities
  command: systemd-resolve --status
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/systemd-resolve/
techniques:
- execution
install:
- method: apt
  package_name: systemd
  commands:
  - apt-get install -y systemd
---

# systemd-resolve

systemd-resolve is a command-line utility. DNS resolution utility from systemd Can leverage capabilities from: less.
