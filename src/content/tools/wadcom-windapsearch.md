---
trust_level: community
id: wadcom-windapsearch
namespace: wadcom:tool:windapsearch
name: windapsearch
description: windapsearch enumerates users, groups, and computers from a Windows domain
  through LDAP queries. The following command enumerates all 3 of the above mentioned
  using provided credentials.
version: 1.0.0
capabilities:
- directory.enumerate.ldap
platforms:
- linux
techniques:
- discovery
execution:
  template: windapsearch
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: Command execution
  command: python3 windapsearch --dc-ip 10.10.10.1 -u test.local\\john -p password123
    -U -G --da -m "Remote Desktop Users" -C -r
references:
- label: Reference 1
  url: https://github.com/ropnop/windapsearch
- label: Reference 2
  url: https://www.attackdebris.com/?p=470
items:
- NoCreds
services:
- LDAP
features:
- process-manip
---

# windapsearch

windapsearch enumerates users, groups, and computers from a Windows domain through LDAP queries. The following command enumerates all 3 of the above mentioned using provided credentials.

Command Reference:

	Target IP: 10.10.10.1

	Domain: test.local

	Username: john

	Password: password123

	Enum Users: -U

	Enum Groups: -G

	Enum Domain Admins: --da

	Enum members of group: -m "Remote Desktop Users"

	Enum Computers and resolve DNS: -C -r

```
python3 windapsearch --dc-ip 10.10.10.1 -u test.local\\john -p password123 -U -G --da -m "Remote Desktop Users" -C -r
```

**Required:** Username, Password
