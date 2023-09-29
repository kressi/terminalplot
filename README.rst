************
terminalplot
************

.. image:: https://img.shields.io/pypi/v/terminalplot.svg
    :alt: PyPi Version
    :target: https://pypi.python.org/pypi/terminalplot
.. image:: https://codeclimate.com/github/kressi/terminalplot/badges/gpa.svg
    :target: https://codeclimate.com/github/kressi/terminalplot
    :alt: Code Climate
.. image:: https://codecov.io/gh/kressi/terminalplot/graph/badge.svg?token=WCyd0O14aA
    :target: https://codecov.io/gh/kressi/terminalplot
    :alt: Test Coverage

Terminalplot is a minimalistic packgage, that only prints points
to the terminal. It does not have any dependencies.

.. image:: https://raw.githubusercontent.com/kressi/terminalplot/master/plot.png
    :alt: Console plot

Installation
############

.. code:: bash

    pip install terminalplot

Usage
#####

Command Line
************
Get size of terminal emulator (tty)::

    $ plot -s
    Rows: 25, Columns: 80

Plot some points::

    $ plot -x '-1 0 1 2 3 4' -y '0.1 0.2 0.23 0.234 0.24'


API
***

Plotting a graph

.. code:: python

    from terminalplot import plot
    x = range(100)
    y = [i**2 for i in x]
    plot(x, y)

Get size of current terminal window

.. code-block:: python

    from terminalplot import get_terminal_size
    get_terminal_size()
