---
id: windows-execution-mmc
namespace: windows:execution:mmc
name: mmc
description: 'Load snap-ins to locally and remotely manage Windows systems Located
  at: C:\Windows\System32\mmc.exe; C:\Windows\SysWOW64\mmc.exe.'
author: '@bohops'
version: 1.0.0
capabilities:
- security.execution.command
- security.privilege-escalation.uac-bypass
- network.transfer.download
platforms:
- windows
risk_level: critical
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
  - privilege_escalation
  - process_spawn
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
- mmc
parameters: []
features:
- local
- network-intensive
- pipes-stdin
- pipes-stdout
- remote
- requires-root
- stealth
execution:
  template: mmc
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Launch a 'backgrounded' MMC process and invoke a COM payload (Configure
    a snap-in to load a COM custom class (CLSID) that has been added to the registry)
  command: mmc.exe -Embedding {PATH_ABSOLUTE:.msc}
- description: Load an arbitrary payload DLL by configuring COR Profiler registry
    settings and launching MMC to bypass UAC. (Modify HKCU\Environment key in Registry
    with COR profiler values then launch MMC to load the payload DLL.)
  command: mmc.exe gpedit.msc
- description: Download and save an executable to disk (Download file from Internet)
  command: mmc.exe -Embedding {PATH_ABSOLUTE:.msc}
references:
- label: ''
  url: https://bohops.com/2018/08/18/abusing-the-com-registry-structure-part-2-loading-techniques-for-evasion-and-persistence/
- label: UAC-bypass-dotnet.html
  url: https://offsec.almond.consulting/UAC-bypass-dotnet.html
- label: watch?v=LFgZOTmhzeA
  url: https://www.youtube.com/watch?v=LFgZOTmhzeA
techniques:
- execution
- defense-evasion
- privilege-escalation
- exfiltration
mitre_ids:
- T1218.014
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_mmc_susp_child_process.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/file/file_event/file_event_win_uac_bypass_dotnet_profiler.yml
install:
- method: choco
  package_name: mmc
  commands:
  - choco install mmc
---

# mmc

mmc is a Windows LOLBin. Load snap-ins to locally and remotely manage Windows systems Located at: C:\Windows\System32\mmc.exe; C:\Windows\SysWOW64\mmc.exe.
