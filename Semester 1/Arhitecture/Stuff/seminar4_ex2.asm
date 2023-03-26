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
    s1 dw 2345h, 0a5h, 368h, 3990h
    lens1 equ ($-s1) / 2
    s2 dw 4h, 2655h, 10h
    lens2 equ ($-s2) / 2
    res times (lens1 + lens2) dw 0
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov esi, s1
        mov edi, res
        mov ecx, lens1
        jecxz final
        
        while1:
            movsb
            inc esi
        loop while1
        
        mov esi, s2+1
        mov ecx,lens2
        jecxz final
        while2:
            movsb
            inc esi
        loop while2
        
        ;sorting
        
        mov ecx, lens1 + lens2
        jecxz final
        
        while3:
            mov bl, 0
            mov esi, res
            mov edi, res+1
            mov ecx, lens1+lens2-1
            jecxz final
            for:
                mov al, [esi]
                cmp al, [edi]
                jle skip
                xchg al, [edi]
                mov [esi], al
                inc bl
                skip:
                inc esi
                inc edi
            loop for
            cmp bl, 0
            jne while3
            
        final:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
