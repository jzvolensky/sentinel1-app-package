cwlVersion: v1.0
$graph:
  - id: execute
    class: Workflow
    label: launchscript
    inputs:
      - id: aoi
        label: AreaOfInterest
        doc: BBOX of the AoI
        type: string
    outputs:
      - id: wf_out
        type: Directory
    steps:
      - id: pyexec_step
        in:
          - id: aoi
            source:
              - aoi
        out:
          - results
        run: '#pyexec'
    doc: ADD LATER
  - id: pyexec
    class: CommandLineTool
    baseCommand:
      - python
      - '-m'
      - app
    label: ExecuteScript
    doc: ADD LATER
    inputs:
      - id: aoi
        type: string
        inputBinding:
          prefix: '--aoi'
    outputs:
      - id: results
        type: Directory
        outputBinding: {}
    requirements:
      DockerRequirement:
        dockerPull: potato55/app-package:amd64
        # Add resource limits here
        resourceRequirement:
          coresMin: 1
          coresMax: 2
          ramMin: 1G
          ramMax: 2G
$namespaces:
  s: https://schema.org/
s:softwareVersion: 0.0.1
s:dateCreated: '2023-07-13'
