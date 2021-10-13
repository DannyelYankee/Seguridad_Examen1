from collections import Counter
def desencriptar(texto):
    #texto = texto.lower()
    letras_mensaje = Counter(texto)
    print("cantidad de letras = ", len(letras_mensaje))
    
    frec_castellano = {'e': 16.78,'a': 11.96, 'o': 8.69, 'l': 8.37, 's': 7.88, 'n': 7.01, 'd': 6.87, 'r': 4.94, 'u': 4.8, 'i': 4.15,
                        't': 3.31, 'c': 2.92, 'p': 2.776, 'm': 2.12, 'y': 1.54, 'q': 1.53, 'b': 0.92 ,'h':0.89,'g':0.73,'f':0.52,'v':0.39,
                        'j':0.3,'ñ':0.29,'z':0.15,'x':0.06,'k':0,'w':0}
    descifrado ={}
    abecedario = "abcdefghijklmnñopqrstuvwxyz"
    abecedario_lista = list(abecedario)
    #Inicializamos el diccionario descifrado
    for i in abecedario_lista:
        descifrado[i] = ' '

    print(frec_castellano)
    letras_mensaje.pop(' ') #Eliminamos de la frecuencia de letras del mensaje los espacios en blanco ' '.
    print("-------------------------------------------------------------------------------------------------------------------------------------------------")
    print(letras_mensaje)

    itr = 2
    while itr >0: #vamos a cambiar en el mensaje las dos letras mas frecuentes por las 2 mas frecuentes del castellano
        maximo_valor_frec = max(frec_castellano, key=frec_castellano.get)    
        maximo_valor_letras_mensaje = max(letras_mensaje, key=letras_mensaje.get)    
        texto = texto.replace(maximo_valor_letras_mensaje,maximo_valor_frec)
        descifrado[maximo_valor_frec] = maximo_valor_letras_mensaje
        frec_castellano.pop(maximo_valor_frec)
        letras_mensaje.pop(maximo_valor_letras_mensaje)
        itr-=1
    print()   
    '''Ahora vamos a agrupar en 2 arrays las palabras de 2 y 3 letras para ver si sacamos mas informacion'''
    texto_lista = texto.split(" ")    
    palabras_tres_letras = []
    palabras_dos_letras = []
    for i in texto_lista:
        if len(i) == 3:
            palabras_tres_letras.append(i)
        elif len(i) == 2:
            palabras_dos_letras.append(i)
    print()
    print(palabras_dos_letras)
    print(palabras_tres_letras)
    print()
    texto = texto.replace("T","l") #Viendo las palabras de dos letras podemos suponer que T es l, haciendo referencia a los articulos determinados    
    descifrado["l"] = "T"
    '''Volvemos a reemplazar la letra mas frecuente del mensaje con la de la tabla de frecuencias,
    teniendo en cuenta que las letras que reemplazamos de igual forma previamente ya no estan en los diccionarios.
    '''
    maximo_valor_frec = max(frec_castellano, key=frec_castellano.get)    
    maximo_valor_letras_mensaje = max(letras_mensaje, key=letras_mensaje.get)    
    texto = texto.replace(maximo_valor_letras_mensaje,maximo_valor_frec)
    descifrado[maximo_valor_frec] = maximo_valor_letras_mensaje
    frec_castellano.pop(maximo_valor_frec)
    letras_mensaje.pop(maximo_valor_letras_mensaje)
    '''AQUI MIRANDO EL MENSAJE VAMOS SUPONIENDO QUE VALOR TIENE CADA LETRA'''
    texto = texto.replace("A","d") #suponiendo que A es d
    descifrado["d"] = "A"
    texto = texto.replace("o","r")
    texto = texto.replace("P", "m")
    descifrado["m"] = "P"
    texto = texto.replace("Q", "b")
    descifrado["b"] = "Q"
    texto = texto.replace("C", "i")
    descifrado["i"] = "C"
    texto = texto.replace("I", "o")
    descifrado["o"] = "I"
    texto = texto.replace("Z", "u")
    descifrado["u"] = "Z"
    texto = texto.replace("R", "c")
    descifrado["c"] = "R"
    texto = texto.replace("J", "n")
    descifrado["n"] = "J"
    texto = texto.replace("N", "s")
    descifrado["s"] = "N"
    texto = texto.replace("V", "y")
    descifrado["y"] = "V"
    texto = texto.replace("L", "z")
    descifrado["z"] = "L"
    texto = texto.replace("H", "t")
    descifrado["t"] = "H"
    texto = texto.replace("D", "p")
    descifrado["p"] = "D"
    texto = texto.replace("O", "f")
    descifrado["f"] = "O"
    texto = texto.replace("X", "p")
    descifrado["p"] = "X"
    texto = texto.replace("F", "x")
    descifrado["x"] = "F"
    texto = texto.replace("S", "q")
    descifrado["q"] = "S"
    texto = texto.replace("G", "j")
    descifrado["j"] = "G"
    texto = texto.replace("U", "g")
    descifrado["g"] = "U"
    texto = texto.replace("M", "h")
    descifrado["h"] = "M"
    print(descifrado)
    '''Vamos a ver si encontramos alguna clave en la tabla de equivalencias '''
    clave = []
    for i in abecedario_lista:
        clave.append(descifrado[i])
    print(clave)
    print("Mensaje descifrado: ")
    return texto
mensaje = "RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE. AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."


print(desencriptar(mensaje))