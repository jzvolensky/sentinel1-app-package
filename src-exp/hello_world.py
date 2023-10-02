import click
import pystac
import json
import yaml
from datetime import datetime
import os 

@click.command()
@click.option("-f", "--file", type=click.Path(exists=True), default="/app/params.yaml", help="Path to parameter file")
@click.option("-o", "--output", type=click.Path(), default="/app/catalog.json", help="Path to output STAC catalog JSON file")

def main(file, output):
    with open(file, "r") as params_file:
        params = yaml.safe_load(params_file)

    click.echo('Starting Hello World Catalogue')
    click.echo(f"Input String: {params.get('input_string')}")

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
    click.echo(json.dumps(catalog_dict, indent=4))
    
    click.echo(f"Item Title: {item.common_metadata.title}")

    absolute_output_path = os.path.abspath(output)
    with open(absolute_output_path, "w") as catalog_file:
        json.dump(catalog_dict, catalog_file, indent=4)

    click.echo(f"Catalogue written to {absolute_output_path}")
    click.echo('Finished Hello World Catalogue')

if __name__ == "__main__":
    main()