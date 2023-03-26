bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)      
global _convert


; our data is declared here (the variables needed by our program)
segment data use32 class=data public
    ; ...
    table db "0123456789ABCDEF"
; our code starts here
segment code use32 class=code public
    _convert:
        ; ...
        push ebp
        mov ebp, esp
        mov edx, [ebp+8]
        
        mov edi, [ebp+12]
       
        mov ebx, table
        mov ecx, 8
        for:
            mov al, 0
            
            shl edx, 1
            jnc .skip1
            add al, 8
            .skip1:
            
           shl edx, 1
           jnc .skip2
           add al, 4
           .skip2:
           
           shl edx, 1
           jnc .skip3
           add al, 2
           .skip3:
           
           shl edx, 1
           jnc .skip4
           add al, 1
           .skip4:
            
            xlat
            stosb
        loop for
        
        
        mov esp, ebp
        pop ebp
        
        ret
