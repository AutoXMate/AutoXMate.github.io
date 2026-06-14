---
id: text-gettext-msgcat
namespace: text:gettext:msgcat
name: msgcat
description: Gettext catalog concatenation, can read files.
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
  - msgconv
  - msgfilter
  - msgmerge
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
  - msgcat
  - Bash
  - execFile
parameters: []
features:
  - file-system
execution:
  template: "msgcat /path/to/file.po"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read a file via msgcat
    command: msgcat /path/to/file.po
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/msgcat/"
techniques:
  - collection
install:
  - method: apt
    package_name: "gettext"
    commands:
      - "apt-get install -y gettext"
---
