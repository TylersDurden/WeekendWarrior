global _start

section .date
    msg db "Hello x86!", 0x0a
    len equ $ -msg

section .text
_start:
    mov eax, 4		; sys_write system call
    mov ebx, 1		; stdout file descriptor
    mov ecx, msg	; bytes to write 
    mov edx, len	; number of bytes to write
    int 0x80		; perform system call
    mov eax, 1		; perform sys_exit call
    mov ebx, 0		; exit status is 0 
    int 0x80 
