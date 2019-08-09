import numpy

def trackPositionChanges(v_id, graph_stack):
    positionChanges = numpy.empty([len(graph_stack),])
    positionChanges[0] = 0
    for k in range(len(graph_stack)-1):
        if graph_stack[k+1][v_id].exists() and graph_stack[k][v_id].exists():
            a, b = graph_stack[k+1][v_id].getPosition(), graph_stack[k][v_id].getPosition()
            posChange = numpy.linalg.norm(a-b)
            positionChanges[k+1] = posChange
        else:
            positionChanges[k+1] = 0
    return positionChanges

def trackVectorChanges(v_id, graph_stack):
    vectorChanges = numpy.empty((len(graph_stack),))
    vectorChanges[0] = numpy.zeros((2,))
    for k in range(len(graph_stack)-1):
        vec = numpy.subtract(graph_stack[k+1].getPosition(), graph_stack[k].getPosition)
        vectorChanges[k+1] = vec
    return vectorChanges

def trackIntensityChanges(v_id, graph_stack):
    intensityChanges = numpy.empty([len(graph_stack),])
    intensityChanges[0] = 0
    for k in range(len(graph_stack)-1):
        diff = graph_stack[k+1].getIntensity() - graph_stack[k].getIntensity()
        intensityChanges[k+1] = diff
    return intensityChanges

def statistically_compare(v1, v2, graph_stack):
    vecs1, vecs2 = trackVectorChanges(v1, graph_stack), trackVectorChanges(v2, graph_stack)
    return vecs2 - vecs1