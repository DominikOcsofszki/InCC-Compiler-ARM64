; ASM_FILE:
; xxx.s
.text
	.global main
	.align	2

main:
	stp FP, LR, [sp, -0x10]!;epilogue

;==============================
;========STACK_MACHINE=========
;==============================
;										==loadc 100
	mov x0, #100
;										====push
	str	x0, [SP, #-16]!
;										==loadc 123
	mov x0, #123
;										====push
	str	x0, [SP, #-16]!
;										==add
	ldr x1, [sp], #16
	ldr x2, [sp], #16
	add  x0, x1, x2
;										====push
	str	x0, [SP, #-16]!
;										==pop
	ldr x0, [sp], #16
;==============================
;========STACK_MACHINE=========
;==============================

	str x0, [sp]
	adrp x0, FinResult@PAGE
	add x0, x0, FinResult@PAGEOFF
	bl _printf
	ldp FP, LR, [sp], 0x10;prologue:

	mov x0, #0
	ret
.data
FinResult: .asciz "FinResult: %d \n"
HelperResult: .asciz "HelperResult: %d \n"
