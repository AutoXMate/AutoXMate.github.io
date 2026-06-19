---
id: system-terminal-tmux
namespace: system:terminal:tmux
name: tmux
description: Terminal multiplexer for managing multiple shell sessions, persistent
  remote workspaces, and split-pane terminal layouts.
author: Repository Maintainers
version: 1.0.0
techniques:
- execution
capabilities:
- system.terminal.multiplex
- system.terminal.session
- system.terminal.split
- system.process.background
- system.session.persist
- system.remote.detach
platforms:
- linux
- macos
- cross-platform
risk_level: low
trust_level: verified
execution_policy: enabled
architectures:
- amd64
- arm64
- cross-platform
dependencies: []
related_tools:
- screen
- byobu
- wezterm
- zellij
artifacts:
- type: system.terminal.session
  description: Tmux session state
  trust_level: verified
- type: system.terminal.capture
  description: Captured terminal pane content
  mime: text/plain
  trust_level: verified
workflow_edges:
  produces:
  - tmux-session
  - captured-output
  consumes:
  - shell-command
contract:
  inputs:
  - type: system.terminal.command
    description: Command to execute in a tmux pane
  outputs:
  - type: system.terminal.capture
    description: Output captured from the pane
    mime: text/plain
  side_effects:
  - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 8
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 8
  network: none
  disk_io: low
allowed-tools:
- tmux
- Bash
- execFile
parameters:
- name: flag-2
  type: string
  required: false
  description: Force tmux to assume the terminal supports 256 colours
  aliases:
  - '-2'
- name: flag-c
  type: string
  required: false
  description: Execute shell-command using the default shell. If neces- sary, the
    tmux server will be started to retrieve the default-shell option. This option
    is for compatibility with sh(1) when tmux is used as...
  aliases:
  - -c
  - -c
- name: flag-f
  type: string
  required: false
  description: Specify an alternative configuration file. By default
  aliases:
  - -f
- name: flag-h
  type: string
  required: false
  description: Print usage information and exit
  aliases:
  - -h
- name: flag-L
  template_key: flag-l
  type: file
  required: false
  description: tmux stores the server socket in a directory under TMUX_TMPDIR or /tmp
    if it is unset. The default socket is named default. This option allows a different
    socket name to be specified, allowing seve...
  aliases:
  - -L
  - -n
- name: flag-l
  type: string
  required: false
  description: Behave as a login shell. This flag currently has no ef-
  aliases:
  - -l
- name: flag-S
  template_key: flag-s
  type: file
  required: false
  description: Specify a full alternative path to the server socket. If -S is specified,
    the default socket directory is not used and any -L flag is ignored
  aliases:
  - -S
  - -p
- name: flag-T
  template_key: flag-t
  type: string
  required: false
  description: Set terminal features for the client. This is a comma-
  aliases:
  - -T
- name: flag-u
  type: string
  required: false
  description: Write UTF-8 output to the terminal even if the first envi-
  aliases:
  - -u
- name: flag-v
  type: string
  required: false
  description: Request verbose logging. Log messages will be saved into
  aliases:
  - -v
- name: flag-c-2
  type: file
  required: false
  description: to working-directory
  aliases:
  - -c
- name: flag-a
  type: string
  required: false
  description: flag clears alerts (bell, activity, or silence) in all win- dows linked
    to the session
  aliases:
  - -a
- name: flag-n
  type: string
  required: false
  description: Set the flag-n parameter
  aliases:
  - -n
  - -c
  - -t
- name: flag-F
  template_key: flag-f
  type: string
  required: false
  description: Set the flag-F parameter
  aliases:
  - -F
