
from enum import Enum


class Ast(Enum):
    WHILE = 'while'
    AST_while_start = 'while-start'
    AST_while_end = 'while-end'
    IF_THEN_ELSE = 'if-then-else'
    BINARY_COMPARE = 'binary-compare'
    BINARY_OPERATOR = 'binary-operator'
    SEQUENCE = 'sequence'
    ASSIGN = 'assign'
    AST_variable = 'variable'
    PRINT_STACK_5 = 'print_stack_5'
    PROC = 'procedur'
    PROC_CALL = 'procedur_call'
    ID = 'ID'



