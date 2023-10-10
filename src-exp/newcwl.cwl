cwlVersion: v1.0
$namespaces:
  s: https://schema.org/
schemas:
  - http://http://schema.org/version/9.0/schemaorg-current-http.rdf
s:softwareVersion: 0.2.0

$graph:
  #Beginning of Workflow
  - class: Workflow
    doc: Hello World Stac
    id: hello-world-stac
    label: Hello World Stac app
    inputs:
      param:
        type: string
        inputBinding:
          position: 1
          prefix: --param
    outputs:
      - id: wf_outputs
        type: Directory
        outputSource: hello-world-stac/results
    steps:
      hello-world-stac:
        run: "#hwstacapp"
        in:
          param: param
        out:
          - results

  - class: CommandLineTool
    id: hwstacapp
    baseCommand: 
      -python 
      -hello_world.py
    inputs:
      param:
        type: string
        inputBinding:
          position: 1
          prefix: --param
    outputs:
      results:
        type: Directory
        outputBinding:
          glob: .
    requirements:
      DockerRequirement:
        dockerPull: potato55/hello-world-app:7.0
    stdin: hello-world.py