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

![Image of Webmap](https://github.com/ShararAk/Sentinel1-to-Inteferogeam-Preprocessing/blob/main/Capture.PNG)

# Sentinel1-to-Inteferogeam-Processing

## Graph Processing Framework (GPF)
The SNAP architecture includes a flexible Graph Processing Framework (GPF) that allows users to construct processing graphs for batch processing as well as customizable processing chains. In SNAP-Desktop, the GraphBuilder in SNAP Desktop allows users to graphically construct complicated graphs from a list of available operators and link operator nodes to their sources. See the Sentinel-1 Toolbox Graph Building tutorial to learn more about how to drop in operators, connect them, and specify parameters. When you save a graph, the parameters for the current data product(s) are also saved to the graph file. To reuse the graph from the command line and make the graph generic for any input product, some key values for some parameters were deleted or replaced.

### SAR to InSAR
![Image of First Graph](https://github.com/ShararAk/Sentinel1-to-Inteferogeam-Preprocessing/blob/main/SAR2InSAR.PNG)

### InSAR to Displacement map

![Image of Second Graph](https://github.com/ShararAk/Sentinel1-to-Inteferogeam-Preprocessing/blob/main/InSAR2Displacement.PNG)


## The SNAP Graph Processing Tool (GPT)
SNAP EO Data Processors are implemented as GPF operators and can be invoked via the Windows or UNIX command-line using the GPF Graph Processing Tool (gpt) which can be found in the bin directory of your SNAP installation. Here are two graphs that we generated in SNAP and then modified to handle all data automatically using the GPT.

All needed operators for generating an interferogram on two Single Sentinel1 data and subsequently producing a displacement map are given in two attached xml-encoded graph files (SAR2InSAR.xml and  InSAR2Displacement). Simply passing the graph as a parameter to the gpt will be sufficient.

## To run gpt on a graph file type
You could execute the graphs using the following command, adjusting the file path and other arguments to match yours. Henceforth, the 9 variables must always be defined.

${Input1Path} : The full path to the first scene of the downloaded Sentinel 1 zip-file.
${Input2Path} : The full path to the second scene of the downloaded Sentinel 1 zip-file.
${firstBurstIndex1} : The starting range of the desired IW1 subswath bursts.
${firstBurstIndex2} : The ending range of the desired IW1 subswath bursts.
${firstBurstIndex3} : The starting range of the desired IW2 subswath bursts.
${lastBurstIndex1} : The ending range of the desired IW2 subswath bursts.
${lastBurstIndex2} : The starting range of the desired IW3 subswath bursts.
${lastBurstIndex3} : The ending range of the desired IW3 subswath bursts.
${OutputPath} : The full path to save the final product.

```ruby
gpt <GraphFile.xml> -PInput1Path=<source-file-1.zip> -PInput2Path=<source-file-2.zip> -PfirstBurstIndex1=1 -PlastBurstIndex1=2 -PfirstBurstIndex2=1 -PlastBurstIndex2=2 -PfirstBurstIndex3=1 -PlastBurstIndex3=2 -POutputPath=<output-Path>
```

${InputPath} : The full path to the Unwrapped Interferogram which should be generated by SNAP or snaphu.
${OutputPath} : The full path to save the final product.

```ruby
gpt <InSAR2Displacement.xml< -PInputPath=<source-file.dim> -POutputPath=<output-Path>
```
