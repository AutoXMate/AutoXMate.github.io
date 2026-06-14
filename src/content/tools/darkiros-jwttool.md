---
trust_level: community
id: darkiros-jwttool
namespace: darkiros:tool:jwttool
name: "JwtTool"
description: "Bruteforce a JWT token key"
version: "1.0.0"
capabilities:
  - credential.discovery.reconnaissance
platforms:
  - cross-platform
techniques:
  - discovery
execution:
  template: "jwttool"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Bruteforce a JWT token key"
    command: "python3 jwt_tool.py -d [wordlist] [token]"
  - description: "JWT tool perform all test on a token"
    command: "python3 jwt_tool.py -M at -t \\\"[url]\\\" -rh \\\"Authorization: Bearer [JWT_Token]\\\" -rh \\\"[other_header]\\\" -rc \\\"[cookies]\\\""
references:
  - label: "Source"
    url: "https://github.com/ticarpi/jwt_tool"
  - label: "Darkiros"
    url: "https://darkiros.github.io/commands.html"
items:
  - Password
services:
  - HTTP
  - HTTPS
---

# JwtTool

Darkiros cheat sheet commands:

**Bruteforce a JWT token key**
```
python3 jwt_tool.py -d [wordlist] [token]
```

**JWT tool perform all test on a token**
```
python3 jwt_tool.py -M at -t \"[url]\" -rh \"Authorization: Bearer [JWT_Token]\" -rh \"[other_header]\" -rc \"[cookies]\"
```
