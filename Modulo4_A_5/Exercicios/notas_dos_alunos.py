notas = []
alunos = []
media_final =[]

mf = 0

for x in range(3):
    nome = str(input("Digite o nome dos seus alunos\n"))
    alunos.append(nome)
    for y in range(4):
        nota = float(input("Digite as 4 notas do aluno:\n"))
        mf += nota
    mf = mf /4
    media_final.append(mf)
 



for x in range(3):
    if (media_final[x] >= 7):
        print(f"O aluno {alunos[x]} tirou {media_final[x]} de média,parabéns!\n")
        