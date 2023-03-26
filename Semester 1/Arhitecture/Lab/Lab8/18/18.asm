bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fread, printf, fopen, fclose               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll 
import fopen msvcrt.dll 
import fclose msvcrt.dll 
import fread msvcrt.dll 
import printf msvcrt.dll 

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    file_name db "text.txt", 0
    access_mode db "r", 0
    file_descriptor  dd 0
    txt times 100 db 0
    nm dd 0
    format db '%d', 0
; our code starts here
segment code use32 class=code
    start:
        ; ...
        push dword access_mode
        push file_name
        call [fopen]
        add esp, 4*2
        
        cmp eax, 0
        je final
        mov [file_descriptor], eax
        
        while:
            push dword [file_descriptor]
            push dword 100
            push dword 1
            push dword txt
            call [fread]
            add esp, 4*4
            
            cmp eax, 0
            je end
            
            mov ecx, eax
            mov esi, txt
            for:
                cmp byte [esi], ' '
                jne skip1
                inc dword [nm]
                
                skip1:
                cmp byte [esi], '.'
                jne skip2
                inc dword [nm]
                
                skip2:
                inc esi
            loop for
        end:
        push dword [file_descriptor]
        call [fclose]
        add esp, 4
        
        inc dword [nm]
        push dword [nm]
        push dword format
        call [printf]
        add esp, 4*2
        
        final:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
