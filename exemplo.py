def ler_notas_e_calcular_media(turma):
    alunos = []
    for i in range(3):  
        print(f"\nDigite as notas do aluno {i + 1} da {turma}:")
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        media = (nota1 + nota2) / 2
        alunos.append([nota1, nota2, media])  
    return alunos
def calcular_media_turma(alunos):
    soma_medias = sum(aluno[2] for aluno in alunos)  
    media_turma = soma_medias / 3
    return media_turma
def alunos_com_media_acima(alunos, media_turma):
    for i, aluno in enumerate(alunos):
        if aluno[2] > media_turma:
            print(f"O aluno {i + 1} teve média {aluno[2]:.2f}, maior que a média da turma ({media_turma:.2f})")
print("Turma 1:")
turma1 = ler_notas_e_calcular_media("Turma 1")
print("\nTurma 2:")
turma2 = ler_notas_e_calcular_media("Turma 2")
media_turma1 = calcular_media_turma(turma1)
media_turma2 = calcular_media_turma(turma2)
turma_media = [media_turma1, media_turma2]
print(f"\nMédia da Turma 1: {media_turma1:.2f}")
print(f"Média da Turma 2: {media_turma2:.2f}")
if media_turma1 > media_turma2:
    print("\nA Turma 1 teve a maior média.")
elif media_turma2 > media_turma1:
    print("\nA Turma 2 teve a maior média.")
else:
    print("\nAs duas turmas têm a mesma média.")
print("\nAlunos com média maior que a média da Turma 1:")
alunos_com_media_acima(turma1, media_turma1)
print("\nAlunos com média maior que a média da Turma 2:")
alunos_com_media_acima(turma2, media_turma2)