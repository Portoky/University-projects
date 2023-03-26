
bits 32
segment code use32 public code
global common_prefix
;what this subprogram do is returns the number of common prefix elements i
common_prefix:
    mov esi, [esp + 4]; first string starting address
    mov edi, [esp + 8]; second string starting address
    mov ecx, 0
    while:
        cmpsb
        jne endwhile
        inc ecx
        
        cmp byte [esi], 0
        je endwhile
        cmp byte [edi], 0
        je endwhile
        jmp while
    endwhile: 
    
    mov esi, [esp+4]
    mov edi, [esp+12] ;result
    jecxz .final
    for:
        movsb
    loop for
    final:
    mov byte [edi], 0 ;putting 0 at the end for the print function
    ret