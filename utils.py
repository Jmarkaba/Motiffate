from pandas import read_csv
from numpy import asarray, empty
from skimage.external.tifffile import TiffSequence, imsave
from graph_structs.atom_graphs import Graph, ObservableGraph


def readCSVData(filename):
    df = read_csv(filename)
    res = df[['image', 'atom_id', 'x_coordinate', 'y_coordinate', 'norm_integrated_intensity']]
    return res


def saveStackAsTiff(graph_stack, inputTiff=None, outputTiff=None, connections=True, **kwargs):
    combinedTiff = []
    if inputTiff != None:
        tiff = TiffSequence(inputTiff)
        multi = tiff.asarray()[0]
        # finalShape = len(graph_stack), *multi[0].shape
        for cnt, graph in enumerate(graph_stack):
            oa = ObservableGraph(graph, image=multi[cnt], with_connections=connections, **kwargs)
            combinedTiff.append(oa.image())
    else:
        for cnt, graph in enumerate(graph_stack):
            oa = ObservableGraph(graph, with_connections=connections, **kwargs)
            combinedTiff.append(oa.image())

    combinedTiff = asarray(combinedTiff, dtype='float16')
    imsave(outputTiff, combinedTiff)