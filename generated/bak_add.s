; ASM_FILE:
; add
.text
	.global main
	.align	2

main:
	stp FP, LR, [sp, -0x10]!;epilogue

;==============================
;========STACK_MACHINE=========
;==============================
;										==loadc 1
	mov x0, #1
;										====push
	str	x0, [SP, #-16]!
;										==loadc 2
	mov x0, #2
;										====push
	str	x0, [SP, #-16]!
;										==add
	ldr x1, [sp], #16
	ldr x2, [sp], #16
	add  x0, x1, x2
;										====push
	str	x0, [SP, #-16]!
;==============================
;========STACK_MACHINE=========
;==============================

	ldr x0, [sp], #16
	str x0, [sp]
	adrp x0, FinalResult@PAGE
	add x0, x0, FinalResult@PAGEOFF
	bl _printf
	ldp FP, LR, [sp], 0x10;prologue:

	mov x0, #0
	ret
.data
FinalResult: .asciz "FinalResult: %d \n"
HelperResult: .asciz "HelperResult: %d \n"
