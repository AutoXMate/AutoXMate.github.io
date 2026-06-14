---
trust_level: community
id: wadcom-mitm6
namespace: wadcom:tool:mitm6
name: mitm6
description: mitm6 is a pentesting tool that exploits the default configuration of
  Windows to take over the default DNS server. It does this by replying to DHCPv6
  messages, providing victims with a link-local IPv6 address and setting the attackers
  host as default DNS server. The following command will respond to DHCPv6 messages
  and set the DNS server to the attack host IP. Leverage this command with ntlmrelayx.py
  to capture the WPAD configuration requests.
version: 1.0.0
capabilities:
- network.intercept.mitm
platforms:
- linux
techniques:
- collection
execution:
  template: mitm6
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: Command execution
  command: mitm6 -d test.local --ignore-nofqnd
references:
- label: Reference 1
  url: https://github.com/dirkjanm/mitm6
- label: Reference 2
  url: https://dirkjanm.io/worst-of-both-worlds-ntlm-relaying-and-kerberos-delegation/
items:
- Hash
services:
- DNS
- SMB
- LDAP
- LLMNR
- MDNS
- NBT-NS
features:
- file-system
- local
- network-intensive
- remote
---

# mitm6

mitm6 is a pentesting tool that exploits the default configuration of Windows to take over the default DNS server. It does this by replying to DHCPv6 messages, providing victims with a link-local IPv6 address and setting the attackers host as default DNS server. The following command will respond to DHCPv6 messages and set the DNS server to the attack host IP. Leverage this command with ntlmrelayx.py to capture the WPAD configuration requests. 

Command Reference:

	Domain: test.local

```
mitm6 -d test.local --ignore-nofqnd
```

**Services:** DNS

**Required:** No_Creds
