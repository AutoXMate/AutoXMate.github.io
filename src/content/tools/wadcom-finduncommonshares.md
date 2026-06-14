---
trust_level: community
id: wadcom-finduncommonshares
namespace: wadcom:tool:finduncommonshares
name: "FindUncommonShares"
description: "The script FindUncommonShares.py is a Python equivalent of PowerView's Invoke-ShareFinder.ps1 allowing to quickly find uncommon shares in vast Windows Domains."
version: "1.0.0"
capabilities:
  - network.enumerate.shares
platforms:
  - windows
  - linux
techniques:
  - discovery
execution:
  template: "finduncommonshares"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Command execution"
    command: "python3 FindUncommonShares.py -u 'john' -d 'TEST.local' -p 'password123' --dc-ip 10.10.10.1"
references:
  - label: "Reference 1"
    url: "https://github.com/p0dalirius/FindUncommonShares"
items:
  - NoCreds
services:
  - SMB
---

# FindUncommonShares

The script FindUncommonShares.py is a Python equivalent of PowerView's Invoke-ShareFinder.ps1 allowing to quickly find uncommon shares in vast Windows Domains.

Command Reference:

	Target IP: 10.10.10.1

	Attacker IP: 10.10.10.2

	Domain: test.local

	Username: john

	Password: password123

```
python3 FindUncommonShares.py -u 'john' -d 'TEST.local' -p 'password123' --dc-ip 10.10.10.1
```

**Services:** SMB

**Required:** Password, Username, Hash
