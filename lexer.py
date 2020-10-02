import ply.lex as lex
import sys

tokens = (
'ID','INTCONST','CHARCONST','PLUS','MINUS','TIMES','DIVISION','EQ','NE',
'LT','GT', 'LE','GE','LPAR','RPAR','LBR','RBR','ASSIGN','DOT','COMMA',
'SEMICOLON','COLON','RANGE', 'PROGRAM', 'VAR', 'ARRAY', 'OF', 'PROCEDURE', 
'BEGIN', 'END', 'WRITE', 'READ', 'IF', 'THEN', 'ELSE', 'WHILE', 'DO', 'NOT',
'OR', 'DIV', 'AND', 'CONST', 'TYPE', 'INTEGER', 'BOOLEAN', 'TRUE', 'FALSE',
'CHAR', 'ABSOLUTE', 'ASM', 'CASE', 'DESTRUCTOR', 'DOWNTO', 'FUNCTION', 'IN',
'INTERFACE', 'LABEL', 'NIL', 'OBJECT', 'PRIVATE', 'REPEAT', 'SHL', 'STRING',
'TO', 'UNIT', 'USES', 'VIRTUAL', 'WITH', 'CONSTRUCTOR', 'EXTERNAL', 'FILE',
'FORWARD', 'GOTO', 'IMPLEMENTATION', 'INLINE', 'INTERRUPT', 'MOD', 'PACKED',
'RECORD', 'SET', 'SHR', 'UNTIL', 'XOR')

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
t_ignore_comment = r'\(\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*?\*+\)|{[^{]*}'


# funciones keywords
def t_PROGRAM(t):
	r'program|PROGRAM'
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

def t_WRITE(t):
	r'write'
	return t

def t_READ(t):
	r'read'
	return t

def t_WHILE(t):
	r'while'
	return t

def t_DO(t):
	r'do'
	return t

def t_NOT(t):
	r'not'
	return t

def t_OR(t):
	r'or'
	return t

def t_DIV(t):
	r'div'
	return t

def t_AND(t):
	r'AND'
	return t

def t_CONST(t):
	r'const|CONST'
	return t

def t_TYPE(t):
	r'type|TYPE'
	return t

def t_INTEGER(t):
	r'integer'
	return t

def t_BOOLEAN(t):
	r'boolean'
	return t

def t_CHAR(t):
	r'char'
	return t

def t_TRUE(t):
	r'true'
	return t

def t_FALSE(t):
	r'false'
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

def t_ABSOLUTE(t):
	r'absolute'
	return t

def t_ASM(t):
	r'asm'
	return t

def t_CASE(t):
	r'case'
	return t

def t_DESTRUCTOR(t):
	r'destructor'
	return t

def t_DOWNTO(t):
	r'downto'
	return t

def t_FUNCTION(t):
	r'function'
	return t

def t_IN(t):
	r'in'
	return t

def t_INTERFACE(t):
	r'interface'
	return t

def t_LABEL(t):
	r'label'
	return t

def t_NIL(t):
	r'nil'
	return t

def t_OBJECT(t):
	r'object'
	return t

def t_PRIVATE(t):
	r'private'
	return t

def t_REPEAT(t):
	r'repeat'
	return t

def t_SHL(t):
	r'shl'
	return t

def t_STRING(t):
	r'string'
	return t

def t_TO(t):
	r'to'
	return t

def t_UNIT(t):
	r'unit'
	return t

def t_USES(t):
	r'uses'
	return t

def t_VIRTUAL(t):
	r'virtual'
	return t

def t_WITH(t):
	r'with'
	return t

def t_CONTRUCTOR(t):
	r'constructor'
	return t

def t_EXTERNAL(t):
	r'external'
	return t

def t_FILE(t):
	r'file'
	return t

def t_FORWARD(t):
	r'forward'
	return t

def t_GOTO(t):
	r'goto'
	return t

def t_IMPLEMENTATION(t):
	r'implememtation'
	return t

def t_INLINE(t):
	r'inline'
	return t

def t_INTERRUPT(t):
	r'interrupt'
	return t

def t_MOD(t):
	r'mod'
	return t

def t_PACKED(t):
	r'packed'
	return t

def t_RECORD(t):
	r'record'
	return t

def t_SET(t):
	r'set'
	return t

def t_SHR(t):
	r'shr'
	return t

def t_UNTIL(t):
	r'until'
	return t

def t_XOR(t):
	r'xor'
	return t

# ---------------
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    print ("new line")

def t_ID(t):
    r'\w+(_\d\w)*'
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
