bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global b_module  ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    rank dd -1
    bytes dd -1
    sum dd 0
; our code starts here
segment code public use32 class=code
    b_module:
        mov edi, 0; index
        mov esi, [esp + 12]; dd_string
        mov ecx, [esp + 16]; len
        
        .for:
            mov dl, 0; in edx we save the rank
            mov bl, 4;indexing
            mov al, 0;calculating the max byte
            .while:
                cmp [esi], al
                jb .skip
                mov al, [esi]
                mov dl, bl
                .skip:
                inc esi
                dec bl
                cmp bl, 0
            ja .while
            
            cbw
            cwde
            add [sum], eax; adding to the sum the chosen byte
            
            add edi, [esp + 4]; we pont into the string bytes the byte at the corresponding index
            mov [edi], al
            
            sub edi, [esp + 4]
            add edi, [esp + 8]; we point to the string rank ath the corresponding index
            mov [edi], dl
            
            sub edi, [esp+8]; now edi is an index again
            inc edi
        
        loop .for
        
        mov eax, [sum]
        
        ret
            
        
        
