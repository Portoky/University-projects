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
    c dw 3
    e dd 4
    x dq 5
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov al, [a]
        sub al , 2
        cbw
        cwd; dx:ax = a - 2
        
        ;? mov eax, 0;
        ;mov al, [a]; positive
        
        ;?mov al, [a]; negative
        ;cbw
        ;cwde
        
        push ax
        push dx ;stack = dx, ax
        mov al, [b]
        cbw
        add ax, [c] ;ax = b+c
        mov bx, ax ;bx = b+c
        pop dx
        pop ax ; dx:ax = a-2
        idiv bx ;ax = (a-2) / (b+c), dx = (a-2) % (b+c)
        
        mov bx, ax
        mov cx, dx ;bx = (a-2) / (b+c), cx = (a-2) % (b+c)
        push cx
        push bx ;stack = bx, cx
        mov al, [a]
        cbw ;ax = a
        imul word [c] ; DX:AX = a * c
        push dx
        push ax ;stack = ax, dx, bx, cx
        
        mov eax, [e]
        cdq ;edx:eax = e
        
        clc
        sub eax, dword [x+0]
        sbb edx, dword [x+4] ;edx: eax = e - x
        mov ebx, eax
        mov ecx, edx ;ecx : ebx = e - x 
        
        pop eax; eax = dx:ax = a*c it loads it like that
                ;stack bx, cx
        cdq ;edx:eax = a*c
        
        clc
        add ebx, eax
        adc ecx, edx ;ecx:ebx = (e-x) + a * c
        
        pop ax ; ax = bx = (a-2) / (b+c)
        cwd; eax = (a-2) / (b+c)
        cdq; edx:eax = (a-2) / (b+c)
        
        clc
        add eax, ebx
        adc edx, ecx ; edx:eax = (a-2) / (b+c) + (e-x) + a * c
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
