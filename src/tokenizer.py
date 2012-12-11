# -*- coding: utf-8 -*-

import re

class Tokenizer(object):

	@staticmethod
	def symbol_escaper(raw):
		replace = re.sub(r"[\~\`\!\@\#\$\%\^\&\*\-\_\=\+\\|\:\;\.\,\?\/\<\>\(\)\{\}\[\]\"\'\n]", " ", raw)
		return re.sub(r"[\s]+", " ", replace).strip()

	@staticmethod
	def space_tokenizer(raw):
		return raw.split(" ")

	@staticmethod
	def number_filter(raw):
		return re.findall(r"([0-9]+)", raw)

	@staticmethod
	def number_comma_filter(raw):
		return re.findall(r"([1-9][0-9,]+)", raw)

	@staticmethod
	def alphabet_filter(raw):
		return re.findall(r"[a-zA-Z]+", raw)

	@staticmethod
	def korean_filter(raw):
		return re.findall(r"[ㄱ-ㅎㅏ-ㅣ가-힣]+", raw)

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
