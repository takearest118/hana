# -*- coding: utf-8

class Dic(set):
	def __init__(self, filename):
		try:
			fp = open(filename, "rb")
		except Exception, err:
			raise err
		else:
			raw = fp.read()
			self.name = fp.name
		finally:
			fp.close()
		for el in raw.split("\n"):
			self.add(el)
