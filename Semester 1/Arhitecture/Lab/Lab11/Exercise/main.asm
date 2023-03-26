bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fopen, fclose, fscanf, fprintf, prime            
import fprintf msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll
import fscanf msvcrt.dll
import exit msvcrt.dll

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    file_name_in db "numbers.txt", 0
    file_name_out db "primes.txt", 0
    descriptor_in dd 0
    descriptor_out dd 0
    access_in db "r", 0
    access_out db "w",0
    format db "%d", 0
    formatout db "%d ", 0
    number dd 0
; our code starts here
segment code use32 class=code public
    

    start:
        ; ...
        push dword access_in
        push dword file_name_in
        call [fopen]
        add esp, 4*2
        
        cmp eax, 0
        je end1
        mov [descriptor_in], eax
        
        push dword access_out
        push dword file_name_out
        call [fopen]
        add esp, 4*2
        
        cmp eax, 0
        je end2
        mov [descriptor_out], eax
        
        
        while:
            push dword number
            push dword format
            push dword [descriptor_in]
            call [fscanf]
            add esp, 4*3
            
            cmp eax, -1;we didnt read anything -> end of file
            je endwhile
            
            push dword [number]
            call prime
            add esp, 4
        
            cmp eax, 1
            jne skip
            
            push dword [number]
            push dword formatout
            push dword [descriptor_out]
            call [fprintf]
            add esp, 4*2
            
            skip:
        
        jmp while
        endwhile:
        
        
        push dword [descriptor_out]
        call [fclose]
        add esp, 4
        
        end2:
        push dword [descriptor_in]
        call [fclose]
        add esp, 4
        
        end1:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
