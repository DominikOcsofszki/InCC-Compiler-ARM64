; ASM_FILE:
; print_stack
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
	sub sp, sp, #80; x20 as BottomStackPointer
	stp FP, LR, [sp, -0x10]!;epilogue

;==============================
;========STACK_MACHINE=========
;==============================
	mov x0, #11
	stp	x0, x0, [SP, #-16]!;push item twice, since width = 16!
	mov x0, #16
	stp	x0, x0, [SP, #-16]!;push item twice, since width = 16!
;==============>>>>>>>>>>>STORE-GLOBAL===========
	ldr x1, [sp], #16
	ldr x0, [sp], #16
	mov x7, x20;			  SPBase(x20) into x7
	sub x7, x7, x1;			Add calced address to SPBase
	stp x0,x0, [x7];			  load lvalue in rvalue; load twice since mac stack=2x
	stp	x0, x0, [SP, #-16]!;push item twice, since width = 16!
;==============<<<<<<<<<<<STORE-GLOBAL===========
	ldr x0, [sp], #16; POP!!!!!!!
	mov x0, #22
	stp	x0, x0, [SP, #-16]!;push item twice, since width = 16!
	mov x0, #32
	stp	x0, x0, [SP, #-16]!;push item twice, since width = 16!
;==============>>>>>>>>>>>STORE-GLOBAL===========
	ldr x1, [sp], #16
	ldr x0, [sp], #16
	mov x7, x20;			  SPBase(x20) into x7
	sub x7, x7, x1;			Add calced address to SPBase
	stp x0,x0, [x7];			  load lvalue in rvalue; load twice since mac stack=2x
	stp	x0, x0, [SP, #-16]!;push item twice, since width = 16!
;==============<<<<<<<<<<<STORE-GLOBAL===========
	ldr x0, [sp], #16; POP!!!!!!!
	mov x0, #33
	stp	x0, x0, [SP, #-16]!;push item twice, since width = 16!
	mov x0, #48
	stp	x0, x0, [SP, #-16]!;push item twice, since width = 16!
;==============>>>>>>>>>>>STORE-GLOBAL===========
	ldr x1, [sp], #16
	ldr x0, [sp], #16
	mov x7, x20;			  SPBase(x20) into x7
	sub x7, x7, x1;			Add calced address to SPBase
	stp x0,x0, [x7];			  load lvalue in rvalue; load twice since mac stack=2x
	stp	x0, x0, [SP, #-16]!;push item twice, since width = 16!
;==============<<<<<<<<<<<STORE-GLOBAL===========
	ldr x0, [sp], #16; POP!!!!!!!
	mov x0, #44
	stp	x0, x0, [SP, #-16]!;push item twice, since width = 16!
	mov x0, #64
	stp	x0, x0, [SP, #-16]!;push item twice, since width = 16!
;==============>>>>>>>>>>>STORE-GLOBAL===========
	ldr x1, [sp], #16
	ldr x0, [sp], #16
	mov x7, x20;			  SPBase(x20) into x7
	sub x7, x7, x1;			Add calced address to SPBase
	stp x0,x0, [x7];			  load lvalue in rvalue; load twice since mac stack=2x
	stp	x0, x0, [SP, #-16]!;push item twice, since width = 16!
;==============<<<<<<<<<<<STORE-GLOBAL===========
	ldr x0, [sp], #16; POP!!!!!!!
	mov x0, #55
	stp	x0, x0, [SP, #-16]!;push item twice, since width = 16!
	mov x0, #80
	stp	x0, x0, [SP, #-16]!;push item twice, since width = 16!
;==============>>>>>>>>>>>STORE-GLOBAL===========
	ldr x1, [sp], #16
	ldr x0, [sp], #16
	mov x7, x20;			  SPBase(x20) into x7
	sub x7, x7, x1;			Add calced address to SPBase
	stp x0,x0, [x7];			  load lvalue in rvalue; load twice since mac stack=2x
	stp	x0, x0, [SP, #-16]!;push item twice, since width = 16!
;==============<<<<<<<<<<<STORE-GLOBAL===========
;==============================
;========STACK_MACHINE=========
;==============================

	adrp x0, StackItems@PAGE
	add x0, x0, StackItems@PAGEOFF
	bl _printf
.data
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
.text 
	adrp x0, FinalResult@PAGE
	add x0, x0, FinalResult@PAGEOFF
	bl _printf
	add sp, sp, 0x10; Remvoe Last Stack Item
	adrp x0, IR@PAGE
	add x0, x0, IR@PAGEOFF
	bl _printf

	ldp FP, LR, [sp], 0x10;prologue:

	;===Local Vars, remove!
	add sp, sp, #80; x20 as BottomStackPointer
	mov x0, #0
	ret
.data
FinalResult: .asciz "FinalResult: %d \n"
HelperResult: .asciz "HelperResult: %d \n"
.data
IR: .asciz "
=========IR-CODE===========
loadc 11
loadc 16
store
pop
loadc 22
loadc 32
store
pop
loadc 33
loadc 48
store
pop
loadc 44
loadc 64
store
pop
loadc 55
loadc 80
store
=========IR-CODE===========
"
