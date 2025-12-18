import random

print('===================')
print('Rock Paper Scissors')
print('===================')


print('  1)✊ ')
print('  2)✋ ')
print('  3)✌️ ')

player = int(input('Pick a number:' ))

if player == 1:
    print('You chose: ✊')
elif player == 2:
    print('You chose: ✋')
else:
    print('You chose: ✌️')

cpu = random.randint(1, 3)

if cpu == 1:
    print('CPU chose: ✊')
elif cpu == 2:
    print('CPU chose: ✋')
else:
    print('CPU chose: ✌️')

if player == cpu:
    print('TIE')
elif player == 1 and cpu == 3:
    print('The player won!')
elif player == 2 and cpu == 1:
    print('The player won!')
elif player == 3 and cpu == 2:
    print('The player won!')
else:
    print('The CPU won!')