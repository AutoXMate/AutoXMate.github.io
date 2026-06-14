---
id: windows-ads-regedit
namespace: windows:ads:regedit
name: regedit
description: 'Used by Windows to manipulate registry Located at: C:\Windows\regedit.exe.'
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
- regedit
parameters: []
features: []
execution:
  template: regedit
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Export the target Registry key to the specified .REG file. (Hide registry data in alternate data stream)
  command: regedit /E {PATH_ABSOLUTE}:regfile.reg HKEY_CURRENT_USER\MyCustomRegKey
- description: Import the target .REG file into the Registry. (Import hidden registry data from alternate data stream)
  command: regedit {PATH_ABSOLUTE}:regfile.reg
references:
- label: cdd2d0d0ec9abb686f0e89306e277b8f
  url: https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f
techniques:
- defense-evasion
mitre_ids:
- T1564.004
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_regedit_import_keys_ads.yml
- type: ioc
  description: regedit.exe reading and writing to alternate data stream
- type: ioc
  description: regedit.exe should normally not be executed by end-users
install:
- method: choco
  package_name: regedit
  commands:
  - choco install regedit
---


# regedit

regedit is a Windows LOLBin. Used by Windows to manipulate registry Located at: C:\Windows\regedit.exe.
