---
trust_level: community
id: wtfbin-pangphip-exe
namespace: wtf:bin:pangphip-exe
name: PanGpHip.exe
description: Palo Alto GP Firewall HIP check runs whoami.exe as SYSTEM
version: 1.0.0
capabilities:
- security.execution.command
- credential.discovery.whoami
platforms:
- cross-platform
techniques:
- execution
- discovery
execution:
  template: PanGpHip.exe
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Documentation
  url: https://live.paloaltonetworks.com/t5/globalprotect-discussions/pan-gp-hip/td-p/423158
- label: WTFBins
  url: https://wtfbins.netlify.app/wtfbins/pangphip-exe/
features:
- pipes-stdin
- process-manip
---

examples:
  - description: "Execute PanGpHip.exe and observe the unusual behavior"
    command: "PanGpHip.exe"

# PanGpHip.exe

Palo Alto GP Firewall HIP check runs whoami.exe as SYSTEM.

*Contributed by mttaggart*
