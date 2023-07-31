from sentinelhub import SHConfig, SentinelHubCatalog, SentinelHubDownloadClient, SentinelHubRequest, BBox, CRS, DataCollection, MimeType
from sentinelhub import CRS, BBox, DataCollection, SHConfig
import requests
import numpy as np
import sh_credentials
import click
import yaml
import pystac



def aoi2box(aoi):
    return [float(c) for c in aoi.split(",")]

time_interval = "2019-01-01", "2019-02-01"

evalscript = '''
//VERSION=3

function setup() {
  return {
    input: [
      {
        bands: ["VV","VH"],                  
      }
    ],
    output: [
      {
        id: "default",
        bands: 1,
        sampleType: "AUTO",        
      },    
    ],
    mosaicking: "SIMPLE",
  };
}


function evaluatePixel(sample) {
        return [sample.VV];
}
  
'''
def get_data(aoi, time_start, time_end, instance_id, client_id, client_secret):
    
    config = SHConfig()
    config.instance_id = instance_id
    config.sh_client_id = client_id
    config.sh_client_secret = client_secret

    catalog = SentinelHubCatalog(config=config)
    collections = catalog.get_collections()
    
    aoi = aoi2box(aoi)
    bbox = BBox(bbox=aoi, crs=CRS.WGS84)
    requestdata = SentinelHubRequest(
        data_folder='testing',
        evalscript=evalscript,
        input_data=[
            SentinelHubRequest.input_data(
            DataCollection.SENTINEL1,
            time_interval=(time_start, time_end)
            )
        ],
        responses=[SentinelHubRequest.output_response("default", MimeType.TIFF)],
        bbox=bbox,
        size=[512, 343.697],
        config=config,
        )
    sentinel_data = requestdata.get_data(save_data=True)
    
    return sentinel_data


#@click.command(
#    short_help='statcalc',
#    help='takes input parameters to calculate statistics on images'
#)
#@click.option(
#    '--aoi',
#    'aoi',
#    help='Bounding box of the Area of Interest'
#)

def calculate_statistics(aoi, time_start, time_end, instance_id, client_id, client_secret):
    
    sentinel_data = get_data(aoi, time_start, time_end, instance_id, client_id, client_secret)
    
    stddev = np.nanstd(sentinel_data)
    mean = np.nanmean(sentinel_data)
    quant10 = np.quantile(sentinel_data, 0.1)
    quant50 = np.quantile(sentinel_data, 0.5)
    quant90 = np.quantile(sentinel_data, 0.9)
    r_o_values = np.ptp(sentinel_data)

    catalog = pystac.Catalog(id='statistics_catalog', description='Statistical results of image processing.')

    # Create an Item for the statistical results
    item = pystac.Item(id='statistics_item',
                       geometry=None,
                       bbox=None,
                       datetime=None,
                       properties={
                           'STDDEV': stddev,
                           'Mean': mean,
                           'Quantile_10': quant10,
                           'Quantile_50': quant50,
                           'Quantile_90': quant90,
                           'Range_of_Values': r_o_values
                       })

    # Add the item to the catalog
    catalog.add_item(item)

    # Save the STAC catalog to a JSON file
    catalog.save('output_catalog.json')

if __name__ == "__main__":
    with open("params.yml", "r") as f:
        parameters = yaml.safe_load(f)
        aoi_value = parameters.get("aoi")
        time_start = parameters.get("time_start") 
        time_end = parameters.get("time_end")
        instance_id_value = parameters.get("instance_id")
        client_id_value = parameters.get("client_id")
        client_secret_value = parameters.get("client_secret")
        
        calculate_statistics(
            aoi=aoi_value,
            time_start=time_start,
            time_end=time_end,
            instance_id=instance_id_value,
            client_id=client_id_value,
            client_secret=client_secret_value,
        )


