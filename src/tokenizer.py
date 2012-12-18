# -*- coding: utf-8 -*-

import re
import string

class Tokenizer(object):

	@staticmethod
	def symbol_escaper(raw):
		#quotation_marks = u"‘’“”"
		regex = r"[%s%s]" % (string.punctuation, string.whitespace)
		replace = re.sub(regex, " ", raw)
		return re.sub(r"[\s]+", " ", replace).strip()

	@staticmethod
	def space_tokenizer(raw):
		return raw.split(" ")

	@staticmethod
	def number_filter(raw):
		regex = r"[%s]+" % string.digits
		return re.findall(regex, raw)

	@staticmethod
	def number_comma_filter(raw):
		regex = r"([1-9][0-9,]+)"
		return re.findall(regex, raw)

	@staticmethod
	def alphabet_filter(raw):
		regex = r"[%s]+" % string.letters
		return re.findall(regex, raw)

	@staticmethod
	def korean_filter(raw):
		regex = r"[ㄱ-ㅎㅏ-ㅣ가-힣]+" 
		return re.findall(regex, raw)

	@staticmethod
	def check_token(raw):
		if len(Tokenizer.number_filter(raw)) != 0:
			return "number"
		elif len(Tokenizer.alphabet_filter(raw)) != 0:
			return "alphabet"
		elif len(Tokenizer.korean_filter(raw)) != 0:
			return "korean"
		else:
			return "not supported"
