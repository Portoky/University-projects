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
        mov al, [a]
        cbw
        cwde
        cdq; edx:eax = a
        
        mov ebx, dword [d+0]
        mov ecx, dword [d+4] ; ecx:ebx = d
        
        clc
        sub eax, ebx
        sbb edx, ecx ; edx:eax =  a-d
        
        mov ebx, eax
        mov ecx, edx ; ecx:ebx = a-d
        
        mov ax, [b]
        cwde
        cdq; edx:eax = b
        
        clc
        add ebx, eax
        adc ecx, edx ;ecx:ebx = a-d+b
        
        mov ax, [b]
        cwde ;eax = b
        add eax, [c] ;eax = c + b
        cdq; edx:eax = c+b
        
        clc
        sub eax, ebx
        sbb edx, ecx ;edx:eax = c+b - (a-d+b)
        
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
