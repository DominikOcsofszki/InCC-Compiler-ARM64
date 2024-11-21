; ASM_FILE:
; while2
.text
	.global main
	.align	2

main:
;Add for sanity_checks
	mov x0, 0x1993
	mov x1, 0x1111
	mov x2, 0x2222
	mov x3, 0x3333
	mov x4, 0x4444
	mov x5, 0x5555
	mov x6, 0x6666
	mov x7, 0x7777
	mov x20, sp; x20 as BottomStackPointer
	sub sp, sp, #16; x20 as BottomStackPointer
	stp FP, LR, [sp, -0x10]!;epilogue

;==============================
;========STACK_MACHINE=========
;==============================
	mov x0, #111
	stp x0, x0, [SP, #-16]!;				push
	mov x0, #0
	stp x0, x0, [SP, #-16]!;				push
;>>>>>>>>>>>STORE===========
	ldr x1, [sp], #16;						pop
	ldr x0, [sp], #16;						pop
	mov x7, x20;			  SPBase(x20) into x7
	sub x7, x7, x1;			Add calced address to SPBase
	stp x0,x0, [x7];				push
	stp x0, x0, [SP, #-16]!;				push
;===========STORE<<<<<<<<<<<
	ldr x0, [sp], #16; ;				pop
while_start_0:
	mov x0, #0
	stp x0, x0, [SP, #-16]!;				push
;>>>>>>>>>>>LOAD============
	ldr x0, [sp], #16; ;				pop
	mov x7, x20;			  SPBase(x20) into x7
	sub x7, x7, x0;			Add calced address to SPBase
	ldr x0, [x7];					push
	stp x0, x0, [SP, #-16]!;				push
;============LOAD<<<<<<<<<<<
	mov x0, #780
	stp x0, x0, [SP, #-16]!;				push
	ldr x2, [sp], #16;				push
	ldr x1, [sp], #16;				push
	subs xzr, x1, x2
	CSET x0, lt
	stp x0, x0, [SP, #-16]!;				push
	ldr x0, [sp], #16; ;				pop
	cbz x0, while_end_0;jumpz
	mov x0, #0
	stp x0, x0, [SP, #-16]!;				push
;>>>>>>>>>>>LOAD============
	ldr x0, [sp], #16; ;				pop
	mov x7, x20;			  SPBase(x20) into x7
	sub x7, x7, x0;			Add calced address to SPBase
	ldr x0, [x7];					push
	stp x0, x0, [SP, #-16]!;				push
;============LOAD<<<<<<<<<<<
	mov x0, #11
	stp x0, x0, [SP, #-16]!;				push
	ldr x2, [sp], #16;				push
	ldr x1, [sp], #16;				push
	add x0, x1, x2 ;						add
	stp x0, x0, [SP, #-16]!;				push
	mov x0, #0
	stp x0, x0, [SP, #-16]!;				push
;>>>>>>>>>>>STORE===========
	ldr x1, [sp], #16;						pop
	ldr x0, [sp], #16;						pop
	mov x7, x20;			  SPBase(x20) into x7
	sub x7, x7, x1;			Add calced address to SPBase
	stp x0,x0, [x7];				push
	stp x0, x0, [SP, #-16]!;				push
;===========STORE<<<<<<<<<<<
	b while_start_0;jump
while_end_0:
;==============================
;========STACK_MACHINE=========
;==============================

	adrp x0, FinalResult@PAGE
	add x0, x0, FinalResult@PAGEOFF
	bl _printf
	adrp x0, IR@PAGE
	add x0, x0, IR@PAGEOFF
	bl _printf

	ldr x0, [SP], #16; ; seems correct: Remove last item from Stack!!! for printing 
	ldp FP, LR, [sp], 0x10;arm64_epiloque:

	add sp, sp, #16; x20 as BottomStackPointer
	mov x0, #0
	ret
.data
FinalResult: .asciz "FinalResult: %d \n"
HelperResult: .asciz "HelperResult: %d \n"
.data
IR: .asciz "
=========IR-CODE===========
loadc 111
loadc 0
store
pop
label while_start_0
loadc 0
load
loadc 780
le
jumpz while_end_0
loadc 0
load
loadc 11
add
loadc 0
store
jump while_start_0
label while_end_0
=========IR-CODE===========
"
;inside STACK_MACHINE: push(+)/pop(-) count = 1
