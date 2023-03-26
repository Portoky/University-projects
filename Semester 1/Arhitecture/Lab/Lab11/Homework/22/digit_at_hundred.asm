bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global digit_at_hundred 
; our data is declared here (the variables needed by our program)
segment data use32 public data
    ; ...
    hundred dw 100
    ten dw 10
; our code starts here
segment code use32 public code
        ; ...
             
        digit_at_hundred:
            mov ax, [esp+8]
            mov dx, [esp+10]
            div word [hundred]; ax = we have the number
            cwd; dx:ax the number
            div word [ten]; dx = we have the digit => basically in dl
            mov edi, [esp+4]
            add dl, 48  ; => converting the digit into characteer
            mov [edi], dl 
            
            ret
