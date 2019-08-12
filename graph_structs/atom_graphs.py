from numpy.linalg import norm
from numpy import empty, full, uint8, amax
from cv2 import line, circle, cvtColor, FILLED, COLOR_GRAY2RGB
from skimage.io import imshow, show
from graph_structs.linsolve import intersects
from variables import MAX_BOND_LENGTH, AMPLITUDE

class _Node:

    def __init__(self, ids, **kwargs):
        self.neighbors = {}
        self.ids = ids
        self._x = kwargs['x'] if 'x' in kwargs else None
        self._y = kwargs['y'] if 'y' in kwargs else None
        if self._x and self._y:
            self.position = empty((2,))
            self.position[0] = self._x
            self.position[1] = self._y
        else:
            self.position = None
        self.intensity = kwargs['intensity'] if 'intensity' in kwargs else 0
        self.setType(kwargs['type']) if 'type' in kwargs else None
    
    def __contains__(self, other):
        return other in self.neighbors
    
    def __iter__(self):
        return iter(self.neighbors)

    def addNeighbor(self, other, dist):
        self.neighbors[other.ids] = dist
    
    def getNeighbor(self, other):
        return self.neighbors[other]

    def getType(self):
        return self._atom_type
    
    def setType(self, atom_type):
        # atom_type should be a string
        # e.g., 'Pt'
        self._atom_type = str.lower(atom_type) if atom_type else None

    def exists(self):
        return self.intensity != 0

    def getPosition(self):
        return self.position



class Graph:

    def __init__(self, atom_list):
        self._vertList = {}
        for atom in atom_list:
            if atom[3] == 0 or not atom[1] >= 0:
                self.addVertex(int(atom[0]))
            else:
                self.addVertex(int(atom[0]), x=atom[1], y=atom[2], intensity=atom[3])
        edge_set = self.keepNearestNeighbors()
        self.removeLargerLatticeBonds(edge_set)
        
    def keepNearestNeighbors(self):
        edge_set = set()
        for key, atom in self:
            if not atom.exists(): continue
            for k, other in self:
                if not other.exists(): continue
                dist = norm(atom.getPosition() - other.getPosition())
                if dist < MAX_BOND_LENGTH and k not in atom:
                    self.addEdge(key, k, dist)
                    edge_set.add((key, k))
                    edge_set.add((k, key))
        return edge_set

    def removeLargerLatticeBonds(self, edge_set):
        def e2ps(e):
            return self[e[0]].getPosition(), self[e[1]].getPosition()
        for edge in edge_set:
            for other_edge in edge_set:
                if edge != other_edge and edge[0] != other_edge[1] and intersects(*e2ps(edge), *e2ps(other_edge)):
                    pass

    def __getitem__(self, i):
        return self._vertList[i]
    
    def __len__(self):
        return len(self._vertList)

    def __contains__(self, i):
        return i in self._vertList
    
    def __iter__(self):
        return iter(self._vertList.items())
    
    def addVertex(self, v_id, **kwargs):
        self._vertList[v_id] = _Node(v_id, **kwargs)

    def addEdge(self, v_id, other_id, dist):
        if v_id not in self:
            self.addVertex(v_id)
        if other_id not in self:
            self.addVertex(other_id)
        self[v_id].addNeighbor(self[other_id], dist)
        self[other_id].addNeighbor(self[v_id], dist)

    def setVertexType(self, v_id, atom_type):
        self._vertList[v_id].setType(atom_type)



class ObservableGraph(Graph):

    def __init__(self, atom_list=[], image=full((512,512,3), 0, dtype=uint8), with_connections=False, **kwargs):
        Graph.__init__(atom_list)

        self._image = cvtColor(image, COLOR_GRAY2RGB) if len(image.shape) == 2 else image
        max_pixel = amax(self._image)
        self._white = (max_pixel, max_pixel, max_pixel)

        if with_connections: 
            self.drawConnections()
        self.drawVertices(**kwargs)

    def drawVertices(self, **kwargs):
        for key, vertex in self:
            if vertex.exists():
                p = vertex.getPosition()
                color = kwargs['color_dict'][key] if 'color_dict' in kwargs and key in kwargs['color_dict'] else self._white
                circle(self._image, p, AMPLITUDE, color, thickness=FILLED)


    def drawConnections(self):
        for key, vertex in self:
            for key in vertex.neighbors:
                nbr = self[key]
                p1 = vertex.getPosition()
                p2 = nbr.getPosition()
                line(self._image, p1, p2, self._white, thickness=3)
        
    def observe(self):
        imshow(self._image)
        show()

    def image(self):
        return self._image