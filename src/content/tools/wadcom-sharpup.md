---
trust_level: community
id: wadcom-sharpup
namespace: wadcom:tool:sharpup
name: "SharpUp"
description: "SharpUp.exe is part of the GhostPack suite of tools and is a C# port of PowerUp that will perform numerous privilege escalation checks. The following command will run all priv esc checks and store the output in a file."
version: "1.0.0"
capabilities:
  - security.privilege-escalation.enumerate
platforms:
  - windows
techniques:
  - privilege-escalation
execution:
  template: "sharpup"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Command execution"
    command: "SharpUp.exe > output.txt"
references:
  - label: "Reference 1"
    url: "https://github.com/GhostPack/SharpUp"
  - label: "Reference 2"
    url: "https://www.harmj0y.net/blog/redteaming/ghostpack/"
items:
  - NoCreds
services:
  - SMB
---

# SharpUp

SharpUp.exe is part of the GhostPack suite of tools and is a C# port of PowerUp that will perform numerous privilege escalation checks. The following command will run all priv esc checks and store the output in a file.

Command Reference:

	Output File: output.txt

```
SharpUp.exe > output.txt
```

**Required:** Shell
