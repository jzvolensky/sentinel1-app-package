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
    # Workflow definition
    - class: Workflow
      doc: This workflow is used to generate Hello World STAC
      id: hello-world-STAC
      inputs:
        input_string:
            type: string
            default: Hello World
      outputs:
        - id: wf_outputs
          type: Directory
          outputSource: wf_step_1/wf_outputs

      steps:
        hello_world:
          run: "#hwapp"
          in:
            input_string: input_string
          out:
            - results
    
    - class: CommandLineTool
      id: hwapp
      baseCommand: [conda,run,-n,ap-hello-world,python,hello_world.py]
      inputs:
        input_string:
          type: string
          inputBinding:
            position: 1
      outputs:
        results:
          type: Directory
          outputBinding:
            glob: .
      requirements:
        DockerRequirement:
          dockerPull: potato55/ap-hello-world:2.5

