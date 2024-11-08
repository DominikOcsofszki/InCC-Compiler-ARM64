
_token_set = {"ASSIGN","ID"}
tokens_assign = list(_token_set)
_token_reserved_words = { }
_token_set = {
    'LT', 'GT', 'LE', 'GE',
    'EQS', 'NEQS'
}
tokens_compare = list(_token_set)

def t_LE(t):
    r'<='
    return t
def t_GE(t):
    r'>='
    return t
def t_EQS(t):
    r'=='
    return t
def t_NEQS(t):
    r'!='
    return t
def t_LT(t):
    r'<'
    return t
def t_GT(t):
    r'>'
    return t

def t_ASSIGN(t):
    r'='
    return t

_token_set ={ 'COMMA','RIGHT_ARROW' }
_token_reserved ={ 'PROC' }
t_COMMA = ','


tokens_proc = list(_token_set)
tokens_proc_reserved = list(_token_reserved)



# tokens_reserved_compare = list(_token_reserved_words)


