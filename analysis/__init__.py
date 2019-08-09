from analysis.columnDataTracking import trackIntensityChanges, trackPositionChanges, trackVectorChanges

def buildPositionChangesDict(graph_stack, *args):
    #if keys in kwargs:
    #    return _buildTrackedPositionChangesDict(graph_stack, kwargs[keys])
    #else:
    #    keys = []
    #    for key in graph_stack[0]:
    #        keys.append[key]
    #    return _buildTrackedPositionChangesDict(graph_stack, keys)
    return _buildTrackedPositionChangesDict(graph_stack, args)

def _buildTrackedPositionChangesDict(graph_stack, keys):
    pos_dict = {}
    for k in keys:
        pos_dict[k] = trackPositionChanges(k, graph_stack)
    return pos_dict


    
    