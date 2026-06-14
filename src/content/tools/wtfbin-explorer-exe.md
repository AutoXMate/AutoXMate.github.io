---
trust_level: community
id: wtfbin-explorer-exe
namespace: wtf:bin:explorer-exe
name: explorer.exe
description: Guests are not invited to Everyone shares
version: 1.0.0
capabilities:
- security.execution.command
platforms:
- windows
techniques:
- execution
execution:
  template: explorer.exe
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Documentation
  url: https://learn.microsoft.com/en-us/answers/questions/224757/failed-type-3-logons-on-domain-workstation-by-gues#:~:text=4%3A56%20AM-,Hello%2C,-Thank%20you%20so
- label: WTFBins
  url: https://wtfbins.netlify.app/wtfbins/explorer-exe/
features:
- pipes-stdin
---

examples:
  - description: "Execute explorer.exe and observe the unusual behavior"
    command: "explorer.exe"

# explorer.exe

Guests are not invited to Everyone shares.


   
Sharing a Windows folder with `Everyone` permissions, will cause a failed logon of user `Guest`.

*Contributed by ygil1234*
