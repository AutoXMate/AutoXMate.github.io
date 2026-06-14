---
trust_level: community
id: wadcom-sharpwmi
namespace: wadcom:tool:sharpwmi
name: "SharpWMI"
description: "SharpWMI.exe is part of the GhostPack suite of tools that provides WMI functionality, such as local/remote WMI queries, remote WMI process creation, and remote execution of arbitrary VBS through WMI events. The following command will simply list all processes running on the local system."
version: "1.0.0"
capabilities:
  - security.execution.wmi
platforms:
  - windows
techniques:
  - execution
execution:
  template: "sharpwmi"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Command execution"
    command: "SharpWMI.exe action=query query=\"select * from win32_process\""
references:
  - label: "Reference 1"
    url: "https://github.com/GhostPack/SharpWMI"
  - label: "Reference 2"
    url: "https://www.harmj0y.net/blog/redteaming/ghostpack/"
items:
  - Shell
services:
  - WMI
  - RPC
  - SMB
---

# SharpWMI

SharpWMI.exe is part of the GhostPack suite of tools that provides WMI functionality, such as local/remote WMI queries, remote WMI process creation, and remote execution of arbitrary VBS through WMI events. The following command will simply list all processes running on the local system.

Command Reference:

	Get all processes: "select * from win32_process"

```
SharpWMI.exe action=query query="select * from win32_process"
```

**Services:** WMI

**Required:** Shell
