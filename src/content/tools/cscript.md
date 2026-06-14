---
id: windows-ads-cscript
namespace: windows:ads:cscript
name: cscript
description: 'Binary used to execute scripts in Windows Located at: C:\Windows\System32\cscript.exe;
  C:\Windows\SysWOW64\cscript.exe.'
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
- cscript
parameters: []
features:
- file-system
- local
- pipes-stdin
- pipes-stdout
- process-manip
- streaming
execution:
  template: cscript
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Use cscript.exe to exectute a Visual Basic script stored in an Alternate
    Data Stream (ADS). (Can be used to evade defensive countermeasures or to hide
    as a persistence mechanism)
  command: cscript //e:vbscript {PATH_ABSOLUTE}:script.vbs
references:
- label: cdd2d0d0ec9abb686f0e89306e277b8f
  url: https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f
- label: ''
  url: https://oddvar.moe/2018/01/14/putting-data-in-alternate-data-streams-and-how-to-execute-it/
techniques:
- defense-evasion
mitre_ids:
- T1564.004
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_wscript_cscript_script_exec.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/file/file_event/file_event_win_net_cli_artefact.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_unusual_dir_ads.toml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/cc241c0b5ec590d76cb88ec638d3cc37f68b5d50/rules/windows/command_and_control_remote_file_copy_scripts.toml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/82ec6ac1eeb62a1383792719a1943b551264ed16/rules/windows/defense_evasion_suspicious_managedcode_host_process.toml
- type: splunk
  url: https://github.com/splunk/security_content/blob/a1afa0fa605639cbef7d528dec46ce7c8112194a/detections/endpoint/wscript_or_cscript_suspicious_child_process.yml
- type: blockrule
  url: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- type: ioc
  description: Cscript.exe executing files from alternate data streams
- type: ioc
  description: DotNet CLR libraries loaded into cscript.exe
- type: ioc
  description: DotNet CLR Usage Log - cscript.exe.log
install:
- method: choco
  package_name: cscript
  commands:
  - choco install cscript
---

# cscript

cscript is a Windows LOLBin. Binary used to execute scripts in Windows Located at: C:\Windows\System32\cscript.exe; C:\Windows\SysWOW64\cscript.exe.
