cwlVersion: v1.0
$graph:
  - class: Workflow
  - id: python
    class: CommandLineTool
    baseCommand:
      - python
    arguments:
      - ./app.py
    outputs:
      - id: result
        type: string
        outputBinding: {}
    requirements:
      DockerRequirement:
        dockerPull: potato55/app-package
      ResourceRequirement:
        coresMin: '1'
        coresMax: '2'
        ramMin: '128'
        ramMax: '256'
$namespaces:
  s: https://schema.org/
s:softwareVersion: 0.0.1
s:dateCreated: '2023-06-21'
s:author:
  - s:name: Juraj Zvolensky
    s:email: juraj.zvolensky@ext.esa.int
    s:affiliation: ESA