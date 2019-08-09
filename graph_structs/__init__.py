from graph_structs.atom_graphs import Graph


def buildGraphFromData(data):
    ##
    ## BUILD GRAPHICAL REPRESENTAION
    # @params
    # data: [][][] with [atom_id, x, y, intensity]
    # as innermost list, second list as all columns in image,
    # and outermost list represents time series
    # e.g., [[1, 121, 66, 0.4], [2, 126, 78, 0.8]...]
    #
    # Returns a TimeSeriesGraph
    ##
    time_series_g = Graph()
    for k, img_row in enumerate(data):
        for row in img_row:
            time_series_g.addVertex(k, row[0], x=row[1], y=row[2], z=row[3])
    
    return time_series_g
