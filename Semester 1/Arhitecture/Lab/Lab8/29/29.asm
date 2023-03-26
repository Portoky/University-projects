bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fscanf, fprintf, fopen, fclose               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import fscanf msvcrt.dll                   
import fopen msvcrt.dll
import fclose msvcrt.dll
import fprintf msvcrt.dll       ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    file_name db "numbers.txt", 0
    access_mode db "a+", 0
    format db "%d", 0
    result db "Biggest number: %d", 0
    biggest dd 0
    current dd 0
    file_descriptor dd 0
    
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
            push dword current
            push dword format 
            push dword [file_descriptor]
            call [fscanf]
            add esp, 4*3
            
            
            cmp eax, 1
            jne final; we didnt read anything-> exit the file
            
            mov eax, [current]
            cmp eax, [biggest]
            jl while
            
            mov [biggest], eax
            jmp while
            
        final:
        
        push dword [biggest]
        push dword result
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
