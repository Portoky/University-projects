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

; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov al,-56 ; AL = C8h = 200 in unsigned interpretation
        mov bl,100
        cmp al, bl ;fictive subtraction al-bl which sets the flags (for our case, we will have SF = 0, OF = 1, CF = 0 and ZF = 0)
        JNGE et2 ;verify condition JNGE - Jump if not greater or equal 
        ;(SIGNED comparison -56 versus 100) 
        ;verifies in fact if the two flags, SF and OF, have different values 
        ; Considering that in our case SF=0 and OF=1, so SF <> OF, the condition is fullfilled (and truly -56 is „NOT GREATER OR ;EQUAL” to 100) so the jump to label et2 will be performed
        mov dx,1 
        et2:
        mov cx,1
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
