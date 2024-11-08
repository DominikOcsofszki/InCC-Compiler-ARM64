

# def p_int(p) :
#     'expression : NUMBER'
#     p[0] = ('number', p[1])

# def p_error_binop(p):
#     '''expression : error PLUS error
#                   | error MINUS error
#                   | error TIMES error
#                   | error DIVIDE error
#     '''
#     print(f"Syntax error in binop: {p[1]} {p[2]} {p[3]}")
#     exit()

# def p_error_assign(p):
#     '''expression : ID ASSIGN error'''
#     print(f"Syntax error in assign expr:  {p[3]}")
#     exit()
#
# def p_error_expressions(p):
#     '''expression : LBRACE error RBRACE '''
#     print(f"Syntax error in sequence expr:  {p[2]}")

# def p_sequences_multi(p):
#     '''sequence : error SEMICOLON error 
#                 | error'''
#     if len(p) == 4:
#         p[0] = ('sequence', (p[1],p[3]))
#     if len(p) == 2:
#         p[0] = p[1]
#     print(f"Syntax error in sequence_multi:  {p[0]}")

def p_error_expression(p):
    'expression : error RBRACE'
    print(f"Syntax error in statement: {p[1]}")
    exit()
