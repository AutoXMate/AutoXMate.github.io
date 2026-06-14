---
id: crypto-pki-easyrsa
namespace: crypto:pki:easyrsa
name: easyrsa
description: Certificate authority management, can execute commands via openssl config.
author: "GTFOBins"
version: "1.0.0"
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
related_tools:
  - openssl
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
  resource_cost:
    cpu: low
    memory_mb: 4
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 4
  network: none
  disk_io: low
allowed-tools:
  - easyrsa
  - openssl
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "easyrsa --vars=<(echo 'set_var EASYRSA_OPENSSL /bin/sh')"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute command via easyrsa with custom openssl
    command: easyrsa --vars=<(echo 'set_var EASYRSA_OPENSSL /bin/sh')
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/easyrsa/"
techniques:
  - execution
install:
  - method: apt
    package_name: "easy-rsa"
    commands:
      - "apt-get install -y easy-rsa"
---
