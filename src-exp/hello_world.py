
import pystac
import json
import yaml
from datetime import datetime
import os 
import argparse


args = argparse.ArgumentParser()
args.add_argument("--params", help="Path to params file", default="params.yaml")


def main():

    with open(args.params, "r") as params_file:
        params = yaml.safe_load(params_file)

    input_string = params.get("input_string")

    catalog = pystac.Catalog(id="hello-catalog", description="Hello World Catalogue")

    item = pystac.Item(id="my-item", 
                    geometry=None, 
                    datetime=datetime(1970,1,1,0,0,0), 
                    bbox=None, 
                    properties={
                        "title": input_string  
                    }
                )
    item.add_asset("data", pystac.Asset(href="http://example.com/data"))

    catalog.add_item(item)

    catalog_dict = catalog.to_dict()
    print(json.dumps(catalog_dict, indent=4))
    
    print(f"Item Title: {item.common_metadata.title}")

    output = "../tmp/outdir/catalog.json"

    absolute_output_path = os.path.abspath(output)
    os.makedirs(os.path.dirname(absolute_output_path), exist_ok=True)

    with open(absolute_output_path, "w") as catalog_file:
        json.dump(catalog_dict, catalog_file, indent=4)

    print(f"Catalogue written to {absolute_output_path}")
    print('Finished Hello World Catalogue')

if __name__ == "__main__":
    args = args.parse_args()
    params_file = args.params
    main()