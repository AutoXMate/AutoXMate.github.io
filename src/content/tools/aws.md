---
id: cloud-aws-cli
namespace: cloud:aws:cli
name: aws
description: AWS command-line interface for managing cloud resources, can read files via EC2 filter option.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - cloud.aws.manage
  - cloud.aws.ec2
  - cloud.aws.s3
  - system.file.read
platforms:
  - linux
  - macos
  - windows
  - cross-platform
risk_level: low
trust_level: verified
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - gcloud
  - az
artifacts:
  - type: cloud.aws.config
    description: AWS configuration
    mime: text/plain
    trust_level: verified
workflow_edges:
  produces:
    - cloud-resources
    - file-content
  consumes:
    - aws-credentials
contract:
  inputs:
    - type: cloud.aws.service
      description: AWS service and command
  outputs:
    - type: cloud.aws.result
      description: AWS CLI output
      mime: application/json
  side_effects:
    - network_traffic
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
  - aws
  - Bash
  - execFile
parameters:
  - name: filter
    type: string
    required: false
    description: "Resource filter option"
    aliases:
      - --filter
features:
  - network-intensive
  - output-json
execution:
  template: "aws {0}"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars:
  target: url
examples:
  - description: Read arbitrary file via EC2 describe-instances filter file
    command: aws ec2 describe-instances --filter file:///path/to/input-file
  - description: Access AWS help via pager (less) for file escape
    command: aws help
references:
  - label: "AWS CLI documentation"
    url: "https://aws.amazon.com/cli/"
techniques:
  - collection
  - discovery
install:
    - method: pip
      commands:
        - "pip install awscli"
---


# aws — AWS Command-Line Interface

The AWS CLI manages Amazon Web Services from the command line. When used with sudo or SUID, it can read arbitrary files through the `--filter file://` option on EC2 describe calls, and spawn a less pager through `aws help`.
