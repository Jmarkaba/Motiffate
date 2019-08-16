from pandas import read_csv
from numpy import asarray, empty
from skimage.external.tifffile import TiffSequence, imsave
from graph_structs.atom_graphs import Graph, ObservableGraph


def readCSVData(filename):
    df = read_csv(filename)
    res = df[['image', 'atom_id', 'x_coordinate', 'y_coordinate', 'norm_integrated_intensity']]
    return res

def loadTiff(graph_stack, inputTiff=None):
    if inputTiff != None:
        graph_stack.setImageStack(TiffSequence(inputTiff).asarray()[0])

def saveStackAsTiff(graph_stack, outputTiff):
    combinedTiff = asarray(graph_stack.getImageStack(), dtype='float16')
    imsave(outputTiff, combinedTiff)