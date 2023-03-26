bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fopen, fprintf, fclose               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll
import fclose msvcrt.dll
import fprintf msvcrt.dll
import fopen msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    text db "abcd efgh lmao lmn op", 0
    lentext equ $-text
    file_name db "word.txt", 0
    descriptor dd 0
    access_mode db "w", 0
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov esi, text
        mov ecx, lentext - 1
        jecxz final
        
        mov dl, 0; if it is even position
        mov al, 1; for position
        while:
            cmp dl, 0
            jne skip
            
            mov [esi], al
            mov dl, 1
            jmp skip2
            
            skip:
            mov dl, 0
            
            skip2:
            inc al
            inc esi
        loop while
        
        push dword access_mode
        push dword file_name
        call [fopen]
        add esp, 4*2
        
        cmp eax, 0
        je final
        
        mov [descriptor], eax
        
        push dword text
        push dword [descriptor]
        call [fprintf]
        add esp, 4*2
        
        push dword [descriptor]
        call [fclose]
        add esp, 4
        final:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
