---
trust_level: community
id: wadcom-pywhisker
namespace: wadcom:tool:pywhisker
name: pyWhisker
description: pyWhisker is a tool allowing users to manipulate the msDS-KeyCredentialLink
  attribute of a target user/computer to obtain full control over that object. It's
  based on Impacket and on our Python equivalent of Michael Grafnetter's DSInternals
  called PyDSInternals. This tool, along with Dirk-jan's PKINITtools allow for a complete
  primitive exploitation on UNIX-based systems only.
version: 1.0.0
capabilities:
- credential.manipulate.pkinit
platforms:
- linux
techniques:
- credential-access
execution:
  template: pywhisker
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: Command execution
  command: python3 pywhisker.py -d "test.local" -u "john" -p "password123" --target
    "user2" --action "list" --dc-ip "10.10.10.1"
references:
- label: Reference 1
  url: https://github.com/shutdownrepo/pywhisker
items:
- PFX
- NoCreds
services:
- LDAP
- RPC
features:
- compression
- file-system
- interactive
- pipes-stdin
---

# pyWhisker

pyWhisker is a tool allowing users to manipulate the msDS-KeyCredentialLink attribute of a target user/computer to obtain full control over that object. It's based on Impacket and on our Python equivalent of Michael Grafnetter's DSInternals called PyDSInternals. This tool, along with Dirk-jan's PKINITtools allow for a complete primitive exploitation on UNIX-based systems only.

Command Reference:

	Target IP: 10.10.10.1

	Domain: test.local

	Username: john

	Password: password123

```
python3 pywhisker.py -d "test.local" -u "john" -p "password123" --target "user2" --action "list" --dc-ip "10.10.10.1"
```

**Services:** Kerberos

**Required:** Password, Username
