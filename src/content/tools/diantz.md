---
id: windows-execution-diantz
namespace: windows:execution:diantz
name: diantz
description: 'Binary that package existing files into a cabinet (.cab) file Located at: c:\windows\system32\diantz.exe; c:\windows\syswow64\diantz.exe.'
author: Tamir Yehuda
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
- diantz
parameters: []
features: []
execution:
  template: diantz
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Compress a file (first argument) into a CAB file stored in the Alternate Data Stream (ADS) of the target file. (Hide data compressed into an Alternate Data Stream.)
  command: diantz.exe {PATH_ABSOLUTE:.exe} {PATH_ABSOLUTE}:targetFile.cab
- description: Download and compress a remote file and store it in a CAB file on local machine. (Download and compress into a cab file.)
  command: diantz.exe {PATH_SMB:.exe} {PATH_ABSOLUTE:.cab}
- description: Execute diantz directives as defined in the specified Diamond Definition File (.ddf); see resources for the format specification. (Bypass command-line based detections)
  command: diantz /f {PATH:.ddf}
references:
- label: diantz
  url: https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/diantz
- label: makecab-directives.html
  url: https://ss64.com/nt/makecab-directives.html
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
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_diantz_ads.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_diantz_remote_cab.yml
- type: ioc
  description: diantz storing data into alternate data streams.
- type: ioc
  description: diantz getting a file from a remote machine or the internet.
install:
- method: choco
  package_name: diantz
  commands:
  - choco install diantz
---


# diantz

diantz is a Windows LOLBin. Binary that package existing files into a cabinet (.cab) file Located at: c:\windows\system32\diantz.exe; c:\windows\syswow64\diantz.exe.
