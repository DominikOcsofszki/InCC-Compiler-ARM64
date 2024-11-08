; ASM_FILE:
; compare
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
	sub sp, sp, #0; x20 as BottomStackPointer
	stp FP, LR, [sp, -0x10]!;epilogue

;==============================
;========STACK_MACHINE=========
;==============================
	mov x0, #111
	str	x0, [SP, #-16]!
	mov x0, #111
	str	x0, [SP, #-16]!
	ldr x2, [sp], #16
	ldr x1, [sp], #16
	subs xzr, x1, x2
	CSET x0, gt
	CSET x1, eq
	add x0, x0, x1
	str	x0, [SP, #-16]!
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
	add sp, sp, #0; x20 as BottomStackPointer
	mov x0, #0
	ret
.data
FinalResult: .asciz "FinalResult: %d \n"
HelperResult: .asciz "HelperResult: %d \n"
.data
IR: .asciz "
=========IR-CODE===========
loadc 111
loadc 111
geq
=========IR-CODE===========
"
