import ply.lex as lex
import sys

keywords = { 'program', 'var', 'array', 'of', 'procedure', 'begin', 'end',
'write', 'read', 'if', 'then', 'else', 'while', 'do', 'not', 'or', 'div',
'and', 'const', 'type', 'integer', 'boolean', 'true', 'false', 'char'
}

tokens = (
'ID','INTCONST','CHARCONST','PLUS','MINUS','TIMES','DIVISION','EQ','NE',
'LT','GT', 'LE','GE','LPAR','RPAR','LBR','RBR','ASSIGN','DOT','COMMA',
'SEMICOLON','COLON','RANGE', 'PROGRAM', 'VAR', 'ARRAY', 'OF', 'PROCEDURE', 
'BEGIN', 'END', 'WRITE', 'READ', 'IF', 'THEN', 'ELSE', 'WHILE', 'DO', 'NOT',
'OR', 'DIV', 'AND', 'CONST', 'TYPE', 'INTEGER', 'BOOLEAN', 'TRUE', 'FALSE', 'CHAR'
)

t_CHARCONST = r'\'[^\']*\'|"[^"]*"'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVISION = r'/'
t_EQ = r'='
t_NE = r'<>'
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_LPAR = r'\('
t_RPAR = r'\)'
t_LBR = r'\['
t_RBR = r'\]'
t_ASSIGN = r':='
t_RANGE = r'\.\.'
t_DOT = r'\.'
t_COMMA = r','
t_SEMICOLON = r';'
t_COLON = r':'

t_ignore = " \t"



# funciones keywords
def t_PROGRAM(t):
	r'program'
	return t

def t_VAR(t):
	r'var'
	return t

def t_ARRAY(t):
	r'array'
	return t

def t_OF(t):
	r'of'
	return t

def t_PROCEDURE(t):
	r'procedure'
	return t

def t_BEGIN(t):
	r'begin'
	return t

def t_INTEGER(t):
	r'integer'
	return t

def t_IF(t):
	r'if'
	return t

def t_THEN(t):
	r'then'
	return t

def t_ELSE(t):
	r'else'
	return t

def t_END(t):
	r'end'
	return t



def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    print ("new line")

def t_ID(t):
    r'\w(_\d\w)*'
    return t

def t_INTCONST(t):
	r'[0-9]+'
	t.value = int(t.value)
	return t

def t_error(t):
	print("Lexical error: {}".format(str(t.value[0])))
	t.lexer.skip(1)

def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print(tok)

lexer = lex.lex()

if __name__ == "__main__":
	if len(sys.argv) > 1 :
		end = sys.argv[1]
	else:
		end = 'input.pas'
	f = open(end, 'r')
	data = f.read().replace(" ","")
	print(data)
	lexer.input(data)
	test(data,lexer)
