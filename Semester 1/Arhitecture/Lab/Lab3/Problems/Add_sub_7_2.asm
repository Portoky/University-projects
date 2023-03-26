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
    a db 1 ;11
    b dw 2 ;1122
    c dd 3 ;11223344
    d dq 4 ;1122334455667788h
; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;mov ebx, [c]
        ;add ebx, [c]
        ;add ebx, [c]; ebx = c+c+c
        
        mov ebx, dword[d+0]
        mov ecx, dword[d+4] ;ecx:ebx = d
        
        mov al, [a]
        cbw
        cwde ;eax = a
        cdq; edx:eax = a
        
        clc
        sub ebx, eax
        sbb ecx, edx ; ecx:ebx = d - a 
        
        mov eax, [c]
        add eax, [c]
        add eax, [c] ;eax = c+c+c
        cdq; edx:eax = c+c+c
        
        clc;
        add ebx, eax
        adc ecx, edx ; ecx:ebx = (c+c+c) + (d-a)
        
        mov ax, [b]
        cwde
        cdq ; edx:eax = b
        
        clc
        sub ebx, eax
        sbb ecx, edx ; ecx:ebx = (c+c+c)-b +(d-a)
        
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
