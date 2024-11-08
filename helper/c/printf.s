	.section	__TEXT,__text,regular,pure_instructions
	.globl	main                           ; -- Begin function main
	.p2align	2
main:                                  ; @main
	sub	sp, sp, #112
	stp	x24, x23, [sp, #48]             ; 16-byte Folded Spill
	stp	x22, x21, [sp, #64]             ; 16-byte Folded Spill
	stp	x20, x19, [sp, #80]             ; 16-byte Folded Spill
	stp	x29, x30, [sp, #96]             ; 16-byte Folded Spill
	add	x29, sp, #96
	mov	w20, #222                       ; =0xde
	mov	w21, #111                       ; =0x6f
	mov	w22, #999                       ; =0x3e7
	stp	x21, x20, [sp, #24]
	mov	w23, #888                       ; =0x378
	mov	w24, #777                       ; =0x309
	stp	x23, x22, [sp, #8]
	str	x24, [sp]
Lloh0:
	adrp	x19, l_.str@PAGE
Lloh1:
	add	x19, x19, l_.str@PAGEOFF
	mov	x0, x19
	bl	_printf
	stp	x21, x20, [sp, #24]
	stp	x23, x22, [sp, #8]
	str	x24, [sp]
	mov	x0, x19
	bl	_printf
	mov	w0, #0                          ; =0x0
	ldp	x29, x30, [sp, #96]             ; 16-byte Folded Reload
	ldp	x20, x19, [sp, #80]             ; 16-byte Folded Reload
	ldp	x22, x21, [sp, #64]             ; 16-byte Folded Reload
	ldp	x24, x23, [sp, #48]             ; 16-byte Folded Reload
	add	sp, sp, #112
	ret
                                        ; -- End function
	.section	__TEXT,__cstring,cstring_literals
l_.str:                                 ; @.str
	.asciz	"data: %d %d %d %d %d\n"

