

.text
	.global main
	.align	2

main:

;arm64_epilogue
	stp x29, x30, [sp, -0x10]!
	sub sp, sp, 0x10
;arm64_epilogue:end

;;; Start des eigentlichen Programms
;;; Ende des eigentlichen Programms


	mov x8, x0
	str x8, [sp]
	adr x0, Lstr
	bl _printf

;arm64_prologue
	add sp, sp, 0x10
	ldp x29, x30, [sp], 0x10
;arm64_prologue:end
	mov x0, #0
	ret
Lstr: .asciz "Result: %d"

