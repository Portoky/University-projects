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
    a dw 0111011101010111b
    b dw 1001101110111110b
    c dd 0
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov ebx, 0 ;compute the result in ebx
        or ebx, 0000000000001111b ;ebx = 0000000000001111b
        
        mov eax, 0
        mov ax, 0000000000111111b
        and ax, [a]; bits 0-6 saved bitmasking!
        mov cl, 5
        rol ax, cl; bits 0-6-> 5-11; we could have used shr as well
        or ebx, eax; the bits 0-4 of C have the value 1
                    ;the bits 5-11 of C are the same as the bits 0-6 of A
        
        mov eax, 0
        mov eax, 0000000001100101b
        mov cl, 16
        rol eax, cl; once again shr would be good too
                   ; now bits 15-31 on eax are 00....101b
        or ebx, eax; now bits 15-31 on ebx are 00....101b
        
        mov eax, 0 ;bits set to 0
        mov ax, 00000111100000000b
        and ax, [b] ;bits 8-11 of B saved
        shl ax, 4
        or ebx, eax ;the bits 12-15 of C are the same as the bits 8-11 of B
        
        mov [c], ebx ;we put the result in the c variable
        
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
