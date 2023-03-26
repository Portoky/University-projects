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
        mov EAX, dword [d+0]
        mov EDX, dword [d+4] ; EDX:EAX = d
        mov EBX, [c] 
        mov ECX, 0; ECX:EBX = c
        
        clc
        add EAX, EBX
        adc EDX, ECX ;EDX:EAX = d+c
        
        mov EBX, 0
        mov EBX, [c]
        mov ECX, 0
        mov CX, [b]
        add EBX, ECX
        mov ECX, 0 ;ECX:EBX = c + b
                
        clc
        sub EAX, EBX 
        sbb EDX, ECX ; EDX;EAX = (d+c) - (c+b)
        
        ;clearing ECX:EBX
        mov EBX, 0
        mov ECX, 0
        
        mov BX, [b]
        add BL, [a] ;ECX:EBX = b + a
        
        clc
        sub EAX, EBX
        sbb EDX, ECX ; EDX;EAX = (d+c) - (c+b) - (b+a)
   
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
