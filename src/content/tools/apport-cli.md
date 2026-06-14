---
id: system-debug-apport-cli
namespace: system:debug:apport-cli
name: apport-cli
description: Ubuntu crash report handler that can spawn a pager (less) to read arbitrary files.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
  - system.file.read
platforms:
  - linux
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - less
  - systemctl
artifacts: []
workflow_edges:
  produces:
    - file-content
  consumes: []
contract:
  inputs: []
  outputs:
    - type: process.output
      description: File content via pager
      mime: text/plain
  side_effects:
    - process_spawn
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
  - apport-cli
  - Bash
  - execFile
parameters:
  - name: f
    type: string
    required: false
    description: "Report a problem"
    aliases:
      - -f
features: []
execution:
  template: "apport-cli {f}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn less pager via crash report interface to read files
    command: |-
      apport-cli -f
      1
      2
      v
references:
  - label: "Apport documentation"
    url: "https://wiki.ubuntu.com/Apport"
techniques:
  - privilege-escalation
  - execution
install:
    - method: apt
      package_name: "apport"
      commands:
        - "apt-get install -y apport"
---


# apport-cli — Ubuntu Crash Report Handler

apport-cli is Ubuntu's crash report interface. When run, it presents a menu that can spawn a pager (less), which can then be used to read arbitrary files or execute commands via the pager's escape functionality (`!command`).
