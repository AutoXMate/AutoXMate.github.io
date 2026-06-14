---
id: network-http-apache2ctl
namespace: network:http:apache2ctl
name: apache2ctl
description: Apache HTTP server control interface that can leak file contents via config Include directive.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - system.file.read
  - network.http.server.control
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
  - apache2
artifacts: []
workflow_edges:
  produces:
    - file-content
  consumes:
    - config-file
contract:
  inputs:
    - type: system.file.path
      description: Path to file to read
  outputs:
    - type: system.file.content
      description: File content leaked in error messages
      mime: text/plain
  side_effects: []
  resource_cost:
    cpu: low
    memory_mb: 32
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 32
  network: low
  disk_io: low
allowed-tools:
  - apache2ctl
  - Bash
  - execFile
parameters:
  - name: c
    type: string
    required: false
    description: "Pass a config directive"
    aliases:
      - -c
features: []
execution:
  template: "apache2ctl {c}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read arbitrary file via Include directive in config
    command: apache2ctl -c 'Include /path/to/input-file'
references:
  - label: "Apache2ctl documentation"
    url: "https://httpd.apache.org/docs/current/programs/apachectl.html"
techniques:
  - collection
install:
    - method: apt
      package_name: "apache2"
      commands:
        - "apt-get install -y apache2"
---


# apache2ctl — Apache HTTP Server Control

Control interface for Apache HTTP server. When used with sudo, the `-c Include` directive can leak file contents through error messages.
