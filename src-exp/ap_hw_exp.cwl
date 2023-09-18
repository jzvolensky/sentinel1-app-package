cwlVersion: v1.0
$namespaces:
  s: https://schema.org/
s:softwareVersion: '1.0'
s:dateCreated: '2023-09-18'
s:codeRepository: https://github.com/jzvolensky/sentinel1-app-package/tree/experimental
s:author:
  - s:name: Juraj Zvolensky
    s:email: 
    s:affiliation: This gave me depression  
    
$graph:
  - id: workflowHW
    class: Workflow
    label: workflowlabel
    inputs:
      - id: input_wf
        type: File
    outputs:
      - id: wf_output
        outputSource:
          - runHWapp_step/cmd_output
        type: Directory
        outputBinding: {}
    steps:
      - id: runHWapp_step
        in:
          - id: Input_String
            source:
              - input_wf
        out:
          - cmd_output
        run: '#runHWapp'
    requirements:
      DockerRequirement:
        dockerPull: potato55/hello_world_app:2.5
    doc: description of workflow
  - id: runHWapp
    class: CommandLineTool
    baseCommand:
      - conda
      - run
      - '-n'
      - ap-hello-world
      - python
      - hello_world.py
    label: RunTheApplication
    doc: Description Here
    inputs:
      - id: Input_String
        type: File
        inputBinding: {}
    outputs:
      - id: cmd_output
        type: Directory
        outputBinding: {}
    requirements:
      DockerRequirement:
        dockerPull: potato55/hello_world_app:2.5
