import sys
import unittest
from contextlib import contextmanager
from io import StringIO

import terminalplot
from terminalplot import command as cli


@contextmanager
def capture_sys_output():
    capture_out = StringIO()
    try:
        sys.stdout = capture_out
        yield capture_out
    finally:
        sys.stdout = sys.__stdout__


class TestTerminalPlot(unittest.TestCase):
    def test_get_size(self):
        rows, columns = terminalplot.get_terminal_size()
        self.assertIsInstance(rows, int)
        self.assertIsInstance(columns, int)

    def test_plot(self):
        with capture_sys_output() as stdout:
            terminalplot.plot(x=[1, 2, 3], y=[1, 2, 3], rows=7, columns=3)

        expected_output = (
            "  *\n" " * \n" "*  \n" "\nMin x: 1 Max x: 3 Min y: 1 Max y: 3\n"
        )

        self.assertEqual(stdout.getvalue(), expected_output)


class TestCommand(unittest.TestCase):
    def test_list_floats(self):
        self.assertEqual(cli.list_floats("1 0.1 -0.3"), [1, 0.1, -0.3])

    def test_parser(self):
        parser = cli.make_parser()
        args = parser.parse_args(["-x", "1 0.1 -0.3", "-y", "5 0 0"])
        self.assertEqual(args.x, [1, 0.1, -0.3])
        self.assertEqual(args.y, [5, 0, 0])
        self.assertFalse(args.terminal_size)
