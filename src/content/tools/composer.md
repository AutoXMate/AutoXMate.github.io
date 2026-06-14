---
id: dev-php-composer
namespace: dev:php:composer
name: composer
description: PHP dependency manager, can spawn a shell via composer run-script.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
platforms:
  - linux
  - macos
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - php
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
    memory_mb: 16
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: none
  disk_io: low
allowed-tools:
  - composer
  - php
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "composer run-script x"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via composer run-script
    command: |
      echo '{"scripts":{"x":"/bin/sh"}}' >composer.json
      composer run-script x
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/composer/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "composer"
    commands:
      - "apt-get install -y composer"
---
