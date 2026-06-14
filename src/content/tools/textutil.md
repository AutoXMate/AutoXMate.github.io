---
trust_level: community
id: macos-defense-evasion-textutil
namespace: macos:defenseevasion:textutil
name: textutil
description: Manipulate text files in various formats.
author: ezaspy
version: 1.0.0
capabilities:
- security.defenseevasion.bypass
- collection.data
- credential.dump
platforms:
- macos
techniques:
- defense-evasion
- collection
- credential-access
execution:
  template: textutil
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: 'Use the textutil to read several files and build a new file: A one-liner
    can load the content of multiple RTF files in a directory, concatenate their contents,
    and write the results out as a new file. This provides two sub-use-cases; one
    is building a malicious file from a collection of smaller files which could evade
    both network and host-based security controls as the traditional means of signature-based
    detection would be redundant; two is concatenating the content of several, potentially
    sensitive files before exfiltration. This command can also be looped to iterate
    a directory of files.'
  command: textutil -convert html Quote.doc secondQuote.doc
- description: 'Capture clipboard content: By leveraging another command line tool,
    pbpaste, it is possible to write a one-liner which captures the content of the
    clipboard. If an attacker already has access to the system, the attacker could
    run this command to obtain sensitive information such as a password and then elevate
    their privileges or exfiltrate the information.'
  command: pbpaste | textutil -stdin -info > Clipboard.txt
install:
- method: custom
  commands:
  - /usr/bin/textutil
detections:
- type: other
  description: Command Line Argument Detection (args contain textutil AND (-convert
    OR -stdin OR pbpaste))
references:
- label: textutil
  url: https://osxdaily.com/tag/textutil/
features:
- file-system
- local
- stealth
---

The textutil binary is a command-line utility included in macOS that allows users to manipulate text files of various formats, using the mechanisms provided by the Cocoa text system. Formats include rtf, html, docx and others
