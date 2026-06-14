---
id: encode-ascii85
namespace: encode:binary:ascii85
name: ascii85
description: ASCII85 encoder/decoder for binary-to-text encoding, can encode arbitrary
  files.
author: Repository Maintainers
version: 1.0.0
capabilities:
- system.file.read
- encode.ascii85
- decode.ascii85
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
- ascii85
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
  template: ascii85 {0}
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Read and encode file, then decode back to stdout
  command: ascii85 /path/to/input-file | ascii85 --decode
references:
- label: ascii85 man page
  url: https://man7.org/linux/man-pages/man1/ascii85.1.html
techniques:
- collection
install:
- method: apt
  package_name: ascii85
  commands:
  - apt-get install -y ascii85
---

# ascii85 — ASCII85 Encoder/Decoder

ascii85 encodes and decodes binary data in ASCII85 format. When used with sudo or SUID, it can read arbitrary files by encoding and decoding them back to stdout.
