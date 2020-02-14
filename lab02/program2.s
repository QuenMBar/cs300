	.arch armv7-a
	.eabi_attribute 28, 1
	.eabi_attribute 20, 1
	.eabi_attribute 21, 1
	.eabi_attribute 23, 3
	.eabi_attribute 24, 1
	.eabi_attribute 25, 1
	.eabi_attribute 26, 2
	.eabi_attribute 30, 6
	.eabi_attribute 34, 1
	.eabi_attribute 18, 4
	.file	"program2.c"
	.text
	.section	.rodata
	.align	2
.LC0:
	.ascii	"Hello world\000"
	.align	2
.LC1:
	.ascii	"Compiled by an Intel processor and\000"
	.align	2
.LC2:
	.ascii	"running on an ARM processor.\000"
	.text
	.align	1
	.global	main
	.syntax unified
	.thumb
	.thumb_func
	.fpu vfpv3-d16
	.type	main, %function
main:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 1, uses_anonymous_args = 0
	push	{r7, lr}
	add	r7, sp, #0
	ldr	r3, .L3
.LPIC0:
	add	r3, pc
	mov	r0, r3
	bl	puts(PLT)
	ldr	r3, .L3+4
.LPIC1:
	add	r3, pc
	mov	r0, r3
	bl	puts(PLT)
	ldr	r3, .L3+8
.LPIC2:
	add	r3, pc
	mov	r0, r3
	bl	puts(PLT)
	movs	r3, #0
	mov	r0, r3
	pop	{r7, pc}
.L4:
	.align	2
.L3:
	.word	.LC0-(.LPIC0+4)
	.word	.LC1-(.LPIC1+4)
	.word	.LC2-(.LPIC2+4)
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.4.0-1ubuntu1~18.04.1) 7.4.0"
	.section	.note.GNU-stack,"",%progbits
