import ply.yacc as YACC_MODULE

from incc.compiler.cma.enum_ast import Ast
from .lexing import *
from .precedence import precedence
from .parser.error_handling import *
def createParser():
    PARSER_FINAL = YACC_MODULE.yacc(start="expression")
    return PARSER_FINAL

def p_proc_call(p):
    '''expression : ID LPAREN expression_list RPAREN
                   | ID LPAREN RPAREN'''
    if len(p) == 4:
        p[0] = (Ast.PROC_CALL.value, (p[1]), ([]))
    elif len(p) == 5:
        p[0] = (Ast.PROC_CALL.value, (p[1]), (p[3]))
    else:
        raise RuntimeError(f" ERROR in proc {p}")
def p_proc(p):
    '''expression : PROC LPAREN id_list RPAREN id_list RIGHT_ARROW expression
                  | PROC LPAREN  RPAREN id_list RIGHT_ARROW expression
                  | PROC LPAREN  RPAREN  RIGHT_ARROW expression
                  '''
    if len(p) == 6:
        p[0] = (Ast.PROC.value, ([]), ([]), (p[5]))
    elif len(p) == 7:
        p[0] = (Ast.PROC.value, ([]), (p[4]), (p[6]))
        # p[0] = (Ast.PROC.value, (p[3???]), ([]), (p[6]))
    elif len(p) == 8:
        p[0] = (Ast.PROC.value, (p[3]), (p[5]), (p[7]))
    else:
        raise RuntimeError(f" >>>>ERROR in proc {p[0]}")
def p_id_list(p) :
    '''id_list :  ID
                | ID COMMA id_list'''
    if len(p)==2:
        p[0] = p[1]
    elif len(p) == 4:
        # print(p[3])
        p[0] = (p[1], *p[3])

def p_expression_list(p):
    '''expression_list :  expression
                | expression COMMA expression_list'''
    if len(p)==2:
        p[0] = [p[1]]
    elif len(p) == 4:
        p[0] = (p[1], *p[3])

def p_while(p):
    '''expression : WHILE expression DO expression '''
    if len(p) == 5:
        p[0] = (Ast.WHILE.value, (p[2]), (p[4]))
    else:
        raise RuntimeError(f" ERROR in while {p}")

def p_if_then_else(p):
    '''expression : IF expression THEN expression
                  | IF expression THEN expression ELSE expression
    '''
    if len(p) == 5:
        p[0] = (Ast.IF_THEN_ELSE.value, p[2], p[4], None)
        # p[0] = ('if-then', p[2], p[4])
    elif len(p) == 7:
        # p[0] = ('if-then-else', p[2], p[4], p[6])
        p[0] = (Ast.IF_THEN_ELSE.value, p[2], p[4], p[6])
    else:
        raise RuntimeError(f" ERROR in if_then_else {p}")

def p_id(p) :
    'expression : ID'
    p[0] = (Ast.ID.value,  p[1])
    # p[0] = ('load',  p[1])

def p_int(p) :
    'expression : NUMBER'
    p[0] = ('number', p[1])

def p_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
    '''
    p[0] = (Ast.BINARY_OPERATOR.value, p[2], p[1], p[3])

def p_assign(p):
    '''expression : ID ASSIGN expression'''
    p[0] = (Ast.ASSIGN.value, (Ast.AST_variable.value, p[1]), p[3])

def p_expressions(p):
    '''expression : LBRACE sequence RBRACE '''
    p[0] =p[2]

def p_sequences_multi(p):
    '''sequence : sequence SEMICOLON expression 
                | expression'''
    if len(p) == 4:
        p[0] = (Ast.SEQUENCE.value, (p[1],p[3]))
    if len(p) == 2:
        p[0] = p[1]


def p_bin_compare(p):
    '''expression : expression LT expression
                  | expression GT expression
                  | expression LE expression
                  | expression GE expression
                  | expression EQS expression
                  | expression NEQS expression
    '''
    p[0] = (Ast.BINARY_COMPARE.value, p[2], p[1], p[3])



LEXER_FINAL, LH = createLexerAndLH()
PARSER_FINAL = createParser()
# LH.printAll()
# print(LH.get_lexer_entry("lextokens_all"))
# exit()
