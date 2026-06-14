---
trust_level: community
id: darkiros-gobuster
namespace: darkiros:tool:gobuster
name: gobuster
description: Fuzz a web site with gobuster with classic extensions
version: 1.0.0
capabilities:
- security.execution.fuzzing
platforms:
- cross-platform
techniques:
- execution
execution:
  template: gobuster
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: Fuzz a web site with gobuster with classic extensions
  command: gobuster dir -u [url] -w [wordlist] -x php,html,txt,xml,md [add_other]
    -o [outputfile]
references:
- label: Source
  url: https://github.com/OJ/gobuster
- label: Darkiros
  url: https://darkiros.github.io/commands.html
items:
- NoCreds
services:
- HTTP
- HTTPS
- DNS
features:
- pipes-stdin
---

# gobuster

Darkiros cheat sheet commands:

**Fuzz a web site with gobuster with classic extensions**
```
gobuster dir -u [url] -w [wordlist] -x php,html,txt,xml,md [add_other] -o [outputfile]
```
