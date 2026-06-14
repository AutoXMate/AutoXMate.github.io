---
id: network-http-apache2
namespace: network:http:apache2
name: apache2
description: Apache HTTP server that can be used for file read operations via configuration directives.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - system.file.read
  - network.http.server
  - network.http.serve
platforms:
  - linux
  - macos
  - cross-platform
risk_level: low
trust_level: verified
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - apache2ctl
  - nginx
artifacts: []
workflow_edges:
  produces:
    - file-content
  consumes:
    - config-file
contract:
  inputs:
    - type: system.file.path
      description: Path to file read via config
  outputs:
    - type: system.file.content
      description: File content leaked in error messages
      mime: text/plain
  side_effects: []
  resource_cost:
    cpu: medium
    memory_mb: 64
    network: low
    disk_io: low
resource_profile:
  cpu: medium
  memory_mb: 64
  network: low
  disk_io: low
allowed-tools:
  - apache2
  - Bash
  - execFile
parameters:
  - name: f
    type: file
    required: false
    description: "Specify config file path"
    aliases:
      - -f
  - name: C
    type: string
    required: false
    description: "Pass a config directive"
    aliases:
      - -C
features: []
execution:
  template: "apache2 {f} {C}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read arbitrary file via config parsing error message
    command: apache2 -f /path/to/input-file
  - description: Read arbitrary file via Include directive
    command: apache2 -C 'Define APACHE_RUN_DIR /' -C 'Include /path/to/input-file'
references:
  - label: "Apache HTTP documentation"
    url: "https://httpd.apache.org/docs/"
techniques:
  - collection
install:
    - method: apt
      package_name: "apache2"
      commands:
        - "apt-get install -y apache2"
---


# apache2 — Apache HTTP Server

Apache HTTP server. When used with sudo or SUID, config file paths passed with `-f` or `-C Include` can leak arbitrary file content through error messages.
