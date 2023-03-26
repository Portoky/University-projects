bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf             ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll
import printf msvcrt.dll  ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    a dd 17
    b dd 6
    r dd 0
    message db "%d mod %d = %d", 0
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov eax, [a]
        mov ebx, [b]
        cdq ; eax - > edx:eax = [a]
        idiv dword [b] ; eax = quotient, edx = remainder
        mov [r], edx
        push dword [r]
        push dword [b]
        push dword [a]
        push dword message
        call [printf]
        add esp, 4 * 4
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
