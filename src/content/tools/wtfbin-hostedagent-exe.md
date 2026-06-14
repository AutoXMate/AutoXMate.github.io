---
trust_level: community
id: wtfbin-hostedagent-exe
namespace: wtf:bin:hostedagent-exe
name: "HostedAgent.exe"
description: "Whoami? HostedAgent, of course!"
version: "1.0.0"
capabilities:
  - credential.discovery.whoami
platforms:
  - windows
techniques:
  - discovery
execution:
  template: "HostedAgent.exe"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Documentation"
    url: "https://github.com/mttaggart/wtfbins/issues/37"
  - label: "WTFBins"
    url: "https://wtfbins.netlify.app/wtfbins/hostedagent-exe/"
---
examples:
  - description: "Execute HostedAgent.exe and observe the unusual behavior"
    command: "HostedAgent.exe"

# HostedAgent.exe

Whoami? HostedAgent, of course!


 
Trend Micro WFBS Agent runs `whoami.exe` regularly as SYSTEM for reasons unknown.

*Contributed by Biffalo*
