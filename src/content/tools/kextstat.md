---
trust_level: community
id: macos-discovery-kextstat
namespace: macos:discovery:kextstat
name: kextstat
description: Display the status of loaded kernel extensions (kexts)
author: Mark Morowczynsk (@markmorow)
version: 1.0.0
capabilities:
- discovery.enumerate
platforms:
- macos
techniques:
- discovery
execution:
  template: kextstat
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: 'List kernel extensions: Uses kexstat showloaded to display kernel
    extensions and address in kernel memory it has been loaded'
  command: kexstat
install:
- method: custom
  commands:
  - /usr/sbin/kextstat
detections:
- type: other
  description: No detections at time of publishing
references:
- label: kextstat man page
  url: https://ss64.com/osx/kextstat.html
features:
- pipes-stdout
---

Deprecated tool in favor of kmutil. Lists loaded kernel extensions
