---
trust_level: community
id: wtfbin-gc-worker-exe
namespace: wtf:bin:gc-worker-exe
name: "gc_worker.exe"
description: "Base64-encoded PowerShell from Azure's own agent!"
version: "1.0.0"
capabilities:
  - security.execution.powershell
platforms:
  - windows
techniques:
  - execution
execution:
  template: "gc_worker.exe"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Documentation"
    url: "https://github.com/mttaggart/wtfbins/issues/41"
  - label: "WTFBins"
    url: "https://wtfbins.netlify.app/wtfbins/gc-worker-exe/"
---
examples:
  - description: "Execute gc_worker.exe and observe the unusual behavior"
    command: "gc_worker.exe"

# gc_worker.exe

Base64-encoded PowerShell from Azure's own agent!


   
The Azure Connected Machine Agent spawns a process that runs encoded Powershell strings. Triggers when the agent downloads new policies from Azure.

*Contributed by rcegan*
