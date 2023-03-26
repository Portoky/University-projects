bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fopen, fclose, scanf, fprintf, fread         
import exit msvcrt.dll    
import fopen msvcrt.dll    
import fclose msvcrt.dll    
import scanf msvcrt.dll    
import fprintf msvcrt.dll
import fread msvcrt.dll    

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    character db 0
    n dd 0
    content times 100 db 0
    file_name_in times 100 db 0
    access_mode_in db "r", 0
    access_mode_out db "a", 0
    formatc db "%c", 0
    formatd db "%d", 0
    formats db "%s", 0
    file_name_out db "c.txt", 0
    descriptorin dd 0
    descriptorout dd 0
; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;reading the character
        push dword character
        push dword formatc
        call [scanf]
        add esp, 4*2
        
        ;reading  the number
        push dword n
        push dword formatd
        call [scanf]
        add esp, 4*2
        
        ;reading  the filename
        push dword file_name_in
        push dword formats
        call [scanf]
        add esp, 4*2
        
        ;input file open
        push dword access_mode_in
        push dword file_name_in
        call [fopen]
        add esp, 4*2
        
        cmp eax, 0
        je final
        mov dword [descriptorin], eax
        
        ;outputfile open
        push dword access_mode_out
        push dword file_name_out
        call [fopen]
        add esp, 4*2
        
        cmp eax, 0
        je final2
        mov dword [descriptorout], eax
        
        while:
            push dword [descriptorin]
            push dword 100
            push dword 1
            push dword content
            call [fread]
            add esp, 4*4
            
            cmp eax, 0
            je endwhile
            mov ecx, eax
            
            mov eax, 0
            mov al, [character]
            mov edx, 1
            mov edi, content
            for:
                cmp edx, [n]
                jne skip
                
                ;eax multiple of n
                mov [edi], al
                
                mov edx, 0
                
                skip:
                inc edx
                inc edi
            loop for
            
        endwhile:
        
        push dword content
        push dword [descriptorout]
        call [fprintf]
        add esp, 4*2
        
        push dword [descriptorout]
        call [fclose]
        add esp, 4
        
        final2:
        push dword [descriptorin]
        call [fclose]
        add esp, 4
        
        final:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
