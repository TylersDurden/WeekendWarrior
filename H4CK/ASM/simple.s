.global _start

_start:
    MOV R0, #1
    MOV R1, #21
    ADD R0, R1, #21

SWI 0

