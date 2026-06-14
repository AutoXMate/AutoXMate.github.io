---
id: windows-execution-msbuild
namespace: windows:execution:msbuild
name: msbuild
description: 'Used to compile and execute code Located at: C:\Windows\Microsoft.NET\Framework\v2.0.50727\Msbuild.exe; C:\Windows\Microsoft.NET\Framework64\v2.0.50727\Msbuild.exe; C:\Windows\Microsoft.NET\Framework\v3.5\Msbuild.exe.'
author: Oddvar Moe
version: 1.0.0
capabilities:
- security.defense-evasion.bypass
- security.execution.command
platforms:
- windows
risk_level: high
trust_level: community
execution_policy: enabled
architectures:
- amd64
dependencies: []
related_tools: []
artifacts: []
workflow_edges:
  produces:
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
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: low
  disk_io: low
allowed-tools:
- msbuild
parameters: []
features: []
execution:
  template: msbuild
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Build and execute a C# project stored in the target XML file. (Compile and run code)
  command: msbuild.exe {PATH:.xml}
- description: Build and execute a C# project stored in the target csproj file. (Compile and run code)
  command: msbuild.exe {PATH:.csproj}
- description: Executes generated Logger DLL file with TargetLogger export. (Execute DLL)
  command: msbuild.exe /logger:TargetLogger,{PATH_ABSOLUTE:.dll};MyParameters,Foo
- description: Execute JScript/VBScript code through XML/XSL Transformation. Requires Visual Studio MSBuild v14.0+. (Execute project file that contains XslTransformation tag parameters)
  command: msbuild.exe {PATH:.proj}
- description: By putting any valid msbuild.exe command-line options in an RSP file and calling it as above will interpret the options as if they were passed on the command line. (Bypass command-line based detections)
  command: msbuild.exe @{PATH:.rsp}
references:
- label: T1127.md
  url: https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1127/T1127.md
- label: MSBuildShell
  url: https://github.com/Cn33liz/MSBuildShell
- label: ''
  url: https://pentestlab.blog/2017/05/29/applocker-bypass-msbuild/
- label: ''
  url: https://oddvar.moe/2017/12/13/applocker-case-study-how-insecure-is-it-really-part-1/
- label: 4ffc43a281e87d108875f07614324191
  url: https://gist.github.com/bohops/4ffc43a281e87d108875f07614324191
- label: '165'
  url: https://github.com/LOLBAS-Project/LOLBAS/issues/165
- label: msbuild-response-files
  url: https://docs.microsoft.com/en-us/visualstudio/msbuild/msbuild-response-files
- label: msbuild-loggers-and-logging-events
  url: https://www.daveaglick.com/posts/msbuild-loggers-and-logging-events
techniques:
- defense-evasion
- execution
mitre_ids:
- T1127.001
- T1036
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/file/file_event/file_event_win_shell_write_susp_directory.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_msbuild_susp_parent_process.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/network_connection/net_connection_win_silenttrinity_stager_msbuild_activity.yml
- type: splunk
  url: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/suspicious_msbuild_spawn.yml
- type: splunk
  url: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/suspicious_msbuild_rename.yml
- type: splunk
  url: https://github.com/splunk/security_content/blob/a1afa0fa605639cbef7d528dec46ce7c8112194a/detections/endpoint/msbuild_suspicious_spawned_by_script_process.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_msbuild_beacon_sequence.toml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_msbuild_making_network_connections.toml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/ef7548f04c4341e0d1a172810330d59453f46a21/rules/windows/defense_evasion_execution_msbuild_started_by_script.toml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_execution_msbuild_started_by_office_app.toml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_execution_msbuild_started_renamed.toml
- type: blockrule
  url: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- type: ioc
  description: Msbuild.exe should not normally be executed on workstations
install:
- method: choco
  package_name: msbuild
  commands:
  - choco install msbuild
---


# msbuild

msbuild is a Windows LOLBin. Used to compile and execute code Located at: C:\Windows\Microsoft.NET\Framework\v2.0.50727\Msbuild.exe; C:\Windows\Microsoft.NET\Framework64\v2.0.50727\Msbuild.exe; C:\Windows\Microsoft.NET\Framework\v3.5\Msbuild.exe.
