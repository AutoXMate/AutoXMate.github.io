---
id: windows-credential-cmdkey
namespace: windows:credential:cmdkey
name: cmdkey
description: 'creates, lists, and deletes stored user names and passwords or credentials. Located at: C:\Windows\System32\cmdkey.exe; C:\Windows\SysWOW64\cmdkey.exe.'
author: Oddvar Moe
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
- cmdkey
parameters: []
features: []
execution:
  template: cmdkey
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: List cached credentials (Get credential information from host)
  command: cmdkey /list
references:
- label: exploring-cmdkey-an-edge-case-for-privilege-escala
  url: https://web.archive.org/web/20230202122017/https://www.peew.pw/blog/2017/11/26/exploring-cmdkey-an-edge-case-for-privilege-escalation
- label: cmdkey
  url: https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/cmdkey
techniques:
- credential-access
- defense-evasion
mitre_ids:
- T1078
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_cmdkey_recon.yml
install:
- method: choco
  package_name: cmdkey
  commands:
  - choco install cmdkey
---


# cmdkey

cmdkey is a Windows LOLBin. creates, lists, and deletes stored user names and passwords or credentials. Located at: C:\Windows\System32\cmdkey.exe; C:\Windows\SysWOW64\cmdkey.exe.
