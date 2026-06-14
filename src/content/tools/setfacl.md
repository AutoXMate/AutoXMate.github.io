---
id: system-file-setfacl
namespace: system:file:setfacl
name: setfacl
description: Set file ACLs, can read files.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - system.file.read
platforms:
  - linux
  - bsd
risk_level: low
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - getfacl
artifacts: []
workflow_edges:
  produces:
    - file-content
  consumes:
    - file
contract:
  inputs: []
  outputs:
    - type: process.output
      description: File content output
  side_effects: []
  resource_cost:
    cpu: low
    memory_mb: 2
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 2
  network: none
  disk_io: low
allowed-tools:
  - setfacl
  - getfacl
  - Bash
  - execFile
parameters: []
features:
  - file-system
execution:
  template: "setfacl /path/to/file"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read a file via setfacl
    command: setfacl /path/to/file
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/setfacl/"
techniques:
  - collection
install:
  - method: apt
    package_name: "acl"
    commands:
      - "apt-get install -y acl"
---
