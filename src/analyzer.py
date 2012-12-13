# -*- coding: utf-8

from tokenizer import Tokenizer as T
from dictionary import Dictionary

from optparse import OptionParser
import re
import os

__usage__ = "%prog [-f]"
__version__ = "%prog v0.5"
__description__ = """
This program is a Hangeul analyzer
"""
__epilog__ = """
By Kevin Cho
"""

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

def start_analyzer(raw):
	print "[INFO] Analyze Korean"
	print "[INFO] raw data"
	print raw
	print "[INFO] raw data -Done-"
	tokens = T.space_tokenizer(T.symbol_escaper(raw))
	print "[INFO] escape symbol"
	print os.linesep.join(tokens)
	print "[INFO] escape symbol -Done-"
	j_dic = Dictionary("./dic/josa.dic")
	for t in tokens:
		what = T.check_token(t)
		if what == "korean":
			stemm, josa = josa_analyzer(t, j_dic)
			print "%s:\t%s %s" % (t, stemm, josa)
		else:
			print "%s: %s" % (t, what)
	print "[INFO] Analyze Korean -Done-"

def input_file(option, opt_str, value, parser):
	try:
		fp = open(value.lower(), "rb")
	except Exception, err:
		raise err
	else:
		raw = fp.read()
	finally:
		fp.close()
	start_analyzer(raw)

def main():
	parser = OptionParser(usage=__usage__, version=__version__, description=__description__, epilog=__epilog__)
	parser.add_option("-f", "--filename", type="string", help="input raw string data from file.", action="callback", callback=input_file)
	(options, args) = parser.parse_args()

if __name__=="__main__":
	main()
