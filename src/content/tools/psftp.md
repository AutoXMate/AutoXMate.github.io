---
id: network-transfer-psftp
namespace: network:transfer:psftp
name: psftp
description: PuTTY SFTP client, can download and upload files.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - network.transfer.download
  - network.transfer.upload
platforms:
  - linux
  - macos
  - bsd
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - sftp
  - scp
artifacts: []
workflow_edges:
  produces:
    - file-content
  consumes:
    - file
contract:
  inputs: []
  outputs:
    - type: process.output
      description: File transfer output
  side_effects:
    - network_traffic
  resource_cost:
    cpu: low
    memory_mb: 4
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 4
  network: low
  disk_io: low
allowed-tools:
  - psftp
  - sftp
  - scp
  - Bash
  - execFile
parameters: []
features:
  - file-system
execution:
  template: "psftp user@host -b /path/to/batch"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Download a file via psftp
    command: echo 'get /remote/file /local/file' | psftp user@host
  - description: Upload a file via psftp
    command: echo 'put /local/file /remote/file' | psftp user@host
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/psftp/"
techniques:
  - exfiltration
install:
  - method: apt
    package_name: "putty-tools"
    commands:
      - "apt-get install -y putty-tools"
---
