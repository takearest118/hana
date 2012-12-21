# -*- coding: utf-8 -*-

from optparse import OptionParser

import analyzer
import dictionary

__usage__ = "%prog [-f]"
__version__ = "0.6"
__description__ = """
This program is a Hangeul analyzer
"""
__epilog__ = """
By ContextLogic Korea
"""

def _input_raw_file(option, opt_str, value, parser):
	raw = open(value.lower(), "rb").read()
	analyzer.start(raw)

def _input_dic_file(option, opt_str, value, parser):
	dic = dictionary.Dictionary(value.lower())
	print "\n".join(dic)
	while True:
		buff = raw_input(">> ")
		if buff.lower() == "q":
			break

def main():
	parser = OptionParser(usage=__usage__, version=__version__, description=__description__, epilog=__epilog__)
	parser.add_option("-f", "--filename", type="string", help="input raw string data from file.", action="callback", callback=_input_raw_file)
	parser.add_option("-d", "--dictionary", type="string", help="make dictionary from dic file.", action="callback", callback=_input_dic_file)
	(options, args) = parser.parse_args()

if __name__=="__main__":
	main()
