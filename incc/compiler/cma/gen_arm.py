# INFO: Linked from /Users/dominik/HOME/DEV/Compiler/incc24/dom/arm/incc/compiler/cma/ir_to_arm64.py
import re

from configs import Configs
from .gen_ir import STACK_SIZE_ARM

from .arm64_helper import arm64_final, arm64_prefix, l, t, POP_COUNT, PUSH_COUNT, GET_COUNTER
from .enum_ast import Ast
ADD_COMMENTS_IR_TO_ARM_EACH_LINE = Configs.ADD_COMMENTS_IR_TO_ARM_EACH_LINE.value


def c(txt):
    if ADD_COMMENTS_IR_TO_ARM_EACH_LINE:
        return l(txt)
    return ''


COUNT_FOR_PRINT_IN_IR = 1


def ir_to_arm64(cma_code, env):
    code = ""
    global COUNT_FOR_PRINT_IN_IR
    print_em = "=="*COUNT_FOR_PRINT_IN_IR
    COUNT_FOR_PRINT_IN_IR = COUNT_FOR_PRINT_IN_IR+1

    # print(cma_code)
    for line in cma_code.splitlines():
        # <<< print each lines with info
        code += c(f";\t\t\t\t\t\t\t\t\t\t{print_em}{line}")
        match re.split("[,\\s]+", line):
            case ['enter']:
                code += l(f"sub x7, x20, fp;\t\t\t\t\t\tenter")
                code += l(f"mov fp, x7;\t\t\t\t\t\tenter")

            case ['slide', x1, x2]:
                remove_from_stack = int(x2)-int(x1)
                code += ir_to_arm64('pop', env)
                code += l(f'add sp, sp, {remove_from_stack*STACK_SIZE_ARM}')
                for _ in range(remove_from_stack):
                    code += POP_COUNT()
                code += ir_to_arm64('push', env)

            case ['load_addr_label', label_name]:
                code += l(f'adr x0, {label_name}')
                code += ir_to_arm64('push', env)

            case ['return']:
                code += ir_to_arm64('pop', env)
                code += l('mov fp, x0')
                code += l('ret')
            case ['alloc', len_local_vars]:
                # TODO: change it to calc the values before alling alloc
                # code += l(f"sub sp, {len_local_vars}")
                code += ir_to_arm64('pop', env)
                code += ir_to_arm64('push', env)
                for _ in range(int(len_local_vars)):
                    # code += l(";len_local_vars")
                    code += ir_to_arm64('push', env)
            case ['call']:
                code += ir_to_arm64('pop', env)
                code += l(f"blr x0; adds old addr of sp on stack?!?")
                # code += ir_to_arm64('push',env)
            case ['mark']:
                code += t("mov x0, FP; IR:mark")
                # code += t("mov FP, x0; IR:mark")
                code += ir_to_arm64('push', env)
            case ['label', label_name]:
                code += l(label_name+":")

            case ['print_stack_5']:
                code += t("adrp x0, StackItems_5@PAGE")
                code += t("add x0, x0, StackItems_5@PAGEOFF")
                code += ir_to_arm64('push', env)
                code += t("bl _printf")

            # case ['while']:
            #    code += ""
            # case [AST_ENUM.AST_while_start.value]:
            #     code += ""
            # case [AST_ENUM.AST_while_end.value]:
            #     code += ""
            case ['dup']:                # case '<=': ret +=  'leq'
                code += ir_to_arm64('pop', env)
                code += ir_to_arm64('push', env)
                code += ir_to_arm64('push', env)
            case ['swap']:                # case '<=': ret +=  'leq'
                code += ir_to_arm64('popx2x1', env)
                code += t("str	x1, [SP, #-16]!;\t\t\t\t\tpush")
                PUSH_COUNT()

                code += t("str	x2, [SP, #-16]!;\t\t\t\t\tpush")
                PUSH_COUNT()

            case ['add' | 'mul' | 'sub' | 'sdiv' as bin_op]:
                code += ir_to_arm64("popx2x1", env)
                code += t(f'{bin_op} x0, x1, x2 ;\t\t\t\t\t\t{bin_op}')
                code += ir_to_arm64("push", env)

