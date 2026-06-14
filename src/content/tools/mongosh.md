---
id: sys-mongosh
namespace: system:database:mongodb
name: mongosh
description: MongoDB Shell — interactive JavaScript interface to MongoDB.
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
  template: mongosh --help
  sandbox: execFile
examples:
- description: Display help for mongosh
  command: mongosh --help
references:
- label: mongosh Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/mongosh
install:
- method: custom
  description: Install via package manager
  commands:
  - apt-get install -y mongodb-mongosh
---
