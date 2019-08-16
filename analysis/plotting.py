import matplotlib.pyplot as plt
from numpy import arange

def plotChanges(graph_stack, feature):
    if graph_stack.tracked:
        ylabel = 'Distance Change(pixels)' if feature == 'positions' else 'Intensity Change'
        frames = arange(start=1, stop=len(graph_stack)+1)
        for v_id, posChanges in graph_stack.track_data[feature].items():
            plt.plot(frames, posChanges, 
                color=graph_stack.drawKwargs['color_dict'][v_id](1),
                label='Column {}'.format(str(v_id)))
        plt.xlabel('Frame Number')
        plt.ylabel(ylabel)
        plt.legend(loc='upper left')
        plt.show()