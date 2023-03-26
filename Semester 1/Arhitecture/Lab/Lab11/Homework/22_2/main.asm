bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf, convert               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll
import printf msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data public
    ; ...
    number dd 0101_1111_0111_0000_1100_1000_1011_0001b
    result times 9 db 0
; our code starts here
segment code use32 class=code public
    start:
        ; ...
        push dword result
        push dword [number]
        call convert
        add esp, 4*2
        
        push dword result
        call [printf]
        add esp, 4
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