- name: flag-C
  template_key: flag-c
  type: string
  required: false
  description: window for a control mode client, size must be one of `widthxheight'
    or `window ID:widthxheight', for example `80x24' or `@0:80x24'. -A allows a control
    mode client to trigger ac- tions on a pane. ...
  aliases:
  - -C
- name: flag-B
  template_key: flag-b
  type: number
  required: false
  description: 'The argument is split into three items by colons: name is a name for
    the subscription; what is a type of item to subscribe to; format is the format.
    After a subscription is added, changes to the fo...'
  aliases:
  - -B
- name: flag-f-2
  type: string
  required: false
  description: list of client flags, see
  aliases:
  - -f
  - -s
- name: flag-l-2
  type: string
  required: false
  description: cape sequence. If target-pane is given, the clipboard is sent (in encoded
    form), otherwise it is stored in a new paste buffer
  aliases:
  - -l
- name: flag-L-2
  template_key: flag-l-2
  type: string
  required: false
  description: right, up or down by adjustment, if the window is larger than the client.
    -c resets so that the position follows the cursor. See the window-size option
  aliases:
  - -L
  - -R
  - -U
  - -D
- name: flag-a-2
  type: string
  required: false
  description: user. If the user is already attached, the -d flag causes their clients
    to be detached
  aliases:
  - -a
  - -d
- name: flag-r
  type: string
  required: false
  description: clients read-only and -w writable. -l lists current access per- missions
  aliases:
  - -r
  - -w
  - -r
- name: flag-J
  template_key: flag-j
  type: string
  required: false
  description: Set the flag-J parameter
  aliases:
  - -J
  - -T
- name: flag-T-2
  template_key: flag-t-2
  type: string
  required: false
  description: 'will be interpreted from key-table. This may be used to config- ure
    multiple prefix keys, or to bind commands to sequences of keys. For example, to
    make typing `abc'' run the list-keys com- mand:'
  aliases:
  - -T
- name: flag-u-2
  type: string
  required: false
  description: down. -H hides the position indicator in the top right. -q cancels
    copy mode and any other modes
  aliases:
  - -u
  - -d
- name: flag-M
  template_key: flag-m
  type: string
  required: false
  description: ing, see "MOUSE SUPPORT"). -S scrolls when bound to a mouse drag event;
    for example, copy-mode -Se is bound to MouseDrag1ScrollbarSlider by default
  aliases:
  - -M
- name: flag-s
  type: string
  required: false
  description: Set the flag-s parameter
  aliases:
  - -s
  - -p
  - -p
- name: flag-e
  type: string
  required: false
  description: visible screen) should exit copy mode. While in copy mode, pressing
    a key other than those used for scrolling will disable this behaviour. This is
    intended to allow fast scrolling through a pane's ...
  aliases:
  - -e
- name: flag-w
  type: string
  required: false
  description: 'suitable for use with select-layout. For example:'
  aliases:
  - -w
- name: flag-S-2
  template_key: flag-s-2
  type: string
  required: false
  description: the first line of the visible pane and negative numbers are lines in
    the history. `-' to -S is the start of the history and to -E the end of the visible
    pane. The default is to capture only the vis...
  aliases:
  - -S
  - -E
- name: flag-y
  type: string
  required: false
  description: 'used in client mode:'
  aliases:
  - -y

- name: flag-O
  type: string
  required: false
  default: null
  description: "`creation' (time), or `activity' (time). -r reverses the sort order. -f specifies an initial filter: the filter is a format - if it evaluates to zero, the item in the list is not shown, oth- erwise it is shown. If a filter would lead to an empty list, it is ignored. -F specifies the format for each item in the list and -K a format for each shortcut key; both are evaluated once for each line. -N starts without the preview or if given twice with the larger preview. This command works only if at least one client is attached"
  aliases:
    - "-O"
- name: flag-O-2
  type: string
  required: false
  default: null
  description: "`time' (activity). -r reverses the sort order. -f specifies an initial filter: the filter is a format - if it evaluates to zero, the item in the list is not shown, otherwise it is shown. If a filter would lead to an empty list, it is ignored. -F specifies the format for each item in the tree and -K a format for each shortcut key; both are evaluated once for each line. -N starts without the preview or if given twice with the larger preview. -G includes all sessions in any session groups in the tree rather than only the first. This command works only if at least one client is attached"
  aliases:
    - "-O"
