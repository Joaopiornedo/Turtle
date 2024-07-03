from turtle import Turtle
t = Turtle()  #guardar em variavel
t.speed(1)  #definir a velocidade
while True:
    #Frente ou para Trás?
    frente_tras = str(input("Deseja ir para Frente(f) ou para Trás (t)? ").lower())
    if frente_tras == "f":
        distancia_frente = int(input("Quanto devemos andar para frente? ").lower())
        t.forward(distancia_frente)
    elif frente_tras == "t":
        distancia_tras = int(input("Quanto devemos andar para trás? ").lower())
        t.backward(distancia_tras)
    else:
        break
        #Rotacionar ?
    rotacionar =str(input("Deseja Rotacionar Esquerda (e) ou Direita(d) não Rotacionar(n) ? ").lower())
    if rotacionar == "e":
        rotacionar_esquerda = int(input("Quanto rotacionar para esquerda? ").lower())
        t.left(rotacionar_esquerda)
    elif rotacionar == "d":
        rotacionar_direita = int(input("Quanto rotacionar para direita? ").lower())
        t.right(rotacionar_direita)
    elif rotacionar == "n":
        continuar_andando = str(input("Deseja continuar andando ?(s) sim (n) não :").lower())
        if continuar_andando == "s":
            print(frente_tras)
        elif continuar_andando =="n":
            break
