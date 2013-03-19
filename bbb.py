

import aaa

class parser_callbacks():
	def syntax_error(self, token):
		print "syntax error on token ", token
	def accept(self):
		print "accept"
	def parse_failed(self):
		print "parse_failed"

x = aaa.Parser(parser_callbacks())
x.parse([[aaa.DO,"banana"]])


