_token_set = {
    'LBRACE',
    'RBRACE',
    'SEMICOLON'
}


def t_LBRACE(t):
   r'{'
   return t

def t_RBRACE(t):
    r'}'
    return t

def t_SEMICOLON(t):
    r';'
    return t

tokens_sequences = list(_token_set)

