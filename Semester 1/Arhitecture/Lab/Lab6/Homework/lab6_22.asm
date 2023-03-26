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
    src db 'lmoxnhi'
    len_src equ $-src
    dst db 'ijkmwop'
    len_dst equ $-dst
    input db 'mlmoolxxnhii'
    len_input equ $-input
    ind dw 0
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov ecx, len_input
        mov esi, input
        jecxz theend
        main_loop:
            
            lodsb; al, element of the input
            push esi ;stack = esi
            
            mov edi, src ;src[i] -> i = edi
            find_element:
                scasb ; cmp al, es:edi while not equal
                jne find_element
            
            sub edi, src; we obtain a scalar value, the index where we found the element in src[]
            dec edi
            add edi, dst; dst[edi] == dst[i]
            
            mov esi, edi
            pop edi; points to the list input
            dec edi ;it was incremented because of the lodsb
            movsb ;[EDI] = [ESI]
            mov esi, edi 
            
        loop main_loop
        
        theend:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
