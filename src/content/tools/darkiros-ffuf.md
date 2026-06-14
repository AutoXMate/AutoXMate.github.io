---
trust_level: community
id: darkiros-ffuf
namespace: darkiros:tool:ffuf
name: ffuf
description: Fuzz a web site with ffuf with classic extensions
version: 1.0.0
capabilities:
- security.execution.fuzzing
platforms:
- cross-platform
techniques:
- execution
execution:
  template: ffuf
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: Fuzz a web site with ffuf with classic extensions
  command: ffuf -u [url]/FUZZ -w [wordlist]
- description: Fuzz a web site with ffuf with a custom header and response size and
    code filter
  command: 'ffuf -u [url]/FUZZ -w [wordlist] -H ''Cookie: [cookie]'' -fs [size] -fc
    [code]'
- description: Fuzz a web site with ffuf with a post data
  command: ffuf -u [url] -w [wordlist] -X POST -d '[data]'
references:
- label: Source
  url: https://github.com/ffuf/ffuf
- label: Darkiros
  url: https://darkiros.github.io/commands.html
items:
- NoCreds
services:
- HTTP
- HTTPS
features:
- pipes-stdin
---

# ffuf

Darkiros cheat sheet commands:

**Fuzz a web site with ffuf with classic extensions**
```
ffuf -u [url]/FUZZ -w [wordlist]
```

**Fuzz a web site with ffuf with a custom header and response size and code filter**
```
ffuf -u [url]/FUZZ -w [wordlist] -H 'Cookie: [cookie]' -fs [size] -fc [code]
```

**Fuzz a web site with ffuf with a post data**
```
ffuf -u [url] -w [wordlist] -X POST -d '[data]'
```
