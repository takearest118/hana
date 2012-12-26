# -*- coding: utf-8

class Dictionary(dict):
	def __init__(self, filename):
		self.name = filename
		self.update()
	
	def update(self):
		try:
			fp = open(self.name, "rb")
		except Exception, err:
			raise err
		else:
			raw = fp.read()
		finally:
			fp.close()
		self.clear()
		for idx in raw.split("\n"):
			self[idx] = 1
		if self.has_key(""):
			self.pop("")
		print "updated from %s" % self.name

__help__ = """
dictionary mode help
- help or h
- list or l
- update or u
- quit or q
"""

def console(dic):
	while True:
		buff = raw_input("%s >> " % dic.name).strip().lower()
		if buff in dic:		# check word in dictionary
			print "\"%s\" exists in dictionary" % buff
		elif buff == "list" or buff == "l":
			print "\n".join(dic)
		elif buff == "help" or buff == "h":
			print __help__
		elif buff == "update" or buff == "u":
			dic.update()
		elif buff == "quit" or buff == "q":
			print "dictionary mode quit."
			break
		else:
			pass
