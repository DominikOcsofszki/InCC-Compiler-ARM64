; ASM_FILE:
; proc0
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
	ldr x0, [sp], #16; ;				pop
	stp x0, x0, [SP, #-16]!;				push
;len_local_vars
	stp x0, x0, [SP, #-16]!;				push
;len_local_vars
	stp x0, x0, [SP, #-16]!;				push
;>>>>>>>>>>>LOADRC=================
	mov x0, -32
	add x0, x0, fp
	stp x0, x0, [SP, #-16]!;				push
;=================LOADRC<<<<<<<<<<<
;>>>>>>>>>>>LOAD============
	ldr x0, [sp], #16; ;				pop
	mov x7, x20;			  SPBase(x20) into x7
	sub x7, x7, x0;			Add calced address to SPBase
	ldr x0, [x7];					push
	stp x0, x0, [SP, #-16]!;				push
;============LOAD<<<<<<<<<<<
;>>>>>>>>>>>LOADRC=================
	mov x0, -48
	add x0, x0, fp
	stp x0, x0, [SP, #-16]!;				push
;=================LOADRC<<<<<<<<<<<
;>>>>>>>>>>>LOAD============
	ldr x0, [sp], #16; ;				pop
	mov x7, x20;			  SPBase(x20) into x7
	sub x7, x7, x0;			Add calced address to SPBase
	ldr x0, [x7];					push
	stp x0, x0, [SP, #-16]!;				push
;============LOAD<<<<<<<<<<<
	ldr x2, [sp], #16;				push
	ldr x1, [sp], #16;				push
	add x0, x1, x2 ;						add
	stp x0, x0, [SP, #-16]!;				push
;>>>>>>>>>>>LOADRC=================
	mov x0, -64
	add x0, x0, fp
	stp x0, x0, [SP, #-16]!;				push
;=================LOADRC<<<<<<<<<<<
;>>>>>>>>>>>LOAD============
	ldr x0, [sp], #16; ;				pop
	mov x7, x20;			  SPBase(x20) into x7
	sub x7, x7, x0;			Add calced address to SPBase
	ldr x0, [x7];					push
	stp x0, x0, [SP, #-16]!;				push
;============LOAD<<<<<<<<<<<
	ldr x2, [sp], #16;				push
	ldr x1, [sp], #16;				push
	add x0, x1, x2 ;						add
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
	mov x0, #16
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
	mov x0, #333
	stp x0, x0, [SP, #-16]!;				push
	mov x0, #222
	stp x0, x0, [SP, #-16]!;				push
	mov x0, #111
	stp x0, x0, [SP, #-16]!;				push
	mov x0, FP; IR:mark
	stp x0, x0, [SP, #-16]!;				push
	mov x0, #16
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

	adrp x0, StackItems@PAGE
	add x0, x0, StackItems@PAGEOFF
	bl _printf
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
StackItems: .asciz "StackItems: 
0:	 %d  %d
1:	 %d  %d
2:	 %d  %d
3:	 %d  %d
4:	 %d  %d
5:	 %d  %d
6:	 %d  %d
7:	 %d  %d
8:	 %d  %d
9:	 %d  %d
10:	 %d  %d
11:	 %d  %d
12:	 %d  %d
13:	 %d  %d
14:	 %d  %d
15:	 %d  %d
16:	 %d  %d
17:	 %d  %d
18:	 %d  %d
19:	 %d  %d \n"
StackItems_5: .asciz "StackItems_5: 
0:	 %d  %d
1:	 %d  %d
2:	 %d  %d
3:	 %d  %d
4:	 %d  %d \n"
.data
IR: .asciz "
=========IR-CODE===========
jump endproc_0
label proc_0
alloc 2
loadrc -32
load
loadrc -48
load
add
loadrc -64
load
add
loadrc -32
store
pop
return
label endproc_0
load_addr_label proc_0
loadc 16
store
pop
loadc 333
loadc 222
loadc 111
mark
loadc 16
load
call
pop
slide 3 1
=========IR-CODE===========
"
;inside STACK_MACHINE: push(+)/pop(-) count = 2
