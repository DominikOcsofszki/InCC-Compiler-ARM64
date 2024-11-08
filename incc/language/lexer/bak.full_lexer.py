# seq_tokens = {
#     'LBRACE',
#     'RBRACE',
#     'SEMICOLON'
# }
#
#
# t_LBRACE = '{'
# t_RBRACE = '}'
# t_SEMICOLON = ';'
# controlflow_reserved_words = {
#     'IF', 'THEN', 'ELSE', 
#     'LOOP', 'FOR',
#     'WHILE', 'DO'
# }
# var_tokens = {
#     'ASSIGN'
# }
var_reserved_words = {
    'LOCK', 'LOCAL', 'IN'
}


# t_ASSIGN = '='
# expr_tokens = {
#     'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
#     'LPAREN', 'RPAREN',
#     'LT', 'GT', 'LE', 'GE',
#     'EQS', 'NEQS'
# }
expr_reserved_words = {
    'EQ', 'NEQ', 'XOR', 'NOT', 'AND', 'OR', 'NAND', 'NOR', 'IMP'
}


t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_EQS = r'=='
t_NEQS = r'!='
struct_tokens = {
    'DOT'
}
struct_reserved_words = {
    'STRUCT', 'EXTEND', 'SET', 'THIS'
}

t_DOT = r'\.'
lit_tokens = {
    'NUMBER', 'STRING', 'CHAR', 'LBRACKET', 'RBRACKET'
}
lit_reserved_words = {
    'TRUE', 'FALSE'
}

t_NUMBER = r'-?\d+(\.\d*)?|\.\d+'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'


def t_STRING(t):
    r'"([^\n"]|\")*"'
    t.value = t.value[1:-1]
    return t


def t_CHAR(t):
    r"'([^\n']|\')'"
    t.value = t.value[1:-1]
    return t



tokens.extend(['IDENT', 'COMMA'])


t_COMMA = ','


def t_IDENT(t):
    """
    [_a-zA-Z][_a-zA-Z0-9]*
    """

    valUp = t.value.upper()
    if valUp in reserved_words:
        t.type = valUp
        t.value = valUp

    return t


def t_newline(t):
    r"""
    \n+
    """
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'
t_ignore_COMMENT = r'\#.*'




functions_tokens = {
    'RIGHT_ARROW', 'BACKSLASH'
}
functions_reserved_words = {
    'FUN', 'PROC'
}

t_RIGHT_ARROW = r'->'
t_BACKSLASH = r'\\'
