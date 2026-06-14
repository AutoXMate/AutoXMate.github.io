---
id: windows-download-ldifde
namespace: windows:download:ldifde
name: ldifde
description: 'Creates, modifies, and deletes LDAP directory objects. Located at: c:\windows\system32\ldifde.exe; c:\windows\syswow64\ldifde.exe.'
author: Grzegorz Tworek
version: 1.0.0
capabilities:
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
- ldifde
parameters: []
features: []
execution:
  template: ldifde
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Import specified .ldf file into LDAP. If the file contains http-based attrval-spec such as `thumbnailPhoto:< http://example.org/somefile.txt`, the file will be downloaded into IE temp folder. (Download file from Internet)
  command: Ldifde -i -f {PATH:.ldf}
references:
- label: '1564968845726580736'
  url: https://twitter.com/0gtweet/status/1564968845726580736
techniques:
- exfiltration
mitre_ids:
- T1105
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/3d172914f6c2bd5c2b5ed471bf0657a662d395af/rules/windows/process_creation/proc_creation_win_ldifde_export.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/3d172914f6c2bd5c2b5ed471bf0657a662d395af/rules/windows/process_creation/proc_creation_win_ldifde_file_load.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/3d172914f6c2bd5c2b5ed471bf0657a662d395af/rules-emerging-threats/2019/TA/APT31/proc_creation_win_apt_apt31_judgement_panda.yml
install:
- method: choco
  package_name: ldifde
  commands:
  - choco install ldifde
---


# ldifde

ldifde is a Windows LOLBin. Creates, modifies, and deletes LDAP directory objects. Located at: c:\windows\system32\ldifde.exe; c:\windows\syswow64\ldifde.exe.
