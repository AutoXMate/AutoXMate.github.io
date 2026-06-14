---
id: windows-download-replace
namespace: windows:download:replace
name: replace
description: 'Used to replace file with another file Located at: C:\Windows\System32\replace.exe;
  C:\Windows\SysWOW64\replace.exe.'
author: Oddvar Moe
version: 1.0.0
capabilities:
- system.file.copy
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
  - filesystem_write
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
- replace
parameters: []
features:
- file-system
- local
- network-intensive
- pipes-stdin
- pipes-stdout
execution:
  template: replace
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Copy .cab file to destination (Copy files)
  command: replace.exe {PATH_ABSOLUTE:.cab} {PATH_ABSOLUTE:folder} /A
- description: Download/Copy executable to specified folder (Download file)
  command: replace.exe {PATH_SMB:.exe} {PATH_ABSOLUTE:folder} /A
references:
- label: '986334113941655553'
  url: https://twitter.com/elceef/status/986334113941655553
- label: '986842299861782529'
  url: https://twitter.com/elceef/status/986842299861782529
techniques:
- collection
- exfiltration
mitre_ids:
- T1105
detections:
- type: ioc
  description: Replace.exe retrieving files from remote server
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_replace.yml
install:
- method: choco
  package_name: replace
  commands:
  - choco install replace
---

# replace

replace is a Windows LOLBin. Used to replace file with another file Located at: C:\Windows\System32\replace.exe; C:\Windows\SysWOW64\replace.exe.
