---
id: archive-arj
namespace: archive:compression:arj
name: arj
description: ARJ archiver that can read and write files with elevated privileges.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - system.file.read
  - system.file.write
  - system.archive.compress
  - system.archive.decompress
platforms:
  - linux
  - cross-platform
risk_level: low
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - unzip
  - tar
artifacts:
  - type: system.archive.file
    description: ARJ archive file
    mime: application/x-arj
    trust_level: community
workflow_edges:
  produces:
    - archive-file
    - file-content
    - extracted-file
  consumes:
    - input-file
contract:
  inputs:
    - type: system.file.path
      description: Path to file to archive
  outputs:
    - type: system.archive.file
      description: ARJ archive
      mime: application/x-arj
  side_effects:
    - filesystem_write
  resource_cost:
    cpu: low
    memory_mb: 8
    network: low
    disk_io: medium
resource_profile:
  cpu: low
  memory_mb: 8
  network: low
  disk_io: medium
allowed-tools:
  - arj
  - Bash
  - execFile
parameters:
  - name: a
    type: string
    required: false
    description: "Add files to archive"
    aliases:
      - a
  - name: p
    type: string
    required: false
    description: "Print file to stdout"
    aliases:
      - p
  - name: e
    type: string
    required: false
    description: "Extract files from archive"
    aliases:
      - e
features:
  - file-system
execution:
  template: "arj {a} {p} {e}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read arbitrary file via archive then print
    command: |-
      arj a /path/to/output-file /path/to/input-file
      arj p /path/to/output-file
  - description: Write arbitrary data via archive creation and extract
    command: |-
      echo DATA >output-file
      arj a x output-file
      arj e x /path/to/output-dir/
references:
  - label: "ARJ documentation"
    url: "http://arj.sourceforge.net/"
techniques:
  - collection
install:
    - method: apt
      package_name: "arj"
      commands:
        - "apt-get install -y arj"
---


# arj — ARJ Archiver

ARJ is a file archiver with compression. When used with sudo or SUID, it can read arbitrary files by adding them to an archive and printing their contents, and write files by creating and extracting archives.
