; =============== S U B	R O U T	I N E =======================================
; ESCRIBE: ES:[DI]
; LEE    : DS:[SI]


		public start
start		proc near
		mov	di, 400h    ; Inicio del string -> ES:0400h
		mov	si, 0C0h    ; SI = 00C0h
		push	si      ; Guarda 00C0h en el stack
		xor	cx, cx      ; Inicializa a 0

lee_entrada:	; lee entrada e inicializa
		mov	ah, 0       ; Inicializa AH a 0 (AH = 0h)
		int	16h		    ; KEYBOARD - READ CHAR (AH = scan code, AL = character)
		cmp	al, 2Eh     ; Comprueba si se ha introducido un '.'
		stosb           ; Escribe el caracter introducido -> ES:[DI] = AL ; DI++
		loopne	lee_entrada ; Repite hasta encontrar '.', resta siempre 1 a CX.
		
		
		not	cx          ; Inicializa al número de caracteres excepto '.' puesto.
		sub	dx, dx      ; Inicializa a 0
		mov	bp, cx      ; Inicializa a CX

loc_10118:				
		pop	 bx         ; Obtenemos el índice de lectura
		push bx         ; y lo mantiene en el stack

aumenta_hasta_menos1:				
		inc	byte ptr [bx]               ; Incrementa el número de bucles tontos | Busc
		jnz	short loc_10121             ; Si el dato del puntero de BX != 0 salta   |
		inc	bx                          ; Aumentamos el índice
		jmp	short aumenta_hasta_menos1  ; Saltamos 

en_menos1:	; Pone a 0 DS:0200h hasta DS:0400h			
		mov	di, 0200h   ; Cambia a la cadena en 0200h
		mov	cx, di      ; Escribe 512 veces
		mov	ax, di      ; AX = DI (0200h)
		rep stosb       ; Ejecuta CX veces escribir parte baja de DI -> 0h
		mov	si, di      ; Índice último de escritura pasa a ser el de lectura (0x0400)

loc_1012C:			
		lodsb               ; Lee un caracter de DS:[SI] en AL (volvemos a la entrada)
		mov	bx, ax          ; BX = 0x0200 + AL
		inc	byte ptr [bx]   ; Incrementa [0x0200 + AL]
		cmp	bl, 2Eh         ; 
		jnz	short loc_1012C
		dec	byte ptr [bx]
		pop	 si
		push si
		mov	cx, bp          ; Número de caracteres excepto '.'

loc_1013C:				; CODE XREF: start+43j
		lodsb               ; Número que el bucle tonto se ejecuta
		mov	bx, ax
		dec	byte ptr [bx]
		jl	short loc_10118 ; SE EJECUTA HASTA LLEGAR A LA POSICION DEL CARACTER MAS PEQUEÑO
		loop	loc_1013C
		inc	dx
		pop	si
		push	si
		mov	cx, bp
		repe cmpsb
		jnz	short loc_10118
		pop	bp
		xchg	ax, dx
		aam
		call	$+3
		xchg	al, ah
		add	al, 30h
		int	29h		; DOS 2+ internal - FAST PUTCHAR
					; AL = character to display
		retn
start		endp ; sp-analysis failed

; ---------------------------------------------------------------------------
		db 93h,	0, 4, 0BEh, 0C0h, 0, 56h, 31h, 0C9h, 0B4h, 0, 0CDh
		db 16h,	3Ch, 2Eh, 0AAh
seg000		ends


		end start
