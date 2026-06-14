---
id: package-rpm-rpm
namespace: package:rpm:rpm
name: rpm
description: RPM package manager, can execute commands via pre/post-install scripts.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - system.file.read
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
  - rpmdb
  - rpmquery
  - rpmverify
  - dnf
  - yum
  - zypper
artifacts: []
workflow_edges:
  produces:
    - file-content
    - command-execution
  consumes:
    - file
    - execution-context
contract:
  inputs: []
  outputs:
    - type: process.output
      description: File or command output
  side_effects:
    - process_spawn
    - filesystem_write
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
  - rpm
  - dnf
  - yum
  - zypper
  - Bash
  - execFile
parameters: []
features:
  - file-system
  - requires-root
  - process-manip
execution:
  template: "rpm -i /path/to/package.rpm"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Read a file via rpm
    command: rpm -i /path/to/file
  - description: Execute command via rpm with crafted RPM
    command: rpm -i /path/to/crafted.rpm
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/rpm/"
techniques:
  - collection
  - execution
install:
  - method: apt
    package_name: "rpm"
    commands:
      - "apt-get install -y rpm"
---
