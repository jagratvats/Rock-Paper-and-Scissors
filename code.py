import random
gamelst = ['stone','paper','scissors']
p=0
c=0
print("score: computer - " +str(c) + " player - " + str(p))

while True:
    computerchoice = gamelst[random.randint(0,len(gamelst)-1)]

    command = input("[1] 'Stone'\n[2] 'paper'\n[3] 'scissors\n[4] 'quit' \n\n>")
    if command == computerchoice:
        print('tie')
    elif command == '1':
        if computerchoice == 'stone':
            print("player won!")
            p += 1
        else:
            print("computer won!")
            c += 1
    elif command =='2' :
        if computerchoice == 'scissors':
            p+=1
        else :
            c+=1
    elif command == '3':
        if computerchoice == 'paper':
            print('player won!')
            p += 1
        else:
            print('computer won!')
            c += 1
    elif command == '4':
        print('your this session high score is :',p)
        break
    else:
        print('wrong command!')
    print('player: ' + command)
    print('computer: ' + str(computerchoice))
    print(' ')
    print('score: computer' + str(c) + '    player' + str(p))
    print(' ')