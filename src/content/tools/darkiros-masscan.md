---
trust_level: community
id: darkiros-masscan
namespace: darkiros:tool:masscan
name: masscan
description: masscan - scan all port
version: 1.0.0
capabilities:
- credential.discovery.reconnaissance
platforms:
- cross-platform
techniques:
- discovery
execution:
  template: masscan
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: masscan - scan all port
  command: masscan -p1-65535 [ip] -e [interface] --rate 1000
references:
- label: Source
  url: https://github.com/robertdavidgraham/masscan
- label: Darkiros
  url: https://darkiros.github.io/commands.html
items:
- NoCreds
services:
- DNS
features:
- network-intensive
mitre_ids:
- T1046
- T1595
---

# masscan

Darkiros cheat sheet commands:

**masscan - scan all port**
```
masscan -p1-65535 [ip] -e [interface] --rate 1000
```
