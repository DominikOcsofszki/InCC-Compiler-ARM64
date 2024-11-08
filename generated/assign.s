; ASM_FILE:
; assign
.text
	.global main
	.align	2

main:
	mov x20, sp; x20 as BottomStackPointer
	stp FP, LR, [sp, -0x10]!;epilogue

;==============================
;========STACK_MACHINE=========
;==============================
;										==loadc 1
	mov x0, #1
;										====push
	str	x0, [SP, #-16]!
;==============================
;========STACK_MACHINE=========
;==============================

	str x0, [sp];;print_x0 ;Change Configs to use x0 or stack-item as result print
	adrp x0, FinalResult@PAGE
	add x0, x0, FinalResult@PAGEOFF
	bl _printf
	adrp x0, IR@PAGE
	add x0, x0, IR@PAGEOFF
	bl _printf
	ldp FP, LR, [sp], 0x10;prologue:

	;===At this point:sp ==x20  else wrong!
	;mov sp, x20; prologue: restore sp from x20
	mov x0, #0
	ret
.data
FinalResult: .asciz "FinalResult: %d \n"
HelperResult: .asciz "HelperResult: %d \n"
.data
IR: .asciz "
=========IR-CODE===========
loadc 1
=========IR-CODE===========
"
