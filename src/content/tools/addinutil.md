---
id: windows-execution-addinutil
namespace: windows:execution:addinutil
name: addinutil
description: '.NET Tool used for updating cache files for Microsoft Office Add-Ins. Located at: C:\Windows\Microsoft.NET\Framework\v4.0.30319\AddinUtil.exe; C:\Windows\Microsoft.NET\Framework64\v4.0.30319\AddinUtil.exe; C:\Windows\Microsoft.NET\Framework\v3.5\AddInUtil.exe.'
author: Michael McKinley @MckinleyMike
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
- addinutil
parameters: []
features: []
execution:
  template: addinutil
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: AddinUtil is executed from the directory where the 'Addins.Store' payload exists, AddinUtil will execute the 'Addins.Store' payload. (Proxy execution of malicious serialized payload)
  command: C:\Windows\Microsoft.NET\Framework\v4.0.30319\AddinUtil.exe -AddinRoot:.
references:
- label: addinutil-lolbas.html
  url: https://www.blue-prints.blog/content/blog/posts/lolbin/addinutil-lolbas.html
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_addinutil_suspicious_cmdline.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_addinutil_uncommon_child_process.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_addinutil_uncommon_cmdline.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_addinutil_uncommon_dir_exec.yml
install:
- method: choco
  package_name: addinutil
  commands:
  - choco install addinutil
---


# addinutil

addinutil is a Windows LOLBin. .NET Tool used for updating cache files for Microsoft Office Add-Ins. Located at: C:\Windows\Microsoft.NET\Framework\v4.0.30319\AddinUtil.exe; C:\Windows\Microsoft.NET\Framework64\v4.0.30319\AddinUtil.exe; C:\Windows\Microsoft.NET\Framework\v3.5\AddInUtil.exe.
