reservadas = ['while','do']
operador  = ['<','=','+']
terminais = ';'
numeros = ['0','1','2','3','4','5','6','7','8','9']
palavra = 'while i < 100 - do i = i + j;'

token = ''
const = ''
listadesimbolos = []
temp = ''


arq = open('arquivo.txt', 'w',encoding='utf-8')

tabela_de_simbolo = []
def buscaSimbolo(verificador):
    if verificador in tabela_de_simbolo:
        return tabela_de_simbolo.index(verificador) + 1
    else:
        tabela_de_simbolo.append(verificador)
        return tabela_de_simbolo.index(verificador) + 1


for x in range(len(palavra)):
    if palavra[x] in reservadas[0] or  palavra[x] in reservadas[1]:
        token = token + palavra[x]
        #print(token)
        if token == 'while' or token == 'do':
            #print(palavra[x].index)
            var = {'token': token, 'id': 'palavra reservada','tam': len(token),'pos': (0,x+1 - len(token)) }
            arq.write(str(var)+'\n')
            token = ''

    elif palavra[x] == ' ':
        
        if palavra[x+1] == 'i':
            
            if palavra[x+1] not in temp:
                temp = temp + palavra[x+1]
                var = {'token': palavra[x+1], 'id': ['identificador', buscaSimbolo(palavra[x+1])],'tam': 1,'pos': (0, x+1)}
                listadesimbolos.append((palavra[x+1],str(buscaSimbolo(palavra[x+1]))))
            else:
                var = {'token': palavra[x+1], 'id': ['identificador', buscaSimbolo(palavra[x+1])],'tam': 1,'pos': (0, x+1)}
            arq.write(str(var)+'\n')
        elif  palavra[x+1] == 'j':
            
            if palavra[x+1] not in temp:
                temp = temp + palavra[x+1]
                var = {'token': palavra[x+1], 'id': ['identificador', buscaSimbolo(palavra[x+1])],'tam': 1,'pos': (0, x+1)}
                listadesimbolos.append((palavra[x+1],str(buscaSimbolo(palavra[x+1]))))
            else:
                var = {'token': palavra[x+1], 'id': ['identificador', palavra[x+1]],'tam': 1,'pos': (0, x+1)}
            arq.write(str(var)+'\n')
    elif palavra[x] in operador:
        var = {'token': palavra[x], 'id': 'operador','tam': 1,'pos': (0, x)}
        arq.write(str(var)+'\n')

    elif palavra[x] == terminais:
        var = {'token': palavra[x], 'id': 'terminador','tam': 1,'pos': (0, x)}
        arq.write(str(var)+'\n')

    elif palavra[x] in numeros:
        const = const + palavra[x]
        if palavra[x+1] == ' ':
            var = {'token': const,'id': ['constante',buscaSimbolo(palavra[x])],'tam': len(const),'pos': (0, x+1 - len(const))}
            if const not in temp:
                listadesimbolos.append((const,str(buscaSimbolo(palavra[x]))))
                arq.write(str(var)+'\n')
    else: 
        print('error: linha {} ,coluna {}'.format(0,x+1))
        break
arq.close()  

arq2 = open('simbolos.txt', 'w',encoding='utf-8')
for x in listadesimbolos:
    var = {'indice':x[1], 'simbolos': x[0] }
    arq2.write(str(var))
    print(var)
arq2.close()
    