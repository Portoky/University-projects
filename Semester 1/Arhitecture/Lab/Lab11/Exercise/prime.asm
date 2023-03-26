bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global prime

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...

; our code starts here
segment code use32 class=code public
    prime:
        mov eax, [esp+4]
        ;mov ax, [esp+4]
        ;mov dx, [esp+6]
        
        cmp eax, 1
        jbe .endwhile2
        cmp eax, 2
        je .endwhile1
        
        mov ecx, 2
        .while:
            mov edx, 0
            
            push eax
            div ecx
            pop eax
            
            cmp edx, 0
            je .endwhile2
            
            
            
            inc ecx
            cmp ecx, [esp+4]
            jb .while
            
        jmp .endwhile1
        
        .endwhile2:
        mov eax, 0
        jmp .end
        
        .endwhile1:
        mov eax, 1
        
        .end:
        ret
