---
trust_level: community
id: darkiros-kerbrute
namespace: darkiros:tool:kerbrute
name: "kerbrute"
description: "kerbrute - kerberos user enumeration"
version: "1.0.0"
capabilities:
  - credential.bruteforce.generic
platforms:
  - cross-platform
techniques:
  - credential-access
execution:
  template: "kerbrute"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "kerbrute - kerberos user enumeration"
    command: "kerbrute userenum --dc [dc-ip] -d [domain] [user.txt]"
references:
  - label: "Source"
    url: "https://github.com/ropnop/kerbrute"
  - label: "Darkiros"
    url: "https://darkiros.github.io/commands.html"
items:
  - NoCreds
  - Password
services:
  - Kerberos
---

# kerbrute

Darkiros cheat sheet commands:

**kerbrute - kerberos user enumeration**
```
kerbrute userenum --dc [dc-ip] -d [domain] [user.txt]
```
