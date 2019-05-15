/* Using syscall 3 to read from the keyboard */
        .global _start
_start:
_read:
    MOV R7, #3      @ Syscall Number
    MOV R0, #0      @ Stdin is Keyboard
    MOV R2, #12     @ read 12 Characters
    LDR R1, =string @ string placed at string:
    SWI 0

_write:

    MOV R7, #4      @ Write SysCall
    MOV R0, #1      @ Stdout is Monitor
    MOV R2, #19     @ String is 19 chars long
    LDR R1, =string
    SWI 0


_exit:
    @exit syscall
    MOV R7, #1
    SWI 0


.data
string:
.ascii "Hello World String\n"
