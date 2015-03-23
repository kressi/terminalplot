############
terminalplot
############
|Console plot| image:: /plot.png

************
Installation
************
.. code-block::
	pip install terminalplot

*****
Usage
*****

Command Line
============
Get size of terminal emulator (tty)
.. code-block::
	$ plot -s
	> Rows: 25 Columns: 80

Plot some points
.. code-block::
	$ plot -x '-1 0 1 2 3 4' -y '0.1 0.2 0.23 0.234 0.24'

API
===
Plotting a graph
.. code-block:: python
	from terminalplot import plot
	x = range(100)
	y = [i**2 for i in x]
	plot(x, y)


Get size of current terminal window
.. code-block:: python
	from terminalplot import get_terminal_size
	get_terminal_size()

