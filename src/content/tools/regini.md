---
id: windows-ads-regini
namespace: windows:ads:regini
name: regini
description: 'Used to manipulate the registry Located at: C:\Windows\System32\regini.exe;
  C:\Windows\SysWOW64\regini.exe.'
author: Oddvar Moe
version: 1.0.0
capabilities:
- system.file.alternate-data-stream
platforms:
- windows
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
- amd64
dependencies: []
related_tools: []
artifacts: []
workflow_edges:
  produces:
  - command-output
  consumes: []
contract:
  inputs: []
  outputs:
  - type: process.output
    description: Command execution output
  side_effects:
  - filesystem_write
  resource_cost:
    cpu: low
    memory_mb: 16
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: low
  disk_io: low
allowed-tools:
- regini
parameters: []
features:
- file-system
- local
- pipes-stdin
- pipes-stdout
- streaming
execution:
  template: regini
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Write registry keys from data inside the Alternate data stream. (Write
    to registry)
  command: regini.exe {PATH}:hidden.ini
references:
- label: cdd2d0d0ec9abb686f0e89306e277b8f
  url: https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f
techniques:
- defense-evasion
mitre_ids:
- T1564.004
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_regini_ads.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_regini_execution.yml
- type: ioc
  description: regini.exe reading from ADS
install:
- method: choco
  package_name: regini
  commands:
  - choco install regini
---

# regini

regini is a Windows LOLBin. Used to manipulate the registry Located at: C:\Windows\System32\regini.exe; C:\Windows\SysWOW64\regini.exe.
