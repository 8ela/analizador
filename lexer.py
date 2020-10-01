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

t_PROGRAM = r'program'
t_VAR = r'var'
t_ARRAY = r'array'
t_OF = r'of'
t_PROCEDURE = r'procedure'
t_BEGIN = r'begin'
t_END = r'end'
t_WRITE = r'write'
t_READ = r'read'
t_IF = r'if'
t_THEN = r'then'
t_ELSE = r'else'
t_WHILE = r'while'
t_DO = r'do'
t_NOT = r'not'
t_OR = r'or'
t_DIV = r'div'
t_AND = r'and'
t_CONST = r'const'
t_TYPE = r'type'
t_INTEGER = r'integer'
t_BOOLEAN = r' boolean'
t_TRUE = r'true'
t_FALSE = r'false'
t_CHAR = r'char'

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
	data = f.read()
	print(data)
	lexer.input(data)
	test(data,lexer)
