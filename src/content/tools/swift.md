---
trust_level: community
id: macos-execution-swift
namespace: macos:execution:swift
name: swift
description: Arbitrarily execute swift code from the terminal.
author: 0v3rride (https://github.com/0v3rride)
version: 1.0.0
capabilities:
- security.execution.command
- security.defenseevasion.bypass
platforms:
- macos
techniques:
- execution
- defense-evasion
execution:
  template: swift
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: 'Execute Swift code file: Executes the Swift code that is in a .swift
    file'
  command: swift mycode.swift
- description: 'Execute Swift one-liner before swift 5.8 / Xcode 14.3 Beta 1: Executes
    a Swift one-liner by piping an echoed string into the swift command'
  command: echo 'print("loobins")' | swift -
- description: 'Execute Swift one-liner with swift 5.8 / Xcode 14.3 Beta 1 or greater:
    Executes a Swift one-liner that executes the ls command to list the current directory
    using the -e option that was implemented in swift 5.8 / Xcode 14.3 Beta 1'
  command: 'swift -e ''import Foundation; let process = Process(); process.executableURL
    = URL(fileURLWithPath:"/bin/bash"); process.arguments = ["-c", "ls -alh"]; let
    stdout = Pipe(); let stderr = Pipe(); process.standardOutput = stdout; process.standardError
    = stderr; try process.run(); print(String(decoding: stdout.fileHandleForReading.readDataToEndOfFile(),
    as: UTF8.self)); print(String(decoding: stderr.fileHandleForReading.readDataToEndOfFile(),
    as: UTF8.self));'''
install:
- method: custom
  commands:
  - /usr/bin/swift
detections:
- type: other
  description: Process & Command Line Argument Detection (process contains swift)
- type: other
  url: https://github.com/jamf/jamfprotect/blob/main/custom_analytic_detections/swift_oneline_command_execution
  description: 'Jamf Protect: Detect arbitrary code execution using a swift one-liner'
references:
- label: Introduction to the Swift REPL
  url: https://developer.apple.com/swift/blog/?id=18
- label: Scripting and Compiling Swift on the Command Line
  url: https://jblevins.org/log/swift
- label: Scripting in Swift is Pretty Awesome
  url: https://krakendev.io/blog/scripting-in-swift
- label: Swift -e runs code directly from the command line
  url: https://blog.eidinger.info/swift-e-runs-code-directly-from-the-command-line
- label: Swift Programming From The Command Line
  url: https://ed.com/command-line-swift/
features:
- file-system
- pipes-stdin
- process-manip
- stealth
---

The swift command is an interactive environment (REPL) for Swift.
