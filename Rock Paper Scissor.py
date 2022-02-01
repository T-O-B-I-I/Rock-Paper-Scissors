import random

def play():
    user = input("What's your choice?\n'r' for rock, 'p' for paper, 's' for scissor\n\n")
    computer =  random.choice(['r','p','s'])

    if user == computer:
        return 'it\'s a tie'

# r>s, s>p, p>r

    elif user > computer:
         return 'you won!'

    else:
         return  'You lost'

def is_win(player,opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r') :
        return True

print(play())        
