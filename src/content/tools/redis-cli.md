---
id: redis-cli
namespace: system:database:redis
name: redis-cli
description: Redis command line client for querying and managing Redis instances.
version: 1.0.0
capabilities:
- system.information-gathering
- system.monitoring
- system.administration
platforms:
- linux
features:
- local
mitre_ids: []
parameters: []
execution:
  template: redis-cli --help
  sandbox: execFile
examples:
- description: Display help for redis-cli
  command: redis-cli --help
references:
- label: redis-cli Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/redis-cli
install:
- method: custom
  description: Install via package manager
  commands:
  - apt-get install -y redis-tools
---
