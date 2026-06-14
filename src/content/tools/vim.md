---
id: editor-vim-vim
namespace: editor:vim:vim
name: vim
description: "Vim text editor; can execute arbitrary commands and read/write files via embedded interpreters."
author: GTFOBins
version: 1.0.0
capabilities:
- system.file.read
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
- vim
parameters: []
features: []
execution:
  template: vim
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Read arbitrary files (sudo, suid, unprivileged)
  command: vim -c ':redir! >/path/to/output-file | echo "DATA" | redir END | q'
- description: Leverage python capabilities
  command: vim -c ':py ...'
- description: Leverage lua capabilities
  command: vim -c ':lua ...'
- description: Leverage vi capabilities
  command: vim
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/vim/
techniques:
- collection
install:
- method: apt
  package_name: vim
  commands:
  - apt-get install -y vim
---


# vim

vim is a command-line utility. Improved vi editor, can execute arbitrary commands and read/write files; can also read arbitrary files Can also leverage capabilities from: python, lua, vi.
