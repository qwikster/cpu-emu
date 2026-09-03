R|M|I = register | memory source | immediate (value)

== control flow ==
JMP  - Jump to address - R|M|I
CALL - JMP to address, push PC to stack - R|M|I
RET  - Load PC from stack and JMP back - no operands
PUSH - Push value to stack - R|M|I
POP  - read out SP - R|M

== conditionals ==
CMP
JE / JNE

== memory stuff ==
WWORD - write 16 bit (big endian) - low byte R|M|I | value R|M|I
RWORD - read 16 bit - address R|M|I - output R|M

== mathematics / logic / bitwise ==
ADD
SUB - 
MUL - discard DWORD or write to memory
DIV - intp 9 for div/0
INC - R
DEC - R
AND - R|M|I, R|M|I so multiple modes
OR -  ^
XOR - ^
NOT - one R|M|I
SHL - R|M|I, R|M|I
SHR - ^

==  interrupts   ==
MAKEINTP MODE NUM R|M|I (reserve 0x00-0x0F for hardware)
EDITINTP MODE NUM R|M|I
DELINTP NUM
READINTP NUM R|M - read IVT value
UNINTP - POP flags and PC, JMP to PC
DOINTP NUM - PUSH flags and PC, IRQ lookup, pull 

==  sys control  ==
NOP - do nothing
HLT - stop processor until interrupt


== flag set + clear + control ==
SETZF / CLZF
SETCF / CLCF
SETOF / CLOF
SETIF / CLIF
SETTF / CLTF

SETPC - R|M|I
SETIR - R|M|I
GETPC - R|M
GETIR - R|M
