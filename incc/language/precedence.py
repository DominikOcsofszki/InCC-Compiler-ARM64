
precedence = [
    ['nonassoc', 'THEN'],
    ['nonassoc', 'ELSE', 'DO', 'WHILE', 'IN'],
    ['left', 'COMMA'],
    ['right', 'ASSIGN'],
    ['right', 'RIGHT_ARROW'],
    ['left', 'OR', 'NOR', 'XOR'],
    ['left', 'IMP'],
    ['left', 'AND', 'NAND'],
    ['left', 'EQS', 'NEQS', 'EQ', 'NEQ'],
    ['left', 'LT', 'GT', 'LE', 'GE'],
    ['left', 'PLUS', 'MINUS'],
    ['left', 'TIMES', 'DIVIDE'],
    ['right', 'NOT', 'UMINUS', 'UPLUS'],
    ['right', 'LPAREN', 'LBRACKET', 'DOT'], #<<correct
    # ['right', 'LPAREN'],
]

    # 'LBRACE',
    # 'RBRACE',
    # 'SEMICOLON'

precedence = [
    ['nonassoc', 'THEN'],
     #['nonassoc', 'ELSE', 'DO', 'WHILE', 'IN'],
    ['nonassoc', 'ELSE', 'DO', 'WHILE'],
    ['left', 'COMMA'],
    ['right', 'ASSIGN'],
    ['right', 'RIGHT_ARROW'],
    # ['left', 'OR', 'NOR', 'XOR'],
    # ['left', 'IMP'],
    # ['left', 'AND', 'NAND'],
    # ['left', 'EQS', 'NEQS', 'EQ', 'NEQ'],
    ['left', 'EQS', 'NEQS'],
    ['left', 'LT', 'GT', 'LE', 'GE'],
    ['left', 'PLUS', 'MINUS'],
    ['left', 'TIMES', 'DIVIDE'],
    # ['right', 'NOT', 'UMINUS', 'UPLUS'],
    # ['right', 'LPAREN', 'LBRACKET', 'DOT'], #<<correct
    ['right', 'LPAREN'], #<<correct
    # ['right', 'LPAREN'],
]
