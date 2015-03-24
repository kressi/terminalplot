"""
terminalplot.command.py
=======================

Implements command line interface for terminalplot.


usage: plot [-h] [-v] [-x X] [-y Y] [-s]

Minimalistic plot of a graph in terminal.

optional arguments:
  -h, --help           show this help message and exit
  -v, --version        show program's version number and exit
  -x X                 Values on x-axis. If empty, values on y-axis will be plotted according to their indices, E.g. (0, y0), (1, y1), ...
  -y Y                 Values on y-axis, at least one value has to be provided.
  -s, --terminal-size  Returns size of terminal <columns>, <rows>. No plot will be generated.

Either -s or -x and -y have to be provided.

Example:
        plot -x '-1 0 1 2 3 4' -y '0.1 0.2 0.23 0.234 0.24'
        plot -s

"""

import argparse
from argparse import RawTextHelpFormatter

from terminalplot import plot, get_terminal_size


def list_floats(value):
    values = value.split()
    if len(values) == 0:
        raise argparse.ArgumentError
    return map(float, values)

parser = argparse.ArgumentParser(description='Minimalistic plot of a graph in terminal.',
                                 formatter_class=RawTextHelpFormatter,
                                 epilog=("Either -s or -x and -y have to be provided.\n"
                                         "\nExample:\n"
                                         "\tplot -x '-1 0 1 2 3 4' -y '0.1 0.2 0.23 0.234 0.24'\n"
                                         "\tplot -s"))

parser.add_argument('-v',
                    '--version',
                    action='version',
                    version='%(prog)s 0.2.2')

parser.add_argument('-x',
                    type=list_floats,
                    action='store',
                    help=("Values on x-axis. If empty, values on y-axis will be plotted "
                           "according to their indices, E.g. (0, y0), (1, y1), ..."))

parser.add_argument('-y',
                    action='store',
                    type=list_floats,
                    help='Values on y-axis, at least one value has to be provided.')

parser.add_argument('-s',
                    '--terminal-size',
                    action='store_true',
                    help='Returns size of terminal <columns>, <rows>. No plot will be generated.')


def main():

    args = vars(parser.parse_args())

    if not any(args.values()):
        parser.error('No arguments provided.')

    if args['y']:
        y = args['y']
        x = args['x'] if args['x'] else range(len(y))
        plot(x, y)

    if args['terminal_size']:
        rc = get_terminal_size()
        print(''.join(['Rows: ', str(rc[0]), ' Columns: ', str(rc[1])]))
