# from incc.compiler.cma import arith_expr
from configs import Configs
from incc.compiler.cma.arm64_helper import l, t
from incc.compiler.cma.gen_ir import code_r
from incc.compiler.cma.gen_arm import arm64_final_prog, ir_to_arm64

# BASE_NAME = ""


def setBaseName(bname):
    global BASE_NAME
    BASE_NAME = bname


def _readFromFile(code_file,dir_load_file=Configs.CODE_DIR.value):
    with open(f"{dir_load_file}/{code_file}") as f:
        data = str(f.read())
        f.close()
        return str.strip(data)


def _printIRCode(stack_code):
    print("============IR-CODE==========>>>\n")
    print(stack_code)
    print("============IR-CODE==========<<<")


def _printStackCode(prog):
    print("======GENERATED:ASM-CODE======>>>")
    print(prog)
    print("======GENERATED:ASM-CODE======<<<")


def _writeCodeIRToFile(codeIR):
    f = open(f"{Configs.GENERATED_IR_CODE_DIR.value}/{BASE_NAME}.ir", "w")
    f.write(codeIR)
    f.close()


def _writeProgToFile(prog):
    f = open(f"{Configs.GENERATED_DIR.value}/{BASE_NAME}.s", "w")
    f.write("; ASM_FILE:\n")
    f.write(f"; {BASE_NAME}\n")
    f.write(prog)
    f.close()


def compiler_ast(ast, env):
    # codeIR = ast.code(env)
    codeIR = code_r(ast, env)
    _printIRCode(codeIR)
    _writeCodeIRToFile(codeIR)
    arm_64_asm = ir_to_arm64(codeIR, env)
    prog = arm64_final_prog(arm_64_asm, "")
    _printStackCode(prog)
    _writeProgToFile(prog)
    print(env)


def compile_data_PARSER_FINAL(data, PARSER_FINAL):
    env = {}
    ast = PARSER_FINAL.parse(input=data)
    codeIR = ast.code(env)
    _printIRCode(codeIR)
    _writeCodeIRToFile(codeIR)
    arm_64_asm = ir_to_arm64(codeIR, env)
    prog = arm64_final_prog(arm_64_asm, "")
    _printStackCode(prog)
    _writeProgToFile(prog)
    print(env)


def compile_file(base_file_name_in_code_dir, PARSER_FINAL):
    print(f"\nDIR: {Configs.GENERATED_DIR.value}")
    print(f"Name:   {base_file_name_in_code_dir}.s\n")

    data = _readFromFile(base_file_name_in_code_dir + ".incc")
    compile_data_PARSER_FINAL(data, PARSER_FINAL)
