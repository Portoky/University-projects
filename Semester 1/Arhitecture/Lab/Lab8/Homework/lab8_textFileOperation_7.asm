bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fopen, fclose, fread, printf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll
import fread msvcrt.dll
import printf msvcrt.dll

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    file_name db "letters.txt", 0
    access_mode db  "r", 0
    descriptor dd -1
    len dd 0
    frequent_number dd 0
    frequent_element db -1
    result db "Most frequent element is %c with %d appearance.", 0
    text resb 100
; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;opening the file
        push dword access_mode
        push dword file_name
        call [fopen]
        add esp, 4*2
        
        cmp eax, 0
        je final
        mov [descriptor], eax
        
        ;reading from the file into text string
        push dword [descriptor]
        push dword 100
        push dword 1
        push dword text
        call [fread]
        add esp, 4*4
        
        mov [len], eax ; eax = letters read
        mov esi, 0
        for1:
            mov ecx, 0
            mov al, [text+esi] ; al = text[esi], ++esi
            inc esi
            mov edi, 0
            for2:
                cmp al, [text+edi]
                jne skip
                ;if equal increment the number
                inc ecx
                
                skip:
                inc dword edi
                
                cmp edi, [len]
                jb for2
            
            cmp ecx, [frequent_number]
            jbe no_update
            
            mov [frequent_number], ecx
            mov [frequent_element], al
            
            no_update:
            mov edx, [len]
            dec edx
            cmp esi, edx
            jb for1
        
        ;printing, displaying result
        push dword [frequent_number]
        push dword [frequent_element]
        push dword result
        call [printf]
        add esp, 4
        final:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
