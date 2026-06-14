---
trust_level: community
id: wadcom-sharpdump
namespace: wadcom:tool:sharpdump
name: "SharpDump"
description: "SharpDump.exe is part of the GhostPack suite of tools and is a C# port of PowerSploit's Out-Minidump.ps1. It can dump the process for LSASS or a specific process given it's PID. This dump can then be fed into mimikatz to extract sensitive information. The following command simply dumps the LSASS process."
version: "1.0.0"
capabilities:
  - credential.dump.lsass
platforms:
  - windows
techniques:
  - credential-access
execution:
  template: "sharpdump"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Command execution"
    command: "SharpDump.exe"
references:
  - label: "Reference 1"
    url: "https://github.com/GhostPack/SharpDump"
  - label: "Reference 2"
    url: "https://www.harmj0y.net/blog/redteaming/ghostpack/"
items:
  - Hash
  - Password
services:
  - SMB
---

# SharpDump

SharpDump.exe is part of the GhostPack suite of tools and is a C# port of PowerSploit's Out-Minidump.ps1. It can dump the process for LSASS or a specific process given it's PID. This dump can then be fed into mimikatz to extract sensitive information. The following command simply dumps the LSASS process.

```
SharpDump.exe
```

**Required:** Shell
