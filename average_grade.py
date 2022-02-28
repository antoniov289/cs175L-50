#Antonio Vinagre
#CS 175L
#average_grade.py

def main():
    score1 = float(input('Enter score 1: '))
    score2 = float(input('Enter score 2: '))
    score3 = float(input('Enter score 3: '))
    score4 = float(input('Enter score 4: '))
    score5 = float(input('Enter score 5: '))
    g1 = determine_grade(score1)
    g2 = determine_grade(score2)
    g3 = determine_grade(score3)
    g4 = determine_grade(score4)
    g5 = determine_grade(score5)
    avg = calc_average(score1, score2, score3, score4, score5)
    g_avg = determine_grade(avg)
    print()
    print(f'{"Score":<14}{"Numeric Grade":^15}{"Letter Grade":^15}')
    print('--------------------------------------------')
    print(f'{"Score 1:":<14}{score1:^15}{g1:^15}',
          f'{"Score 2:":<14}{score2:^15}{g2:^15}',
          f'{"Score 3:":<14}{score3:^15}{g3:^15}',
          f'{"Score 4:":<14}{score4:^15}{g4:^15}',
          f'{"Score 5:":<14}{score5:^15}{g5:^15}',
          f'{"Average Score:":<14}{avg:^15}{g_avg:^15}',
          sep = '\n')
    print()
    repeat()

def determine_grade(score):
    if 90 <= score:
        grade = 'A'
    elif 80 <= score:
        grade = 'B'
    elif 70 <= score:
        grade = 'C'
    elif 60 <= score:
        grade = 'D'
    else: #score < 60
        grade = 'F'
    return grade

def calc_average(s1, s2, s3, s4, s5):
    summ = s1 + s2 + s3 + s4 + s5
    avg = summ / 5
    return avg

def repeat():
    again = input('Enter \'yes\' if you would like to do another calculation: ')
    print()
    if again == 'yes':
        main()

main()
