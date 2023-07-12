from sentinelhub import SHConfig, SentinelHubCatalog, SentinelHubDownloadClient, SentinelHubRequest, BBox, CRS, DataCollection, MimeType
from sentinelhub import CRS, BBox, DataCollection, SHConfig
import requests
import matplotlib.pyplot as plt
import numpy as np

# ADD env file with the credentials


config = SHConfig()
config.instance_id = instance_id
config.sh_client_id = client_id
config.sh_client_secret = client_secret

catalog = SentinelHubCatalog(config=config)
collections = catalog.get_collections()

BBOX = BBox((-87.72171, 17.11848, -87.342682, 17.481674), crs=CRS.WGS84)
time_interval = "2019-01-01", "2019-02-01"

search_iterator = catalog.search(
    DataCollection.SENTINEL1,
    bbox=BBOX,
    time=time_interval,
    #filter="",
    fields={"include": ["id", "properties.datetime"], "exclude": []},
)

results = list(search_iterator)
print("Total number of results:", len(results))

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
requestdata = SentinelHubRequest(
    data_folder='testing',
    evalscript=evalscript,
    input_data=[
        SentinelHubRequest.input_data(
        DataCollection.SENTINEL1,
        time_interval=('2019-01-01','2019-02-01')
        )
    ],
    responses=[SentinelHubRequest.output_response("default", MimeType.TIFF)],
    bbox=BBOX,
    size=[512, 343.697],
    config=config,
)

sentinel_data = requestdata.get_data(save_data=True)

stddev = np.nanstd(sentinel_data)
mean = np.nanmean(sentinel_data)
quant10 = np.quantile(sentinel_data, 0.1)
quant50 = np.quantile(sentinel_data, 0.5)
quant90 = np.quantile(sentinel_data, 0.9)
r_o_values = np.ptp(sentinel_data)

final_results = open("results.txt", "w")

res_stddev = repr(stddev)
res_mean = repr(mean)
res_quant10 = repr(quant10)
res_quant50 = repr(quant50)
res_quant90 = repr(quant90)
res_r_o_values = repr(r_o_values)

final_results.write("STDDEV = " + res_stddev + "\n" +"Mean = "+ res_mean + "\n"+"Quant10 = "+res_quant10 + "\n" +"Quant50 = "+res_quant50+ "\n" +"Quant90 = "+res_quant90+ "\n" +"Range of values = "+res_r_o_values)

final_results.close()
