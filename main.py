from utils import readCSVData, saveStackAsTiff
from analysis.plotting import plotPositionChanges
from graph_structs.graph_stack import GraphStack

import pandas

if __name__ == '__main__':

    colordict = {47: (255, 0, 0), 93: (0, 255, 0), 124: (0, 0, 255)}

    ceo2_csv_data = readCSVData('./data/inputs/csv/CeO2_Pt-on-CeO2_40-frames_N2.csv')
    pt_csv_data = readCSVData('./data/inputs/csv/Pt_Pt-on-CeO2_40-frames_N2.csv')
    gs = GraphStack()
    gs.createFromDFS(ceo2_csv_data, pt_csv_data)
    gs.trackVertices(*colordict.keys())
    plotPositionChanges(gs, color_dict=colordict)

    saveStackAsTiff(
        gs, 
        inputTiff='./data/inputs/tiff/Pt on CeO2 rod-5e-03TorrN2-20C-1677kx-1.0s-40fps-bin.xy4-6pm-5063eA2s.tif',
        outputTiff='./data/outputs/tiff/Pt-on-CeO2-rod_N2_specific-16bit.tif',
        connections=True,
        color_dict=colordict)