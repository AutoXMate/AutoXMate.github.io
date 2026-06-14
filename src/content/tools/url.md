---
id: windows-execution-url
namespace: windows:execution:url
name: url
description: 'Internet Shortcut Shell Extension DLL. Located at: c:\windows\system32\url.dll;
  c:\windows\syswow64\url.dll.'
author: LOLBAS Team
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
- url
parameters: []
features:
- interactive
- pipes-stdin
- pipes-stdout
execution:
  template: url
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Launch a HTML application payload by calling OpenURL. (Invoke an HTML
    Application via mshta.exe (Default Handler).)
  command: rundll32.exe url.dll,OpenURL {PATH_ABSOLUTE:.hta}
- description: Launch an executable payload via proxy through a .url (information)
    file by calling OpenURL. (Load an executable payload by calling a .url file.)
  command: rundll32.exe url.dll,OpenURL {PATH_ABSOLUTE:.url}
- description: Launch an executable by calling OpenURL. (Load an executable payload
    by specifying the file protocol handler (obfuscated).)
  command: rundll32.exe url.dll,OpenURL file://^C^:^/^W^i^n^d^o^w^s^/^s^y^s^t^e^m^3^2^/^c^a^l^c^.^e^x^e
- description: Launch an executable by calling FileProtocolHandler. (Launch an executable.)
  command: rundll32.exe url.dll,FileProtocolHandler {PATH_ABSOLUTE:.exe}
- description: Launch an executable by calling FileProtocolHandler. (Load an executable
    payload by specifying the file protocol handler (obfuscated).)
  command: rundll32.exe url.dll,FileProtocolHandler file://^C^:^/^W^i^n^d^o^w^s^/^s^y^s^t^e^m^3^2^/^c^a^l^c^.^e^x^e
- description: Launch a HTML application payload by calling FileProtocolHandler. (Invoke
    an HTML Application via mshta.exe (Default Handler).)
  command: rundll32.exe url.dll,FileProtocolHandler file:///C:/test/test.hta
references:
- label: ''
  url: https://bohops.com/2018/03/17/abusing-exported-functions-and-exposed-dcom-interfaces-for-pass-thru-command-execution-and-lateral-movement/
- label: '995348436353470465'
  url: https://twitter.com/DissectMalware/status/995348436353470465
- label: '974043815655956481'
  url: https://twitter.com/bohops/status/974043815655956481
- label: '997355558070927360'
  url: https://twitter.com/yeyint_mth/status/997355558070927360
- label: '974063407321223168'
  url: https://twitter.com/Hexacorn/status/974063407321223168
- label: url_dll.html
  url: https://windows10dll.nirsoft.net/url_dll.html
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218.011
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
install:
- method: choco
  package_name: url
  commands:
  - choco install url
---

# url

url is a Windows LOLBin. Internet Shortcut Shell Extension DLL. Located at: c:\windows\system32\url.dll; c:\windows\syswow64\url.dll.
