---
id: dev-vm-vagrant
namespace: dev:vm:vagrant
name: vagrant
description: "Development environment virtualization tool; can spawn a shell."
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
- vagrant
parameters: []
features: []
execution:
  template: vagrant
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Leverage ruby capabilities
  command: 'echo ''...'' >Vagrantfile

    vagrant up'
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/vagrant/
techniques:
- execution
install:
- method: apt
  package_name: vagrant
  commands:
  - apt-get install -y vagrant
---


# vagrant

vagrant is a command-line utility. Development environment virtualization tool Can leverage capabilities from: ruby.
