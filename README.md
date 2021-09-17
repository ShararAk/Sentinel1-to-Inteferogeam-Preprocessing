# Downloading Sentinel1 

It is straightforward to search for, download, and download Sentinel1 images and their metadata using the Copernicus Open Access Hub via Sentinelsat.
Using the username and password to access the Copernicus Open Access Hub, execute a basic search query and download all Sentinel-1 scenes of type SLC across a search polygon for starting and ending acquisition dates. Search regions should be given as GeoJSON polygons, which may be converted from a .kml file using kml2geojson.

```ruby
require  'kml2geojson'
kml2geojson.main.convert('/path to .kml file/', '/path to save JSON file/')
```

Search and download all Sentinel-1 scenes of type SLC over a search polygon, in descending orbit for the year 2015.
## command line interface 

```ruby
sentinelsat -u <user> -p <password> -g <search_polygon.geojson> -s startingDate -e EndingDate -producttype <SLC> -q "orbitdirection=Descending" -url "https://scihub.copernicus.eu/dhus"

```
## Python API

```ruby

AOI = read_geojson('Study Area.geojson')

# search by polygon, time, and SciHub query keywords
api = SentinelAPI('user', 'password', 'https://scihub.copernicus.eu/dhus')
footprint = geojson_to_wkt(AOI)

products = api.query(footprint,
                     date=('startingDate', 'EndingDate'),
                     platformname= 'Sentinel-1',
                     producttype='SLC',
                     sensoroperationalmode= 'IW',
                     orbitdirection= 'DESCENDING')
# download all results from the search
api.download_all(products)

```

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
