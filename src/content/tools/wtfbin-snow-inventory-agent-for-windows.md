---
trust_level: community
id: wtfbin-snow-inventory-agent-for-windows
namespace: wtf:bin:snow-inventory-agent-for-windows
name: Snow Inventory Agent for Windows
description: Yet another PowerShell weirdo
version: 1.0.0
capabilities:
- security.execution.powershell
platforms:
- windows
techniques:
- execution
execution:
  template: Snow Inventory Agent for Windows
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Documentation
  url: https://stackoverflow.com/questions/60503948/is-this-code-a-keylogger-what-does-it-do/65027626#65027626
- label: WTFBins
  url: https://wtfbins.netlify.app/wtfbins/snow-inventory-agent-for-windows/
features:
- interactive
- pipes-stdin
---

examples:
  - description: "Execute Snow Inventory Agent for Windows and observe the unusual behavior"
    command: "Snow Inventory Agent for Windows"

# Snow Inventory Agent for Windows

Yet another PowerShell weirdo.



Snow Inventory Agent for Windows (`snowagent.exe`) runs PowerShell which resembles shellcode (bindshell)

* `powershell.exe -command`
* `Invoke-Expression`
* byte arrays
* string encoding operations
* pipes.

*Contributed by Luke Humberdross (@ukejjh)*