- name: flag-f-3
  type: string
  required: false
  default: null
  description: "evaluates to zero, the item in the list is not shown, otherwise it is shown. If a filter would lead to an empty list, it is ig- nored. -F specifies the format for each item in the tree. -N starts without the option information. This command works only if at least one client is attached"
  aliases:
    - "-f"
- name: flag-d
  type: string
  required: false
  default: null
  description: "means the indicator stays until a key is pressed. While the in- dicator is on screen, a pane may be chosen with the `0' to `9' keys, which will cause template to be executed as a command with `%%' substituted by the pane ID. The default template is \"se- lect-pane -t '%%'\". With -b, other commands are not blocked from running until the indicator is closed"
  aliases:
    - "-d"
    - "-p"
    - "-t"
- name: flag-m
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "-m"
- name: flag-k
  type: string
  required: false
  default: null
  description: "and a window named window-name already exists, it is selected (unless -d is also given in which case the command does noth- ing)"
  aliases:
    - "-k"
    - "-S"
- name: flag-c-3
  type: string
  required: false
  default: null
  description: "created"
  aliases:
    - "-c"
- name: flag-e-2
  type: string
  required: false
  default: null
  description: "able for the newly created window; it may be specified multiple times"
  aliases:
    - "-e"
- name: flag-I
  type: string
  required: false
  default: null
  description: "connected to the pane: with -I stdout is connected (so anything shell-command prints is written to the pane as if it were typed); with -O stdin is connected (so any output in the pane is piped to shell-command). Both may be used together and if nei- ther are specified, -O is used"
  aliases:
    - "-I"
    - "-O"
    - "-c"
- name: flag-D
  type: integer
  required: false
  default: null
  description: "adjustment is given in lines or columns (the default is 1); -x and -y may be a given as a number of lines or columns or fol- lowed by `%' for a percentage of the window size (for example `-x 10%'). With -Z, the active pane is toggled between zoomed (occupying the whole of the window) and unzoomed (its normal po- sition in the layout)"
  aliases:
    - "-D"
    - "-L"
    - "-R"
    - "-x"
    - "-y"
- name: flag-M-2
  type: string
  required: false
  default: null
  description: "binding, see \"MOUSE SUPPORT\")"
  aliases:
    - "-M"
- name: flag-T-3
  type: string
  required: false
  default: null
  description: "lines out of the history to replace them"
  aliases:
    - "-T"
- name: flag-D-2
  type: string
  required: false
  default: null
  description: "The"
  aliases:
    - "-D"
    - "-L"
    - "-R"
    - "-x"
    - "-y"
- name: flag-Z
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "-Z"
- name: flag-D-3
  type: string
  required: false
  default: null
  description: "left, to the right, or above the target pane is used. -Z keeps the window zoomed if it was zoomed. -l is the same as using the last-pane command. -e enables or -d disables input to the pane. -T sets the pane title"
  aliases:
    - "-D"
    - "-L"
    - "-R"
    - "-U"
- name: flag-m-2
  type: string
  required: false
  default: null
  description: "one marked pane at a time, setting a new marked pane clears the last. The marked pane is the default target for -s to join-pane, move-pane, swap-pane and swap-window"
  aliases:
    - "-m"
    - "-M"
- name: flag-Z-2
  type: string
  required: false
  default: null
  description: "ready zoomed"
  aliases:
    - "-Z"
- name: flag-m-3
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "-m"
- name: flag-m-4
  type: string
  required: false
  default: null
  description: "the current window"
  aliases:
    - "-m"
- name: flag-M-3
  type: string
  required: false
  default: null
  description: "key binding, see \"MOUSE SUPPORT\")"
  aliases:
    - "-M"
- name: flag-X
  type: string
  required: false
  default: null
  description: "AND PANES\" section. -N specifies a repeat count and -F expands formats in arguments where appropriate"
  aliases:
    - "-X"
- name: flag-q
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "-q"
- name: flag-F-2
  type: string
  required: false
  default: null
  description: "option, so a session inherits the option from the global options (or with -g, restores a global option to the default). -U un- sets an option (like -u) but if the option is a pane option also unsets the option on any panes in the window. value depends on the option and its type and can be omitted for flag and choice options to toggle its value (choice options toggle between the first two choices)"
  aliases:
    - "-F"
    - "-u"
