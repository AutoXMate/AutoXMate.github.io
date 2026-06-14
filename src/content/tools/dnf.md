---
id: package-rpm-dnf
namespace: package:rpm:dnf
name: dnf
description: Fedora package manager, can execute commands by installing crafted RPM packages.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.execution.command
platforms:
  - linux
risk_level: high
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - rpm
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
  - dnf
  - Bash
  - execFile
parameters: []
features:
  - requires-root
  - process-manip
execution:
  template: "dnf install -y package.rpm --disablerepo=*"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Execute a command via dnf with crafted RPM
    command: |
      echo '#!/bin/sh
      /path/to/command' >x.sh
      fpm -n x -s dir -t rpm -a all --before-install x.sh .
      dnf install -y x-1.0-1.noarch.rpm --disablerepo=*
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/dnf/"
techniques:
  - execution
install:
  - method: dnf
    package_name: "dnf"
    commands:
      - "dnf install -y dnf"
---
