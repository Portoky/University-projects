bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    ;0)
    a db 'abcd'
    b db $-a
    ;c db 'A,B,C'
    ;d equ $-a
    ;0a)
    ;a db 3
    ;b times 2 dw 2
    ;c times 4 dd 3,5,7
    ;d dd 89h
    ;e equ $-a
    ;0b)
    ;a db 'Orice text digerabil : )', 0
    ;b times $-a db 1
    ;len equ $-a
; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;mov ax, len
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
