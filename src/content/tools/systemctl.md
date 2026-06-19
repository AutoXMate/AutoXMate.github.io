---
id: system-service-systemctl
namespace: system:service:systemctl
name: systemctl
description: Control the systemd system and service manager
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - system.service.systemctl
platforms:
  - linux
risk_level: medium
trust_level: verified
execution_policy: enabled
architectures:
  - amd64
  - arm64
features:
  - local
  - requires-root
techniques:
  - execution
  - persistence
parameters:
  - name: help
    type: string
    required: false
    description: "Show this help"
    aliases:
      - -h
      - --help
  - name: version
    type: string
    required: false
    description: "Show package version"
    aliases:
      - --version
  - name: system
    type: string
    required: false
    description: "Connect to system manager"
    aliases:
      - --system
  - name: user
    type: string
    required: false
    description: "Connect to user service manager"
    aliases:
      - --user
  - name: capsule
    type: string
    required: false
    description: "Connect to service manager of specified capsule"
    aliases:
      - -C
      - --capsule
  - name: host
    type: string
    required: false
    description: "Set the host parameter"
    aliases:
      - -H
      - --host
  - name: machine
    type: string
    required: false
    description: "Set the machine parameter"
    aliases:
      - -M
      - --machine
  - name: type
    type: string
    required: false
    description: "List units of a particular type"
    aliases:
      - -t
      - --type
  - name: state
    type: string
    required: false
    description: "List units with particular LOAD or SUB or ACTIVE state"
    aliases:
      - --state
  - name: failed
    type: string
    required: false
    description: "Shortcut for --state=failed"
    aliases:
      - --failed
  - name: property
    type: string
    required: false
    description: "Show only properties by this name"
    aliases:
      - -p
      - --property
  - name: flag-P
    template_key: flag-p
    type: string
    required: false
    description: "Equivalent to --value --property=NAME"
    aliases:
      - -P
  - name: all
    type: string
    required: false
    description: "Show all properties/all units currently in memory"
    aliases:
      - -a
      - --all
  - name: full
    type: string
    required: false
    description: "Don't ellipsize unit names on output"
    aliases:
      - -l
      - --full
  - name: recursive
    type: array
    required: false
    description: "Show unit list of host and local containers"
    aliases:
      - -r
      - --recursive
  - name: reverse
    type: string
    required: false
    description: "Show reverse dependencies with 'list-dependencies'"
    aliases:
      - --reverse
  - name: before
    type: string
    required: false
    description: "Show units ordered before with 'list-dependencies'"
    aliases:
      - --before
  - name: after
    type: string
    required: false
    description: "Show units ordered after with 'list-dependencies'"
    aliases:
      - --after
  - name: with-dependencies S
    template_key: with-dependencies-s
    type: string
    required: false
    description: "'list-units', and 'list-unit-files'. --job-mode=MODE Specify how
      to deal with already queued jobs, when queueing a new job"
    aliases:
      - --with-dependencies S
  - name: show-transaction
    type: string
    required: false
    description: "--show-types When showing sockets, explicitly show their type --value
      When showing properties, only print the value --check-inhibitors=MODE Whether
      to check inhibitors before shutting down, sleepin..."
    aliases:
      - -T
      - --show-transaction
  - name: flag-i
    type: string
    required: false
    description: "Shortcut for --check-inhibitors=no"
    aliases:
      - -i
  - name: signal
    type: string
    required: false
    description: "Which signal to send"
    aliases:
      - -s
      - --signal
  - name: kill-whom
    type: string
    required: false
    description: "Whom to send signal to"
    aliases:
      - --kill-whom
  - name: kill-value
    type: integer
    required: false
    description: "Signal value to enqueue"
    aliases:
      - --kill-value
  - name: kill-subgroup
    type: file
    required: false
    description: "Send signal to sub-control group only --what=RESOURCES Which types
      of resources to remove --now Start or stop unit after enabling or disabling
      it --dry-run Only print what would be done Currently s..."
    aliases:
      - --kill-subgroup
  - name: quiet
    type: string
    required: false
    description: "Suppress output"
    aliases:
      - -q
      - --quiet
  - name: verbose
    type: string
    required: false
    description: "Show unit logs while executing operation"
    aliases:
      - -v
      - --verbose
  - name: no-warn
    type: string
    required: false
    description: "Suppress several warnings shown by default"
    aliases:
      - --no-warn
  - name: wait
    type: string
    required: false
    description: "For (re)start, wait until service stopped again"
    aliases:
      - --wait
  - name: no-block
    type: string
    required: false
    description: "Do not wait until operation finished"
    aliases:
      - --no-block

  - name: boot-loader-menu
    type: number
    required: false
    default: null
    description: "Boot into boot loader menu on next boot --boot-loader-entry=NAME Boot into a specific boot loader entry on next boot --reboot-argument=ARG Specify argument string to pass to reboot() --plain Print unit dependencies as a list instead of a tree --timestamp=FORMAT Change format of printed timestamps (pretty, unix, us, utc, us+utc) --read-only Create read-only bind mount --mkdir Create directory before mounting, if missing --marked Restart/reload previously marked units --drop-in=NAME Edit unit files using the specified drop-in file name --when=TIME Schedule halt/power-off/reboot/kexec action after a certain timestamp --stdin Read new contents of edited file from stdin"
    aliases:
      - "--boot-loader-menu"
  - name: boot_loader_entry
    type: boolean
    required: false
    description: ""
    aliases:
      - "--boot-loader-entry"
  - name: check_inhibitors
    type: boolean
    required: false
    description: ""
    aliases:
      - "--check-inhibitors"
  - name: drop_in
    type: boolean
    required: false
    description: "Edit unit files using the specified drop-in file name"
    aliases:
      - "--drop-in"
  - name: dry_run
    type: boolean
    required: false
    description: "Only print what would be done"
    aliases:
      - "--dry-run"
  - name: firmware-setup
    type: string
    required: false
    default: null
    description: "Tell the firmware to show the setup menu on next boot"
    aliases:
      - "--firmware-setup"
  - name: force
    type: string
    required: false
    default: null
    description: "When enabling unit files, override existing symlinks"
    aliases:
      - "-f"
      - "--force"
  - name: global
    type: string
    required: false
    default: null
    description: "Edit/enable/disable/mask default user unit files"
    aliases:
      - "--global"
  - name: image
    type: file
    required: false
    default: null
    description: "Edit/enable/disable/mask unit files in the specified"
    aliases:
      - "--image"
  - name: image-policy
    type: string
    required: false
    default: null
    description: "Specify disk image dissection policy"
    aliases:
      - "--image-policy"
  - name: job_mode
    type: boolean
    required: false
    description: "Specify how to deal with already queued jobs, when"
    aliases:
      - "--job-mode"
  - name: legend
    type: string
    required: false
    default: null
    description: "Enable/disable the legend (column headers and hints)"
    aliases:
      - "--legend"
  - name: lines
    type: integer
    required: false
    default: null
    description: "Number of journal entries to show"
    aliases:
      - "-n"
      - "--lines"
  - name: marked
    type: boolean
    required: false
    description: "Restart/reload previously marked units"
    aliases:
      - "--marked"
  - name: message
    type: string
    required: false
    default: null
    description: "Specify human-readable reason for system shutdown"
    aliases:
      - "--message"
  - name: mkdir
    type: boolean
    required: false
    description: "Create directory before mounting, if missing"
    aliases:
      - "--mkdir"
  - name: no-ask-password
    type: string
    required: false
    default: null
    description: "Do not ask for system passwords"
    aliases:
      - "--no-ask-password"
  - name: no-pager
    type: string
    required: false
    default: null
    description: "Do not pipe output into a pager"
    aliases:
      - "--no-pager"
  - name: no-reload
    type: string
    required: false
    default: null
    description: "Don't reload daemon after en-/dis-abling unit files"
    aliases:
      - "--no-reload"
  - name: no-wall
    type: string
    required: false
    default: null
    description: "Don't send wall message before halt/power-off/reboot"
    aliases:
      - "--no-wall"
  - name: now
    type: boolean
    required: false
    description: "Start or stop unit after enabling or disabling it"
    aliases:
      - "--now"
  - name: output
    type: string
    required: false
    default: null
    description: "Change journal output mode (short, short-precise"
    aliases:
      - "-o"
      - "--output"
  - name: plain
    type: boolean
    required: false
    description: "Print unit dependencies as a list instead of a tree"
    aliases:
      - "--plain"
  - name: preset-mode
    type: string
    required: false
    default: null
    description: "Apply only enable, only disable, or all presets"
    aliases:
      - "--preset-mode"
  - name: read_only
    type: boolean
    required: false
    description: "Create read-only bind mount"
    aliases:
      - "--read-only"
  - name: reboot_argument
    type: boolean
    required: false
    description: ""
    aliases:
      - "--reboot-argument"
  - name: root
    type: file
    required: false
    default: null
    description: "Edit/enable/disable/mask unit files in the specified"
    aliases:
      - "--root"
  - name: runtime
    type: string
    required: false
    default: null
    description: "Edit/enable/disable/mask unit files temporarily until"
    aliases:
      - "--runtime"
  - name: show_types
    type: boolean
    required: false
    description: "When showing sockets, explicitly show their type"
    aliases:
      - "--show-types"
  - name: stdin
    type: boolean
    required: false
    description: "Read new contents of edited file from stdin"
    aliases:
      - "--stdin"
  - name: value
    type: boolean
    required: false
    description: "When showing properties, only print the value"
    aliases:
      - "--value"
  - name: what
    type: boolean
    required: false
    description: "Which types of resources to remove"
    aliases:
      - "--what"
  - name: when
    type: boolean
    required: false
    description: "/reboot/kexec action after"
    aliases:
      - "--when"
      - "-off"

