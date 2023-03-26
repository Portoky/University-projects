bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, scanf, fprintf, fopen, fclose               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll 
import fopen msvcrt.dll 
import fclose msvcrt.dll 
import scanf msvcrt.dll 
import fprintf msvcrt.dll 
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    file_name db "words.txt", 0
    access_mode db "w", 0
    file_descriptor  dd 0
    format db "%s", 0
    theword times 100 db 0
; our code starts here
segment code use32 class=code
    start:
        ; ...
        push dword access_mode
        push dword file_name
        call [fopen]
        add esp, 4*2
        
        cmp eax, 0
        je end
        mov [file_descriptor], eax
        
        while:
            push dword theword
            push dword format
            call [scanf]
            add esp, 4*2
            
            cmp byte [theword], '$'
            je final
            
            mov esi, theword-1
            mov bl, 0
            for:
                inc esi
                cmp byte [esi], 48
                jb skip
                cmp byte [esi], 57
                ja skip
                
                inc bl
                
                skip:
                
                cmp byte [esi], 0
                jne for
            cmp bl, 0
            je skip2
            push dword theword
            push dword format
            push dword [file_descriptor]
            call [fprintf]
            add esp, 4*3
            
            skip2:
            mov ecx, 100
            mov edi, theword
            mov al, 0
            rep stosb
            
            jmp while
        final:
        push dword [file_descriptor]
        call [fclose]
        
        end:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
