#from biomas.application.views  import biomas_map
import unittest

class TestMap(unittest.TestCase):
    """docstring for TestMap"""
    def __init__(self, arg):
        super(TestMap, self).__init__()
        self.arg = arg

    def test_mapid(self):
        _map = {"mapid": "ahsuahsuhsua", "token": "ashuahsuahusha"}
        self.assertEqual(_map.keys(), ["mapid", "token"])

    if __name__ == '__main__':
        unittest.main()
