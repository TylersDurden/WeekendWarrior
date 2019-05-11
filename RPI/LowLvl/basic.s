@ My First Assembly Program
		.global _start
_start:		MOV R1, #0x02
		MOV R2, #0x03
   		ADD R3, R2, R1
		MOV R7, #1
		SVC 0

