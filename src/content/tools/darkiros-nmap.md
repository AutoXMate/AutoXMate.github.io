---
trust_level: community
id: darkiros-nmap
namespace: darkiros:tool:nmap
name: nmap
description: Nmap - hosts alive
version: 1.0.0
capabilities:
- credential.discovery.reconnaissance
platforms:
- cross-platform
techniques:
- discovery
execution:
  template: nmap
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: Nmap - hosts alive
  command: nmap -sn [ip_range]
- description: Nmap - classic scan
  command: nmap -sC -sV [ip]
- description: Nmap - read targets from file
  command: nmap -iL [file]
- description: Nmap - scan all port full
  command: nmap -Pn -sC -sV -p [port] [ip] -oN scan.txt --reason --script=vuln
- description: Nmap - UDP scan
  command: nmap -sU [ip]
- description: Nmap - SMB signin disabled
  command: nmap -Pn -sS -T4 --open --script smb-security-mode -p 445 [ip]
- description: Nmap - kerberos user enumeration
  command: nmap -p 88 --script krb5-enum-users --script-args krb5-enum-users.realm=[domain]
    [dc-ip]
references:
- label: Source
  url: https://nmap.org/
- label: Darkiros
  url: https://darkiros.github.io/commands.html
items:
- NoCreds
services:
- DNS
features:
- network-intensive
mitre_ids:
- T1046
- T1595
---

# nmap

Darkiros cheat sheet commands:

**Nmap - hosts alive**
```
nmap -sn [ip_range]
```

**Nmap - classic scan**
```
nmap -sC -sV [ip]
```

**Nmap - read targets from file**
```
nmap -iL [file]
```

**Nmap - scan all port full**
```
nmap -Pn -sC -sV -p [port] [ip] -oN scan.txt --reason --script=vuln
```

**Nmap - UDP scan**
```
nmap -sU [ip]
```

**Nmap - SMB signin disabled**
```
nmap -Pn -sS -T4 --open --script smb-security-mode -p 445 [ip]
```

**Nmap - kerberos user enumeration**
```
nmap -p 88 --script krb5-enum-users --script-args krb5-enum-users.realm=[domain] [dc-ip]
```