- name: flag-a-3
  type: string
  required: false
  default: null
  description: "ground"
  aliases:
    - "-a"
- name: flag-d-2
  type: string
  required: false
  default: null
  description: "acter. The default is 80x24"
  aliases:
    - "-d"
- name: flag-1
  type: integer
  required: false
  default: null
  description: "resulting input is a single character. -k is like -1 but the key press is translated to a key name. -N makes the prompt only accept numeric key presses. -i executes the command every time the prompt input changes instead of when the user exits the com- mand prompt"
  aliases:
    - "-1"
- name: flag-T-4
  type: string
  required: false
  default: null
  description: "are offered when Tab is pressed. Available types are: `command', `search', `target' and `window-target'"
  aliases:
    - "-T"
- name: flag-b
  type: string
  required: false
  default: null
  description: "See popup-border-lines for possible values for border-lines"
  aliases:
    - "-b"
- name: flag-H
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "-H"
- name: flag-s-2
  type: string
  required: false
  default: null
  description: "menu border (see \"STYLES\")"
  aliases:
    - "-s"
    - "-S"
- name: flag-T-5
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "-T"
- name: flag-C-2
  type: string
  required: false
  default: null
  description: "bound to a mouse key binding"
  aliases:
    - "-C"
- name: flag-x
  type: string
  required: false
  default: null
  description: "column number, or one of the following special values:"
  aliases:
    - "-x"
    - "-y"
- name: flag-M-4
  type: string
  required: false
  default: null
  description: "only menus opened from mouse key bindings do so"
  aliases:
    - "-M"
- name: flag-v-2
  type: string
  required: false
  default: null
  description: "the format variables and their values"
  aliases:
    - "-v"
    - "-a"
- name: flag-I-2
  type: string
  required: false
  default: null
  description: "target-pane"
  aliases:
    - "-I"
- name: flag-s-3
  type: string
  required: false
  default: null
  description: "nored"
  aliases:
    - "-s"
    - "-S"
- name: flag-E
  type: string
  required: false
  default: null
  description: "-E closes the popup only if shell-command exited with success. -k allows any key to dismiss the popup instead of only `Escape' or `C-c'"
  aliases:
    - "-E"
    - "-c"
- name: flag-x-2
  type: string
  required: false
  default: null
  description: "meaning as for the display-menu command. -w and -h give the width and height - both may be a percentage (followed by `%'). If omitted, half of the terminal size is used"
  aliases:
    - "-x"
    - "-y"
- name: flag-B-2
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "-B"
- name: flag-b-2
  type: string
  required: false
  default: null
  description: "When -B is specified, the -b option is ignored. See popup-border-lines for possible values for border-lines"
  aliases:
    - "-b"
- name: flag-s-4
  type: string
  required: false
  default: null
  description: "popup border (see \"STYLES\")"
  aliases:
    - "-s"
    - "-S"
- name: flag-e-3
  type: string
  required: false
  default: null
  description: "able for the popup; it may be specified multiple times"
  aliases:
    - "-e"
- name: flag-T-6
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "-T"
- name: flag-N
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "-N"
    - "-E"
    - "-E"
    - "-k"
- name: flag-T-7
  type: string
  required: false
  default: null
  description: "See"
  aliases:
    - "-T"
- name: flag-y-2
  type: string
  required: false
  default: null
  description: "used in buffer mode:"
  aliases:
    - "-y"
- name: flag-O-3
  type: string
  required: false
  default: null
  description: "`name' or `size'. -r reverses the sort order. -f specifies an initial filter: the filter is a format - if it evaluates to zero, the item in the list is not shown, otherwise it is shown. If a filter would lead to an empty list, it is ignored. -F specifies the format for each item in the list and -K a format for each shortcut key; both are evaluated once for each line. -N starts without the preview. This command works only if at least one client is attached"
  aliases:
    - "-O"
