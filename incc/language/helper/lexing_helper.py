



class LexingHelper():
    def __init__(self, finalLexer):
        self.finalLexer = finalLexer
        self.currentLexerState = self.finalLexer.__dict__
        # self.check_lexer_entry('lextokens_all')
        self.AllEntriesInLexerDict = ["lexre",
                                    "lexretext",
                                    "lexstatere",
                                    "lexstateretext",
                                    "lexstaterenames",
                                    "lexstate",
                                    "lexstatestack",
                                    "lexstateinfo",
                                    "lexstateignore",
                                    "lexstateerrorf",
                                    "lexstateeoff",
                                    "lexreflags",
                                    "lexdata",
                                    "lexpos",
                                    "lexlen",
                                    "lexerrorf",
                                    "lexeoff",
                                    "lextokens",
                                    "lexignore",
                                    "lexliterals",
                                    "lexmodule",
                                    "lineno",
                                    "lexoptimize",
                                    "lextokens_all",
                                    "lexmatch"
                                     ]

    def print_possible_keys(self):
        print(self.AllEntriesInLexerDict)
    def print_keys(self):
        keys = self.currentLexerState.keys()
        for key in keys:
            print(key)

    def get_keys(self):
        keys = self.currentLexerState.keys()
        return keys

    def get_lexer_entry(self,key):
        # entry = self.currentLexerState[key]
        entry = self.currentLexerState.get(key)
        print(">>>>"+key+": "+str(entry))
        return entry

    def printAll(self):
        keys = self.get_keys()


        for key in keys:
            self.get_lexer_entry(key)

    def print_token_keys(self,tok):
        print("==============================")
        print("==============================")
        token_dict = tok.__dict__
        for x in token_dict:
            print(x)


    def print_token_CurrentLexerStateFromToken(self,tok):
        token_dict = tok.__dict__
        currentLexerState = token_dict['lexer'].__dict__
        print(str(currentLexerState.get('lexmatch')) +"\tlineno: "+str(currentLexerState.get('lineno'))+" ",end="")
        print("lexpos: "+str(currentLexerState['lexpos']))

