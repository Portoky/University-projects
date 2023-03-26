bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, scanf, fprintf, fopen, fclose               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import scanf msvcrt.dll                        
import fprintf msvcrt.dll                        
import fopen msvcrt.dll                        
import fclose msvcrt.dll                        

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    file_name db "words.txt", 0
    access_mode db "w", 0
    file_descriptor dd -1
    format db "%s", 0
    max_len equ 100
    cuvant times max_len db 0
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        push dword access_mode
        push dword file_name
        call [fopen]
        add esp, 4*2
        
        cmp eax, 0
        je final
        mov [file_descriptor], eax
        
        while:
            push dword cuvant
            push dword format
            call [scanf]
            add esp, 4*2
            
            mov edi, cuvant
            cmp byte [edi], "$"
            je end
            
            mov bl, 0
            mov ecx, max_len
            for:
                cmp byte [edi], "0"
                jb skip
                cmp byte [edi], "9"
                ja skip
                
                mov bl, 1
                
                skip:
                inc edi
            loop for
            
            cmp bl, 0
            je dont_print
            
            push dword cuvant
            push dword format
            push dword [file_descriptor]
            call [fprintf]
            add esp, 4*3
            dont_print:
            ;clearing the string so we can read again without having any problems from the previous read
            mov ecx, max_len
            mov edi, cuvant
            mov al, 0
            rep stosb
            
            jmp while
            
        end:
        push dword [file_descriptor]
        call [fclose]
        add esp, 4
        
        final:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
