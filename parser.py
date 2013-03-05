import ply.yacc as yacc
from ply.lex import LexToken



def gen(code):
	for line in code:
		for item in line:
			t = LexToken()
			t.type = item[1]
			t.value = item[0]
			yield t
	yield None
 


def parse_code(code):
	code_yielder = gen(code)
	print parser.parse(tokenfunc=code_yielder.next,lexer=3)




tokens = (
	'NUMBER',
	'PLUS',
	'MINUS',
	'TIMES',
	'DIVIDE',
	'LPAREN',
	'RPAREN'
)	




def p_expression_plus(p):
	'expression : expression PLUS term'
	p[0] = p[1] + p[3]

def p_expression_minus(p):
	'expression : expression MINUS term'
	p[0] = p[1] - p[3]

def p_expression_term(p):
	'expression : term'
	p[0] = p[1]

def p_term_times(p):
	'term : term TIMES factor'
	p[0] = p[1] * p[3]

def p_term_div(p):
	'term : term DIVIDE factor'
	p[0] = p[1] / p[3]

def p_term_factor(p):
	'term : factor'
	p[0] = p[1]

def p_factor_num(p):
	'factor : NUMBER'
	p[0] = p[1]

def p_factor_expr(p):
	'factor : LPAREN expression RPAREN'
	p[0] = p[2]

def p_error(p):
	print "Syntax error in input!"




parser = yacc.yacc()

parse_code([[[1, "NUMBER"],["2", "PLUS"],[3, "NUMBER"]]])
