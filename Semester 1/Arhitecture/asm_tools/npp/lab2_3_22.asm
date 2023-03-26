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
    two equ 2
    ten equ 10
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov al, [a]
        mul byte [a] ; ax = a*a
        mov bx, ax ; bx = a*a
        mov al, byte two 
        mul byte [b];ax = 2*b
        sub bx, ax ;bx = a*a - 2*b
        mov ax, word ten
        add ax, [d] ; ax = 10+d
        sub ax, bx ;ax = (10 + d) - a*a - 2*b
        div byte[c]; ax = [(10 + d) - a*a - 2*b] / c dx = % 
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
