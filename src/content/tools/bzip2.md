---
id: archive-bzip2
namespace: archive:compression:bzip2
name: bzip2
description: File compression utility using Burrows-Wheeler algorithm that can read files via compression pipeline.
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
  - bzcat
  - bzless
  - bunzip2
  - gzip
artifacts:
  - type: system.archive.file
    description: Bzip2 compressed file
    mime: application/x-bzip2
    trust_level: community
workflow_edges:
  produces:
    - compressed-file
    - file-content
  consumes:
    - input-file
contract:
  inputs:
    - type: system.file.path
      description: Path to file to compress
  outputs:
    - type: system.archive.file
      description: Compressed file
      mime: application/x-bzip2
  side_effects:
    - filesystem_write
  resource_cost:
    cpu: medium
    memory_mb: 16
    network: low
    disk_io: medium
resource_profile:
  cpu: medium
  memory_mb: 16
  network: low
  disk_io: medium
allowed-tools:
  - bzip2
  - Bash
  - execFile
parameters:
  - name: c
    type: string
    required: false
    description: "Compress to stdout"
    aliases:
      - -c
      - --stdout
  - name: d
    type: string
    required: false
    description: "Decompress"
    aliases:
      - -d
      - --decompress
features:
  - file-system
execution:
  template: "bzip2 {c} {d}"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Read arbitrary file via compression pipeline
    command: bzip2 -c /path/to/input-file | bzip2 -d
references:
  - label: "bzip2 man page"
    url: "https://man7.org/linux/man-pages/man1/bzip2.1.html"
techniques:
  - collection
install:
    - method: apt
      package_name: "bzip2"
      commands:
        - "apt-get install -y bzip2"
---


# bzip2 — File Compressor

bzip2 compresses files using the Burrows-Wheeler algorithm. When used with sudo or SUID, it can read arbitrary files by compressing them to stdout and then decompressing. Related utilities (bzless, bzcat, bunzip2) also support privileged reads if bzip2 itself is SUID.
