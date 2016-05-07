import unittest
import mock
from src import pipspect


class TestPipSpect(unittest.TestCase):

    def setUp(self):
        pass

    def test_success(self):
        self.assertTrue(pipspect.pipspect(mock))

if __name__ == '__main__':
    unittest.main()
