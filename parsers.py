import argparse

subparser_groups = []

main_parser = argparse.ArgumentParser()
subparsers = main_parser.add_subparsers(dest='command')

subparsers.add_parser('q')
subparsers.add_parser('quit')

## Loading data (and image)
load_parser = subparsers.add_parser('load')
load_parser.add_argument(
    'data_paths', 
    help='The filepaths to each of the csv data',
    nargs='+'
)
load_parser.add_argument(
    '-i', '--image', 
    help='The filepath to the image stack tif/tiff file',
    required=False
)
subparser_groups.append(load_parser)

## Tracking column data between frames
track_parser = subparsers.add_parser('track')
track_parser.add_argument(
    'column_ids',
    help='A list of the atomic columns to track',
    nargs='+'
)
track_parser.add_argument(
    '--positions',
    help='To exclude data on the position changes between frames',
    action='store_true',
    dest='positions',
    default=True,
    required=False
)
track_parser.add_argument(
    '--no-positions',
    help='To exclude data on the position changes between frames',
    action='store_false',
    dest='positions',
    required=False
)
track_parser.add_argument(
    '-v','--vectors',
    help='To include data on the change vectors between frames',
    action='store_true',
    dest='positions',
    default=False,
    required=False
)
track_parser.add_argument(
    '-i','--intensities',
    help='To include data on the change of intensity between frames',
    action='store_true',
    dest='intensities',
    default=False,
    required=False
)

## Plotting
plot_parser = subparsers.add_parser('plot')
plot_parser.add_argument(
    'feature', 
    help='The feature to plot in the time series data. Currently only supports "positions" and "intensities"',
    choices=['positions', 'intensities']
)

## Displaying frames
plot_parser = subparsers.add_parser('show')
plot_parser.add_argument(
    'index', 
    help='The index of the frame to view',
)
plot_parser.add_argument(
    '--original', 
    help='Specifies that the unaltered version should be viewed',
    action='store_true'
)


## Drawing new image data
draw_parser = subparsers.add_parser('draw')
draw_parser.add_argument(
    'image', 
    help='The filepath to the image stack tif/tiff file',
)
draw_parser.add_argument(
    '-c','--connections',
    help='Specifies whether to save with connections between vertices or not',
    action='store_true',
    required=False
)

## Saving the processed result
save_parser = subparsers.add_parser('save')
save_parser.add_argument(
    'destination',
    help='The output path (where to save the resulting tiff)'
)
subparser_groups.append(save_parser)


## Formatting
for subparser in subparser_groups:
    subparser.usage = subparser.format_usage().replace('usage: main.py ', '')