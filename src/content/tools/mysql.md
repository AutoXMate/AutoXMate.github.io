---
id: database-mysql-mysql
namespace: database:mysql:mysql
name: mysql
description: MySQL client, can execute SQL queries and read files via LOAD DATA.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - system.file.read
  - security.execution.command
platforms:
  - linux
  - macos
  - bsd
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - psql
  - sqlite3
artifacts: []
workflow_edges:
  produces:
    - file-content
    - command-execution
  consumes:
    - file
    - execution-context
contract:
  inputs: []
  outputs:
    - type: process.output
      description: Query output
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
  - mysql
  - psql
  - Bash
  - execFile
parameters: []
features:
  - file-system
  - interactive
execution:
  template: "mysql -e 'SELECT LOAD_FILE(\"/path/to/file\")'"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Read a file via mysql
    command: mysql -e 'SELECT LOAD_FILE("/path/to/file")'
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/mysql/"
techniques:
  - collection
  - execution
install:
  - method: apt
    package_name: "mysql-client"
    commands:
      - "apt-get install -y mysql-client"
---
