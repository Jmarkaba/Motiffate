from utils import readCSVData, loadTiff, saveStackAsTiff
from analysis.plotting import plotChanges
from graph_structs.graph_stack import GraphStack
from parsers import main_parser

import shlex

graphs = GraphStack()

def executeCommand(results={}):
    cmd = results.pop('command')

    # Quit
    if cmd == 'q' or cmd == 'quit':
        return False
    print('\n...')
    # Load
    if cmd == 'load':
        graphs = GraphStack()
        dfs = []
        for path in results['data_paths']:
            dfs.append(readCSVData(path))
        graphs.createFromDFS(*dfs)
        img = results.pop('image')
        if img != None:
            loadTiff(graphs, img)
        print('Loaded data\n')
    # Draw
    elif cmd == 'draw':
        loadTiff(graphs, results.pop('image'))
        graphs.drawAll()
        print('Successfully drawn\n')
    # Plot
    elif cmd == 'plot':
        plotChanges(graphs, **results)
        print()
    # Save
    elif cmd == 'save':
        saveStackAsTiff(graphs, results['destination'])
        print('Saved file as {}\n'.format(results['destination']))
    # Track
    elif cmd == 'track':
        if False:
            graphs.clearTrack()
            return
        col_ids = list(map(int, results.pop('column_ids')))
        if len(col_ids) > 6:
            print('More than 6 column ids provided. The extras will be ignored.')
            col_ids = col_ids[:5]
        graphs.trackVertices(*col_ids,**results)
        print('Tracked vertices: {}'.format(col_ids))
    return True



if __name__ == '__main__':
    command = None
    while True:
        command = input('$: ').strip()
        try:
            main_args = main_parser.parse_args(shlex.split(command))
        except:
            print()
            continue

        results = main_args.__dict__
        try:
            cont = executeCommand(results)
            if not cont: break
        except Exception as error:
            print('Error: {}'.format(error))
            continue