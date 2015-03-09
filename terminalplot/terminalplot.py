import fcntl
import os
import termios
import struct


def plot(x, y, rows=None, columns=None):
    """
    x, y list of values on x- and y-axis
    plot those values within canvas size (rows and columns)
    """
    if not rows or not columns:
        rows, columns = get_terminal_size()
    # offset for caption
    rows -= 4

    # Scale points such that they fit on canvas
    scale_x = float(columns - 1) / \
        (max(x) - min(x)) if x and max(x) - min(x) != 0 else columns
    scale_y = float(rows - 1) / \
        (max(y) - min(y)) if y and max(y) - min(y) != 0 else rows
    x_scaled = [int((i - min(x)) * scale_x) for i in x]
    y_scaled = [int((i - min(y)) * scale_y) for i in y]

    # Create empty canvas
    canvas = [[' ' for _ in range(columns)] for _ in range(rows)]

    # Add scaled points to canvas
    for ix, iy in zip(x_scaled, y_scaled):
        canvas[rows - iy - 1][ix] = '*'

    # Print rows of canvas
    for row in [''.join(row) for row in canvas]:
        print(row)

    # Print scale
    print(''.join([
        '\nMin x: ', str(min(x)),
        ' Max x: ',  str(max(x)),
        ' Min y: ',  str(min(y)),
        ' Max y: ',  str(max(y))
    ]))


def get_terminal_size():
    try:
        with open(os.ctermid(), 'r') as fd:
            rc = struct.unpack(
                'hh', fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
    except:
        rc = (os.getenv('LINES', 25), os.getenv('COLUMNS', 80))

    return rc
