from graph_structs.atom_graphs import Graph, ObservableGraph
from analysis import buildPositionChangesDict, buildVectorChangesDict, buildIntensityChangesDict

class GraphStack:
    
    def __init__(self, graphs=[], observables=False, **kwargs):
        self._z_stack = []
        self.tracked = False
    
    def addGraph(self, atom_list, **kwargs):
        graph = ObservableGraph(atom_list, **kwargs) if self.observables else Graph(atom_list)
        self._z_stack.append(graph)

    def trackVertices(self, *v_ids, positions=True, vectors=False, intensities=False):
        if positions:
            self.tracked['positions'] = buildPositionChangesDict(self._z_stack, *v_ids)
        if vectors:
            self.tracked['vectors'] = buildVectorChangesDict(self._z_stack, *v_ids)
        if intensities:
            self.tracked['intensities'] = buildIntensityChangesDict(self._z_stack, *v_ids) 
        self.tracked = True

    def createFromDFS(self, *dataframes, **kwargs):
        image_num = None
        atom_list = []
        for image_num in range(1, dataframes[0]['image'].max() + 1):
            for df in dataframes:
                image_df = df.loc[df['image'] == image_num]
                for k, row in image_df.iterrows():
                    atom_list.append(row[1:])
            self.addGraph(atom_list, **kwargs)
            atom_list = []

    def __iter__(self):
        return iter(self._z_stack)

    def __len__(self):
        return len(self._z_stack)
