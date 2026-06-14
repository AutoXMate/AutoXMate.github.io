---
id: windows-execution-winget
namespace: windows:execution:winget
name: winget
description: 'Windows Package Manager tool Located at: C:\Users\user\AppData\Local\Microsoft\WindowsApps\winget.exe.'
author: Paul Sanders
version: 1.0.0
capabilities:
- security.execution.command
- network.transfer.download
- security.defense-evasion.bypass
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
  - network_traffic
  - process_spawn
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
- winget
parameters: []
features:
- local
- network-intensive
- pipes-stdin
- pipes-stdout
- process-manip
- stealth
execution:
  template: winget
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: 'Downloads a file from the web address specified in .yml file and executes
    it on the system. Local manifest setting must be enabled in winget for it to work:
    `winget settings --enable LocalManifestFiles` (Download and execute an arbitrary
    file from the internet)'
  command: winget.exe install --manifest {PATH:.yml}
- description: 'Download and install any software from the Microsoft Store using its
    name or Store ID, even if the Microsoft Store App itself is blocked on the machine.
    For example, use "Sysinternals Suite" or `9p7knl5rwt25` for obtaining ProcDump,
    PsExec via the Sysinternals Suite. Note: a Microsoft account is required for this.
    (Download and install software from Microsoft Store, even if Microsoft Store App
    is blocked)'
  command: winget.exe install --accept-package-agreements -s msstore {name or ID}
- description: 'Download and install any software from the Microsoft Store using its
    name or Store ID, even if the Microsoft Store App itself is blocked on the machine,
    and even if AppLocker is active on the machine. For example, use "Sysinternals
    Suite" or `9p7knl5rwt25` for obtaining ProcDump, PsExec via the Sysinternals Suite.
    Note: a Microsoft account is required for this. (Download and install software
    from Microsoft Store, even if Microsoft Store App is blocked, and AppLocker is
    activated on the machine)'
  command: winget.exe install --accept-package-agreements -s msstore {name or ID}
references:
- label: New-Year-New-LOLBAS.html
  url: https://saulpanders.github.io/2022/01/02/New-Year-New-LOLBAS.html
- label: '#production-recommended'
  url: https://docs.microsoft.com/en-us/windows/package-manager/winget/#production-recommended
- label: watch?v=zuL7x4Wltto
  url: https://www.youtube.com/watch?v=zuL7x4Wltto
techniques:
- execution
- exfiltration
- defense-evasion
mitre_ids:
- T1105
detections:
- type: ioc
  description: winget.exe spawned with local manifest file
- type: ioc
  description: Sysmon Event ID 1 - Process Creation
- type: other
  url: https://saulpanders.github.io/2022/01/02/New-Year-New-LOLBAS.html
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_winget_local_install_via_manifest.yml
install:
- method: choco
  package_name: winget
  commands:
  - choco install winget
---

# winget

winget is a Windows LOLBin. Windows Package Manager tool Located at: C:\Users\user\AppData\Local\Microsoft\WindowsApps\winget.exe.
