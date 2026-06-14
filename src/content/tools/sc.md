---
id: windows-ads-sc
namespace: windows:ads:sc
name: sc
description: 'Used by Windows to manage services Located at: C:\Windows\System32\sc.exe; C:\Windows\SysWOW64\sc.exe.'
author: Oddvar Moe
version: 1.0.0
capabilities:
- system.file.alternate-data-stream
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
  resource_cost:
    cpu: low
    memory_mb: 16
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: low
  disk_io: low
allowed-tools:
- sc
parameters: []
features: []
execution:
  template: sc
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Creates a new service and executes the file stored in the ADS. (Execute binary file hidden inside an alternate data stream)
  command: sc create evilservice binPath="\"c:\\ADS\\file.txt:cmd.exe\" /c echo works > \"c:\ADS\works.txt\"" DisplayName= "evilservice" start= auto\ & sc start evilservice
- description: Modifies an existing service and executes the file stored in the ADS. (Execute binary file hidden inside an alternate data stream)
  command: sc config {ExistingServiceName} binPath="\"c:\\ADS\\file.txt:cmd.exe\" /c echo works > \"c:\ADS\works.txt\"" & sc start {ExistingServiceName}
references:
- label: ''
  url: https://oddvar.moe/2018/04/11/putting-data-in-alternate-data-streams-and-how-to-execute-it-part-2/
techniques:
- defense-evasion
mitre_ids:
- T1564.004
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_susp_service_creation.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_sc_change_sevice_image_path_by_non_admin.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_sc_service_path_modification.yml
- type: splunk
  url: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/sc_exe_manipulating_windows_services.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/lateral_movement_cmd_service.toml
- type: ioc
  description: Unexpected service creation
- type: ioc
  description: Unexpected service modification
install:
- method: choco
  package_name: sc
  commands:
  - choco install sc
---


# sc

sc is a Windows LOLBin. Used by Windows to manage services Located at: C:\Windows\System32\sc.exe; C:\Windows\SysWOW64\sc.exe.
