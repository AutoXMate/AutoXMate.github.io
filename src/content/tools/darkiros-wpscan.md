---
trust_level: community
id: darkiros-wpscan
namespace: darkiros:tool:wpscan
name: "WPSCAN"
description: "Scan wordpress web site with wpscan"
version: "1.0.0"
capabilities:
  - credential.discovery.reconnaissance
platforms:
  - cross-platform
techniques:
  - discovery
execution:
  template: "wpscan"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Scan wordpress web site with wpscan"
    command: "wpscan --proxy http://127.0.0.1:8080 --url [url] --disable-tls-checks -e ap,tt,cb,dbe,u1-20,m --api-token [wpscan_apitoken]"
references:
  - label: "Source"
    url: "https://github.com/wpscanteam/wpscan"
  - label: "Darkiros"
    url: "https://darkiros.github.io/commands.html"
items:
  - NoCreds
services:
  - HTTP
  - HTTPS
---

# WPSCAN

Darkiros cheat sheet commands:

**Scan wordpress web site with wpscan**
```
wpscan --proxy http://127.0.0.1:8080 --url [url] --disable-tls-checks -e ap,tt,cb,dbe,u1-20,m --api-token [wpscan_apitoken]
```
