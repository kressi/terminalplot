import shutil

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
    x_scaled = scale(x, columns)
    y_scaled = scale(y, rows)

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

def scale(x, length):
    """
    Scale points in 'x', such that distance between
    max(x) and min(x) equals to 'length'. min(x)
    will be moved to 0.
    """
    s = float(length - 1) / \
        (max(x) - min(x)) if x and max(x) - min(x) != 0 else length
    return [int((i - min(x)) * s) for i in x]

def get_terminal_size():
    try: 
        (columns, lines) = shutil.get_terminal_size()
        rc = (lines, columns)
    except:
      try:
          import os, fcntl, termios, struct
          with open(os.ctermid(), 'r') as fd:
              rc = struct.unpack(
                  'hh', fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
      except:
          rc = (os.getenv('LINES', 25), os.getenv('COLUMNS', 80))

    return rc
