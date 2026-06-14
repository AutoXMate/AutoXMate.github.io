---
trust_level: community
id: wtfbin-teramind-s-dwm-exe
namespace: wtf:bin:teramind-s-dwm-exe
name: Teramind's dwm.exe
description: Nacho dwm
version: 1.0.0
capabilities:
- security.execution.command
platforms:
- windows
techniques:
- execution
execution:
  template: Teramind's dwm.exe
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Documentation
  url: https://kb.teramind.co/en/articles/8791033-antivirus-configuration-guide
- label: WTFBins
  url: https://wtfbins.netlify.app/wtfbins/teramind-s-dwm-exe/
features:
- pipes-stdin
---

examples:
  - description: "Execute Teramind's dwm.exe and observe the unusual behavior"
    command: "Teramind's dwm.exe"

# Teramind's dwm.exe

Nacho dwm


   
Teramind installs its own dwm.exe file inside a subfolder of `C:\ProgramData\{4cec2908-5ce4-48f0-a717-8fc833d8017a}`.

*Contributed by Leo T.*
