---
id: windows-credential-ntdsutil
namespace: windows:credential:ntdsutil
name: ntdsutil
description: 'Command line utility used to export Active Directory. Located at: C:\Windows\System32\ntdsutil.exe.'
author: Tony Lambert
version: 1.0.0
capabilities:
- credential.dump
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
  - process_spawn
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
- ntdsutil
parameters: []
features: []
execution:
  template: ntdsutil
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Dump NTDS.dit into folder (Dumping of Active Directory NTDS.dit database)
  command: ntdsutil.exe "ac i ntds" "ifm" "create full c:\" q q
references:
- label: ?p=2398#CreateIFM
  url: https://adsecurity.org/?p=2398#CreateIFM
techniques:
- credential-access
mitre_ids:
- T1003.003
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_ntdsutil_usage.yml
- type: splunk
  url: https://github.com/splunk/security_content/blob/2b87b26bdc2a84b65b1355ffbd5174bdbdb1879c/detections/endpoint/ntdsutil_export_ntds.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/5bdf70e72c6cd4547624c521108189af994af449/rules/windows/credential_access_cmdline_dump_tool.toml
- type: ioc
  description: ntdsutil.exe with command line including "ifm"
install:
- method: choco
  package_name: ntdsutil
  commands:
  - choco install ntdsutil
---


# ntdsutil

ntdsutil is a Windows LOLBin. Command line utility used to export Active Directory. Located at: C:\Windows\System32\ntdsutil.exe.
