---
id: windows-ads-extrac32
namespace: windows:ads:extrac32
name: extrac32
description: 'Extract to ADS, copy or overwrite a file with Extrac32.exe Located at:
  C:\Windows\System32\extrac32.exe; C:\Windows\SysWOW64\extrac32.exe.'
author: Oddvar Moe
version: 1.0.0
capabilities:
- system.file.alternate-data-stream
- network.transfer.download
- system.file.copy
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
- extrac32
parameters: []
features:
- file-system
- local
- network-intensive
- pipes-stdin
- pipes-stdout
- streaming
execution:
  template: extrac32
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Extracts the source CAB file into an Alternate Data Stream (ADS) of
    the target file. (Extract data from cab file and hide it in an alternate data
    stream.)
  command: extrac32 {PATH_ABSOLUTE:.cab} {PATH_ABSOLUTE}:file.exe
- description: Extracts the source CAB file on an unc path into an Alternate Data
    Stream (ADS) of the target file. (Extract data from cab file and hide it in an
    alternate data stream.)
  command: extrac32 {PATH_ABSOLUTE:.cab} {PATH_ABSOLUTE}:file.exe
- description: Copy the source file to the destination file and overwrite it. (Download
    file from UNC/WEBDav)
  command: extrac32 /Y /C {PATH_SMB} {PATH_ABSOLUTE}
- description: Command for copying file from one folder to another (Copy file)
  command: extrac32.exe /C {PATH_ABSOLUTE:.source.exe} {PATH_ABSOLUTE:.dest.exe}
references:
- label: ''
  url: https://oddvar.moe/2018/04/11/putting-data-in-alternate-data-streams-and-how-to-execute-it-part-2/
- label: cdd2d0d0ec9abb686f0e89306e277b8f
  url: https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f
- label: '985994639202283520'
  url: https://twitter.com/egre55/status/985994639202283520
techniques:
- defense-evasion
- exfiltration
- collection
mitre_ids:
- T1564.004
- T1105
detections:
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/12577f7380f324fcee06dab3218582f4a11833e7/rules/windows/defense_evasion_misc_lolbin_connecting_to_the_internet.toml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_extrac32.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_extrac32_ads.yml
install:
- method: choco
  package_name: extrac32
  commands:
  - choco install extrac32
---

# extrac32

extrac32 is a Windows LOLBin. Extract to ADS, copy or overwrite a file with Extrac32.exe Located at: C:\Windows\System32\extrac32.exe; C:\Windows\SysWOW64\extrac32.exe.
