def TirarBarraN(conteudo):
    """Tira o \n da string"""
    palavra=""
    for j in conteudo:
        if j != "\n":
            palavra += j
    return palavra
def merge_two_dicts(x, y):
    z = x.copy()   
    z.update(y)    
    return z

#Ler base de dados original
arq=open("twitch.txt","r")
quantidade = arq.readlines()
arq.close()
contador=0

verdade2=True
nao=False
lista=[]
dictionary={}
vertices=[]
inf=False
temZero=False
contF= 0
#Inteira na base de dados e cria um dicionário com peso 0 para cada vértice.
for k in range(len(quantidade)):
    entrada=TirarBarraN(quantidade[k])
    dividirEntrada= entrada.split(",")    

    try:
        if dividirEntrada[0] in dictionary:
            first=1     
            teste2=dictionary[dividirEntrada[0]][0]
            teste= {dividirEntrada[1]:0}
            z=[]
        
            z=merge_two_dicts(teste,teste2)
            
            dictionary[dividirEntrada[0]] = [z]

        else:
            dictionary[dividirEntrada[0]]=[{dividirEntrada[1]:0}]
            first=1
        if dividirEntrada[1] in dictionary:
            first=1 
            teste2=dictionary[dividirEntrada[1]][0]
            teste= {dividirEntrada[0]:0}
            z=[]
            z=merge_two_dicts(teste,teste2)
        
            dictionary[dividirEntrada[1]] = [z]
        else:
            dictionary[dividirEntrada[1]]=[{dividirEntrada[0]:0}]
            first=1
        for i in dividirEntrada :
            if i.isnumeric():
                pass
            elif i in vertices:
                pass
            else:
                vertices.append(i)
        for l in vertices:
            if l in dictionary:
                pass
            else:
                dictionary[l]=[{}]
    except:
        pass
#Coloca o peso em cada vertice de acordo com a quantidade de amizades
for k in dictionary:
    for i in dictionary[k][0]:
        dictionary[k][0][i]= len(dictionary[i][0])

#Escreve no arquivo cada elemento do dicionário que agora possui os pesos corretos
for k in dictionary:
    for i in dictionary[k][0]:
        escrever= "{0},{1},{2}".format(k,i,dictionary[k][0][i])
        arq2=open("twitch3.txt","a")
  
        arq2.write(escrever)
        arq2.write("\n")
        arq2.close()