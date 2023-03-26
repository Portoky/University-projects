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
    a dd 10011011101111100111011101010111b
    b dw 0111011101010101b
    c dd 0
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov ebx, 0; we compute the result in ebx
        mov eax, [a]
        not eax; we inverted [a]
        shr eax, 20 ;bits 20-24 -> 0-4
        mov ebx, 1111b ;ebx = 00...1111b
        and ebx, eax ;ebx : the bits 0-4 of C are the invert of the bits 20-24 of A
        
        mov eax, 0
        mov eax, 111100000b; eax = 0...1111000000b
        or ebx, eax ;the bits 5-8 of C have the value 1
        
        mov eax, 0
        mov ax, 1111000000000000b
        and ax, [b]; now ax contains the bits 12-15 of B
        shr eax, 3 ;now these bits are on position 9-12
        or ebx, eax
        
        mov eax, 0
        mov eax, 1110000000b
        and eax, [a]
        shl eax, 6
        or ebx, eax;the bits 13-15 of C are the same as the bits 7-9 of A
        
        mov [c], ebx
        
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