# LABEL ++!
            case ['jumpz', label]:                # case '<=': ret +=  'leq'
                code += ir_to_arm64('pop', env)
                code += t(f"cbz x0, {label};jumpz")
            case ['jump', label]:                # case '<=': ret +=  'leq'
                code += t(f"b {label};jump")

            case ['loada', addr]:
                code += ir_to_arm64(f'loadc {addr}',
                                    env) + ir_to_arm64('load', env)

            # case ['storerc'] :
            #     code += l(";>>>>>>>>>>>LOADRC=================")
            #     code += ir_to_arm64("pop",env)
            #     # code += t(f"mov x0, {addr_offset}")
            #     code += t("mov x7, FP")
            #     code += t("sub x7, x7, x0")
            #     code += t("ldr x0, [x7]")
            #     code += ir_to_arm64("push",env)
            #     code += l(";=================LOADRC<<<<<<<<<<<")
            case ['loadrc', addr_offset]:
                code += l(";>>>>>>>>>>>LOADRC=================")
                # code += ir_to_arm64("pop",env)
                code += t(f"mov x0, {addr_offset}")
                code += t("add x0, x0, fp")
                # code += t("sub x7, x20, fp")
                # code += t("mov x7, FP")
                # code += t("sub x0, x7, x0")
                # code += t("ldr x0, [x7]")
                code += ir_to_arm64("push", env)
                code += l(";=================LOADRC<<<<<<<<<<<")
            case ['load']:
                code += l(";>>>>>>>>>>>LOAD============")
                code += ir_to_arm64("pop", env)
                code += t("mov x7, x20;\t\t\t  SPBase(x20) into x7")
                code += t("sub x7, x7, x0;\t\t\tAdd calced address to SPBase")
                code += t("ldr x0, [x7];\t\t\t\t\tpush")
                code += ir_to_arm64("push", env)
                code += l(";============LOAD<<<<<<<<<<<")
            case ['store']:
                code += l(";>>>>>>>>>>>STORE===========")
                # code += ir_to_arm64("popx1x0",env)
                code += t("ldr x1, [sp], #16;\t\t\t\t\t\tpop")
                POP_COUNT()
                code += t("ldr x0, [sp], #16;\t\t\t\t\t\tpop")
                POP_COUNT()
                code += t("mov x7, x20;\t\t\t  SPBase(x20) into x7")
                code += t("sub x7, x7, x1;\t\t\tAdd calced address to SPBase")
                # code += t("str x0, [x7];\t\t\t  load lvalue in rvalue")
                code += t("stp x0,x0, [x7];\t\t\t\tpush")
                code += ir_to_arm64("push", env)
                code += l(";===========STORE<<<<<<<<<<<")

                # code += ir_to_arm64("pop", env)
            case ['push']:
                # code += t("str	x0, [SP, #-16]!;push!")
                code += t("stp x0, x0, [SP, #-16]!;\t\t\t\tpush")
                PUSH_COUNT()

            case ['popx2x1']:
                code += t("ldr x2, [sp], #16;\t\t\t\tpush")
                POP_COUNT()
                code += t("ldr x1, [sp], #16;\t\t\t\tpush")
                POP_COUNT()

            case ['pop']:
                code += t("ldr x0, [sp], #16; ;\t\t\t\tpop")
                POP_COUNT()

            case ['loadc', q]:
                code += t(f'mov x0, #{str(q)}')
                code += ir_to_arm64("push", env)

            case ['leq']:                # case '<=': ret +=  'leq'
                code += ir_to_arm64("_cmp_x1_x2", env)
                code += t('CSET x0, lt')
                code += t('CSET x1, eq')
                code += t('add x0, x0, x1')
                code += ir_to_arm64("push", env)
            case ['geq']:                # case '>=': ret +=  'geq'
                code += ir_to_arm64("_cmp_x1_x2", env)
                code += t('CSET x0, gt')
                code += t('CSET x1, eq')
                code += t('add x0, x0, x1')
                code += ir_to_arm64("push", env)

            case ['gr']:                # case '>':  ret += 'gr'
                code += ir_to_arm64("_cmp_x1_x2", env)
                code += t('CSET x0, gt')
                code += ir_to_arm64("push", env)
            case ['neq']:                # case '!=': ret +=  'neq'
                code += ir_to_arm64("_cmp_x1_x2", env)
                code += t('CSET x0, ne')
                code += ir_to_arm64("push", env)
            case ['eq']:                # case '==': ret +=  'eq'
                code += ir_to_arm64("_cmp_x1_x2", env)
                code += t('CSET x0, eq')
                code += ir_to_arm64("push", env)
            case ['le']:                # case '<':  ret += 'le'
                code += ir_to_arm64("_cmp_x1_x2", env)
                code += t('CSET x0, lt')
                code += ir_to_arm64("push", env)

            case ['_cmp_x1_x2']:
                code += ir_to_arm64("popx2x1", env)
                code += t('subs xzr, x1, x2')

            case [*unknown]:
                code += l(f'Error: unknown CMa statement {
                          unknown}<<<<<<<<<<<<<<<<<<<=========')

    COUNT_FOR_PRINT_IN_IR = COUNT_FOR_PRINT_IN_IR-1
    # print(Global_Init)
    return code


def _print_ir_if_configs(stack_input_for_print):
    SHOW_IR_IN_ASM = Configs.SHOW_IR_IN_ASM.value
    program = ''
    if SHOW_IR_IN_ASM:
        program = l(".data")
        program += l(f'IR: .asciz "\n=========IR-CODE===========\n{
                     stack_input_for_print}=========IR-CODE===========\n"')
    return program


def arm64_final_prog(arm64_code, env, stack_input_for_print=None):
    program = arm64_prefix(env)
    program += l(";==============================")
    program += l(";========STACK_MACHINE=========")
    program += l(";==============================")
    program += arm64_code
    program += l(";==============================")
    program += l(";========STACK_MACHINE=========")
    program += l(";==============================")
    program += arm64_final(env)
    program += _print_ir_if_configs(stack_input_for_print)
    program += l(f";inside STACK_MACHINE: push(+)/pop(-) count = {
                 GET_COUNTER()}")
    return program
