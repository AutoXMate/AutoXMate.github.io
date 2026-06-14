---
trust_level: community
id: wadcom-seatbelt
namespace: wadcom:tool:seatbelt
name: "Seatbelt"
description: "Seatbelt.exe is part of the GhostPack suite of tools that will perform a lot of \"safety checks\" on the Windows host and collect system data that could be useful for potential privilege escalation or persistence methods. The following command will run all checks on the system and store the output in a file (WARNING: will collect a lot of data. remove `-full` for less output)."
version: "1.0.0"
capabilities:
  - system.enumerate.security
platforms:
  - windows
techniques:
  - discovery
execution:
  template: "seatbelt"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Command execution"
    command: "Seatbelt.exe -group=all -full > output.txt"
references:
  - label: "Reference 1"
    url: "https://github.com/GhostPack/Seatbelt"
  - label: "Reference 2"
    url: "https://www.harmj0y.net/blog/redteaming/ghostpack/"
items:
  - NoCreds
  - Password
services:
  - SMB
---

# Seatbelt

Seatbelt.exe is part of the GhostPack suite of tools that will perform a lot of "safety checks" on the Windows host and collect system data that could be useful for potential privilege escalation or persistence methods. The following command will run all checks on the system and store the output in a file (WARNING: will collect a lot of data. remove `-full` for less output).

Command Reference:

	Run all checks: -group=all

	Output File: output.txt

```
Seatbelt.exe -group=all -full > output.txt
```

**Required:** Shell
