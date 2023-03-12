def hangman():
    stages=["",'___________', '|   O',"|  /|\ ","|  / \ "]
    if wrong==len(letters):
        print('\n'.join(stages))
    else:
        print('\n'.join(stages[0:wrong+1]))
import random
print('ИГРА ВИСЕЛЬНИК')
wrong=0
word=['кот','кит','мышь','краб', input()]
n=random.randrange(0,5)
letters=[]
for i in word[n-1]:
    letters.append(i)
board=['_']*len(word[n-1])
stages=["",'___________', '|   O',"|  /|\ ","|  / \ "]
while wrong<len(letters):
    your_choice=input('Введи букву: ')
    if your_choice in letters:
        i=letters.index(your_choice)
        board[i], letters[i]=letters[i], '$'
        print(' '.join(board))
        hangman()
    else:
        wrong+=1
        print(' '.join(board))
        hangman()
    if '_' not in board:
        print("You are winner!", '\n Secret word:', ''.join(board))
        break
if wrong==len(letters):
    print('You can try again. \nVery well! You tried!')
    hangman()
    print('Загадоное слово: ', word[n-1])
# print(word[1])
