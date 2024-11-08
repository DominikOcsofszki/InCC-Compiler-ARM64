; ASM_FILE:
; cond
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
	mov x0, #777
	str	x0, [SP, #-16]!;push!
	mov x0, #111
	str	x0, [SP, #-16]!;push!
	ldr x2, [sp], #16
	ldr x1, [sp], #16
	subs xzr, x1, x2
	CSET x0, lt
	str	x0, [SP, #-16]!;push!
ite:
	ldr x0, [sp], #16; POP!!!!!!!
	cbz x0, else
then:
	mov x0, #123
	str	x0, [SP, #-16]!;push!
	b endif
else:
	mov x0, #222
	str	x0, [SP, #-16]!;push!
endif:
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
loadc 777
loadc 111
le
ite
then
loadc 123
else
loadc 222
endif
=========IR-CODE===========
"
