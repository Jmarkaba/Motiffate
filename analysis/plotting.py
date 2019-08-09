import matplotlib.pyplot as plt
from numpy import arange

def plotPositionChanges(graph_stack, **kwargs):
    frames = arange(start=1, stop=len(graph_stack)+1)
    if graph_stack.tracked:
        for v_id, posChanges in graph_stack.tracked_position_changes.items():
            plt.plot(frames, posChanges, 
                color=tuple(map(lambda x: x/255, kwargs['color_dict'][v_id])),
                label='Column {}'.format(str(v_id)))
        plt.xlabel("Frame Number")
        plt.ylabel("Distance Change(pixels)")
        plt.legend(loc='upper left')
        plt.show()