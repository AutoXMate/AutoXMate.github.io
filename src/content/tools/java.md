---
id: runtime-java
namespace: runtime:jvm:java
name: java
description: Java runtime that can execute compiled Java class files to spawn shells.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
  - security.execution.command
  - runtime.java.execute
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
  - javac
  - jshell
artifacts: []
workflow_edges:
  produces:
    - shell-access
  consumes:
    - class-file
contract:
  inputs:
    - type: system.file.path
      description: Path to Java class file
  outputs:
    - type: process.output
      description: Shell output
  side_effects:
    - process_spawn
  resource_cost:
    cpu: high
    memory_mb: 64
    network: low
    disk_io: low
resource_profile:
  cpu: high
  memory_mb: 64
  network: low
  disk_io: low
allowed-tools:
  - java
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "java {0}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn interactive shell via compiled Java class
    command: |-
      cat >Shell.java <<EOF
      public class Shell {
          public static void main(String[] args) throws Exception {
              new ProcessBuilder("/bin/sh").inheritIO().start().waitFor();
          }
      }
      EOF
      javac Shell.java
      java Shell
references:
  - label: "Java documentation"
    url: "https://docs.oracle.com/en/java/"
techniques:
  - privilege-escalation
  - execution
install:
    - method: apt
      package_name: "default-jre"
      commands:
        - "apt-get install -y default-jre"
---


# java — Java Runtime

java executes compiled Java class files. With sudo, it can spawn a shell by uploading and running a compiled class file that executes `/bin/sh`.
