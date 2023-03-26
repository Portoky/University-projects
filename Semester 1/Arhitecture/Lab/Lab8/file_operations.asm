bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fopen, fclose, fprintf, fread, printf           ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import fopen msvcrt.dll 
import fclose msvcrt.dll                    ; msvcrt.dll contains exit, printf and all the other important 
import fprintf msvcrt.dll
import fread msvcrt.dll
import printf msvcrt.dll

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    file db "file.txt", 0
    access db "a+", 0
    message db "My first message with the number: %d.", 0
    message2 db "Another message added.", 0
    number dd 5
    file_descriptor dd -1
    read_message resb 100
; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;opening
        push dword access
        push dword file
        call [fopen] ;eax = file_descriptor
        add esp, 4*2 
        
        cmp eax, 0
        je final
        mov [file_descriptor], eax
        
        
        
        ;reading
        push dword [file_descriptor]
        push dword 100
        push dword 1
        push dword read_message
        call [fread]
        add esp, 4*4
        
        ;closing
        push dword [file_descriptor]
        call [fclose]
        add esp, 4
        
        push read_message
        call [printf]
        add esp, 4
        
        
        ; exit(0)
        final:
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
