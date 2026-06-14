---
id: windows-tamper-fltmc
namespace: windows:tamper:fltmc
name: fltmc
description: 'Filter Manager Control Program used by Windows Located at: C:\Windows\System32\fltMC.exe.'
author: John Lambert
version: 1.0.0
capabilities:
- security.defense-evasion.tamper
platforms:
- windows
risk_level: high
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
- fltmc
parameters: []
features: []
execution:
  template: fltmc
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Unloads a driver used by security agents (Defense evasion)
  command: fltMC.exe unload SysmonDrv
references:
- label: operating-offensively-against-sysmon
  url: https://www.darkoperator.com/blog/2018/10/5/operating-offensively-against-sysmon
techniques:
- defense-evasion
mitre_ids:
- T1562.001
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_fltmc_unload_driver_sysmon.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_via_filter_manager.toml
- type: splunk
  url: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/unload_sysmon_filter_driver.yml
- type: ioc
  description: 4688 events with fltMC.exe
install:
- method: choco
  package_name: fltmc
  commands:
  - choco install fltmc
---


# fltmc

fltmc is a Windows LOLBin. Filter Manager Control Program used by Windows Located at: C:\Windows\System32\fltMC.exe.
