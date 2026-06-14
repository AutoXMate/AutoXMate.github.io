---
id: database-postgres-psql
namespace: database:postgres:psql
name: psql
description: PostgreSQL client, can execute SQL queries and read files via COPY.
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
  - mysql
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
    memory_mb: 8
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 8
  network: none
  disk_io: low
allowed-tools:
  - psql
  - mysql
  - Bash
  - execFile
parameters: []
features:
  - file-system
  - interactive
execution:
  template: "psql -c \"COPY (SELECT '') TO PROGRAM '/bin/sh'\""
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Execute command via psql
    command: psql -c "COPY (SELECT '') TO PROGRAM '/bin/sh'"
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/psql/"
techniques:
  - collection
  - execution
install:
  - method: apt
    package_name: "postgresql-client"
    commands:
      - "apt-get install -y postgresql-client"
---
