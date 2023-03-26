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
    a db '112687531513'
    lena equ $-a
    b db '123554689'
    lenb  equ $-b
    c times lena+lenb db 0
    two db 2
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov ecx, lenb; we suppose a is longer
        mov al, lena
        cmp al, lenb
        ja alonger
        
        mov ecx, lena
        
        alonger:
        
        mov esi, 0
        mov edi, c
        jecxz final
        
        
        while:
            mov al, [a+esi]
            cmp al, [b+esi]
            ja abig
            
            mov al, [b+esi]
            
            abig:
            stosb
            inc esi
        loop while
        
        mov ecx, lena  ; we consider a is longer
        sub ecx, lenb
        mov al, lena
        cmp al, lenb
        ja alonger2
        
        mov ecx, lenb
        sub ecx, lena
        
        alonger2:
        
        jecxz final
        mov bx, 1
        for:
            mov ax, bx
            div byte [two]

            add ah, 48 ;-> transforming into charahcter
            mov [edi], ah
            inc edi
            inc bx
        loop for
        
        
        final:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
