bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fopen, fclose, fprintf             
import exit msvcrt.dll    
import fopen msvcrt.dll    
import fclose msvcrt.dll    
import fprintf msvcrt.dll    

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    file_name db "man.txt", 0
    access_mode db "w", 0
    text db "0Ka2ka9ha_75", 0
    lentext equ $-text-1
    file_descriptor dd 0
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov al, "c"
        mov edi, text
        mov ecx, lentext
        jecxz end
        while:
            cmp byte [edi], 48
            jb skip
            cmp byte [edi], 57
            ja skip
            
            mov [edi], al
            skip:
            inc edi
        loop while
        
        push dword access_mode
        push dword file_name
        call [fopen]
        add esp, 4*2
        
        cmp eax, 0
        je end
        mov [file_descriptor], eax
        
        push dword text
        push dword [file_descriptor]
        call [fprintf]
        add esp, 4*2
        
        push dword [file_descriptor]
        call [fclose]
        add esp, 4
        
        end:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
