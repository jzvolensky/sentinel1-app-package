import click
import pystac
import requests
import json
import yaml

@click.command()
@click.option("-f", "--file", type=click.Path(exists=True), default="params.yaml", help="Path to parameter file")

def main(file):
    with open(file, "r") as params_file:
        params = yaml.safe_load(params_file)

    input_string = params.get("input_string")

    catalog = pystac.Catalog(id="hello-catalog", description="Hello World Catalogue")

    item = pystac.Item(id="my-item", geometry=None, bbox=None, datetime=None)
    item.add_asset("data", pystac.Asset(href="http://example.com/data"))

    catalog.add_item(item)

    click.echo(response.text)

if __name__ == "__main__":
    main()