---
id: windows-execution-defaultpack
namespace: windows:execution:defaultpack
name: defaultpack
description: 'This binary can be downloaded along side multiple software downloads
  on the Microsoft website. It gets downloaded when the user forgets to uncheck the
  option to set Bing as the default search provider. Located at: C:\Program Files
  (x86)\Microsoft\DefaultPack\DefaultPack.exe.'
author: '@checkymander'
version: 1.0.0
capabilities:
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
- defaultpack
parameters: []
features:
- file-system
- local
- network-intensive
- pipes-stdin
- pipes-stdout
execution:
  template: defaultpack
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Use DefaultPack.EXE to execute arbitrary binaries, with added argument
    support. (Can be used to execute stagers, binaries, and other malicious commands.)
  command: DefaultPack.EXE /C:"{CMD}"
references:
- label: '1311509470275604480.'
  url: https://twitter.com/checkymander/status/1311509470275604480.
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_lolbin_defaultpack.yml
- type: ioc
  description: DefaultPack.EXE spawned an unknown process
install:
- method: choco
  package_name: defaultpack
  commands:
  - choco install defaultpack
---

# defaultpack

defaultpack is a Windows LOLBin. This binary can be downloaded along side multiple software downloads on the Microsoft website. It gets downloaded when the user forgets to uncheck the option to set Bing as the default search provider. Located at: C:\Program Files (x86)\Microsoft\DefaultPack\DefaultPack.exe.
