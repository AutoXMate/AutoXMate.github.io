---
id: encode-base32
namespace: encode:binary:base32
name: base32
description: Base32 encoder/decoder that can encode and decode arbitrary files to
  read their contents.
author: Repository Maintainers
version: 1.0.0
capabilities:
- system.file.read
- encode.base32
- decode.base32
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
- base64
- base58
- basenc
artifacts: []
workflow_edges:
  produces:
  - file-content
  consumes:
  - input-file
contract:
  inputs:
  - type: system.file.path
    description: Path to file to encode
  outputs:
  - type: system.file.content
    description: File content encoded/decoded
    mime: text/plain
  side_effects: []
  resource_cost:
    cpu: low
    memory_mb: 4
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 4
  network: low
  disk_io: low
allowed-tools:
- base32
- Bash
- execFile
parameters:
- name: decode
  type: string
  required: false
  description: Decode the input
  aliases:
  - --decode
features:
- file-system
- local
execution:
  template: base32 {decode}
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Read arbitrary file by encoding then decoding to stdout
  command: base32 /path/to/input-file | base32 --decode
references:
- label: base32 man page
  url: https://man7.org/linux/man-pages/man1/base32.1.html
techniques:
- collection
install:
- method: apt
  package_name: coreutils
  commands:
  - apt-get install -y coreutils
---

# base32 — Base32 Encoder/Decoder

base32 encodes and decodes data in base32 format. When used with sudo or SUID, it can read arbitrary files by encoding them and then decoding the output back to stdout.
