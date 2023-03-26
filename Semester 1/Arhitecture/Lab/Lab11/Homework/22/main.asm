bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, scanf, printf, digit_at_hundred             ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    n resd 1
    number resd 1
    format db "%d", 0
    s2 times 100 db 0
    k dw 25
    
; our code starts here
segment code use32 class=code

    start:
        ; ...
        push dword n
        push dword format
        call [scanf]
        add esp, 4
        
        mov edi, s2
        for:
            push dword number
            push dword format
            call [scanf]
            
            ;determining the digit at 100s place
            push dword [number]
            push dword edi
            call digit_at_hundred
            add esp, 4*2
            
            inc edi
            sub dword [n], 1 
            
            cmp dword [n], 0
            jne for
        
        push dword s2
        call [printf]
        add esp, 4
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
