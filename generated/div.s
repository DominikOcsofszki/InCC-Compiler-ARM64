; ASM_FILE:
; div
.text
	.global main
	.align	2

main:
	stp FP, LR, [sp, -0x10]!;epilogue

;==============================
;========STACK_MACHINE=========
;==============================
;										==loadc 6
	mov x0, #6
;										====push
	str	x0, [SP, #-16]!
;										==loadc 3
	mov x0, #3
;										====push
	str	x0, [SP, #-16]!
;										==div
	ldr x1, [sp], #16
	ldr x2, [sp], #16
	sdiv  x0, x2, x1
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
	adrp x0, IR@PAGE
	add x0, x0, IR@PAGEOFF
	bl _printf
	ldp FP, LR, [sp], 0x10;prologue:

	mov x0, #0
	ret
.data
FinalResult: .asciz "FinalResult: %d \n"
HelperResult: .asciz "HelperResult: %d \n"
.data
IR: .asciz "
=========IR-CODE===========
loadc 6
loadc 3
div
=========IR-CODE===========
"
