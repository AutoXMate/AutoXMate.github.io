---
trust_level: community
id: darkiros-scshell
namespace: darkiros:tool:scshell
name: SCShell
description: Stealthy psexec
version: 1.0.0
capabilities:
- network.connect.remote
platforms:
- cross-platform
techniques:
- lateral-movement
execution:
  template: scshell
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: Stealthy psexec
  command: python3 scshell.py -service-name [service_name|defragsvc] -hashes :[ntlm_hash]
    [domain]/[user]@[ip]
references:
- label: Source
  url: https://github.com/Mr-Un1k0d3r/SCShell
- label: Darkiros
  url: https://darkiros.github.io/commands.html
items:
- Shell
- Hash
services:
- SMB
- WinRM
- RPC
features:
- interactive
- network-intensive
- process-manip
- remote
- stealth
---

# SCShell

Darkiros cheat sheet commands:

**Stealthy psexec**
```
python3 scshell.py -service-name [service_name|defragsvc] -hashes :[ntlm_hash] [domain]/[user]@[ip]
```
