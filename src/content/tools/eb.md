---
id: system-log-eb
namespace: system:log:eb
name: eb
description: "AWS Elastic Beanstalk CLI for managing environments; can read logs via journalctl."
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
- eb
parameters: []
features: []
execution:
  template: eb
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Leverage journalctl capabilities
  command: eb logs
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/eb/
techniques:
- execution
install:
- method: apt
  package_name: awsebcli
  commands:
  - apt-get install -y awsebcli
---


# eb

eb is a command-line utility. AWS Elastic Beanstalk CLI log viewer Can leverage capabilities from: journalctl.
