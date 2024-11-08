from configs import Configs
from helper.file_loader import getFileNameFromcodeTX
from helper_compiler import (
    _printIRCode,
    _printStackCode,
    _readFromFile,
    _writeCodeIRToFile,
    _writeProgToFile,
    setBaseName,
)
from incc.compiler.cma.ast_to_expression import code_r
from incc.compiler.cma.ir_to_arm64 import arm64_final_prog, ir_to_arm64
from incc.language.parsing import LEXER_FINAL, LH, PARSER_FINAL

# LH is a helperfunction for checking out the LEXER and get information
# Could be use for adding more data
# LH.printAll()
# LH.print_possible_keys()
PRINT_GENERATED_IR_CODE = True
PRINT_GENERATED_ASM_CODE = True
PRINT_GENERATED_AST = True
PRINT_FILE_DATA = True


def print_final_env(env):
    print("final env: ")
    for x in env:
        print(x + ": " + str(env[x]))

def compiler_ir(ir_input, env):
    codeIR = ir_input
    if PRINT_GENERATED_IR_CODE:
        _printIRCode(codeIR)
    _writeCodeIRToFile(codeIR)
    arm_64_asm = ir_to_arm64(codeIR, env)
    prog = arm64_final_prog(arm_64_asm, env, stack_input_for_print=codeIR)
    if PRINT_GENERATED_ASM_CODE:
        _printStackCode(prog)
    _writeProgToFile(prog)
    print_final_env(env)

def compiler_ast(ast, env):
    codeIR = code_r(ast, env)
    compiler_ir(codeIR,env)
    print_final_env(env)


def load_file(base_file_name_in_code_dir, ir=False):
    print(f"\nDIR: {Configs.GENERATED_DIR.value}")
    print(f"Name:   {base_file_name_in_code_dir}.s\n")
    setBaseName(base_file_name_in_code_dir)
    ext = ".incc"
    dir_load_file=Configs.CODE_DIR.value
    if ir:
        dir_load_file=Configs.GENERATED_IR_CODE_DIR.value
        ext = ".ir"
    data = _readFromFile(base_file_name_in_code_dir + ext,dir_load_file=dir_load_file)
    return data


def print_ast(ast):
    ast_string = str(ast)
    x = ast_string.replace("((", "((\n")
    x = x.replace("))", "))\n")
    print(x)

def compileIRFileFromCodeFolderBaseName(fname, env):
    data = load_file(fname,ir=True)
    if PRINT_FILE_DATA:
        print(data)
    compiler_ir(data, env)

def compileFileFromCodeFolderBaseName(fname, env):
    data = load_file(fname)
    if PRINT_FILE_DATA:
        print(data)
    ast = PARSER_FINAL.parse(data)
    if PRINT_GENERATED_AST:
        print_ast(ast)

    compiler_ast(ast, env)


def run():
    FILE_NAME = getFileNameFromcodeTX()[0]
    print(FILE_NAME)
    fromIncc=True

    if fromIncc:
        compileFileFromCodeFolderBaseName(FILE_NAME, Configs.ENV.value)
    else:
        compileIRFileFromCodeFolderBaseName(FILE_NAME, Configs.ENV.value)



if __name__ == "__main__":
    run()
