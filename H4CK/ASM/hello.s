.global _start

_start:
    MOV R0, #1
    MOV R7, #4
    MOV R2, #12
    LDR R1, =message
    SWI 0

_end:
    MOV R7, #1
    SWI 0

_data:
message:
    .ascii "Hello World\n"
