---
id: windows-execution-desk
namespace: windows:execution:desk
name: desk
description: 'Desktop Settings Control Panel Located at: C:\Windows\System32\desk.cpl; C:\Windows\SysWOW64\desk.cpl.'
author: Hai Vaknin
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
- desk
parameters: []
features: []
execution:
  template: desk
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Launch an executable with a .scr extension by calling the InstallScreenSaver function. (Launch any executable payload, as long as it uses the .scr extension.)
  command: rundll32.exe desk.cpl,InstallScreenSaver {PATH_ABSOLUTE:.scr}
- description: Launch a remote executable with a .scr extension, located on an SMB share, by calling the InstallScreenSaver function. (Launch any executable payload, as long as it uses the .scr extension.)
  command: rundll32.exe desk.cpl,InstallScreenSaver {PATH_SMB:.scr}
references:
- label: 29A-7.030.txt
  url: https://vxug.fakedoma.in/zines/29a/29a7/Articles/29A-7.030.txt
- label: '998627081360695297'
  url: https://twitter.com/pabraeken/status/998627081360695297
- label: '1517027824984547329'
  url: https://twitter.com/VakninHai/status/1517027824984547329
- label: InstallScreenSaver-SCR-files
  url: https://jstnk9.github.io/jstnk9/research/InstallScreenSaver-SCR-files
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218.011
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/file/file_event/file_event_win_new_src_file.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_rundll32_installscreensaver.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/940f89d43dbac5b7108610a5bde47cda0d2a643b/rules/windows/registry/registry_set/registry_set_scr_file_executed_by_rundll32.yml
install:
- method: choco
  package_name: desk
  commands:
  - choco install desk
---


# desk

desk is a Windows LOLBin. Desktop Settings Control Panel Located at: C:\Windows\System32\desk.cpl; C:\Windows\SysWOW64\desk.cpl.
