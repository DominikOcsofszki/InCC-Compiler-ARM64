import ply.lex as LEX
from icecream import ic
from .lexer.arith_expr import *
# from .lexer.assign_expr import *
from .lexer.sequences import *
from .lexer.controllflow_expr import *
from .lexer.compare import *
from .lexer.print_expr import *
from .lexer.proc_lexer import *
from .helper.lexing_helper import LexingHelper

reserved_tokens = tokens_reserved_controllflow+\
        tokens_reserved_printf+\
        tokens_proc_reserved+\
        []

tokens = tokens_arith +\
        tokens_sequences +\
        tokens_assign +\
        tokens_compare +\
        tokens_proc +\
        []+\
        reserved_tokens

# DATA = '''
#     x = 1
#
#
#     x = 1
#     x = 1
#     '''

def t_ID(t):
    """
    [_a-zA-Z][_a-zA-Z0-9]*
    """

    t.lexer.global_counter =     t.lexer.global_counter + 1
    valUp = t.value.upper()
    if valUp in reserved_tokens:
        t.type = valUp
        t.value = valUp
        #exit()
    # print(t)

    return t
def t_NEWLINE(t):
    r'\n+'
    # t.__dict__['lexer'].__dict__['lineno'] = t.__dict__['lexer'].__dict__['lineno'] + 1
    t.lexer.lineno += len(t.value)
    return
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    exit()
    # t.lexer.skip(1)


def run(data):
    LEXER_FINAL=LEX.lex(debug=True)
    LH = LexingHelper(LEXER_FINAL)
    LEXER_FINAL.input(data)
    printAndConsumeAllToken(LEXER_FINAL,LH)

def printAndConsumeAllToken(_LEXER_FINAL,_LH):
    while True:
        tok = _LEXER_FINAL.token()
        if not tok: 
            break      # No more input
        # LH.print_token_keys(tok)
        _LH.print_token_CurrentLexerStateFromToken(tok)

# run(DATA)

def createLexerAndLH(debug_input=False):
    LEXER_FINAL=LEX.lex(debug=debug_input)
    LEXER_FINAL.global_counter = 0
    LH = LexingHelper(LEXER_FINAL)
    return LEXER_FINAL, LH

#
# def runTrial():
#     LEXER_FINAL, LH = createLexerAndLH()
#     LEXER_FINAL.input(DATA)
#     LH.print_possible_keys()
#     print(LEXER_FINAL.__dict__.get('global_counter'))
#     # LH.get_lexer_entry('lexmatch')
#     # LH.get_lexer_entry('lexpos')
#     printAndConsumeAllToken(LEXER_FINAL,LH)
#     print(LEXER_FINAL.__dict__.get('global_counter'))


