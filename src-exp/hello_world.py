import click
import pystac
import requests
import json
import yaml
from datetime import datetime

@click.command()
@click.option("-f", "--file", type=click.Path(exists=True), default="params.yaml", help="Path to parameter file")

def main(file):
    with open(file, "r") as params_file:
        params = yaml.safe_load(params_file)

    input_string = params.get("input_string")

    catalog = pystac.Catalog(id="hello-catalog", description="Hello World Catalogue")

    item = pystac.Item(id="my-item", 
                    geometry=None, 
                    datetime=datetime(1970,1,1,0,0,0), 
                    bbox=None, 
                    properties={
                        "title": input_string  # Set the title to the input_string value
                    }
                )
    item.add_asset("data", pystac.Asset(href="http://example.com/data"))

    catalog.add_item(item)

    # Print the entire catalog structure
    catalog_dict = catalog.to_dict()
    click.echo(json.dumps(catalog_dict, indent=4))
    
    # Access the title of the item
    click.echo(f"Item Title: {item.common_metadata.title}")

if __name__ == "__main__":
    main()