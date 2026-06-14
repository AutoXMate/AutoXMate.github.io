---
trust_level: community
id: wadcom-targetedkerberoast
namespace: wadcom:tool:targetedkerberoast
name: "targetedKerberoast"
description: "targetedKerberoast is a Python script that can, like many others (e.g. GetUserSPNs.py), print \"kerberoast\" hashes for user accounts that have a SPN set. This tool brings the following additional feature: for each user without SPNs, it tries to set one (abuse of a write permission on the servicePrincipalName attribute), print the \"kerberoast\" hash, and delete the temporary SPN set for that operation."
version: "1.0.0"
capabilities:
  - credential.dump.kerberos
platforms:
  - linux
techniques:
  - credential-access
execution:
  template: "targetedkerberoast"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Command execution"
    command: "python3 targetedKerberoast.py -d test.local -u john -p password123 --dc-ip 10.10.10.1"
references:
  - label: "Reference 1"
    url: "https://github.com/ShutdownRepo/targetedKerberoast"
items:
  - TGS
  - Hash
services:
  - Kerberos
  - LDAP
---

# targetedKerberoast

targetedKerberoast is a Python script that can, like many others (e.g. GetUserSPNs.py), print "kerberoast" hashes for user accounts that have a SPN set. This tool brings the following additional feature: for each user without SPNs, it tries to set one (abuse of a write permission on the servicePrincipalName attribute), print the "kerberoast" hash, and delete the temporary SPN set for that operation.

Command Reference:

	Target IP: 10.10.10.1

	Attacker IP: 10.10.10.2

	Domain: test.local

	Username: john

	Password: password123

```
python3 targetedKerberoast.py -d test.local -u john -p password123 --dc-ip 10.10.10.1
```

**Services:** Kerberos, NTLM

**Required:** Password, Username
