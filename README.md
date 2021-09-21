# Downloading Sentinel1 

It is straightforward to search for, download, and download Sentinel1 images and their metadata using the Copernicus Open Access Hub via Sentinelsat.
Using the username and password to access the Copernicus Open Access Hub, execute a basic search query and download all Sentinel-1 scenes of type SLC across a search polygon for starting and ending acquisition dates. Search regions should be given as GeoJSON polygons, which may be converted from a .kml file using kml2geojson.

```ruby
require  'kml2geojson'
kml2geojson.main.convert('/path to .kml file/', '/path to save JSON file/Study Area/')
```

Search and download all Sentinel-1 scenes of type SLC over a search polygon, in descending orbit for a specific time.
## command line interface 

```ruby
sentinelsat -u <user> -p <password> -g <search_polygon.geojson> -s startingDate -e EndingDate -producttype <SLC> -q "orbitdirection=Descending" -url "https://scihub.copernicus.eu/dhus"

```
## Python API
Authentication is required by the Copernicus Open Access Hub and, most likely, by the rest of Data Hubs. SentinelAPI (your username>, your password>) can be used to provide your credentials.
Copernicus Open Access Hub no longer stores all products available for quick access. Offline products can be requested from the Long Term Archive (LTA) and are expected to be accessible within 24 hours.
In this example, we query Sentinel-1 scenes for a certain area and convert the results to a Pandas DataFrame. After that, the DataFrame is sorted by platformname and relativeorbitnumber. We restrict the query to the first two results within our timeframe. The product's availability will be checked, and a list of offline and online products will be provided. Online products will start downloading instantly, while offline products will start retrieving in the background.

  
```ruby

python DownloadSentinel1.py -U=<user> -P=<password> -AOI=<search_polygon.geojson> -SD=startingDate -ED=EndingDate

```

You can view all subswaths of the downloded product, save data as a shapefile, JSON, or CSV.

```ruby
 python VisualizeSentinel1.py -I=<S1_image.zip>  -P=<search_polygon.shp>
```
Or

```ruby
python stsa.py -zip Image.zip --swath iw2 iw3 -polar vv -shp out_shp.shp -csv out_csv.csv -json out_json.jso
```
You can also interact it with data using a webmap. In addition, you can add a polygon to visualize its extent with regards to the data.

```ruby
from stsa import TopsSplitAnalyzer
s1 = TopsSplitAnalyzer(image='Image.zip', target_subswaths=['iw1', 'iw2', 'iw3'], polarization='vv')
s1.visualize_webmap(polygon='Area of Interest.shp')
```

![Image of Yaktocat](https://github.com/ShararAk/Sentinel1-to-Inteferogeam-Preprocessing/blob/main/Capture.PNG)

# Sentinel1-to-Inteferogeam-Processing

## Graph Processing Framework (GPF)
The SNAP architecture provides a flexible Graph Processing Framework (GPF) allowing the user to create processing graphs for batch processing and customized processing chains. The Graph Builder, in SNAP-Desktop, allows the user to graphically assemble graphs from a list of available operators and connect operator nodes to their sources. 

The graphs are saved here for batch processing from the command line.

## The SNAP Graph Processing Tool (GPT)
SNAP EO Data Processors are implemented as GPF operators and can be invoked via the Windows or UNIX command-line using the GPF Graph Processing Tool gpt which can be found in the bin directory of your SNAP installation.

## Calling GPT with a Graph 
The GraphBuilder in SNAP Desktop could be used to construct complicated graphs with interconnected operators. See the Sentinel-1 Toolbox Graph Building tutorial to learn more about how to drop in operators, connect them, and specify parameters.
When you save a graph, the parameters you have specified for the current data product(s) are also saved to the graph file. Here, to reuse the graph from the command line using gpt and to make the graph generic for any input product, some important values removed or replaced for some parameters.

All required operators to generate an Interferogram on two Single Sentinel1 data are passed in an xml-encoded graph file. It Simply passing the graph as a parameter to the gpt will sufficient.

## To run gpt on a graph file type:
gpt <GraphFile.xml> [options] [<source-file-1> <source-file-2> ...]