- name: flag-w-2
  type: string
  required: false
  default: null
  description: "target-client using the xterm(1) escape sequence, if possible. If path is `-', the contents are read from stdin"
  aliases:
    - "-w"
- name: flag-E-2
  type: file
  required: false
  default: null
  description: "it. If -c is given, the current working directory is set to start-directory. If -C is not given, any output to stdout is displayed in view mode (in the pane specified by -t or the cur- rent pane if omitted) after the command finishes. If the com- mand fails, the exit status is also displayed"
  aliases:
    - "-E"

features:
- local
- interactive
execution:
  template: tmux {flag-2} {flag-c} {flag-f} {flag-h} {flag-l}
  sandbox: execFile
  timeout_seconds: 300
  shell: false
examples:
- description: Create a new named session
  command: tmux new-session -s mysession -d
- description: Attach to an existing session
  command: tmux attach-session -t mysession
- description: Split window horizontally
  command: tmux split-window -h
- description: Send a command to a pane
  command: tmux send-keys -t mysession:0 'htop' Enter
- description: Capture pane content to file
  command: tmux capture-pane -t mysession:0 -p > output.txt
- description: List all running sessions
  command: tmux list-sessions
- description: 'Start a new session:'
  command: tmux
- description: 'Start a new named session:'
  command: tmux new-session -s name
- description: 'List existing sessions:'
  command: tmux ls
- description: 'Attach to the most recently used session:'
  command: tmux attach-session
- description: 'Attach to a named session:'
  command: tmux attach-session -t name
references:
- label: Tmux manual
  url: https://man7.org/linux/man-pages/man1/tmux.1.html
- label: Tmux cheat sheet
  url: https://tmuxcheatsheet.com/
install:
- method: apt
  package_name: tmux
  commands:
  - apt-get install -y tmux
mitre_ids:
- T1059
---

# Tmux — Terminal Multiplexer

Tmux is a terminal multiplexer that allows multiple terminal sessions to be accessed simultaneously in a single window. It's essential for remote work, long-running processes, and efficient terminal workflows.

## Key Bindings

The default prefix key is `Ctrl+b`. Release both keys before pressing the command.

### Sessions
| Binding | Action |
|---------|--------|
| `Ctrl+b` `d` | Detach from session |
| `Ctrl+b` `s` | List sessions (interactive) |
| `Ctrl+b` `$` | Rename current session |
| `Ctrl+b` `(` / `)` | Switch to previous/next session |

### Windows
| Binding | Action |
|---------|--------|
| `Ctrl+b` `c` | Create new window |
| `Ctrl+b` `,` | Rename current window |
| `Ctrl+b` `n` / `p` | Next/previous window |
| `Ctrl+b` `w` | List windows |

### Panes
| Binding | Action |
|---------|--------|
| `Ctrl+b` `%` | Split vertically |
| `Ctrl+b` `"` | Split horizontally |
| `Ctrl+b` `arrow` | Navigate panes |
| `Ctrl+b` `z` | Zoom pane fullscreen |
| `Ctrl+b` `x` | Kill current pane |

## Configuration

Create `~/.tmux.conf`:

```bash
# Use Ctrl+a as prefix (easier reach)
set -g prefix C-a
unbind C-b
bind C-a send-prefix

# Mouse support
set -g mouse on

# Increase scrollback
set -g history-limit 50000

# Status bar customization
set -g status-bg colour235
set -g status-fg white
set -g status-interval 5
```

## Headless Operation

```bash
# Create session without attaching
tmux new-session -d -s mysession 'python server.py'

# Send additional commands later
tmux send-keys -t mysession 'curl http://localhost:8080/health' Enter

# Capture output
tmux capture-pane -t mysession -p
```

## Related Tools

- **[screen](../../terminal/screen.md)** — Classic terminal multiplexer
- **[byobu](../../terminal/byobu.md)** — Screen/tmux wrapper with profiles
- **[zellij](../../terminal/zellij.md)** — Modern terminal multiplexer written in Rust
