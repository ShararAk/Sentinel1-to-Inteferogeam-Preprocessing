#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
import numpy as np 
import time
import datetime
import kml2geojson
import json
import sys
import argparse

parser = argparse.ArgumentParser(description="Download Sentinel1")

parser.add_argument('--Username','-U', action="store", type=str, required=True,help="Please indicate the Username of the Copernicus Open Access Hub")
parser.add_argument('--Password', '-P', action="store", type=str, required=True,help="Please indicate the Password of the Copernicus Open Access Hub")
parser.add_argument('--AOIPath','-AOI', type=str, required=True, help="Please indicate the path to .geojson file of your area of interest")
parser.add_argument('--orbitdirection','-O', type=str, required=False, default= 'DESCENDING', help="ascending or descending orbit")
parser.add_argument('--StartingDate','-SD',required=True, help="Start date refer of the acquisition date. YYYYMMDD")
parser.add_argument('--EndingDate','-ED', required=True, help="End date refer of the acquisition date. YYYYMMDD")

args =  parser.parse_args(sys.argv[1:])


# search by polygon, time, and SciHub query keywords
api = SentinelAPI(args.Username, args.Password)
footprint = geojson_to_wkt(read_geojson(args.AOIPath))

products = api.query(footprint,
                     date=(args.StartingDate, args.EndingDate),
                     platformname= 'Sentinel-1',
                     producttype='SLC',
                     sensoroperationalmode= 'IW',
                     orbitdirection= args.orbitdirection)

# convert to Pandas DataFrame
products_df = api.to_dataframe(products)

# sort and limit to first 2 sorted products
products_df_sorted = products_df.sort_values([ 'platformname','relativeorbitnumber'])
products_df_sorted = products_df_sorted.head(2)
print(products_df_sorted)

for id in products.keys():
    is_online = api.is_online(id)
    #print(is_online)
    if is_online:
        print(f'Product {id} is online. Starting download.')
        api.download(id)
    else:
        print(f'Product {id} is not online.')
        api.trigger_offline_retrieval(id)


# In[ ]:


# python DownloadSentinel1.py -U=shararehakbarian -P=sharar6237 -AOI="C:/Users/z5235097/OneDrive - UNSW/Skycatch/2. InSAR/Python/Study Area/Kumamoto.geojson" -SD=20210801 -ED=20210907

