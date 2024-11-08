; ASM_FILE:
; assign_multi
.text
	.global main
	.align	2

main:
	mov x20, sp; x20 as BottomStackPointer
	sub sp, sp, #32; x20 as BottomStackPointer
	stp FP, LR, [sp, -0x10]!;epilogue

;==============================
;========STACK_MACHINE=========
;==============================
;										==loadc 1
	mov x0, #1
;										====push
	str	x0, [SP, #-16]!
;										==loadc 16
	mov x0, #16
;										====push
	str	x0, [SP, #-16]!
;										==store
;====ADD-GLOBAL==================================================>>>>>>>>>>>
;										====popx2x1
	ldr x2, [sp], #16
	ldr x1, [sp], #16
	mov x7, x20;			SPBase(x20) into x7
	sub x7, x7, x2;			Add calced address to SPBase
	str	x1, [x7];			load lvalue in rvalue
;====END-GLOBAL==================================================>>>>>>>>>>>
;										==pop
	ldr x0, [sp], #16
;										==loadc 2
	mov x0, #2
;										====push
	str	x0, [SP, #-16]!
;										==loadc 32
	mov x0, #32
;										====push
	str	x0, [SP, #-16]!
;										==store
;====ADD-GLOBAL==================================================>>>>>>>>>>>
;										====popx2x1
	ldr x2, [sp], #16
	ldr x1, [sp], #16
	mov x7, x20;			SPBase(x20) into x7
	sub x7, x7, x2;			Add calced address to SPBase
	str	x1, [x7];			load lvalue in rvalue
;====END-GLOBAL==================================================>>>>>>>>>>>
;==============================
;========STACK_MACHINE=========
;==============================

;print_item_on_stack; Change Configs to use x0 or stack-item as result print
	adrp x0, FinalResult@PAGE
	add x0, x0, FinalResult@PAGEOFF
	bl _printf
	adrp x0, IR@PAGE
	add x0, x0, IR@PAGEOFF
	bl _printf

	ldp FP, LR, [sp], 0x10;prologue:

	;===Local Vars, remove!
	add sp, sp, #32; x20 as BottomStackPointer
	mov x0, #0
	ret
.data
FinalResult: .asciz "FinalResult: %d \n"
HelperResult: .asciz "HelperResult: %d \n"
.data
IR: .asciz "
=========IR-CODE===========
loadc 1
loadc 16
store
pop
loadc 2
loadc 32
store
=========IR-CODE===========
"
