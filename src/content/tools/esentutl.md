---
id: windows-ads-esentutl
namespace: windows:ads:esentutl
name: esentutl
description: 'Binary for working with Microsoft Joint Engine Technology (JET) database Located at: C:\Windows\System32\esentutl.exe; C:\Windows\SysWOW64\esentutl.exe.'
author: Oddvar Moe
version: 1.0.0
capabilities:
- system.file.copy
- system.file.alternate-data-stream
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
- esentutl
parameters: []
features: []
execution:
  template: esentutl
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Copies the source VBS file to the destination VBS file. (Copies files from A to B)
  command: esentutl.exe /y {PATH_ABSOLUTE:.source.vbs} /d {PATH_ABSOLUTE:.dest.vbs} /o
- description: Copies the source EXE to an Alternate Data Stream (ADS) of the destination file. (Copy file and hide it in an alternate data stream as a defensive counter measure)
  command: esentutl.exe /y {PATH_ABSOLUTE:.exe} /d {PATH_ABSOLUTE}:file.exe /o
- description: Copies the source Alternate Data Stream (ADS) to the destination EXE. (Extract hidden file within alternate data streams)
  command: esentutl.exe /y {PATH_ABSOLUTE}:file.exe /d {PATH_ABSOLUTE:.exe} /o
- description: Copies the remote source EXE to the destination Alternate Data Stream (ADS) of the destination file. (Copy file and hide it in an alternate data stream as a defensive counter measure)
  command: esentutl.exe /y {PATH_SMB:.exe} /d {PATH_ABSOLUTE}:file.exe /o
- description: Copies the source EXE to the destination EXE file (Use to copy files from one unc path to another)
  command: esentutl.exe /y {PATH_SMB:.source.exe} /d {PATH_SMB:.dest.exe} /o
- description: Copies a (locked) file using Volume Shadow Copy (Copy/extract a locked file such as the AD Database)
  command: esentutl.exe /y /vss c:\windows\ntds\ntds.dit /d {PATH_ABSOLUTE:.dit}
references:
- label: '985994639202283520'
  url: https://twitter.com/egre55/status/985994639202283520
- label: ''
  url: https://dfironthemountain.wordpress.com/2018/12/06/locked-file-access-using-esentutl-exe/
- label: '1094810861095534592'
  url: https://twitter.com/bohops/status/1094810861095534592
techniques:
- collection
- exfiltration
- defense-evasion
- credential-access
mitre_ids:
- T1105
- T1564.004
- T1003.003
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_esentutl_params.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_esentutl_webcache.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/registry/registry_event/registry_event_esentutl_volume_shadow_copy_service_keys.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_esentutl_sensitive_file_copy.yml
- type: splunk
  url: https://github.com/splunk/security_content/blob/86a5b644a44240f01274c8b74d19a435c7dae66e/detections/endpoint/esentutl_sam_copy.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/f6421d8c534f295518a2c945f530e8afc4c8ad1b/rules/windows/credential_access_copy_ntds_sam_volshadowcp_cmdline.toml
install:
- method: choco
  package_name: esentutl
  commands:
  - choco install esentutl
---


# esentutl

esentutl is a Windows LOLBin. Binary for working with Microsoft Joint Engine Technology (JET) database Located at: C:\Windows\System32\esentutl.exe; C:\Windows\SysWOW64\esentutl.exe.
