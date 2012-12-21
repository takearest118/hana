# -*- coding: utf-8

from tokenizer import Tokenizer
from dictionary import Dictionary

import re
import os

"""
Analyze scenario
sentence -> symbol -> space -> korean -> compare basic dictionary -> output
							-> alphabet                           -> bigram
				            -> number
"""

def bigram_analyzer(raw):
	UTF8_BYTE = 3	# count byte of utf-8 per one Korean character
	return [raw[idx:idx+UTF8_BYTE*2] for idx in xrange(0, len(raw)-UTF8_BYTE, UTF8_BYTE)]

def josa_analyzer(raw, dic):
	UTF8_BYTE = 3	# count byte of utf-8 per one Korean character
	for idx in xrange(0, len(raw)-UTF8_BYTE, UTF8_BYTE):
		if raw[idx+UTF8_BYTE:] in dic:
			return raw[:idx+UTF8_BYTE], raw[idx+UTF8_BYTE:]
	return raw, None

def start(raw):
	print "[INFO] Analyze Korean"
	print "[INFO] raw data"
	print raw
	print "[INFO] raw data -Done-"
	tokens = Tokenizer.space_tokenizer(Tokenizer.symbol_escaper(raw))
	print "[INFO] escape symbol"
	print os.linesep.join(tokens)
	print "[INFO] escape symbol -Done-"
	j_dic = Dictionary("./dic/josa.dic")
	for t in tokens:
		what = Tokenizer.check_token(t)
		if what == "korean":
			stemm, josa = josa_analyzer(t, j_dic)
			print "%s:\t%s %s" % (t, stemm, josa)
		else:
			print "%s: %s" % (t, what)
	print "[INFO] Analyze Korean -Done-"
