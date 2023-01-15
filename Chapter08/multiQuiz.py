import random, time
from inputimeout import inputimeout


def prompt():
        global limit
        try:
            answer = inputimeout(prompt="Enter the answer1: ".strip(), timeout=8)
            limit += 1
            print(limit)
            if limit == 3:
                print("No. of tries is only 3!!!")
                return False
            return answer
        except Exception:
            print('Your time is over!')
            return None

def check(ans):
        global correctAnswers
        if ans == str(n1 * n2):
            print('Correct!!')
            time.sleep(1)
            correctAnswers += 1
        else:
            print('Incorrect!!Try again')
            answer = prompt()
            check(answer)


numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
    n1 = random.randint(0, 9)
    n2 = random.randint(0, 9)

    print(f'{questionNumber+1}: {n1} x {n2} = ')
    
    try:
        ans = inputimeout(prompt="Enter the answer: ".strip(), timeout=8)
        limit = 1
    except Exception:
        print('Your time is over!')
        continue

    while not ans.isdigit():
        print("Enter a number")
        ans = prompt()
        print('hi')
        print('ans: ', ans)
        if ans ==  False:
            break
    if ans == False:
        continue
    check(ans)
    
print(f'Score: {correctAnswers} / {numberOfQuestions}')
