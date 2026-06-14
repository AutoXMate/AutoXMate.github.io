---
id: windows-execution-control
namespace: windows:execution:control
name: control
description: 'Binary used to launch controlpanel items in Windows Located at: C:\Windows\System32\control.exe;
  C:\Windows\SysWOW64\control.exe.'
author: Oddvar Moe
version: 1.0.0
capabilities:
- system.file.alternate-data-stream
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
  - filesystem_write
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
- control
parameters: []
features:
- file-system
- local
- pipes-stdin
- pipes-stdout
- streaming
execution:
  template: control
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute evil.dll which is stored in an Alternate Data Stream (ADS).
    (Can be used to evade defensive countermeasures or to hide as a persistence mechanism)
  command: control.exe {PATH_ABSOLUTE}:evil.dll
- description: Execute .cpl file. A CPL is a DLL file with CPlApplet export function)
    (Use to execute code and bypass application whitelisting)
  command: control.exe {PATH_ABSOLUTE:.cpl}
references:
- label: ''
  url: https://pentestlab.blog/2017/05/24/applocker-bypass-control-panel/
- label: ''
  url: https://www.contextis.com/resources/blog/applocker-bypass-registry-key-manipulation/
- label: '955659561008017409'
  url: https://twitter.com/bohops/status/955659561008017409
- label: executing-control-panel-items
  url: https://docs.microsoft.com/en-us/windows/desktop/shell/executing-control-panel-items
- label: ''
  url: https://bohops.com/2018/01/23/loading-alternate-data-stream-ads-dll-cpl-binaries-to-bypass-applocker/
techniques:
- defense-evasion
- execution
mitre_ids:
- T1218.002
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules-emerging-threats/2021/Exploits/CVE-2021-40444/proc_creation_win_exploit_cve_2021_40444.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_control_dll_load.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/0875c1e4c4370ab9fbf453c8160bb5abc8ad95e7/rules/windows/defense_evasion_execution_control_panel_suspicious_args.toml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_unusual_dir_ads.toml
- type: ioc
  description: Control.exe executing files from alternate data streams
- type: ioc
  description: Control.exe executing library file without cpl extension
- type: ioc
  description: Suspicious network connections from control.exe
install:
- method: choco
  package_name: control
  commands:
  - choco install control
---

# control

control is a Windows LOLBin. Binary used to launch controlpanel items in Windows Located at: C:\Windows\System32\control.exe; C:\Windows\SysWOW64\control.exe.
