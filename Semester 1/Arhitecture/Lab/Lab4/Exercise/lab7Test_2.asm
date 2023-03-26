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
    a db 1,2,3,4,5
    b db 1,2,3,4,5
    lenz2 equ $-b
    lenz3 equ $-a
    c dw 1,2,3,4,5
    
    lenA1 equ $-a ; $ - current position minus start of a = 0
                  ; $ we are at position 20(byte) 
                  ; we defined 10 byte + 5 words = 20 bytes
    lenA2 equ $-b
    lenA3 equ $-c
    lenB1 equ $-b
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov ax, lenz2
        mov bx, lenz3
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
