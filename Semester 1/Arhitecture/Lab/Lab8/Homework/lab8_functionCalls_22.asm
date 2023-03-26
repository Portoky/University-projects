bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll
import printf msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    a dd 12345678
    b dd 12345679
    k dd 152
    r dq 0
    message db "(%d + %d)*%d = %lld", 0
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov eax, dword [a]
        mov ebx, dword [b]
        add eax, ebx
        imul dword [k]; edx:eax = (a+b)*k
        push edx
        push eax
        pop dword [r]
        pop dword [r+4]
        
        push dword [r+4]
        push dword [r]
        push dword [k]
        push dword [b]
        push dword [a]
        push dword message
        call [printf]
        add esp, 4*6
        
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
