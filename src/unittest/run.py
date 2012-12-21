# -*- coding: utf-8 -*-
"""
This script executes all unittest
"""

import unittest
import glob

def make_suite():
	suite = unittest.TestSuite()
	for module in glob.glob("test_*.py"):
		suite.addTest(unittest.TestLoader().loadTestsFromModule(__import__(module.split('.')[0])))
	return suite

if __name__=="__main__":
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(make_suite())
