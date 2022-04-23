# sometimes run wrong
# why
# File "play_dice.py", line 40, in <module>
# coin_user += result
# TypeError: unsupported operand type(s) for +=: 'int' and 'NoneType'


from random import randrange

coin_user,coin_bot = 3,3
rounds_of_game = 0

def bet(dice,wager):
    if dice == 7:
        print(f'The dice is {dice};\nDRAW!\n')
        return 0
    elif dice < 7:
        if wager == 's':
            print(f'The dice is {dice};\nYOU WIN!\n')
            return 1
        else:
            print(f'The dice is {dice};\nYOU LOST!\n')
            return -1
    elif dice < 7:
        if wager == 'b':
            print(f'The dice is {dice};\nYOU LOST!\n')
            return -1
        else:
            print(f'The dice is {dice};\nYOU WIN!\n')
            return 1
        
while True:
    print(f'YOU: {coin_user}\t Bot:{coin_bot}')
    dice = randrange(2,13)
    
    rounds_of_game += 1
    wager = input("What's your bet: \n")
    result = bet(dice,wager)

    if wager == 'q':
        break
    elif wager == 's':
        coin_user += result
        coin_bot -= result
    elif wager == 'b':
        coin_user += result
        coin_bot -= result
        
    if coin_user == 0:
        print('Woops,you have LOST ALL,and game over!')
        break
    elif coin_bot == 0:
        print('Woops,the robots have LOST ALL,the game over!')
        break

print(f"You've played{rounds_of_game} rounds.\n")
print(f"You have {coin_user} coin now.\nBye")