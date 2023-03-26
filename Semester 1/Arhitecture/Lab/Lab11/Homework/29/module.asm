bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)       
global reverse
; declare external functions needed by our program    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data public

    ; ...

; our code starts here
segment code use32 class=code public

    reverse:
        mov edi, [esp+4] ;where will bereversed
        mov esi, [esp+8] ; to reverse
        dec ecx
        add edi, ecx
       .while:
            cld
            lodsb
            std
            stosb
        cmp byte [esi], 0
        jne .while
        
        cld 
        ret
