---
id: network-email-alpine
namespace: network:email:alpine
name: alpine
description: Alpine email client that can read arbitrary files when invoked with the -F flag.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - system.file.read
  - network.email.client
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
  - mutt
  - mail
artifacts:
  - type: system.file.content
    description: File content displayed in the terminal interface
    mime: text/plain
    trust_level: community
workflow_edges:
  produces:
    - file-content
  consumes:
    - input-file
contract:
  inputs:
    - type: system.file.path
      description: Path to file to read
  outputs:
    - type: system.file.content
      description: File content displayed in terminal
      mime: text/plain
  side_effects: []
  resource_cost:
    cpu: low
    memory_mb: 8
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 8
  network: low
  disk_io: low
allowed-tools:
  - alpine
  - Bash
  - execFile
parameters:
  - name: F
    type: file
    required: false
    description: "Open a file for reading in the terminal interface"
    aliases:
      - -F
features: []
execution:
  template: "alpine {F}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read an arbitrary file displayed in the alpine terminal interface
    command: alpine -F /path/to/input-file
references:
  - label: "Alpine documentation"
    url: "https://alpineapp.email/"
techniques:
  - collection
install:
    - method: apt
      package_name: "alpine"
      commands:
        - "apt-get install -y alpine"
---


# Alpine — Email Client

Alpine is a text-based email client. When invoked with the `-F` flag, it can open and display the content of arbitrary files in its terminal interface, making it useful for file read operations when used with elevated privileges.

## File Read

```bash
alpine -F /path/to/input-file
```
