bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, scanf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    
import scanf msvcrt.dll  
  
;the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    n dd 0
    len_max equ 65535
    number dd 0
    sum_digits times len_max db 0
    format db "%d", 0
    ten dw 10
; our code starts here
segment code use32 class=code
    start:
        ; ...
        push dword n
        push dword format 
        call [scanf]
        add esp, 4*2
        
        mov ecx, [n]
        mov edi, sum_digits
        for:
            push ecx; saving volatile registers
            push dword number
            push dword format
            call [scanf]
            add esp, 4*2
            pop ecx
            mov bl, 0; sum of digits
            while:
                mov ax, [number]
                mov dx, [number+2]
                div word [ten]; in dx we have the digit, basically in dl, since its small
                
                push ax
                mov eax, 0
                pop ax
                mov [number], eax; updateing the number after division with 10
                
                test dl, 01h ;testng if the digit is even or add
                jnz skip
                add bl, dl
                skip:
                
                cmp dword [number], 0
                jne while
                
                mov al, bl
                stosb
                mov al, 0
        loop for
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
