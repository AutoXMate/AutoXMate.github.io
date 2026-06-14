---
id: windows-tamper-cipher
namespace: windows:tamper:cipher
name: cipher
description: 'File Encryption Utility Located at: c:\windows\system32\cipher.exe; c:\windows\syswow64\cipher.exe.'
author: Adetutu Ogunsowo
version: 1.0.0
capabilities:
- security.defense-evasion.tamper
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
- cipher
parameters: []
features: []
execution:
  template: cipher
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Zero out a file (Can be used to forensically erase a file.)
  command: cipher /w:{PATH_ABSOLUTE:folder}
- description: Encrypt a file (Can be used to impair defences by e.g. encrypting a critical EDR solution file.)
  command: cipher.exe /e {PATH_ABSOLUTE}
references:
- label: ''
  url: https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access/
techniques:
- defense-evasion
- impact
mitre_ids:
- T1485
- T1562
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c7998c92b3c5f23ea67045bee8ee364d2ed1a775/rules/windows/process_creation/proc_creation_win_cipher_overwrite_deleted_data.yml
- type: ioc
  description: cipher.exe process with /w on the command line
install:
- method: choco
  package_name: cipher
  commands:
  - choco install cipher
---


# cipher

cipher is a Windows LOLBin. File Encryption Utility Located at: c:\windows\system32\cipher.exe; c:\windows\syswow64\cipher.exe.
