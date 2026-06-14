---
id: windows-execution-cdb
namespace: windows:execution:cdb
name: cdb
description: 'Debugging tool included with Windows Debugging Tools. Located at: C:\Program
  Files (x86)\Windows Kits\10\Debuggers\x64\cdb.exe; C:\Program Files (x86)\Windows
  Kits\10\Debuggers\x86\cdb.exe.'
author: Oddvar Moe
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
- cdb
parameters: []
features:
- file-system
- local
- pipes-stdin
- pipes-stdout
execution:
  template: cdb
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Launch 64-bit shellcode from the specified .wds file using cdb.exe.
    (Local execution of assembly shellcode.)
  command: cdb.exe -cf {PATH:.wds} -o notepad.exe
- description: Attaching to any process and executing shell commands. (Run a shell
    command under a trusted Microsoft signed binary)
  command: 'cdb.exe -pd -pn {process_name}

    .shell {CMD}

    '
- description: Execute arbitrary commands and binaries using a debugging script (see
    Resources section for a sample file). (Run commands under a trusted Microsoft
    signed binary)
  command: cdb.exe -c {PATH:.txt} "{CMD}"
references:
- label: windbg-cdb-shellcode-runner.html
  url: http://www.exploit-monday.com/2016/08/windbg-cdb-shellcode-runner.html
- label: cdb-command-line-options
  url: https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/cdb-command-line-options
- label: 94e2b0a9e3fe1ac0a433b5c3e6bd0bda
  url: https://gist.github.com/mattifestation/94e2b0a9e3fe1ac0a433b5c3e6bd0bda
- label: ''
  url: https://mrd0x.com/the-power-of-cdb-debugging-tool/
- label: '1534957360032120833'
  url: https://twitter.com/nas_bench/status/1534957360032120833
techniques:
- execution
- defense-evasion
mitre_ids:
- T1127
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_cdb.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_process_network_connection.toml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
- type: blockrule
  url: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
install:
- method: choco
  package_name: cdb
  commands:
  - choco install cdb
---

# cdb

cdb is a Windows LOLBin. Debugging tool included with Windows Debugging Tools. Located at: C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\cdb.exe; C:\Program Files (x86)\Windows Kits\10\Debuggers\x86\cdb.exe.
