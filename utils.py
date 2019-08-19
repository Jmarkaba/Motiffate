from pandas import read_csv
from numpy import asarray, empty
from skimage.external.tifffile import TiffSequence, TiffWriter
from graph_structs.atom_graphs import Graph, ObservableGraph


def readCSVData(filename):
    df = read_csv(filename)
    res = df[['image', 'atom_id', 'x_coordinate', 'y_coordinate', 'norm_integrated_intensity']]
    return res

def loadTiff(graph_stack, inputTiff=None):
    if inputTiff != None:
        graph_stack.setImageStack(TiffSequence(inputTiff).asarray()[0])

def saveStackAsTiff(graph_stack, outputTiff):
    data = asarray(graph_stack.getImageStack())
    with TiffWriter(outputTiff, bigtiff=True) as tiff:
        for i in range(data.shape[0]):
            tiff.save(data[i], photometric='rgb') 