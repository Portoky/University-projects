bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    a dd 0F0F0F0F0h
    b dd 00000001h
    c dq 0
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov edx, 0
        mov eax, 0
        
        mov eax, [a]
        mov cl, 11 
        rol eax, cl ; bits 21-28 are now on 0-7
        and eax, 0FFh;  isolating bytes 0-7
        
        mov ebx, [b]
        neg ebx
        mov cl, 15
        shr ebx, cl
        and ebx, 0FF00h; bitmasking
        or eax, ebx
        
        mov ebx, 0000_0000_0010_1010_0000_0000_0000_0000b
        or eax, ebx
        
        mov ebx, 0000_0000_0011_1111_1111_1111_1111_1111b
        and eax, ebx
        
        mov ebx, [b]
        mov cl, 21
        shr ebx, cl
        and ebx, 0000_0000_0000_0000_0000_0111_1111_1111b
        or edx, ebx
        
        mov ebx, [a]
        mov cl, 10
        shl ebx, cl
        and ebx, 0000_0000_0111_1111_1111_1000_0000_0000b
        or edx, ebx
        
        mov ebx, [a]
        xor ebx, 0abh
        and ebx, 1111_1111_0000_0000_0000_0000_0000_0000b
        or edx, ebx
        
        
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
