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
    a db 1
    b db 2
    c db 3
    e dd 4
    x dq 5
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov al, [a]
        cbw ;ax = a
        mov bl, 2
        idiv bl ;al = a/2, ah = a % 2
        cbw ; ax = a/2
        push ax ;stack = ax
        
        
        mov al, [b]
        imul al; ax = b * b
        push ax; stack = ax, ax = b*b, a/2
        
        mov al, [a]
        mov bl, [b]
        imul bl ;ax = a * b
        mov bx, ax ;bx = a * b
        
        mov al, [c]
        cbw ;ax = c
        imul bx ;dx:ax = ax * bx = a * b * c
        
        push dx
        push ax ; stack = ax,dx, ax, ax =  a * b * c, b*b, a/2
        pop ebx ; ebx = a * b * c ; stack = ax, ax = b * b, a/2
        neg ebx ; ebx = - (a*b*c)
        
        
        pop ax ; ax = b * b ; stack = ax = a/2
        cwde ;eax = b * b
        add ebx, eax ; ebx = b * b - a * b * c 
        
        pop ax; stack empty
        cwde ; eax = a / 2
        add ebx, eax ; ebx = b * b - a * b * c + a / 2
        
        mov eax, [e]
        cdq; edx:eax = e
        
        clc
        add eax, dword [x+0]
        adc edx, dword [x+4] ; edx:eax = e + x
        push edx
        push eax ;stack = eax, edx = e+x
        
        mov eax, ebx 
        cdq ;edx:eax = a * b * c + b * b + a / 2
        pop ebx
        pop ecx ; ecx:ebx = e + x
        
        clc
        add eax, ebx
        adc edx, ecx ; b * b - a * b * c + a / 2 + e + x
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
