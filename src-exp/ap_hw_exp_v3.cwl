cwlVersion: v1.0
$namespaces:
  s: https://schema.org/
s:softwareVersion: '1.3'
s:dateCreated: '2023-09-18'
s:codeRepository: https://github.com/jzvolensky/sentinel1-app-package/tree/experimental
s:author:
  - s:name: Juraj Zvolensky
    s:email: email@email.com
    s:affiliation: None
$graph:
  - class: Workflow
    doc: This workflow is used to generate Hello World STAC cat
    id: hello-world-STAC
    inputs:
      - id: input_string
        default: Hello World
        type: string
    outputs:
      - id: wf_outputs
        type: Directory
        outputSource: wf_step_1/wf_outputs
    steps:
      - id: hello_world
        run: '#hwapp'
        in:
          - id: input_string
            source:
              - input_string
        out:
          - results
  - class: CommandLineTool
    id: hwapp
    baseCommand:
      - python
      - /app/hello-world.py
      - '--param'
    inputs:
      - id: input_string
        default: Hello World
        type: string
        inputBinding:
          position: 1
    outputs:
      - id: results
        type: Directory
        outputBinding:
          glob: .
    requirements:
      DockerRequirement:
        dockerPull: potato55/hello-world-app:6.0