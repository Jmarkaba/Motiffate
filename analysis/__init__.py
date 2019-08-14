from analysis.columnDataTracking import trackIntensityChanges, trackPositionChanges, trackVectorChanges

def buildPositionChangesDict(graph_stack, *args):
    if args.length > 0:
        return _buildTrackedPositionChangesDict(graph_stack, args)
    else: 
        return _buildTrackedPositionChangesDict(graph_stack, graph_stack.keys())

def _buildTrackedPositionChangesDict(graph_stack, keys):
    pos_dict = {}
    for k in keys:
        pos_dict[k] = trackPositionChanges(k, graph_stack)
    return pos_dict

def buildVectorChangesDict(graph_stack, *args):
    if args.length > 0:
        return _buildTrackedVectorChangesDict(graph_stack, args)
    else: 
        return _buildTrackedVectorChangesDict(graph_stack, graph_stack.keys())

def _buildTrackedVectorChangesDict(graph_stack, keys):
    vec_dict = {}
    for k in keys:
        vec_dict[k] = trackVectorChanges(k, graph_stack)
    return vec_dict

def buildIntensityChangesDict(graph_stack, *args):
    if args.length > 0:
        return _buildTrackedIntensityChangesDict(graph_stack, args)
    else: 
        return _buildTrackedIntensityChangesDict(graph_stack, graph_stack.keys())

def _buildTrackedIntensityChangesDict(graph_stack, keys):
    int_dict = {}
    for k in keys:
        int_dict[k] = trackIntensityChanges(k, graph_stack)
    return int_dict