---
id: text-convert-iconv
namespace: text:convert:iconv
name: iconv
description: Convert text from one character encoding to another, can read/write arbitrary files.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - system.file.read
  - system.file.write
  - text.convert.encoding
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
related_tools: []
artifacts: []
workflow_edges:
  produces:
    - file-content
    - converted-file
  consumes:
    - input-file
contract:
  inputs:
    - type: system.file.path
      description: Path to file to convert
  outputs:
    - type: system.file.content
      description: Converted file content
      mime: text/plain
  side_effects:
    - filesystem_write
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
  - iconv
  - Bash
  - execFile
parameters:
  - name: f
    type: string
    required: false
    description: "From encoding"
    aliases:
      - -f
      - --from-code
  - name: t
    type: string
    required: false
    description: "To encoding"
    aliases:
      - -t
      - --to-code
  - name: o
    type: file
    required: false
    description: "Output file"
    aliases:
      - -o
      - --output
features: []
execution:
  template: "iconv {f} {t} {o}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read arbitrary file via identity encoding conversion
    command: iconv -f 8859_1 -t 8859_1 /path/to/input-file
  - description: Write arbitrary data to file
    command: echo DATA | iconv -f 8859_1 -t 8859_1 -o /path/to/output-file
references:
  - label: "iconv man page"
    url: "https://man7.org/linux/man-pages/man1/iconv.1.html"
techniques:
  - collection
install:
    - method: apt
      package_name: "libc-bin"
      commands:
        - "apt-get install -y libc-bin"
---


# iconv — Character Encoding Converter

iconv converts text between character encodings. Using the `8859_1` encoding (which accepts any single-byte sequence), it can read and write arbitrary files when used with elevated privileges.
