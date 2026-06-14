---
id: text-gettext-msgmerge
namespace: text:gettext:msgmerge
name: msgmerge
description: Gettext catalog merging, can read files.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - system.file.read
platforms:
  - linux
  - bsd
risk_level: low
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - msgattrib
  - msgcat
  - msgconv
  - msgfilter
  - msguniq
artifacts: []
workflow_edges:
  produces:
    - file-content
  consumes:
    - file
contract:
  inputs: []
  outputs:
    - type: process.output
      description: File content output
  side_effects: []
  resource_cost:
    cpu: low
    memory_mb: 4
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 4
  network: none
  disk_io: low
allowed-tools:
  - msgmerge
  - Bash
  - execFile
parameters: []
features:
  - file-system
execution:
  template: "msgmerge /path/to/file.po"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read a file via msgmerge
    command: msgmerge /path/to/file.po
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/msgmerge/"
techniques:
  - collection
install:
  - method: apt
    package_name: "gettext"
    commands:
      - "apt-get install -y gettext"
---
