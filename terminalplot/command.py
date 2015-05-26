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

from argparse import RawTextHelpFormatter, ArgumentParser
from terminalplot import plot, get_terminal_size
from .version import __version__


def list_floats(value):
    return [float(v) for v in value.split()]

def make_parser():

    parser = ArgumentParser( description     = 'Minimalistic plot of a graph in terminal.',
                             formatter_class = RawTextHelpFormatter,
                             epilog          = ("Either -s or -x and -y have to be provided.\n"
                                                "\nExample:\n"
                                                "\tplot -x '-1 0 1 2 3 4' -y '0.1 0.2 0.23 0.234 0.24'\n"
                                                "\tplot -s") )

    parser.add_argument( '-v',
                         '--version',
                         action  = 'version',
                         version = '%(prog)s '+__version__ )

    parser.add_argument( '-x',
                         action = 'store',
                         type   = list_floats,
                         help   = ("Values on x-axis. If empty, values on y-axis will be plotted "
                                   "according to their indices, E.g. (0, y0), (1, y1), ...") )

    parser.add_argument( '-y',
                         action = 'store',
                         type   = list_floats,
                         help   = 'Values on y-axis, at least one value has to be provided.' )

    parser.add_argument( '-s',
                         '--terminal-size',
                         action = 'store_true',
                         help   = 'Returns size of terminal <columns>, <rows>. No plot will be generated.' )

    return parser


def main():

    parser = make_parser()
    args   = parser.parse_args()

    if not args.terminal_size and not args.y:
        parser.error('Not enough arguments provided.')

    if args.y:
        y = args.y
        x = args.x or range(len(y))
        plot(x, y)

    if args.terminal_size:
        print("Rows: {}, Columns: {}".format(*get_terminal_size()))

if __name__ == '__main__':
    main()