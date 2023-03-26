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
    a db 1
    b db 2
    c db 3
    d dw 4
    hundred equ 100
    three equ 3
    ten equ 10
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov AX, [d]
        add AX, word three
        mov DX, 100
        mul DX ;DX:AX = 100*(d+3)
        mov BX, word ten
        mov CX, 0 ;CX:BX = 10
        
        clc 
        sub AX, BX
        sbb DX, CX ;DX:AX = 100*(d+3)-10
            
            
        ;sub AX, dword ten ; AX = 100*(d+3) - 10; ax<10!!!
        div word [d] ; AX = (100*(d+3) - 10)/d DX = %
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
