bits 32 ; assembling for the 32 bits architecture
global convert       

; our data is declared here (the variables needed by our program)
segment data use32 class=data public
    ; ...
    table db "0123456789ABCDEF"
; our code starts here
segment code use32 class=code public
    convert:
        mov edi, [esp+8]
        mov ebx, table
        mov edx, [esp+4]
        mov ecx, 8
        while:
            mov al, 0
            
            shl edx, 1; we have the bit in carry flag
            jnc skip1
            add al, 8
            
            skip1:
            shl edx, 1
            jnc skip2
            add al, 4
            
            skip2:
            shl edx, 1
            jnc skip3
            add al, 2
            
            skip3:
            shl edx, 1
            jnc skip4
            add al, 1
            
            skip4:
            
            xlat
            stosb ;mov [edi], al
        loop while
        
        ret