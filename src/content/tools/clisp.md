---
id: lang-lisp-clisp
namespace: lang:lisp:clisp
name: clisp
description: Common Lisp interpreter, can spawn a shell via run-shell-command.
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
  - clisp
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "clisp -x '(ext:run-shell-command \"/bin/sh\")(ext:exit)'"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via clisp
    command: clisp -x '(ext:run-shell-command "/bin/sh")(ext:exit)'
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/clisp/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "clisp"
    commands:
      - "apt-get install -y clisp"
---
