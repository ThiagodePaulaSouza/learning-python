turma = []
media = 0
for i in range (3):
    linha = []
    for j in range (5):
        linha.append(int(input('digite a nota[' + str(i) + ',' + str (j) + ']:')))
    turma.append(linha)
media += turma.append(linha)
media = media / 15
print('a media da turma é:', media)