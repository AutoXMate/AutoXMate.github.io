---
id: windows-copy-colorcpl
namespace: windows:copy:colorcpl
name: colorcpl
description: 'Binary that handles color management Located at: C:\Windows\System32\colorcpl.exe; C:\Windows\SysWOW64\colorcpl.exe.'
author: Arjan Onwezen
version: 1.0.0
capabilities:
- system.file.copy
platforms:
- windows
risk_level: low
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
- colorcpl
parameters: []
features: []
execution:
  template: colorcpl
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Copies the referenced file to C:\Windows\System32\spool\drivers\color\. (Copies file(s) to a subfolder of a generally trusted folder (c:\Windows\System32), which can be used to hide files or make them blend into the environment.)
  command: colorcpl {PATH}
references:
- label: '1480468728324231172'
  url: https://twitter.com/eral4m/status/1480468728324231172
techniques:
- collection
- defense-evasion
mitre_ids:
- T1036.005
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_colorcpl.yml
- type: ioc
  description: colorcpl.exe writing files
install:
- method: choco
  package_name: colorcpl
  commands:
  - choco install colorcpl
---


# colorcpl

colorcpl is a Windows LOLBin. Binary that handles color management Located at: C:\Windows\System32\colorcpl.exe; C:\Windows\SysWOW64\colorcpl.exe.
