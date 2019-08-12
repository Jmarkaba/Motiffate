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
    vectorChanges = numpy.empty([len(graph_stack),])
    vectorChanges[0] = numpy.zeros((2,))
    for k in range(len(graph_stack)-1):
        if graph_stack[k+1][v_id].exists() and graph_stack[k][v_id].exists():
            vec = numpy.subtract(graph_stack[k+1][v_id].getPosition(), graph_stack[k][v_id].getPosition)
            vectorChanges[k+1] = vec
        else:
            vectorChanges[k+1] = numpy.zeros((2,))
    return positionChanges

def trackIntensityChanges(v_id, graph_stack):
    intensityChanges = numpy.empty([len(graph_stack),])
    intensityChanges[0] = 0
    for k in range(len(graph_stack)-1):
        diff = graph_stack[k+1].getIntensity() - graph_stack[k].getIntensity()
        intensityChanges[k+1] = diff
    return intensityChanges