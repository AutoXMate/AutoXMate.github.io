---
id: network-mqtt-mosquitto
namespace: network:mqtt:mosquitto
name: mosquitto
description: MQTT message broker, can execute commands via config.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.execution.command
platforms:
  - linux
  - bsd
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
    - command-execution
  consumes:
    - execution-context
contract:
  inputs: []
  outputs:
    - type: process.output
      description: Command execution output
  side_effects:
    - process_spawn
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
  - mosquitto
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "mosquitto -c /path/to/config"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute command via mosquitto
    command: mosquitto -c /path/to/config
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/mosquitto/"
techniques:
  - execution
install:
  - method: apt
    package_name: "mosquitto"
    commands:
      - "apt-get install -y mosquitto"
---
