; ASM_FILE:
; while
.text
	.global main
	.align	2

main:
;Add for sanity_checks
	mov x0, #1993
	mov x1, #1111
	mov x2, #2222
	mov x3, #3333
	mov x4, #4444
	mov x5, #5555
	mov x6, #6666
	mov x7, #7777
	mov x20, sp; x20 as BottomStackPointer
	sub sp, sp, #16; x20 as BottomStackPointer
	stp FP, LR, [sp, -0x10]!;epilogue

;==============================
;========STACK_MACHINE=========
;==============================
	mov x0, #0
	str	x0, [SP, #-16]!;push!
	mov x0, #16
	str	x0, [SP, #-16]!;push!
;==============>>>>>>>>>>>STORE-GLOBAL===========
	ldr x1, [sp], #16
	ldr x0, [sp], #16
	mov x7, x20;			  SPBase(x20) into x7
	sub x7, x7, x1;			Add calced address to SPBase
	str x0, [x7];			  load lvalue in rvalue
	str	x0, [SP, #-16]!;push!
;==============<<<<<<<<<<<STORE-GLOBAL===========
	ldr x0, [sp], #16; POP!!!!!!!
while_start_0:
	mov x0, #16
	str	x0, [SP, #-16]!;push!
;==============>>>>>>>>>>>LOAD-GLOBAL============
	ldr x0, [sp], #16; POP!!!!!!!
	mov x7, x20;			  SPBase(x20) into x7
	sub x7, x7, x0;			Add calced address to SPBase
	ldr x0, [x7];			  load lvalue in rvalue
	str	x0, [SP, #-16]!;push!
;==============<<<<<<<<<<<LOAD-GLOBAL============
	mov x0, #10
	str	x0, [SP, #-16]!;push!
	ldr x2, [sp], #16
	ldr x1, [sp], #16
	subs xzr, x1, x2
	CSET x0, lt
	CSET x1, eq
	add x0, x0, x1
	str	x0, [SP, #-16]!;push!
	cbz x0, while_end_0
	mov x0, #16
	str	x0, [SP, #-16]!;push!
;==============>>>>>>>>>>>LOAD-GLOBAL============
	ldr x0, [sp], #16; POP!!!!!!!
	mov x7, x20;			  SPBase(x20) into x7
	sub x7, x7, x0;			Add calced address to SPBase
	ldr x0, [x7];			  load lvalue in rvalue
	str	x0, [SP, #-16]!;push!
;==============<<<<<<<<<<<LOAD-GLOBAL============
	mov x0, #1
	str	x0, [SP, #-16]!;push!
	ldr x2, [sp], #16
	ldr x1, [sp], #16
	add x0, x1, x2
	str	x0, [SP, #-16]!;push!
	mov x0, #16
	str	x0, [SP, #-16]!;push!
;==============>>>>>>>>>>>STORE-GLOBAL===========
	ldr x1, [sp], #16
	ldr x0, [sp], #16
	mov x7, x20;			  SPBase(x20) into x7
	sub x7, x7, x1;			Add calced address to SPBase
	str x0, [x7];			  load lvalue in rvalue
	str	x0, [SP, #-16]!;push!
;==============<<<<<<<<<<<STORE-GLOBAL===========
	ldr x0, [sp], #16; POP!!!!!!!
	b while_start_0
while_end_0:
;==============================
;========STACK_MACHINE=========
;==============================

	adrp x0, FinalResult@PAGE
	add x0, x0, FinalResult@PAGEOFF
	bl _printf
	add sp, sp, 0x10; move pointer back to top stack item + print removes it
	adrp x0, IR@PAGE
	add x0, x0, IR@PAGEOFF
	bl _printf

	ldp FP, LR, [sp], 0x10;prologue:

	;===Local Vars, remove!
	add sp, sp, #16; x20 as BottomStackPointer
	mov x0, #0
	ret
.data
FinalResult: .asciz "FinalResult: %d \n"
HelperResult: .asciz "HelperResult: %d \n"
.data
IR: .asciz "
=========IR-CODE===========
loadc 0
loadc 16
store
pop
label while_start_0
loada 16
loadc 10
leq
jumpz while_end_0
loada 16
loadc 1
add
loadc 16
store
pop
jump while_start_0
label while_end_0
=========IR-CODE===========
"
