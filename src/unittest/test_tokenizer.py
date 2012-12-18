# -*- coding: utf-8 -*-

import unittest

from hana import tokenizer
import string

class TestTokenizerFunctions(unittest.TestCase):

	def setUp(self):
		pass
	
	def test_symbol_escaper(self):
		self.assertEqual(tokenizer.Tokenizer.symbol_escaper("I am a boy."), "I am a boy")
		self.assertEqual(tokenizer.Tokenizer.symbol_escaper("It's gorgeous!"), "It s gorgeous")
		self.assertEqual(tokenizer.Tokenizer.symbol_escaper("고시원 주인은 8㎡(2평 남짓) 방값을 월 5만원 더 올려"), "고시원 주인은 8㎡ 2평 남짓 방값을 월 5만원 더 올려")
		self.assertEqual(tokenizer.Tokenizer.symbol_escaper(""), "")
	
	def test_space_tokenizer(self):
		ttest = "Python is a dynamic programming language that can be used for many kinds of software development."
		answer = ["Python", "is", "a", "dynamic", "programming", "language", "that", "can", "be", "used", "for", "many", "kinds", "of", "software", "development."]
		self.assertEqual(tokenizer.Tokenizer.space_tokenizer(ttest), answer)
	
	def test_number_filter(self):
		ttest = "18일 입시업체 진학사는 지난 10일부터 6일간 최근 고3 회원 1548명을 설문조사를 실시해 그 결과 수험생의 48%(737명)가 ‘합격한 다른 대학이 있다면 그냥 다니겠다’고 답한 것으로 드러났다."
		answer = ["18", "10", "6", "3", "1548", "48", "737"]
		self.assertEqual(tokenizer.Tokenizer.number_filter(ttest), answer)
	
	def test_number_comma_filter(self):
		ttest = "18일 전력거래소에 따르면 이날 오전 10∼11시 최대전력수요는 평균 7,517만2,000 ㎾로, 올해 8월6일 기록한 최고치(7,429만1,000 ㎾)보다 88만1,000 ㎾가량 높았다. 순간최대전력수요는 오전 10시28분 7,558만5,000 ㎾까지 치솟았다."
		answer = ["18", "10", "11", "7,517", "2,000", "7,429", "1,000", "88", "1,000", "10", "28", "7,558", "5,000"]
		self.assertEqual(tokenizer.Tokenizer.number_comma_filter(ttest), answer)

	def test_alphabet_filter(self):
		ttest = "iTunes App Store의 iPhone, iPod touch 및 iPad용 능률 영어표현찾기"
		answer = ["iTunes", "App", "Store", "iPhone", "iPod", "touch", "iPad"]
		self.assertEqual(tokenizer.Tokenizer.alphabet_filter(ttest), answer)
	
	def test_korean_filter(self):
		ttest = "iTunes App Store의 iPhone, iPod touch 및 iPad용 능률 영어표현찾기"
		answer = ["의", "및", "용", "능률", "영어표현찾기"]
		self.assertEqual(tokenizer.Tokenizer.korean_filter(ttest), answer)
	
	def test_check_token(self):
		self.assertEqual(tokenizer.Tokenizer.check_token("Python이란 무엇인가?"), "alphabet")
		self.assertEqual(tokenizer.Tokenizer.check_token("2012"), "number")
		self.assertEqual(tokenizer.Tokenizer.check_token("대통령선거"), "korean")
		self.assertEqual(tokenizer.Tokenizer.check_token("!?!?!?!"), "not supported")
	
if __name__=="__main__":
	#unittest.main()
	suite = unittest.TestLoader().loadTestsFromTestCase(TestTokenizerFunctions)
	unittest.TextTestRunner(verbosity=2).run(suite)
