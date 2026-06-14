---
id: dev-infra-terraform
namespace: dev:infra:terraform
name: terraform
description: Infrastructure-as-code provisioning tool; can spawn a shell.
author: GTFOBins
version: 1.0.0
capabilities:
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
- terraform
parameters: []
features:
- file-system
- interactive
- local
- process-manip
execution:
  template: terraform
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Read arbitrary files (sudo, suid, unprivileged)
  command: 'terraform console

    file("/path/to/input-file")'
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/terraform/
techniques:
- collection
install:
- method: apt
  package_name: terraform
  commands:
  - apt-get install -y terraform
---

# terraform

terraform is a command-line utility. Infrastructure-as-code provisioning tool; can also read arbitrary files.
