.text
	.global main
	.align	2

main:
	stp x29, x30, [sp, -0x10]!
	sub sp, sp, 0x10

;;; Start des eigentlichen Programms
;;; Ende des eigentlichen Programms


	mov x8, #66
	str x8, [sp]
	adr x0, Lstr
	bl _printf


	mov x0, #0
	add sp, sp, 0x10
	ldp x29, x30, [sp], 0x10
	ret

Lstr: .asciz "test: %x"

