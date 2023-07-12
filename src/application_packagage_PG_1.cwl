cwlVersion: v1.0
$graph:
  - id: pyexec
    class: Workflow
    label: executescript
    inputs:
      - id: id
        label: id
        default: app.py
        type: File
    doc: Script execution
  - id: execute
    class: CommandLineTool
    baseCommand:
      - python3
      - app.py
    label: exec
    doc: Execute python script
    requirements:
      DockerRequirement:
        dockerPull: potato55/app-package
      ResourceRequirement:
        coresMax: '2'
        ramMax: '4096'
$namespaces:
  s: https://schema.org/
s:softwareVersion: 0.0.1
s:dateCreated: '2023-07-12'
s:codeRepository: https://github.com/jzvolensky/sentinel1-app-package
s:author:
  - s:name: Juraj Zvolensky
    s:email: juraj.zvolensky@ext.esa.int
    s:affiliation: ESA
