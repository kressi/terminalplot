import unittest
import terminalplot
import sys

try:
    # Python 3
    from io import StringIO
except ImportError:
    # Python 2
    from StringIO import StringIO

class TestTerminalPlot(unittest.TestCase):

    def test_get_size(self):
        terminal_size = terminalplot.get_terminal_size()
        self.assertTrue(type(terminal_size) is tuple)

    def test_plot(self):
        try:
            out = StringIO()
            sys.stdout = out
            terminalplot.plot( x=[1,2,3], y=[1,2,3], rows=7, columns=3 )
            output = out.getvalue()
            expected_output = ( "  *\n"
                                " * \n"
                                "*  \n"
                                "\nMin x: 1 Max x: 3 Min y: 1 Max y: 3\n" )
            self.assertEqual(output, expected_output)
        finally:
            sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main()
