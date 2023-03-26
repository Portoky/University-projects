bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf, common_prefix              ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll
import printf msvcrt.dll  
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    s1 db "abcd1235", 0
    len1 equ $-s1
    s2 db "abcd12", 0
    len2 equ $-s2
    s3 db "abc", 0  
    len3 equ $-s3
    
    result times len3+len1+len2 db 0
    message db "%s", 0ah, 0
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        push result
        push s1
        push s2
        call common_prefix; now in ecx we have  the length of the prefix
        add esp, 4*3
        
        ;printing
        push result
        push message
        call [printf]
        add esp, 4*2
        
        push result
        push s1
        push s3
        call common_prefix
        add esp, 4*3
        
        push result
        push message
        call [printf]
        add esp, 4*2
        
        push result
        push s2
        push s3
        call common_prefix
        add esp, 4*3
        
        push result
        push message
        call [printf]
        add esp, 4*2
        
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
