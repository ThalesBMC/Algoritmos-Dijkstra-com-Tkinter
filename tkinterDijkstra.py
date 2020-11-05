from tkinter import *
################################################################################################################################
#Daqui até proxima faixa é a interface gráfica

root = Tk()

top = Frame(root, width = 1920, height = 1080)
top.pack(side=TOP)

text_Input = StringVar()

text_Input2 = StringVar()

txtDisplay = Entry(top, font = ('arial', 18, 'bold'), bg = 'purple', textvariable = text_Input, width = 21, bd = 3, justify = 'left',fg = 'white')
txtDisplay.pack(side=TOP)
txtDisplay.insert(0, 'Começo')
txtDisplay.configure(state=DISABLED)

def on_click(event):
    txtDisplay.configure(state=NORMAL)
    txtDisplay.delete(0, END)
    txtDisplay.unbind('<Button-1>', on_click_id)

on_click_id = txtDisplay.bind('<Button-1>', on_click)

txtDisplay2 = Entry(top, font = ('arial', 18, 'bold'), bg = 'purple', textvariable = text_Input2, width = 21, bd = 3, justify = 'left',fg = 'white')
txtDisplay2.pack(side=TOP)
txtDisplay2.insert(0, 'Chegada')
txtDisplay2.configure(state=DISABLED)


def on_click2(event):
    txtDisplay2.configure(state=NORMAL)
    txtDisplay2.delete(0, END)
    txtDisplay2.unbind('<Button-1>', on_click_id2)

on_click_id2 = txtDisplay2.bind('<Button-1>', on_click2)

#######################################################################################################
#Daqui para baixo o algoritmo
class Heap:
    #Classe com todas as funções
    def __init__(self):
        self.array = []
    def add(self, item):
        self.array.append(item)
        self.menorUp()
    def pop(self):
        if not self.array:
            return None
        trocar(self.array, 0, len(self.array) - 1)
        node = self.array.pop()
        self.menorDown()
        return node

    def PegarMenorchild(self, parent):
        return min([it for it in Pegarchildren(parent) if it < len(self.array)], 
        key=lambda it: self.array[it], default=-1)

    def menorDown(self):
        parent = 0
        menor = self.PegarMenorchild(parent)
        while menor != -1 and self.array[menor] < self.array[parent]:
            trocar(self.array, menor, parent)
            parent, menor = menor, self.PegarMenorchild(menor)

    def menorUp(self):
        index = len(self.array) - 1
        parent = Pegarparent(index)
        while parent != -1 and self.array[index] < self.array[parent]:
            trocar(self.array, index, parent)
            index, parent = parent, Pegarparent(parent)

    def __bool__(self):
        return bool(self.array)




def dijkstra(grafoPonderado, start, end):
    #Algoritmo de dijkstra
    distancias = {i: float("inf") for i in grafoPonderado}
    melhorParent = {i: None for i in grafoPonderado}

    paraVisitar = Heap()
    paraVisitar.add((0, start))
    distancias[start] = 0
    visitado = set()

    while paraVisitar:
        sourceDistancia,    source = paraVisitar.pop()
        if sourceDistancia > distancias[source]:
            continue
        if source == end:
            break
        visitado.add(source)
        for alvo, distancia in grafoPonderado[source][0].items():
            if alvo in visitado:
                continue
            novaDistancia = int(distancias[source]) + int(grafoPonderado[source][0][alvo])
            if distancias[alvo] > novaDistancia:
                distancias[alvo] = novaDistancia
                melhorParent[alvo] = source
                paraVisitar.add((novaDistancia, alvo))

    return caminho(melhorParent, start, end)
def JuntarDicts(x, y):
    """Junta dois dicionários """
    z = x.copy()   
    z.update(y)    
    return z
def trocar(array, a, b):
    array[a], array[b] = array[b], array[a]

def Pegarparent(pos):
    return (int(pos) + 1) // 2 - 1

def Pegarchildren(pos):
    direita = (int(pos) + 1) * 2
    esquerda = direita - 1
    return esquerda, direita

def TirarBarraN(conteudo):
    """Tira o \n da string"""
    palavra=""
    for j in conteudo:
        if j != "\n":
            palavra += j
    return palavra
def caminho(melhorParent, start, end):
    #Faz o histórico
    if end not in melhorParent:
        return None
    cursor = end
    path = [cursor]
    
    while cursor in melhorParent:
        cursor = melhorParent[cursor]
        path.append(cursor)
        if cursor == start:
            return list(reversed(path))
    return None



#Ler aquivo
arq=open("twitchPesos.txt","r")
quantidade = arq.readlines()
arq.close()

verdade2=True
nao=False
lista=[]
dictionary={}
vertices=[]
inf=False
###Cria o dicionário

for k in range(len(quantidade)):
    entrada=TirarBarraN(quantidade[k])
    separador= entrada.split(",")    

    if  len(separador)==3:
        first=1
        temNoDic=False

        for f in separador:
            if first==1:
                first=2
                separador[0]=f
            elif first==2:
                first=0
                separador[1]=f
            else:
                    
                if separador[0] in dictionary:
                    first=1

                    if  separador[1] in dictionary[separador[0]][0]:
                        #Para selecionar o menor peso caso sejam repetidos
                        if float(f) > dictionary[separador[0]][0][separador[1]]:
                            pass
                        elif float(f) == dictionary[separador[0]][0][separador[1]]:
                            pass
                        else:
                            dictionary[separador[0]][0][separador[1]]= float(separador[2])
                    else:
                        #Adiciona os dicionários antigos com o novo.
                        teste2=dictionary[separador[0]][0]
                        teste= {separador[1]:float(separador[2])}
                        z=[]
                        z=JuntarDicts(teste,teste2)
                        
                        dictionary[separador[0]] = [z]
        
                else:
                    #Caso não exista no dicionário
                    dictionary[separador[0]]=[{separador[1]:float(separador[2])}]
                    first=1
               
        if separador[0] in vertices :
            pass
        else:
            #Adiciona os vertices
            vertices.append(separador[0])
        if separador[1] in vertices:
            pass
        else:
            vertices.append(separador[1])





def show_answer():
    #Interface gráfica para mostrar a resposta
    inf=False
    stringFinal=""
    comeco = str(txtDisplay.get())
    final = str(txtDisplay2.get())
    
    condInicial = comeco in vertices
    condFinal = final in vertices  
    if condInicial == False or condFinal == False:
        stringFinal="inf"
    else:
        valores=(dijkstra(dictionary,comeco,final))

        if valores == None or valores =="inf":
            stringFinal="inf"	
            inf= True  
        cont=1
        peso=0
        
        if inf == False:
            #Calcula o peso
            for l in valores:

                if dictionary[l][0][valores[cont]]:
                    peso += float(dictionary[l][0][valores[cont]])
                    cont+=1
                if len(valores) == cont:
                    break
                
        
            peso=int(peso)
            peso = str(peso)
            peso = ("Peso: "+peso)
            valores.append(peso)
    #Mostra o resultado na tela
    resultado = StringVar()
    if stringFinal=="inf":
        pass
    else:
        stringFinal= "=> ".join(valores)
    resultado.set(stringFinal)
    large_font = ('Verdana',10)
    Entry(root,fg="white",font=large_font, bg="purple",width=1000,text = "%s" %(resultado)).pack(side=TOP)
                

Button(root, text='Calcular', width = 10, height = 1, command=show_answer).pack(side=TOP)
root.configure(bg = 'black')
root.geometry('920x1040+200+200')
root.title('Twitch')
root.mainloop()