global loader
global outb
extern sum_of_three
extern pchar
MAGIC_NUMBER equ 0x1BADB002
ALIGN_MODULES   equ 0x00000001 
FLAGES       equ 0x0
CHECKSUM    equ -(MAGIC_NUMBER + ALIGN_MODULES)   ;计算校验和(MAGIC_NUMBER + FLAGES + CHECKSUM = 0)
KERNEL_STACK_SIZE equ 4096

 

section .text
align 4
    dd MAGIC_NUMBER
    dd ALIGN_MODULES
    dd CHECKSUM
loader:
    mov eax,0xCAFEBABE
    mov esp, kernel_stack + KERNEL_STACK_SIZE
    push dword 3
    push dword 2
    push dword 1
    call sum_of_three

.loop:
    
    jmp .loop
; outb - send a byte to an I/O port
; stack: [esp + 8] the data byte
;        [esp + 4] the I/O port
;        [esp    ] return address
outb:
    mov  al,[esp + 8]
    mov  bx,[esp + 4]
    out  bx,al
    ret
    
section .bss
align 4
kernel_stack:
    resb KERNEL_STACK_SIZE