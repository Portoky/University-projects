bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start
extern b_module      

; declare external functions needed by our program
extern exit, printf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll 
import printf msvcrt.dll   ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    dd_string dd 1234A678h, 12345678h, 1AC3B47Dh, 0FEDC9876h
    len equ ($-dd_string) / 4
    rank times len db 0
    bytes times len db 0
    formatu db "%u", 0ah ,0
    formatd db "%d", 0
; our code starts here
segment code public use32 class=code
    start:
        ; ...
        push dword len
        push dword dd_string
        push dword rank
        push dword bytes
        call b_module
        add esp, 4*3; in eax we have the sum of the bytes
        
        push eax; we save it
        
        mov esi, bytes
        mov ecx, len
        
        for:
            mov eax, 0
            mov al, [esi]; in eax we have the byte to print
            push ecx
            
            push eax
            push dword formatu
            call [printf]
            add esp, 4*2
            
            pop ecx
            inc esi
        loop for
        
        pop eax
        
        push eax
        push dword formatd
        call [printf]
        add esp, 4*2
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
