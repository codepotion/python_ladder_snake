import random
import os
ladder = {2: 23, 6: 45, 20: 59, 57: 96, 52: 72, 71: 92}
snake = {50: 5, 43: 17, 56: 8, 73: 15, 84: 58, 87: 49, 98: 40}
player = []
inf = {}
counter = cur = 0
p_n = int(input("Enter PLayers Number : "))
for i in range(p_n):
    pl = input("Enter PLayer Names : ")
    player.append(pl)
for i in player:
    print('Player {0} Start The Game'.format(i))
    while cur < 100:
        start = input('press any key to roll the dice and continue the game or press e to exit from the game ')
        if start != 'e':
            dice = random.randint(1, 6)
            cur += dice
            pre = cur
            if cur in ladder:
                os.system('cls')
                cur = ladder[cur]
                counter += 1
                print('Your Dice Stops on {0}, Previuosly were on {1} You have climbed a ladder and now on {2}'.format(dice, pre, cur))
            elif cur in snake:
                os.system('cls')
                cur = snake[cur]
                counter += 1
                print('Your Dice Stops on {0}, Previuosly were on {1} You have Bitten by a Snake and now on {2}'.format(dice, pre, cur))
            else:
                os.system('cls')
                counter += 1
                print('Your Dice Stops on {0}, You position have been increased and now on {1}'.format(dice, cur))
        else:
            print('You have quit the game')
            break
    inf[i] = counter
    counter = cur = 0

for i in inf:
    win_sc = inf[i]
    win_nm = i
os.system('cls')
for i in inf:
    print("{} = {}".format(i, inf[i]))
    if inf[i] < win_sc:
        win_sc = inf[i]
        win_nm = i

print('Winner is {} with {} moves'.format(win_nm, win_sc))
print('Thanks For Playing')
# Made by Rohan
