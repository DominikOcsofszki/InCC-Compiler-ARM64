_token_set = {'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN'}

def t_RIGHT_ARROW(t):
    r'->'
    return t
def t_PLUS(t):
    r'\+'
    return t

def t_MINUS(t):
    r'-'
    return t
def t_TIMES(t):
    r'\*'
    return t
def t_DIVIDE(t):
    r'/'
    return t
def t_LPAREN(t):
    r'\('
    return t
def t_RPAREN(t):
    r'\)'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore  = ' \t'
t_ignore_COMMENT = r'\#.*'


def t_error(t):
    raise Exception("Illegal character '%s'" % t.value[0])

tokens_arith = list(_token_set)

