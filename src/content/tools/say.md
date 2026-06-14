---
trust_level: community
id: macos-defense-evasion-say
namespace: macos:defenseevasion:say
name: say
description: Convert text to audible speech.
author: Pinar Sadioglu (@p_sadioglu)
version: "1.0.0"
capabilities:
  - security.defenseevasion.bypass
  - collection.data
  - reconnaissance.enumerate
  - discovery.enumerate
platforms:
  - macos
techniques:
  - defense-evasion
  - collection
  - recon
  - discovery
execution:
  template: "say"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Read sensitive data: The following command can read and process sensitive files and redirects the output to a file.."
    command: "say -f /home/user/sensitive-files -i  > loot.txt;"
  - description: "Collect clipboard data: The command is designed to enhance privacy by muting the system volume,using a less recognizable \"Whisper\" voice with the \"say\" command, processing the copied text in the clipboard, and saving the output to a file named \"loot.txt.\""
    command: "osascript -e 'set volume output muted true' ;   say $(pbpaste) -i  > loot.txt;"
install:
  - method: custom
    commands:
      - "/usr/bin/say"
detections:
  - type: other
    description: "No detection content available"
references:
  - label: "say man page"
    url: "https://ss64.com/osx/say.html"
---

This tool uses the Speech Synthesis manager to convert input text to audible speech and either play it through the sound output device chosen in System Preferences or save it to an AIFF file.