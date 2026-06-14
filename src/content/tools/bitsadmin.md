---
id: windows-execution-bitsadmin
namespace: windows:execution:bitsadmin
name: bitsadmin
description: 'Used for managing background intelligent transfer Located at: C:\Windows\System32\bitsadmin.exe;
  C:\Windows\SysWOW64\bitsadmin.exe.'
author: Oddvar Moe
version: 1.0.0
capabilities:
- system.file.alternate-data-stream
- network.transfer.download
- system.file.copy
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
  - filesystem_write
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
- bitsadmin
parameters: []
features:
- file-system
- local
- network-intensive
- pipes-stdin
- pipes-stdout
- streaming
execution:
  template: bitsadmin
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Create a bitsadmin job named 1, add cmd.exe to the job, configure the
    job to run the target command from an Alternate data stream, then resume and complete
    the job. (Performs execution of specified file in the alternate data stream, can
    be used as a defensive evasion or persistence technique.)
  command: bitsadmin /create 1 bitsadmin /addfile 1 c:\windows\system32\cmd.exe c:\data\playfolder\cmd.exe
    bitsadmin /SetNotifyCmdLine 1 c:\data\playfolder\1.txt:cmd.exe NULL bitsadmin
    /RESUME 1 bitsadmin /complete 1
- description: Create a bitsadmin job named 1, add cmd.exe to the job, configure the
    job to run the target command, then resume and complete the job. (Download file
    from Internet)
  command: bitsadmin /create 1 bitsadmin /addfile 1 https://live.sysinternals.com/autoruns.exe
    c:\data\playfolder\autoruns.exe bitsadmin /RESUME 1 bitsadmin /complete 1
- description: Command for copying cmd.exe to another folder (Copy file)
  command: bitsadmin /create 1 & bitsadmin /addfile 1 c:\windows\system32\cmd.exe
    c:\data\playfolder\cmd.exe & bitsadmin /RESUME 1 & bitsadmin /Complete 1 & bitsadmin
    /reset
- description: One-liner that creates a bitsadmin job named 1, add cmd.exe to the
    job, configure the job to run the target command, then resume and complete the
    job. (Execute binary file specified. Can be used as a defensive evasion.)
  command: bitsadmin /create 1 & bitsadmin /addfile 1 c:\windows\system32\cmd.exe
    c:\data\playfolder\cmd.exe & bitsadmin /SetNotifyCmdLine 1 c:\data\playfolder\cmd.exe
    NULL & bitsadmin /RESUME 1 & bitsadmin /Reset
references:
- label: windows-attacks-at-is-the-new-black-26672679
  url: https://www.slideshare.net/chrisgates/windows-attacks-at-is-the-new-black-26672679
- label: watch?v=_8xJaaQlpBo
  url: https://www.youtube.com/watch?v=_8xJaaQlpBo
- label: cdd2d0d0ec9abb686f0e89306e277b8f
  url: https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f
- label: '100'
  url: https://www.soc-labs.top/en/detections/100
techniques:
- defense-evasion
- exfiltration
- collection
- execution
mitre_ids:
- T1564.004
- T1105
- T1218
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_bitsadmin_download.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/web/proxy_generic/proxy_ua_bitsadmin_susp_tld.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_bitsadmin_potential_persistence.yml
- type: splunk
  url: https://github.com/splunk/security_content/blob/3f77e24974239fcb7a339080a1a483e6bad84a82/detections/endpoint/bitsadmin_download_file.yml
- type: ioc
  description: Child process from bitsadmin.exe
- type: ioc
  description: bitsadmin creates new files
- type: ioc
  description: bitsadmin adds data to alternate data stream
install:
- method: choco
  package_name: bitsadmin
  commands:
  - choco install bitsadmin
---

# bitsadmin

bitsadmin is a Windows LOLBin. Used for managing background intelligent transfer Located at: C:\Windows\System32\bitsadmin.exe; C:\Windows\SysWOW64\bitsadmin.exe.
