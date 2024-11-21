; ASM_FILE:
; proc1
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
	b endproc_0;jump
proc_0:
sub x7, x20, fp;						enter
mov fp, x7;						enter
	ldr x0, [sp], #16; ;				pop
	stp x0, x0, [SP, #-16]!;				push
	mov x0, #1234
	stp x0, x0, [SP, #-16]!;				push
;>>>>>>>>>>>LOADRC=================
	mov x0, -32
	add x0, x0, fp
	stp x0, x0, [SP, #-16]!;				push
;=================LOADRC<<<<<<<<<<<
;>>>>>>>>>>>STORE===========
	ldr x1, [sp], #16;						pop
	ldr x0, [sp], #16;						pop
	mov x7, x20;			  SPBase(x20) into x7
	sub x7, x7, x1;			Add calced address to SPBase
	stp x0,x0, [x7];				push
	stp x0, x0, [SP, #-16]!;				push
;===========STORE<<<<<<<<<<<
	ldr x0, [sp], #16; ;				pop
	ldr x0, [sp], #16; ;				pop
mov fp, x0
ret
endproc_0:
adr x0, proc_0
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
	mov x0, FP; IR:mark
	stp x0, x0, [SP, #-16]!;				push
	mov x0, #0
	stp x0, x0, [SP, #-16]!;				push
;>>>>>>>>>>>LOAD============
	ldr x0, [sp], #16; ;				pop
	mov x7, x20;			  SPBase(x20) into x7
	sub x7, x7, x0;			Add calced address to SPBase
	ldr x0, [x7];					push
	stp x0, x0, [SP, #-16]!;				push
;============LOAD<<<<<<<<<<<
	ldr x0, [sp], #16; ;				pop
blr x0; adds old addr of sp on stack?!?
	ldr x0, [sp], #16; ;				pop
	ldr x0, [sp], #16; ;				pop
add sp, sp, 32
	stp x0, x0, [SP, #-16]!;				push
;==============================
;========STACK_MACHINE=========
;==============================

	adrp x0, FinalResult@PAGE
	add x0, x0, FinalResult@PAGEOFF
	bl _printf
	adrp x0, IR@PAGE
	add x0, x0, IR@PAGEOFF
	bl _printf

	ldr x0, [SP], #16; remove last item from STACK; is this CORRECT???
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
jump endproc_0
label proc_0
enter
alloc 0
loadc 1234
loadrc -32
store
pop
return
label endproc_0
load_addr_label proc_0
loadc 0
store
pop
mark
loadc 0
load
call
pop
slide -1 1
=========IR-CODE===========
"
;inside STACK_MACHINE: push(+)/pop(-) count = -3
