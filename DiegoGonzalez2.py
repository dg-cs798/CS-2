def main():
    student = int(input('Total number of students: '))
    scores = input(f'Enter {student} score(s): ').split()

    while len(scores) < student:
        scores = input(f'Enter {student} score(s): ').split()

    scores = [int(num) for num in scores]
    scores = scores[0:student]
    best = max(scores)

    for i in range(student):
        score = scores[i]
        if score >= best - 10:
            grade = 'A'
        elif score >= best - 20:
            grade = 'B'
        elif score >= best - 30:
            grade = 'C'
        elif score >= best - 40:
            grade = 'D'
        else:
            grade = 'F'

        print(f'Student {i + 1} score is {score} and grade is {grade}')

if __name__ == '__main__':
    main()