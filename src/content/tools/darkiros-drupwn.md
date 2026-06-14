---
trust_level: community
id: darkiros-drupwn
namespace: darkiros:tool:drupwn
name: "drupwn"
description: "Scan drupal web site with drupwn"
version: "1.0.0"
capabilities:
  - credential.discovery.reconnaissance
platforms:
  - cross-platform
techniques:
  - discovery
execution:
  template: "drupwn"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Scan drupal web site with drupwn"
    command: "drupwn --users --nodes --modules --dfiles --themes enum [url]"
references:
  - label: "Source"
    url: "https://github.com/immunIT/drupwn"
  - label: "Darkiros"
    url: "https://darkiros.github.io/commands.html"
items:
  - NoCreds
services:
  - HTTP
  - HTTPS
---

# drupwn

Darkiros cheat sheet commands:

**Scan drupal web site with drupwn**
```
drupwn --users --nodes --modules --dfiles --themes enum [url]
```
