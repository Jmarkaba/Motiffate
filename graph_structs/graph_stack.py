from graph_structs.atom_graphs import Graph
from analysis import buildPositionChangesDict

class GraphStack:
    
    def __init__(self, graphs=[], observables=False):
        self._z_stack = []
        self.tracked = False
    
    def addGraph(self, graph):
        self._z_stack.append(graph)

    def trackVertices(self, *v_ids, positions=True, vectors=False, intensities=False):
        print(v_ids)
        if positions:
            self.tracked_position_changes = buildPositionChangesDict(self._z_stack, *v_ids)
        self.tracked = True

    def createFromDFS(self, *dataframes):
        image_num = None
        atom_list = []
        for image_num in range(1, dataframes[0]['image'].max() + 1):
            for df in dataframes:
                image_df = df.loc[df['image'] == image_num]
                for k, row in image_df.iterrows():
                    atom_list.append(row[1:])
            self.addGraph(Graph(atom_list))
            atom_list = []

    def __iter__(self):
        return iter(self._z_stack)

    def __len__(self):
        return len(self._z_stack)
