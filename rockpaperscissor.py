import random,time
print("\t\tStone Paper and Scissor Game")
win=0
lose=0
tie=0
while True:
    print('%swin, %s lose, %s tie' % (win, lose, tie))
    while True:
        print("enter your move: (r)ock,(p)aper,(s)cissor or (q)uit")
        user=input()
        if user=='q':
            print("\t\tTHANK YOU")
            print("\texit succesfull....")
            time.sleep(1)
            exit()
        if user=='r' or user=='p' or user=='s':
            break
        print("Type one of it p  r s or q")
    if user=='r':
        print("rock verses.......")
    elif user=='p':
        print("paper verses....")
    elif user=='s':
        print("sciscor verses...")
    rn=random.randint(0,2)
    if rn==0:
        bot='r'
        print('rock')
    elif rn==1:
        bot='p'
        print('paper')
    elif rn==2:
        bot='s'
        print('scissor')
    if user==bot:
        print("It is a tie!!!")
        tie = tie + 1
    elif (user=='r' and bot=='s') or (user=='s' and bot=='p') or(user=='p' and bot=='r'):
        print("You won!!")
        win+=1
    elif (user=='p' and bot=='s') or (user=='s' and bot=='r') or(user=='r' and bot=='p'):
        print("You lose")
        lose+=1

