---
id: archive-ar
namespace: archive:compression:ar
name: ar
description: GNU archiver that can read and extract files from archives, useful for file read operations.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - system.file.read
  - system.archive.compress
  - system.archive.decompress
platforms:
  - linux
  - macos
  - cross-platform
risk_level: low
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - tar
  - cpio
artifacts:
  - type: system.archive.file
    description: Archive file in ar format
    mime: application/x-archive
    trust_level: community
workflow_edges:
  produces:
    - archive-file
    - file-content
  consumes:
    - input-file
contract:
  inputs:
    - type: system.file.path
      description: Path to the file to archive/extract
  outputs:
    - type: system.archive.file
      description: Created archive
      mime: application/x-archive
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
  - ar
  - Bash
  - execFile
parameters:
  - name: r
    type: string
    required: false
    description: "Replace existing or insert new files"
    aliases:
      - r
  - name: p
    type: string
    required: false
    description: "Print file contents"
    aliases:
      - p
features:
  - file-system
execution:
  template: "ar {r} {p}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read arbitrary file by inserting it into archive then printing it
    command: |-
      ar r /path/to/output-file /path/to/input-file
      ar p /path/to/output-file
references:
  - label: "ar man page"
    url: "https://man7.org/linux/man-pages/man1/ar.1.html"
techniques:
  - collection
install:
    - method: apt
      package_name: "binutils"
      commands:
        - "apt-get install -y binutils"
---


# ar — GNU Archiver

ar creates, modifies, and extracts from archives. When used with sudo or SUID, it can read arbitrary files by adding them to an archive and then printing the contents.
