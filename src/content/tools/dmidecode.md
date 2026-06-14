---
id: system-firmware-dmidecode
namespace: system:firmware:dmidecode
name: dmidecode
description: DMI/SMBIOS table decoder, can write files via --dump-bin with crafted SMBIOS data.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - system.file.write
platforms:
  - linux
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
  produces: []
  consumes:
    - file
contract:
  inputs: []
  outputs:
    - type: process.output
      description: File write output
  side_effects:
    - filesystem_write
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
  - dmidecode
  - Bash
  - execFile
parameters: []
features:
  - file-system
execution:
  template: "dmidecode --no-sysfs -d x.dmi --dump-bin {output}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Write a file via dmidecode dump-bin
    command: dmidecode --no-sysfs -d x.dmi --dump-bin /path/to/output-file
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/dmidecode/"
techniques:
  - exfiltration
install:
  - method: apt
    package_name: "dmidecode"
    commands:
      - "apt-get install -y dmidecode"
---
