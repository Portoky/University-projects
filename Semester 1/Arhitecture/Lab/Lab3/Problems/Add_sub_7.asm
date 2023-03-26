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
    b dw 2
    c dd 3
    d dq 4
; our code starts here
segment code use32 class=code
    start:
        ; ...
        
        mov EAX, [c]
        mov EDX, 0 ; EDX:EAX = c
        ;11223344  55667788h
        ; EDX       EAX
        clc;
        sub EAX, dword [d+0]
        sbb EDX, dword [d+4]; EDX:EAX = c - d
        
        clc; clear carry flag
        sub eax, dword [d+0]
        sbb edx, dword [d+4]
        clc; clear carry flag
        sub eax, dword [d+0]
        sbb edx, dword [d+4] ; EDX:EAX =  c - (d + d + d)
        
        mov EBX, 0
        mov ECX, 0
        mov BL, [a]
        SUB BX, [b] ;bx = a-b
        
        clc
        add EAX, EBX
        adc EDX, ECX; EDX: EAX = c - (d+d+d) + (a - b) 
        
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
