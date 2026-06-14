---
id: runtime-php-php
namespace: runtime:php:php
name: php
description: PHP interpreter, can execute PHP code and spawn shells.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
  - system.file.read
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
related_tools: []
artifacts: []
workflow_edges:
  produces:
    - shell-access
    - file-content
  consumes:
    - execution-context
    - file
contract:
  inputs: []
  outputs:
    - type: process.output
      description: PHP code output
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
  - php
  - Bash
  - execFile
parameters: []
features:
  - interactive
  - file-system
  - process-manip
execution:
  template: 'php -r "system(\"/bin/sh\");"'
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via php
    command: php -r 'system("/bin/sh");'
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/php/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "php-cli"
    commands:
      - "apt-get install -y php-cli"
---
