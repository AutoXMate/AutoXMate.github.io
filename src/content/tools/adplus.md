---
id: windows-execution-adplus
namespace: windows:execution:adplus
name: adplus
description: 'Debugging tool included with Windows Debugging Tools Located at: C:\Program
  Files (x86)\Windows Kits\10\Debuggers\x64\adplus.exe; C:\Program Files (x86)\Windows
  Kits\10\Debuggers\x86\adplus.exe.'
author: mr.d0x
version: 1.0.0
capabilities:
- credential.dump
- security.execution.command
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
- adplus
parameters: []
features:
- file-system
- local
- pipes-stdin
- pipes-stdout
execution:
  template: adplus
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Creates a memory dump of the lsass process (Create memory dump and
    parse it offline)
  command: adplus.exe -hang -pn lsass.exe -o {PATH_ABSOLUTE:folder} -quiet
- description: Execute arbitrary commands using adplus config file (see Resources
    section for a sample file). (Run commands under a trusted Microsoft signed binary)
  command: adplus.exe -c {PATH:.xml}
- description: Dump process memory using adplus config file (see Resources section
    for a sample file). (Run commands under a trusted Microsoft signed binary)
  command: adplus.exe -c {PATH:.xml}
- description: Execute arbitrary commands and binaries from the context of adplus.
    Note that providing an output directory via '-o' is required. (Run commands under
    a trusted Microsoft signed binary)
  command: adplus.exe -crash -o "{PATH_ABSOLUTE:folder}" -sc {PATH:.exe}
references:
- label: ''
  url: https://mrd0x.com/adplus-debugging-tool-lsass-dump/
- label: '1534916659676422152'
  url: https://twitter.com/nas_bench/status/1534916659676422152
- label: '1534915321856917506'
  url: https://twitter.com/nas_bench/status/1534915321856917506
techniques:
- credential-access
- execution
- defense-evasion
mitre_ids:
- T1003.001
- T1127
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6199a703221a98ae6ad343c79c558da375203e4e/rules/windows/process_creation/proc_creation_win_lolbin_adplus.yml
- type: ioc
  description: As a Windows SDK binary, execution on a system may be suspicious
install:
- method: choco
  package_name: adplus
  commands:
  - choco install adplus
---

# adplus

adplus is a Windows LOLBin. Debugging tool included with Windows Debugging Tools Located at: C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\adplus.exe; C:\Program Files (x86)\Windows Kits\10\Debuggers\x86\adplus.exe.
