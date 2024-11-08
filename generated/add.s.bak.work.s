

.text
	.global main
	.align	2

main:

;arm64_epilogue
	stp x29, x30, [sp, -0x10]!
	sub sp, sp, 0x10
;arm64_epilogue:end

;;; Start des eigentlichen Programms
;loadc
	mov x0, #1
;push
str	x0, [SP, #-16]!
;loadc:END
;loadc
	mov x0, #2
;push
str	x0, [SP, #-16]!
;loadc:END
;add
	ldr x1, [sp], #16 
	ldr x2, [sp], #16 
	add  x0, x1, x2
;pop
	; ldr x0, [sp], #16 
;;; Ende des eigentlichen Programms

	; mov x0, #1 

	mov x8, x0
	str x8, [sp]
	adr x0, Lstr
	bl _printf

;arm64_prologue: X30(LR): Link Register, X29:Frame pointer
	add sp, sp, 0x10
	ldp x29, x30, [sp], 0x10
;arm64_prologue:end
	mov x0, #0
	ret
Lstr: .asciz "Result: %d"
