from graph_structs.atom_graphs import Graph, ObservableGraph
from analysis import buildPositionChangesDict, buildVectorChangesDict, buildIntensityChangesDict
from variables import red, green, blue, yellow, magenta, cyan

COLOR_FUNCTIONS = [red, green, blue, yellow, magenta, cyan]
def COLORS():
    for color in COLOR_FUNCTIONS:
        yield color

class GraphStack:
    
    def __init__(self, graphs=[], observables=True):
        self._z_stack = []
        self.tracked = False
        self.track_data = {}
        self.observables = observables
        self.drawn = False
        self.drawKwargs = {}
    
    def addGraph(self, atom_list, **kwargs):
        graph = ObservableGraph(atom_list, **kwargs) if self.observables else Graph(atom_list)
        self._z_stack.append(graph)

    def trackVertices(self, *v_ids, positions=True, vectors=False, intensities=False):
        color_dict = {}
        colors = COLORS()
        for v_id in v_ids:
            color_dict[v_id] = next(colors)
        self.drawKwargs['color_dict'] = color_dict

        if positions:
            self.track_data['positions'] = buildPositionChangesDict(self._z_stack, *v_ids)
        if vectors:
            self.track_data['vectors'] = buildVectorChangesDict(self._z_stack, *v_ids)
        if intensities:
            self.track_data['intensities'] = buildIntensityChangesDict(self._z_stack, *v_ids) 
        self.tracked = True

    def clearTrack():
        self.tracked = {}
        self.tracked = False

    def createFromDFS(self, *dataframes, **kwargs):
        image_num = None
        atom_list = []
        currentIndexOffset = 0
        for df in dataframes:
            df['atom_id'] += currentIndexOffset
            currentIndexOffset += df['atom_id'].max()

        for image_num in range(1, dataframes[0]['image'].max() + 1):
            for df in dataframes:
                image_df = df.loc[df['image'] == image_num]
                for k, row in image_df.iterrows():
                    atom_list.append(row[1:])
            self.addGraph(atom_list, **kwargs)
            atom_list = []

    def setImageStack(self, tiffstack):
        if self.observables:
            if len(tiffstack) != len(self._z_stack):
                raise Exception('The length of the provided image stack is not the same as the number of frames analyzed.')
            else:
                for k, graph in enumerate(self):
                    graph.setImage(tiffstack[k])
                return True
        else:
            raise Exception('Observables are turned off')


    def getImageStack(self):
        img_stack = []
        if not self.drawn:
            self.drawAll(**self.drawKwargs)
        for graph in self:
            img_stack.append(graph.image())
        return img_stack

    def drawAll(self, **kwargs): 
        if self.observables:
            for key in kwargs:
                self.drawKwargs[key] = kwargs[key]
            for graph in self:
                graph.draw(**self.drawKwargs)
            self.drawn = True
        else:
            raise Exception('Observables are turned off')
    
    def show(self, index, original=False):
        return self[index].observe(original)

    def __getitem__(self, i):
        return self._z_stack[i]

    def __iter__(self):
        return iter(self._z_stack)

    def __len__(self):
        return len(self._z_stack)
