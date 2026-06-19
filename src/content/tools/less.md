---
id: system-file-less
namespace: system:file:less
name: less
description: View file contents page by page
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - system.file.less
  - system.file.search
  - system.file.process
  - system.file.copy
  - system.file.move
  - system.file.delete
platforms:
  - linux
risk_level: low
trust_level: verified
execution_policy: enabled
architectures:
  - amd64
  - arm64
features:
  - local
  - file-system
  - pipes-stdin
  - pipes-stdout
techniques:
  - collection
  - data-manipulation
  - discovery
  - enumeration
  - execution
  - persistence
  - process-manip
parameters:
  - name: help
    type: string
    required: false
    description: "Display help (from command line)"
    aliases:
      - -?
      - --help
  - name: search-skip-screen
    type: string
    required: false
    description: "Search skips current screen"
    aliases:
      - -a
      - --search-skip-screen
  - name: SEARCH-SKIP-SCREEN
    template_key: search-skip-screen
    type: string
    required: false
    description: "Search starts just after target line"
    aliases:
      - -A
      - --SEARCH-SKIP-SCREEN
  - name: buffers
    type: integer
    required: false
    description: "Number of buffers"
    aliases:
      - -b
      - --buffers
  - name: auto-buffers
    type: string
    required: false
    description: "Don't automatically allocate buffers for pipes"
    aliases:
      - -B
      - --auto-buffers
  - name: clear-screen
    type: string
    required: false
    description: "Repaint by clearing rather than scrolling"
    aliases:
      - -c
      - --clear-screen
  - name: dumb
    type: string
    required: false
    description: "Dumb terminal"
    aliases:
      - -d
      - --dumb
  - name: color
    type: string
    required: false
    description: "Set screen colors"
    aliases:
      - -D
      - --color
  - name: quit-at-eof
    type: string
    required: false
    description: "Quit at end of file"
    aliases:
      - -e
      - -E
      - --quit-at-eof
      - --QUIT-AT-EOF
  - name: force
    type: string
    required: false
    description: "Force open non-regular files"
    aliases:
      - -f
      - --force
  - name: quit-if-one-screen
    type: string
    required: false
    description: "Quit if entire file fits on first screen"
    aliases:
      - -F
      - --quit-if-one-screen
  - name: hilite-search
    type: string
    required: false
    description: "Highlight only last match for searches"
    aliases:
      - -g
      - --hilite-search
  - name: HILITE-SEARCH
    template_key: hilite-search
    type: string
    required: false
    description: "Don't highlight any matches for searches"
    aliases:
      - -G
      - --HILITE-SEARCH
  - name: max-back-scroll
    type: integer
    required: false
    description: "Backward scroll limit"
    aliases:
      - -h
      - --max-back-scroll
  - name: ignore-case
    type: string
    required: false
    description: "Ignore case in searches that do not contain uppercase"
    aliases:
      - -i
      - --ignore-case
  - name: IGNORE-CASE
    template_key: ignore-case
    type: string
    required: false
    description: "Ignore case in all searches"
    aliases:
      - -I
      - --IGNORE-CASE
  - name: jump-target
    type: integer
    required: false
    description: "Screen position of target lines"
    aliases:
      - -j
      - --jump-target
  - name: status-column
    type: string
    required: false
    description: "Display a status column at left edge of screen"
    aliases:
      - -J
      - --status-column
  - name: lesskey-file
    type: string
    required: false
    description: "Use a compiled lesskey file"
    aliases:
      - -k
      - --lesskey-file
  - name: quit-on-intr
    type: string
    required: false
    description: "Exit less in response to ctrl-C"
    aliases:
      - -K
      - --quit-on-intr
  - name: no-lessopen
    type: string
    required: false
    description: "Ignore the LESSOPEN environment variable"
    aliases:
      - -L
      - --no-lessopen
  - name: long-prompt
    type: string
    required: false
    description: "Set prompt style"
    aliases:
      - -m
      - -M
      - --long-prompt
      - --LONG-PROMPT
  - name: line-numbers
    type: string
    required: false
    description: "Suppress line numbers in prompts and messages"
    aliases:
      - -n
      - --line-numbers
  - name: LINE-NUMBERS
    template_key: line-numbers
    type: string
    required: false
    description: "Display line number at start of each line"
    aliases:
      - -N
      - --LINE-NUMBERS
  - name: log-file
    type: file
    required: false
    description: "Copy to log file (standard input only)"
    aliases:
      - -o
      - --log-file
  - name: LOG-FILE
    template_key: log-file
    type: file
    required: false
    description: "Copy to log file (unconditionally overwrite)"
    aliases:
      - -O
      - --LOG-FILE
  - name: pattern
    type: string
    required: false
    description: "Start at pattern (from command line)"
    aliases:
      - -p
      - --pattern
  - name: flag-P
    template_key: flag-p
    type: string
    required: false
    description: "--prompt=[prompt]"
    aliases:
      - -P
  - name: quiet
    type: string
    required: false
    description: "Quiet the terminal bell"
    aliases:
      - -q
      - -Q
      - --quiet
      - --QUIET
      - --silent
      - --SILENT
  - name: raw-control-chars
    type: string
    required: false
    description: "Output \"raw\" control characters"
    aliases:
      - -r
      - -R
      - --raw-control-chars
      - --RAW-CONTROL-CHARS

  - name: HILITE-UNREAD
    type: string
    required: false
    default: null
    description: "Highlight first new line after any forward movement"
    aliases:
      - "-W"
      - "--HILITE-UNREAD"
  - name: chop-long-lines
    type: string
    required: false
    default: null
    description: "Chop (truncate) long lines rather than wrapping"
    aliases:
      - "-S"
      - "--chop-long-lines"
  - name: exit-follow-on-close
    type: file
    required: false
    default: null
    description: "Exit F command on a pipe when writer closes pipe. --file-size Automatically determine the size of the input file. --follow-name The F command changes files if the input file is renamed. --header=[L[,C[,N]]] Use L lines (starting at line N) and C columns as headers. --incsearch Search file as each pattern character is typed in. --intr=[C] Use C instead of ^X to interrupt a read. --lesskey-context=text Use lesskey source file contents. --lesskey-src=file Use a lesskey source file. --line-num-width=[N] Set the width of the -N line number field to N characters. --match-shift=[N] Show at least N characters to the left of a search match. --modelines=[N] Read N lines from the input file and look for vim modelines. --mouse Enable mouse input. --no-keypad Don't send termcap keypad init/deinit strings. --no-histdups Remove duplicates from command history. --no-number-headers Don't give line numbers to header lines. --no-search-header-lines Searches do not include header lines. --no-search-header-columns Searches do not include header columns. --no-search-headers Searches do not include header lines or columns. --no-vbell Disable the terminal's visual bell. --redraw-on-quit Redraw final screen when quitting. --rscroll=[C] Set the character used to mark truncated lines. --save-marks Retain marks across invocations of less. --search-options=[EFKNRW-] Set default options for every search. --show-preproc-errors Display a message if preprocessor exits with an error status. --proc-backspace Process backspaces for bold/underline. --PROC-BACKSPACE Treat backspaces as control characters. --proc-return Delete carriage returns before newline. --PROC-RETURN Treat carriage returns as control characters. --proc-tab Expand tabs to spaces. --PROC-TAB Treat tabs as control characters. --status-col-width=[N] Set the width of the -J status column to N characters. --status-line Highlight or color the entire line containing a mark. --use-backslash Subsequent options use backslash as escape char. --use-color Enables colored text. --wheel-lines=[N] Each click of the mouse wheel moves N lines. --wordwrap Wrap lines at spaces"
    aliases:
      - "--exit-follow-on-close"
  - name: file_size
    type: boolean
    required: false
    description: ""
    aliases:
      - "--file-size"
  - name: follow_name
    type: boolean
    required: false
    description: ""
    aliases:
      - "--follow-name"
  - name: hilite-unread
    type: string
    required: false
    default: null
    description: "Highlight first new line after forward-screen"
    aliases:
      - "-w"
      - "--hilite-unread"
  - name: incsearch
    type: boolean
    required: false
    description: ""
    aliases:
      - "--incsearch"
  - name: intr
    type: boolean
    required: false
    description: ""
    aliases:
      - "--intr"
  - name: lesskey_context
    type: boolean
    required: false
    description: ""
    aliases:
      - "--lesskey-context"
  - name: lesskey_src
    type: boolean
    required: false
    description: ""
    aliases:
      - "--lesskey-src"
  - name: line_num_width
    type: boolean
    required: false
    description: ""
    aliases:
      - "--line-num-width"
  - name: match_shift
    type: boolean
    required: false
    description: ""
    aliases:
      - "--match-shift"
  - name: max-forw-scroll
    type: integer
    required: false
    default: null
    description: "Forward scroll limit"
    aliases:
      - "-y"
      - "--max-forw-scroll"
  - name: modelines
    type: boolean
    required: false
    description: ""
    aliases:
      - "--modelines"
  - name: no-init
    type: string
    required: false
    default: null
    description: "Don't use termcap init/deinit strings"
    aliases:
      - "-X"
      - "--no-init"
  - name: no_histdups
    type: boolean
    required: false
    description: ""
    aliases:
      - "--no-histdups"
  - name: no_keypad
    type: boolean
    required: false
    description: ""
    aliases:
      - "--no-keypad"
  - name: no_number_headers
    type: boolean
    required: false
    description: ""
    aliases:
      - "--no-number-headers"
  - name: no_search_header_columns
    type: boolean
    required: false
    description: ""
    aliases:
      - "--no-search-header-columns"
  - name: no_search_header_lines
    type: boolean
    required: false
    description: ""
    aliases:
      - "--no-search-header-lines"
  - name: no_search_headers
    type: boolean
    required: false
    description: ""
    aliases:
      - "--no-search-headers"
  - name: no_vbell
    type: boolean
    required: false
    description: ""
    aliases:
      - "--no-vbell"
  - name: proc_backspace
    type: boolean
    required: false
    description: ""
    aliases:
      - "--proc-backspace"
  - name: proc_return
    type: boolean
    required: false
    description: ""
    aliases:
      - "--proc-return"
  - name: proc_tab
    type: boolean
    required: false
    description: ""
    aliases:
      - "--proc-tab"
  - name: quotes
    type: string
    required: false
    default: null
    description: "Set shell quote characters"
    aliases:
      - "--quotes"
  - name: redraw_on_quit
    type: boolean
    required: false
    description: ""
    aliases:
      - "--redraw-on-quit"
  - name: rscroll
    type: boolean
    required: false
    description: ""
    aliases:
      - "--rscroll"
  - name: save_marks
    type: boolean
    required: false
    description: ""
    aliases:
      - "--save-marks"
  - name: search_options
    type: boolean
    required: false
    description: ""
    aliases:
      - "--search-options"
  - name: shift
    type: integer
    required: false
    default: null
    description: "Set horizontal scroll amount (0 = one half screen width)"
    aliases:
      - "--shift"
  - name: show_preproc_errors
    type: boolean
    required: false
    description: ""
    aliases:
      - "--show-preproc-errors"
  - name: squeeze-blank-lines
    type: string
    required: false
    default: null
    description: "Squeeze multiple blank lines"
    aliases:
      - "-s"
      - "--squeeze-blank-lines"
  - name: status_col_width
    type: boolean
    required: false
    description: ""
    aliases:
      - "--status-col-width"
  - name: status_line
    type: boolean
    required: false
    description: ""
    aliases:
      - "--status-line"
  - name: tabs
    type: string
    required: false
    default: null
    description: "Set tab stops"
    aliases:
      - "-x"
      - "--tabs"
  - name: tag
    type: string
    required: false
    default: null
    description: "Find a tag"
    aliases:
      - "-t"
      - "--tag"
  - name: tag-file
    type: string
    required: false
    default: null
    description: "Use an alternate tags file"
    aliases:
      - "-T"
      - "--tag-file"
  - name: tilde
    type: string
    required: false
    default: null
    description: "Don't display tildes after end of file"
    aliases:
      - "--tilde"
  - name: underline-special
    type: string
    required: false
    default: null
    description: "Change handling of backspaces, tabs and carriage returns"
    aliases:
      - "-u"
      - "-U"
      - "--underline-special"
      - "--UNDERLINE-SPECIAL"
  - name: use_backslash
    type: boolean
    required: false
    description: ""
    aliases:
      - "--use-backslash"
  - name: use_color
    type: boolean
    required: false
    description: ""
    aliases:
      - "--use-color"
  - name: version
    type: integer
    required: false
    default: null
    description: "Display the version number of \"less\""
    aliases:
      - "-V"
      - "--version"
  - name: wheel_lines
    type: boolean
    required: false
    description: ""
    aliases:
      - "--wheel-lines"
  - name: window
    type: integer
    required: false
    default: null
    description: "Set size of window"
    aliases:
      - "-z"
      - "--window"
  - name: wordwrap
    type: boolean
    required: false
    description: ""
    aliases:
      - "--wordwrap"

execution:
  template: "less -? {help} -a {search-skip-screen} -A {search-skip-screen} -b {buffers}
    -B {auto-buffers}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Basic usage with help"
    command: "less ${help}"
  - description: "Display help message"
    command: "less --help"
install:
    - method: apt
      package_name: "less"
      commands:
        - "apt-get install -y less"
---


# less — View file contents page by page

## Overview

`less` is a command-line utility for view file contents page by page.

## Usage

```
less -? {help} -a {search-skip-screen} -A {search-skip-screen} -b {buffers} -B {auto-buffers}
```
