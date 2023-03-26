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
    sir dd 1234A678h, 12785634h, 1A4D3C28h
    len_sir equ ($-sir) / 4
    sir2 times len_sir dw 0 
    format db "%d", 0
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov edi, sir2
        mov esi, sir
        mov ecx, len_sir
        for:
            inc esi
            movsb
            inc esi
            movsb
        loop for
        
        ;numeraing the number of bits 1
        mov bl, 0
        mov esi, sir2
        mov ecx, len_sir * 2; byte multiplying with 2 we obtain the number of bytes in sir2, byt multiplying with 8 we obtain the number of bits
        for2:
            mov dl, 0;used for numerating -> index
            while:
                shl byte[esi], 1
                jnc skip
                inc bl
                skip:
                
                inc dl
                cmp dl, 8
                jb while
            add esi, 1; next byte parsing
        loop for2
        mov eax, 0
        mov al, bl
        push eax
        push dword format
        call [printf]
        add esp, 4*2
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
