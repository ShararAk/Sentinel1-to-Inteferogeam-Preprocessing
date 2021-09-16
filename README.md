# Sentinel1-to-Inteferogeam-Preprocessing

## Graph Processing Framework (GPF)
The SNAP architecture provides a flexible Graph Processing Framework (GPF) allowing the user to create processing graphs for batch processing and customized processing chains. The Graph Builder, in SNAP-Desktop, allows the user to graphically assemble graphs from a list of available operators and connect operator nodes to their sources. 
The graphs are saved here for batch processing from the command line.

## The SNAP Graph Processing Tool (GPT)
SNAP EO Data Processors are implemented as GPF operators and can be invoked via the Windows or UNIX command-line using the GPF Graph Processing Tool gpt which can be found in the bin directory of your SNAP installation.

## Calling GPT with a Graph 
All required operators to generate an Interferogram on two Single Sentinel1 data are passed in an xml-encoded graph file. It
Simply passing the graph as a parameter to the gpt will sufficient.

## To run gpt on a graph file type:
gpt <GraphFile.xml> [options] [<source-file-1> <source-file-2> ...]
