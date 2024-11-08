from configs import SK, Configs
from helper.file_loader import getFileNameFromcodeTX
from helper_compiler import (
    _printIRCode,
    _printStackCode,
    _readFromFile,
    _writeCodeIRToFile,
    _writeProgToFile,
    setBaseName,
)
from incc.compiler.cma.gen_ir import code_r
from incc.compiler.cma.gen_arm import arm64_final_prog, ir_to_arm64
from incc.language.parsing import LEXER_FINAL, LH, PARSER_FINAL

# LH is a helperfunction for checking out the LEXER and get information
# Could be use for adding more data
# LH.printAll()
# LH.print_possible_keys()
PRINT_GENERATED_IR_CODE = True
PRINT_GENERATED_ASM_CODE = True
PRINT_GENERATED_AST = True
PRINT_FILE_DATA = True


def print_final_env(env:SK):
    print("final env: ")
    env.print_all()
    # print(env)
    # for x in env:
    #     print(x + ": " + str(env[x]))


def compiler_ast(ast, env):
    codeIR = code_r(ast, env)
    if PRINT_GENERATED_IR_CODE:
        _printIRCode(codeIR)
    _writeCodeIRToFile(codeIR)
    arm_64_asm = ir_to_arm64(codeIR, env)
    prog = arm64_final_prog(arm_64_asm, env, stack_input_for_print=codeIR)
    if PRINT_GENERATED_ASM_CODE:
        _printStackCode(prog)
    _writeProgToFile(prog)
    print_final_env(env)


def load_file(base_file_name_in_code_dir, ir=False):
    print(f"\nDIR: {Configs.GENERATED_DIR.value}")
    print(f"Name:   {base_file_name_in_code_dir}.s\n")
    setBaseName(base_file_name_in_code_dir)
    data = _readFromFile(base_file_name_in_code_dir + ".incc")
    return data


def print_ast(ast):
    ast_string = str(ast)
    x = ast_string.replace("((", "((\n")
    x = x.replace("))", "))\n")
    print(x)


def compileFileFromCodeFolderBaseName(fname, env):
    data = load_file(fname)
    if PRINT_FILE_DATA:
        print(data)
    ast = PARSER_FINAL.parse(data)
    if PRINT_GENERATED_AST:
        print_ast(ast)

    compiler_ast(ast, env)
def execute_make_for_file_name(fname):
    import subprocess
    cmd = ["make", 
           "-C", f"{Configs.GENERATED_DIR.value}", 
           "-f", "~/.config/asm_Makefile",  
           f"FILE_PATH={Configs.GENERATED_DIR.value}/{fname}"]
    run = subprocess.run(cmd, capture_output=True)
    print(f"RUN PROGRAM for file: {fname}")
    print(run.stderr.decode())
    print(run.stdout.decode())

def run():
    # FILE_NAME = "seq_multi"
    # # FILE_NAME="assign_multi"
    # # FILE_NAME="compare"
    # FILE_NAME = "cond"
    # FILE_NAME = "cond2"
    # FILE_NAME = "while"
    # FILE_NAME = "a"
    FILE_NAME = getFileNameFromcodeTX()[0]
    print(FILE_NAME)

    compileFileFromCodeFolderBaseName(FILE_NAME, Configs.ENV.value)
    execute_make_for_file_name(FILE_NAME)


if __name__ == "__main__":
    run()
