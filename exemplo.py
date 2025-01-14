def read_notes_and_calculate_measure(class):
    students = []
    for i in range(3):  
        print(f"\nDigite as notas do aluno {i + 1} da {class}:")
        note1 = float(input("Digite a primeira nota: "))
        note2 = float(input("Digite a segunda nota: "))
        average = (note1 + note2) / 2
        students.append([note1, note2, average])  
    return students
def calculate_average_class(students):
    average_sum = sum(student[2] for student in students)  
    class_average = average_sum / 3
    return class_average
def students_with_average_above(students, class_average):
    for i, student in enumerate(students):
        if student[2] > class_average:
            print(f"O aluno {i + 1} teve média {student[2]:.2f}, maior que a média da turma ({class_average:.2f})")
print("Turma 1:")
class1 = read_notes_and_calculate_measure("Turma 1")
print("\nTurma 2:")
class2 = read_notes_and_calculate_measure("Turma 2")
class_average1 = calculate_average_class(class1)
class_average2 = calculate_average_class(class2)
class_average = [class_average1, class_average2]
print(f"\nMédia da Turma 1: {class_average1:.2f}")
print(f"Média da Turma 2: {class_average2:.2f}")
if class_average1 > class_average2:
    print("\nA Turma 1 teve a maior média.")
elif class_average2 > class_average1:
    print("\nA Turma 2 teve a maior média.")
else:
    print("\nAs duas turmas têm a mesma média.")
print("\nstudents com média maior que a média da Turma 1:")
students_with_average_above(class1, class_average1)
print("\nstudents com média maior que a média da Turma 2:")
students_with_average_above(class2, class_average2)