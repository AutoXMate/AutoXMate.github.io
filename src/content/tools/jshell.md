---
id: runtime-jdk-jshell
namespace: runtime:jdk:jshell
name: jshell
description: JShell (Java REPL), can execute Java code and spawn shells.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
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
  - java
  - jjs
  - jrunscript
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
  resource_cost:
    cpu: low
    memory_mb: 32
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 32
  network: none
  disk_io: low
allowed-tools:
  - jshell
  - java
  - Bash
  - execFile
parameters: []
features:
  - interactive
  - process-manip
execution:
  template: "jshell -R-e 'Runtime.getRuntime().exec(\"/bin/sh\")'"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via jshell
    command: jshell -R-e 'Runtime.getRuntime().exec("/bin/sh")'
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/jshell/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "jdk"
    commands:
      - "apt-get install -y default-jdk"
---
