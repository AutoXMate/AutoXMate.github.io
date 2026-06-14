---
trust_level: community
id: wtfbin-skype-exe
namespace: wtf:bin:skype-exe
name: Skype.exe
description: It runs whoami because it's lost
version: 1.0.0
capabilities:
- credential.discovery.whoami
- security.execution.command
platforms:
- windows
techniques:
- discovery
- execution
execution:
  template: Skype.exe
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Documentation
  url: https://answers.microsoft.com/en-us/skype/forum/all/skype-issues-after-update-from-82x-to-830/39b7f81a-2a97-4f0f-ac59-1cea5e5fc279
- label: WTFBins
  url: https://wtfbins.netlify.app/wtfbins/skype-exe/
features:
- pipes-stdin
- process-manip
---

examples:
  - description: "Execute Skype.exe and observe the unusual behavior"
    command: "Skype.exe"

# Skype.exe

It runs whoami because it's lost.

*Contributed by g1ng3rr00t*
