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
    s DD 12345678h, 1A2B3C4Dh, 0FE98DC76h
    len equ ($-s) / 4
    d times len dw 0 ;reserve space for most of elements that can be  in our result list
    three db 3
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov ecx, len
        mov eax, 0
        mov esi, s
        mov edi, d
        jecxz end
        repeta:
            
            lodsd; in eax we have the one element from the list
            shr eax, 24; now we have the needed byte in al
            mov bl, al ;save the byte for later
            div byte [three] ; al = /, ah = %
            cmp ah, 0
            jne dont_add_element ;if ah != 0
            mov al, bl;we get back the saved byte
            stosb ; in d we put the byte if needed
            
            
            dont_add_element:
       
        loop repeta
        end:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
