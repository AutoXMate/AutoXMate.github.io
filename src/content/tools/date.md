---
id: system-datetime-date
namespace: system:datetime:date
name: date
description: Display or set system date and time, can read files via -f flag.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - system.file.read
  - system.datetime.display
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
  consumes:
    - input-file
contract:
  inputs:
    - type: system.file.path
      description: Path to file to parse as date strings
  outputs:
    - type: system.file.content
      description: File content with prefix corruption
      mime: text/plain
  side_effects: []
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
  - date
  - Bash
  - execFile
parameters:
  - name: f
    type: file
    required: false
    description: "Read dates from file"
    aliases:
      - -f
features: []
execution:
  template: "date {f}"
  sandbox: execFile
  timeout_seconds: 10
  shell: false
global_vars: {}
examples:
  - description: Read arbitrary file via date format parsing, each line wrapped in quotes with prefix
    command: date -f /path/to/input-file
references:
  - label: "date man page"
    url: "https://man7.org/linux/man-pages/man1/date.1.html"
techniques:
  - collection
install:
    - method: apt
      package_name: "coreutils"
      commands:
        - "apt-get install -y coreutils"
---


# date — Display/Set Date and Time

date displays or sets the system date and time. The GNU version's `-f` flag parses a file for date strings, leaking each line with a prefix in quotes — useful for file read when used with elevated privileges.
