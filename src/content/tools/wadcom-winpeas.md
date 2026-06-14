---
trust_level: community
id: wadcom-winpeas
namespace: wadcom:tool:winpeas
name: winPEAS
description: winpeas.exe is a script that will search for all possible paths to escalate
  privileges on Windows hosts. The below command will run all priv esc checks and
  store the output in a file.
version: 1.0.0
capabilities:
- security.privilege-escalation.enumerate
platforms:
- windows
techniques:
- privilege-escalation
execution:
  template: winpeas
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: Command execution
  command: winpeas.exe cmd > output.txt
references:
- label: Reference 1
  url: https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/winPEAS
- label: Reference 2
  url: https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/blob/master/winPEAS/winPEASexe/README.md
- label: Reference 3
  url: https://book.hacktricks.xyz/windows/windows-local-privilege-escalation
items:
- NoCreds
services:
- SMB
features:
- file-system
- local
- pipes-stdout
- process-manip
- requires-root
---

# winPEAS

winpeas.exe is a script that will search for all possible paths to escalate privileges on Windows hosts. The below command will run all priv esc checks and store the output in a file.

Command Reference:

	Run all checks: cmd

	Output File: output.txt

```
winpeas.exe cmd > output.txt
```

**Required:** Shell
