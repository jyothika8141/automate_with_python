import random, time
from inputimeout import inputimeout


numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
    n1 = random.randint(0, 9)
    n2 = random.randint(0, 9)

    limit = 1
    print(f'{questionNumber+1}: {n1} x {n2} = ')
    corr_ans = str(n1*n2)

    try:
        ans = inputimeout(prompt="Enter the answer: ".strip(), timeout=8)
    except Exception:
        print('Your time is over!')
        continue

    while (not ans.isdigit()) or ans != corr_ans:
        print("Enter a the correct answer")
        try:
            ans = inputimeout(prompt="Enter the answer1: ".strip(), timeout=8)
            if ans == corr_ans:
                    break
            limit += 1
            if limit == 3:
                print("No. of tries is only 3!!!")
                break
        except Exception:
            print('Your time is over!')
            break
    if ans == corr_ans:
        print('Correct!!\n')
        time.sleep(1)
        correctAnswers += 1   
        
print(f'Score: {correctAnswers} / {numberOfQuestions}')
