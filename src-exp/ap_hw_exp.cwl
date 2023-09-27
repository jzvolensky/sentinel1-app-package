#!/usr/bin/env cwl-runner

$graph:
- class: Workflow
  label: workflowlabel
  doc: description of workflow

  requirements:
    DockerRequirement:
      dockerPull: potato55/hello_world_app:2.7

  inputs:
  - id: input_wf
    type: File

  outputs:
  - id: wf_output
    type: Directory
    outputBinding: {}
    outputSource:
    - runHWapp_step/cmd_output

  steps:
  - id: runHWapp_step
    in:
    - id: Input_String
      source:
      - input_wf
    run: '#runHWapp'
    out:
    - cmd_output
  id: workflowHW

- class: CommandLineTool
  label: RunTheApplication
  doc: Description Here

  requirements:
    DockerRequirement:
      dockerPull: potato55/hello_world_app:2.5

  inputs:
  - id: Input_String
    type: File
    inputBinding: {}

  outputs:
  - id: cmd_output
    type: Directory
    outputBinding: {}

  baseCommand:
  - conda
  - run
  - -n
  - ap-hello-world
  - python
  - hello_world.py
  id: runHWapp
$namespaces:
  s: https://schema.org/
cwlVersion: v1.0
s:author:
- s:affiliation: This gave me depression
  s:name: Juraj Zvolensky
s:codeRepository: https://github.com/jzvolensky/sentinel1-app-package/tree/experimental
s:dateCreated: '2023-09-18'
