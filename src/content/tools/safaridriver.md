---
trust_level: community
id: macos-command-and-control-safaridriver
namespace: macos:commandandcontrol:safaridriver
name: safaridriver
description: Enable the WebDriver Safari browser API for Selenium testing.
author: Brendan Chamberlain (@infosecB)
version: "1.0.0"
capabilities:
  - network.commandandcontrol
  - exfiltration.data
platforms:
  - macos
techniques:
  - command-and-control
  - exfiltration
execution:
  template: "safaridriver"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Enable safaridriver: The following command can be used to enable the WebDriver Safari browser API. The command must be run as root or with sudo privileges."
    command: "sudo safaridriver --enable"
install:
  - method: custom
    commands:
      - "/System/Cryptexes/App/usr/bin/safaridriver"
  - method: custom
    commands:
      - "/usr/bin/safaridriver"
detections:
  - type: other
    description: "No detections at time of publishing"
references:
  - label: "About WebDriver for Safari"
    url: "https://developer.apple.com/documentation/webkit/about_webdriver_for_safari"
  - label: "You Talking To Me?"
    url: "https://starlabs.sg/blog/2021/04-you-talking-to-me/"
---

safaridriver is a tool that is used to enable Selenium testing via the macOS WebDriver protocol. Once enabled, the WebDriver API could be abused by attackers to communicate with external servers for command and control or exfiltration purposes.