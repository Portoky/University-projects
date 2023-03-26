bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fopen, fprintf, fclose               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    
import fopen msvcrt.dll    
import fprintf msvcrt.dll    
import fclose msvcrt.dll    

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    file_name db "number.txt", 0
    access_mode db "a", 0
    descriptor dd -1
    number dd 124567
    divisor dw 10
    digit dd 0
    line db '%u', 0ah, 0; 0ah -> newline character in ascii
; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;open/create file_name
        push dword access_mode
        push dword file_name
        call [fopen]
        add esp, 4*2
        
        cmp eax, 0
        je final
        mov [descriptor], eax
        
        
        while:
            mov ax, [number]
            mov dx, [number + 2] ;little endian!
            div word [divisor];ax = rest of the number, dx = last digit
            mov dword [number], 0 ;we clear what was before
            mov [number], ax; update with one less digit
            mov [digit], dx; since there only one digit, no need to clear beforehand
            
            ;displaying the digit
            push dword [digit]
            push dword line
            push dword [descriptor]
            call [fprintf]
            add esp, 4*3
            
            cmp dword [number], 0
            jne while
        
        ;closing the textfile
        push dword [descriptor]
        call [fclose]
        
        
        final:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
