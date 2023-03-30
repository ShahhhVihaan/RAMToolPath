import unittest
from path import Planner


class TestPath(unittest.TestCase):
    def testInit(self):
        pass

    def testReadGcode(self):
        pass

    def testGenerate(self):
        pass

    def testLineGetParams(self):
        a = Planner('sample_gcode/setup.gcode')
        a.generate()




if __name__ == '__main__':	
	unittest.main()
