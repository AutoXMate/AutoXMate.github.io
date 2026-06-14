---
id: windows-execution-installutil
namespace: windows:execution:installutil
name: installutil
description: 'The Installer tool is a command-line utility that allows you to install and uninstall server resources by executing the installer components in specified assemblies Located at: C:\Windows\Microsoft.NET\Framework\v2.0.50727\InstallUtil.exe; C:\Windows\Microsoft.NET\Framework64\v2.0.50727\InstallUtil.exe; C:\Windows\Microsoft.NET\Framework\v4.0.30319\InstallUtil.exe.'
author: Oddvar Moe
version: 1.0.0
capabilities:
- security.defense-evasion.bypass
- security.execution.command
- network.transfer.download
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
- installutil
parameters: []
features: []
execution:
  template: installutil
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute the target .NET DLL or EXE. (Use to execute code and bypass application whitelisting)
  command: InstallUtil.exe /logfile= /LogToConsole=false /U {PATH:.dll}
- description: Execute the target .NET DLL or EXE. (Use to execute code and bypass application whitelisting)
  command: InstallUtil.exe /logfile= /LogToConsole=false /U {PATH:.dll}
- description: It will download a remote payload and place it in INetCache. (Downloads payload from remote server)
  command: InstallUtil.exe {REMOTEURL}
references:
- label: ''
  url: https://pentestlab.blog/2017/05/08/applocker-bypass-installutil/
- label: AppLocker_Bypass_Techniques.html#menu_index_12
  url: https://evi1cg.me/archives/AppLocker_Bypass_Techniques.html#menu_index_12
- label: T1218.004.md
  url: https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.004/T1218.004.md
- label: ''
  url: https://www.blackhillsinfosec.com/powershell-without-powershell-how-to-bypass-application-whitelisting-environment-restrictions-av/
- label: ''
  url: https://oddvar.moe/2017/12/13/applocker-case-study-how-insecure-is-it-really-part-1/
- label: installutil-exe-installer-tool
  url: https://docs.microsoft.com/en-us/dotnet/framework/tools/installutil-exe-installer-tool
techniques:
- defense-evasion
- execution
- exfiltration
mitre_ids:
- T1218.004
- T1105
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_instalutil_no_log_execution.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_installutil_download.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/cc241c0b5ec590d76cb88ec638d3cc37f68b5d50/rules/windows/defense_evasion_installutil_beacon.toml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
install:
- method: choco
  package_name: installutil
  commands:
  - choco install installutil
---


# installutil

installutil is a Windows LOLBin. The Installer tool is a command-line utility that allows you to install and uninstall server resources by executing the installer components in specified assemblies Located at: C:\Windows\Microsoft.NET\Framework\v2.0.50727\InstallUtil.exe; C:\Windows\Microsoft.NET\Framework64\v2.0.50727\InstallUtil.exe; C:\Windows\Microsoft.NET\Framework\v4.0.30319\InstallUtil.exe.
