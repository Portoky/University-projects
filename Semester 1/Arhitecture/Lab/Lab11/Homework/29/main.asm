bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf, scanf, gets              ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll 
import printf msvcrt.dll 
import scanf msvcrt.dll 
import gets msvcrt.dll 
   ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    sentence times 100 db 0
    format db "%s ", 0
    aword times 30 db 0
    reversedword times 30 db 0
    
; our code starts here
segment code use32 class=code
    

    start:
        ; ...
        
            push dword sentence
            ;push dword format
            call [gets]
            add esp, 4
            
            mov esi, sentence
            for:
            
                mov edi, aword
                mov ecx, 0
                while:
                    inc ecx
                    movsb
                    cmp byte [esi], " "
                    je endwhile
                    cmp byte [esi], "."
                    je endwhile
                    jmp while
                endwhile:
                
                push esi
                push dword aword
                push dword reversedword
                call reverse
                add esp, 4*2
                
                
                push dword reversedword
                push dword format
                call [printf]
                add esp, 4*2
                
                pop esi
                mov ecx, 30
                mov edi, aword
                mov al, 0 
                rep stosb
                
                mov ecx, 30
                mov edi, reversedword
                mov al, 0 
                rep stosb
                    
            cmp byte [esi], "."
            jne for
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
