# # INFO: Linked from /Users/dominik/HOME/DEV/Compiler/incc24/dom/arm/incc/compiler/cma/arm64_helper.py
#
# from configs import SK, Configs
# DATA_PRINT_1 = "FinalResult"
# DATA_PRINT_2 = "HelperResult"
# DATA_STACKITEMS = "StackItems"
# DATA_STACKITEMS_5 = "StackItems_5"
# DATA_PRINT_IR = "IR"
#
# def l(line):
#     return f'{line}\n'
# def t(line):
#     return f'\t{line}\n'
#
# def nr_global_vars(env:SK):
#     return env.nr_global_vars()
# def total_size(nr_of_vars):
#     return nr_of_vars * Configs.STACK_SIZE_ARM.value
#
# def sanity_checks(env):
#     program = ''
#     if True:
#         program += l(";Add for sanity_checks")
#         program += t("mov x0, 0x1993")
#         program += t("mov x1, 0x1111")
#         program += t("mov x2, 0x2222")
#         program += t("mov x3, 0x3333")
#         program += t("mov x4, 0x4444")
#         program += t("mov x5, 0x5555")
#         program += t("mov x6, 0x6666")
#         program += t("mov x7, 0x7777")
#
#     return program
#
#
# def arm64_prefix(env):
#     program = l(".text")
#     program += t(".global main")
#     program += t(".align\t2")
#     program += l("")
#     program += l("main:")
#     program += sanity_checks(env)
#     program += arm64_proloque_(env)
#     return program
#
#
# def print_stack_item(env):
#     program = ""
#     program += t(f"adrp x0, {DATA_PRINT_1}@PAGE")
#     program += t(f"add x0, x0, {DATA_PRINT_1}@PAGEOFF")
#     program += t("bl _printf")
#     program += t(f"add sp, sp, 0x10; move pointer back to top stack item + print removes it")
#     return program
#
# def print_last_item_on_stack(env):
#     program = ""
#     program += t(f"adrp x0, {DATA_PRINT_1}@PAGE")
#     program += t(f"add x0, x0, {DATA_PRINT_1}@PAGEOFF")
#     program += t("bl _printf")
#     # program += t(f"add sp, sp, 0x10; Remvoe Last Stack Item")
#     program += print_ir_if_configs(env)
#     return program
#
# def print_ir_if_configs(env):
#     SHOW_IR_IN_ASM = Configs.SHOW_IR_IN_ASM.value
#     program = ''
#     if SHOW_IR_IN_ASM:
#         program += t(f"adrp x0, {DATA_PRINT_IR}@PAGE")
#         program += t(f"add x0, x0, {DATA_PRINT_IR}@PAGEOFF")
#         program += t("bl _printf")
#     return program
#
#
# def arm64_final(env):
#     program = "\n"
#     # if True:
#     #     program += print_all_stack_items(env)
#     program += print_last_item_on_stack(env)
#     program += arm64_epiloque(env)
#
#     program += t("mov x0, #0")
#     program += t("ret")
#     program += data_part(env)
#     return program
#
#
#
# def arm64_proloque_(env):
#     total_size_global_stack  = total_size(nr_global_vars(env))
#     program = t("mov x20, sp; x20 as BottomStackPointer")
#     program += t(f"sub sp, sp, #{total_size_global_stack}; x20 as BottomStackPointer")
#     program += l(t("stp FP, LR, [sp, -0x10]!;epilogue"))
#     # print_all_stack_items(env)
#     return program
#
# def arm64_epiloque(env):
#     total_size_global_stack  = total_size(nr_global_vars(env))
#     program = l("")
#     program += t("ldr x0, [SP], #16; remove last item from STACK; is this CORRECT???")
#     program += l(t("ldp FP, LR, [sp], 0x10;arm64_epiloque:"))
#     # program += t(";===Local Vars, remove!")
#     # program += t("mov sp, x20; prologue: restore sp from x20")
#     program += t(f"add sp, sp, #{total_size_global_stack}; x20 as BottomStackPointer")
#     return program
#
# def add_x_stack_item(size):
#     size_env = size
#     p_d=""
#     for i in range(size_env):
#         p_d += f"\n{i}:\t %d  %d"
#     return p_d
#
# def data_part(env):
#     program = l(".data")
#     program += l(f'{DATA_PRINT_1}: .asciz "{DATA_PRINT_1}: %d \\n"')
#     program += l(f'{DATA_PRINT_2}: .asciz "{DATA_PRINT_2}: %d \\n"')
#     program += l(f'{DATA_STACKITEMS}: .asciz "{DATA_STACKITEMS}: {add_x_stack_item(20)} \\n"')
#     program += l(f'{DATA_STACKITEMS_5}: .asciz "{DATA_STACKITEMS_5}: {add_x_stack_item(5)} \\n"')
#     return program
#
#
# def print_all_stack_items(env, s = 20):
#     size_env = s
#     p_d=""
#     for i in range(size_env):
#         p_d += f"\n{i}:\t %d  %d"
#     program = ""
#     program += t(f"adrp x0, {DATA_STACKITEMS}@PAGE")
#     program += t(f"add x0, x0, {DATA_STACKITEMS}@PAGEOFF")
#     program += t("bl _printf")
#     return program
#
#
#
#
#
#