execution:
  template: "systemctl -h {help} --version {version} --system {system} --user {user}
    -C {capsule}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Basic usage with help"
    command: "systemctl ${help}"
  - description: "Display help message"
    command: "systemctl --help"
  - description: Show only a given value from one of the `show` keys. In this example,
      the value for the `ActiveState` key for the UFW service will be shown, and only
      it; ideal for scripting. Using the `--value` flag causes only the value to be
      displayed.
    command: systemctl show -p ActiveState --value ufw
  - description: Start, stop, or restart a given service(s).
    command: systemctl [start|stop|restart] [SERVICE]
  - description: Check if a given service(s) is active. If it is, 'active' will display.
      An exit status of 0 will be given if it's active, and non-zero otherwise. Use
      the `-q` or `--quiet` flag to rely only on the exit status.
    command: systemctl is-active ufw
  - description: Check if a given service(s) has failed. If it is, 'failed' will display.
      An exit status of 0 will be given if it has failed, and non-zero otherwise.
      Use the `-q` or `--quiet` flag to rely only on the exit status.
    command: systemctl is-active ufw
  - description: Check if a given service(s) is enabled. If it is, 'enabled' will
      display. An exit status of 0 will be given if it's enabled, and non-zero otherwise.
      Use the `-q` or `--quiet` flag to rely only on the exit status.
    command: systemctl is-enabled ufw
  - description: List all failed services.
    command: systemctl --failed
  - description: Shut the system down. Use `suspend` to suspend, `halt` to halt, and
      `reboot` to instead of reboot the machine.
    command: systemctl poweroff
  - description: Enable or disable a given service(s).
    command: systemctl [enable|disable] [SERVICE]
  - description: Show the current status of a given service(s).
    command: systemctl status [SERVICE]
related_tools:
  - system-service-journalctl
install:
    - method: apt
      package_name: "systemd"
      commands:
        - "apt-get install -y systemd"
---


# systemctl — Control the systemd system and service manager

## Overview

`systemctl` is a command-line utility for control the systemd system and service manager.

## Usage

```
systemctl -h {help} --version {version} --system {system} --user {user} -C {capsule}
```
