import unittest
import terminalplot

class TestSequenceFunctions(unittest.TestCase):

    def test_get_size(self):
        assertIsInstance(terminalplot.get_terminal_size(), tuple)

    def test_plot(self):
        assertTrue(True)

if __name__ == '__main__':
    unittest.main()