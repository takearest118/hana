# -*- coding: utf-8 -*-

import unittest

from hana import analyzer
from hana import dictionary

class TestAnalyzerFunctions(unittest.TestCase):

	def setUp(self):
		pass
	
	def test_bigram_analyzer(self):
		self.assertEqual(analyzer.bigram_analyzer("일"), [])
		self.assertEqual(analyzer.bigram_analyzer("선거"), ["선거"])
		self.assertEqual(analyzer.bigram_analyzer("빌딩숲"), ["빌딩", "딩숲" ])
		self.assertEqual(analyzer.bigram_analyzer("녹색텀블러"), ["녹색", "색텀", "텀블", "블러" ])
	
	def test_josa_analyzer(self):
		dic = dictionary.Dictionary("../dic/josa.dic")
		self.assertEqual(analyzer.josa_analyzer("사람은", dic), ("사람", "은"))
		self.assertEqual(analyzer.josa_analyzer("먹었다", dic), ("먹었", "다"))
		self.assertEqual(analyzer.josa_analyzer("만약에", dic), ("만약", "에"))

if __name__=="__main__":
	suite = unittest.TestSuite()
	test = unittest.TestLoader().loadTestsFromTestCase(TestAnalyzerFunctions)
	suite.addTest(test)
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(suite)
