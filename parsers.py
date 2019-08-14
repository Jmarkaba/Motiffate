import argparse

subparser_groups = []

main_parser = argparse.ArgumentParser()
subparsers = main_parser.add_subparsers(dest='command')


## Loading data (and image)
load_parser = subparsers.add_parser('load')
load_parser.add_argument(
    'path_to_data', 
    help='The filepath to the csv data')
load_parser.add_argument(
    '-i', '--image', 
    help='The filepath to the image stack tif/tiff file',
    required=False)
subparser_groups.append(load_parser)


## Saving the processed result
save_parser = subparsers.add_parser('save')
save_parser.add_argument(
    'destination',
    help='The output path (where to save the resulting tiff)')
save_parser.add_argument(
    '-c','--connections',
    help='Specifies whether to save with connections between verticies or not',
    action='store_true',
    required=False)
subparser_groups.append(save_parser)


## Tracking column data between frames
track_parser = subparsers.add_parser('track')
track_parser.add_argument(
    'column_ids',
    help='A list of the atomic columns to track',
    type=list
)
track_parser.add_argument(
    '--no-positions',
    help='To exclude data on the position changes between frames',
    action='store_true',
    default=False,
    required=False
)
track_parser.add_argument(
    '-v','--vectors',
    help='To include data on the change vectors between frames',
    action='store_true',
    default=False,
    required=False
)
track_parser.add_argument(
    '-i','--intensities',
    help='To include data on the change of intensity between frames',
    action='store_true',
    default=False,
    required=False
)


## Formatting
for subparser in subparser_groups:
    subparser.usage = subparser.format_usage().replace('usage: main.py ', '')