cwlVersion: v1.0
$graph:
  - id: wf_execution
    class: Workflow
    inputs:
      - id: input_string
        type: string
    outputs:
      - id: wf_output
        outputSource:
          - execute_step/output_string
        type: Directory
        outputBinding: {}
    steps:
      - id: execute_step
        in:
          - id: input_string
            source:
              - input_string
        out:
          - output_string
        run: '#execute'
  - id: execute
    class: CommandLineTool
    baseCommand:
      - python
      - hello_world_app.py
      - '-f'
    arguments:
      - params.yaml
    inputs:
      - id: input_string
        type: string
        inputBinding: {}
    outputs:
      - id: output_string
        type: Directory
        outputBinding: {}
    requirements:
      DockerRequirement:
        dockerPull: potato55/hello_world_app:2.0
$namespaces:
  s: https://schema.org/
s:softwareVersion: '1.0'
s:dateCreated: '2023-08-30'
s:codeRepository: https://github.com/jzvolensky/sentinel1-app-package/tree/experimental
s:author:
  - s:name: Juraj Zvolensky