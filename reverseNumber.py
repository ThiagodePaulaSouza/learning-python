def reverso(n):
    n=str(n)
    numeroInvertido = (n[::-1]) #n é um string e eu posso por entre [] como eu quero trabalhar com ela quando coloca :: falase descubra pra mim o valor inicial(a primeira posição) depois coloca um incremento
    print(numeroInvertido)
n = int(input("Digite um Numero Grande: "))
reverso(n)