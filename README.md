# Sentinel 1 GRD statistics

The aim of this project is to create an example application package for acquiring Sentinel 1 data and performing some basic statistics

# Development setup

This Application Package is meant to be used on the [EOEPCA](https://github.com/EOEPCA) platform. However, local testing and development can be performed locally.

1. From root set up the conda environment

```sh
conda env create -f src/environment.yml
```

2. Activate conda environment

```sh
conda activate sen1env
```

**You will need to add your Sentinel Hub credentials in src/sh_credentials.py**

3. Set up your preferred Area of Interest (AoI) in the params.yml file and then run the script from the src folder

```sh
python3 app.py
```

# Running on EOEPCA

If you have a working local EOEPCA deployment, for example based on the [deployment guide](https://deployment-guide.docs.eoepca.org/current/), you can also execute the Application Package cwl directly through http requests which can be found in **src/requests.http**. These can be executed using the VS code plugin [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).

**Note: All of the requests are preconfigured with the simple deployment from the deployment guide. If you have a different configuration you might need to tweak the requests too**
