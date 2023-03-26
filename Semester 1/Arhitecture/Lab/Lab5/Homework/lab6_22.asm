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
    s1 db 'aceh'
    s2 db 'bdfg'
    length equ $-s2
    d times length db 0
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov ecx, length
        mov esi, 0
        jecxz end
        repeat:
            mov al, [s1 + esi]
            mov bl, [s2 + esi]
            
            ;if starts here
            cmp al, bl
            jb s1small
            
            mov [d + esi], bl
            jmp endif
            
            s1small:
            mov  [d + esi], al
            
            endif:
            inc esi
        
        loop repeat
        
        end:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
