---
trust_level: community
id: wtfbin-windows-terminal
namespace: wtf:bin:windows-terminal
name: Windows Terminal
description: Windows Terminal runs `wsl` on startup
version: 1.0.0
capabilities:
- security.execution.command
platforms:
- windows
techniques:
- execution
execution:
  template: Windows Terminal
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Documentation
  url: https://youtu.be/VvMn_zYP8Cw?t=11430
- label: WTFBins
  url: https://wtfbins.netlify.app/wtfbins/windows-terminal/
features:
- compression
- file-system
- pipes-stdin
- process-manip
---

examples:
  - description: "Execute Windows Terminal and observe the unusual behavior"
    command: "Windows Terminal"

# Windows Terminal

Windows Terminal runs `wsl` on startup.

Upon launch, Windows Terminal runs `wsl --list` to find potential Linux profiles to add to its list.

*Contributed by mttaggart*
