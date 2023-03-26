bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global _longestPrefix        

   ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data public
    ; ...
; our code starts here
segment code use32 class=code public
   _longestPrefix:
        push ebp
        mov ebp, esp ;creating the new stackframe
        
        mov esi, [ebp + 8]
        mov edi, [ebp + 12]
        
        mov ecx, -1
        while:
            add ecx, 1
            cmpsb
            je while
            
        jecxz final
        
        mov esi, [ebp+8]
        mov edi, [ebp+16]
        rep movsb

        final:
        ;mov eax, [ebp+16]
        mov esp, ebp
        pop ebp
        
        ret