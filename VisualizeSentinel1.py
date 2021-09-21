#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np 
import json
import sys
import argparse
# To use it as a module copy stsa.py to your work directory. (https://github.com/pbrotoisworo/s1-tops-split-analyzer)
from stsa import TopsSplitAnalyzer

parser = argparse.ArgumentParser(description="Visualize Sentinel1")

parser.add_argument('--Image','-I', action="store", type=str, required=True,help="Please indicate the path to downloaded sentinel1 Image")
parser.add_argument('--Polygon','-P', type=str, required=True, help="Please indicate the path to Shapefile of your area of interest")

args =  parser.parse_args(sys.argv[1:])

# Create object
s1 = TopsSplitAnalyzer(image=args.Image, target_subswaths=['iw1', 'iw2', 'iw3'], polarization='vv')

# Write to shapefile
s1.to_shapefile('data.shp')

# Get JSON
s1.to_json('json_output.json')

# Write to CSV
s1.to_csv('output.csv')

# The shapefile stored in a geopandas dataframe
print(s1.df)

# Visualize on a webmap with additional polygon
#s1.visualize_webmap(polygon='C:/Users/z5235097/OneDrive - UNSW/Skycatch/2. InSAR/Python/Study Area/Kumamoto-polygon.shp')


# In[ ]:


# python VisualizeSentinel1.py -I="C:/Users/z5235097/OneDrive - UNSW/Skycatch/2. InSAR/Python/S1A_IW_SLC__1SSV_20160408T091355_20160408T091430_010728_01001F_83EB.zip"  -P="C:/Users/z5235097/OneDrive - UNSW/Skycatch/2. InSAR/Python/Study Area/Kumamoto-polygon.shp"

