from .enum_ast import Ast
from .arm64_helper import l, t
from configs import SK, Configs
from icecream import ic

GLOBAL_AS_STACK_SIZE = 0

COUNT_LABELS = 0
STACK_SIZE_ARM = Configs.STACK_SIZE_ARM.value


def unique_labels(*labels):
    global COUNT_LABELS
    results = []
    for label in labels:
        results.append(label + "_" + str(COUNT_LABELS))
    COUNT_LABELS = COUNT_LABELS + 1
    return results


def new_global__addr():
    global GLOBAL_AS_STACK_SIZE
    ret = GLOBAL_AS_STACK_SIZE * STACK_SIZE_ARM
    GLOBAL_AS_STACK_SIZE = GLOBAL_AS_STACK_SIZE + 1
    return "" + str(ret)

# def new_global__addr(size_in_arm_stack_size_later_byx):
#     global GLOBAL_AS_STACK_SIZE
#     ret = (GLOBAL_AS_STACK_SIZE + size_in_arm_stack_size_later_byx) * STACK_SIZE_ARM
#     GLOBAL_AS_STACK_SIZE = GLOBAL_AS_STACK_SIZE + 1
#     return "" + str(ret)


def setup_local_vars(local_vars, env: SK):
    local_var_addr = STACK_SIZE_ARM  # ARM64/MAC always uses 16 for stack
    for local_var_name in local_vars:
        info = {"addr": local_var_addr,
                "scope": "local", "size": 8, "POS": [0]}
        env.set_local_var(local_var_name, info)
        local_var_addr += STACK_SIZE_ARM


def setup_local_args(local_args, env):
    local_arg_addr = -STACK_SIZE_ARM * 2  # ARM64/MAC always uses 16 for stack
    for local_arg_name in local_args:
        info = {"addr": local_arg_addr,
                "scope": "local", "size": 8, "POS": [0]}
        env.set_local_var(local_arg_name, info)
        local_arg_addr -= STACK_SIZE_ARM


def code_r(node, env: SK):
    ret = ""
    match node:
        case (Ast.PROC_CALL.value, (addr_id), (args)):
            for arg in args[::-1]:
                ret += code_r(arg, env)
            ret += l("mark")
            ret += code_l(("variable", addr_id), env)
            ret += l("load")
            # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<-----------------call jumpto label
            ret += l("call")
            ret += l("pop")
            ret += l(f"slide {len(args)-1} 1")

        case (Ast.PROC.value, args, local_vars, body):
            proc_label, end_proc_label = unique_labels("proc", "endproc")
            ret += l(f"jump {end_proc_label}")
            # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<---call jumpto here
            ret += l(f"label {proc_label}")
            ret += l("enter")
            # TODO: here we add item for the callee
            # CALEE_ENTER>>>
            setup_local_vars(local_vars, env)
            setup_local_args(args, env)
            # TODO: use this in future, calc here, instead of ir_to_arm
            # ret += l(f"alloc {len(local_vars)*STACK_SIZE_ARM}")
            ret += l(f"alloc {len(local_vars)}")
            # CALEE_ENTER<<<
            ret += code_r(body, env)
            # CALEE_EXIT>>>
            ret += l(f"loadrc {-2*STACK_SIZE_ARM}")
            ret += l(f"store")
            ret += l(f"pop")

            # CALEE_EXIT<<<
            ret += l("return")
            ret += l(f"label {end_proc_label}")
            # print(proc_label)
            # ret += l("loadc {proc_label}"),
            ret += l(f"load_addr_label {proc_label}")

            env.reset_locals()
            env.print_all()

        # USE IDs as functiosn => hack for now, remove later!
        case (Ast.ID, Ast.PRINT_STACK_5.value,):
            ret += l("print_stack_5")

        case (Ast.WHILE.value, cond, body):
            while_start, while_end = unique_labels("while_start", "while_end")
            ret += l(f"label {while_start}")
            ret += code_r(cond, env)
            ret += l(f"jumpz {while_end}")
            ret += code_r(body, env)
            ret += l(f"jump {while_start}")
            ret += l(f"label {while_end}")
            # print(cond)
            # print(body)
            # print(ret)
            # exit()

        case (Ast.IF_THEN_ELSE.value, cond, body, else_body):
            ite, ite_else, ite_end = unique_labels(
                "ite", "ite_else", "ite_end")
            ret += l(f"label {ite}")
            ret += code_r(cond, env)
            ret += l(f"jumpz {ite_else}")
            ret += code_r(body, env)
            ret += l(f"jump {ite_end}")
            ret += l(f"label {ite_else}")
            if else_body:
                ret += code_r(else_body, env)
            ret += l(f"label {ite_end}")

        case (Ast.BINARY_COMPARE.value, op, local_var, y):
            op_val = ""
            match op:
                case "<":
                    op_val = "le"
                case ">":
                    op_val = "gr"
                case "<=":
                    op_val = "leq"
                case ">=":
                    op_val = "geq"
                case "==":
                    op_val = "eq"
                case "!=":
                    op_val = "neq"
            ret = code_r(local_var, env) + code_r(y, env) + op_val

        # case ("load", var_name):
        case (Ast.ID.value, var_name):
            ret += code_l(('variable', var_name), env)
            ret += l('load')

        case (Ast.SEQUENCE.value, (seq)):
            for line in seq[:-1]:
                ret += code(line, env)
            ret += code_r(seq[-1], env)

        case ("number", local_var):
            ret = f"loadc {local_var}"

        case (Ast.BINARY_OPERATOR.value, op, local_var, y):
            ret = code_r(local_var, env) + code_r(y, env)
            match op:
                case "+":
                    ret += "add"
                case "*":
                    ret += "mul"
                case "/":
                    ret += "sdiv"
                case "-":
                    ret += "sub"

        case (Ast.ASSIGN.value, ("variable", local_var) as var, val):
            if not env.in_globals(local_var):
                info = {
                    # "addr": new_global__addr(size_in_arm_stack_size_later_byx=1),
                    "addr": new_global__addr(),
                    "scope": "global",
                    "size": 8,
                    "POS": [0],
                }
                env.set_global_var(local_var, info)
            else:
                env.update_global_POS(local_var)
            ret += code_r(val, env) + code_l(var, env) + "store"
            ic(env)

        case _:
            raise Exception(
                l(
                    f"code_r uninplemented for node:  {
                        node} <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
                )
            )

    return ret + "\n" if ret[-1] != "\n" else ret


def code(node, env: SK):
    return code_r(node, env) + "pop" + "\n"


def code_l(node, env: SK):
    ret = ""
    match node:
        case ("variable", var_name):
            if env.in_locals(var_name):
                ret = f'loadrc {env.get_local_addr(var_name)}'
            elif env.in_globals(var_name):
                ret = f'loadc {env.get_global_addr(var_name)}'
                # TODO: always load global if cant find local?
            else:
                raise Exception("Wrong arg in type")
        case _:
            raise Exception(f"code_l uninplemented, node: {node}")
    return ret + "\n" if ret[-1] != "\n" else ret
