---
trust_level: community
id: macos-execution-funzip
namespace: macos:execution:funzip
name: funzip
description: The malicious binaries use funzip to extract the malicious binary with a password and using head or tail commands.
author: Pratik Jeware
version: "1.0.0"
capabilities:
  - security.execution.command
platforms:
  - macos
techniques:
  - execution
execution:
  template: "funzip"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "extracts a ZIP or gzip file directly to output from archives or other piped input: funzip is a macOS utility used to extract ZIP or gzip files directly to output. Malicious binaries misuse funzip, along with head or tail, to extract and reconstruct password-protected malicious payloads."
    command: "tail -c <> $0 | funzip  -<password>"
install:
  - method: custom
    commands:
      - "/usr/bin/funzip"
detections:
  - type: other
    description: "No detections at time of publishing"
references:
  - label: "MacOS: Bashed Apples of Shlayer and Bundlore"
    url: "https://www.uptycs.com/blog/threat-research-report-team/macos-bashed-apples-of-shlayer-and-bundlore"
  - label: "funzip man page"
    url: "https://linux.die.net/man/1/funzip"
---

funzip is a macOS utility that extracts a ZIP or gzip file directly to output from archives or other piped input. The malicious binaries use funzip to extract the malicious binary with a password and using head or tail commands.