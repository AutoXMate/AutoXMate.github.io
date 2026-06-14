---
id: windows-execution-diskshadow
namespace: windows:execution:diskshadow
name: diskshadow
description: 'Diskshadow.exe is a tool that exposes the functionality offered by the volume shadow copy Service (VSS). Located at: C:\Windows\System32\diskshadow.exe; C:\Windows\SysWOW64\diskshadow.exe.'
author: Oddvar Moe
version: 1.0.0
capabilities:
- credential.dump
- security.execution.command
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
- diskshadow
parameters: []
features: []
execution:
  template: diskshadow
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute commands using diskshadow.exe from a prepared diskshadow script. (Use diskshadow to exfiltrate data from VSS such as NTDS.dit)
  command: diskshadow.exe /s {PATH:.txt}
- description: Execute commands using diskshadow.exe to spawn child process (Use diskshadow to bypass defensive counter measures)
  command: diskshadow> exec {PATH:.exe}
references:
- label: ''
  url: https://bohops.com/2018/03/26/diskshadow-the-return-of-vss-evasion-persistence-and-active-directory-database-extraction/
techniques:
- credential-access
- execution
- defense-evasion
mitre_ids:
- T1003.003
- T1202
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_diskshadow.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_susp_shadow_copies_deletion.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/5bdf70e72c6cd4547624c521108189af994af449/rules/windows/credential_access_cmdline_dump_tool.toml
- type: ioc
  description: Child process from diskshadow.exe
install:
- method: choco
  package_name: diskshadow
  commands:
  - choco install diskshadow
---


# diskshadow

diskshadow is a Windows LOLBin. Diskshadow.exe is a tool that exposes the functionality offered by the volume shadow copy Service (VSS). Located at: C:\Windows\System32\diskshadow.exe; C:\Windows\SysWOW64\diskshadow.exe.
