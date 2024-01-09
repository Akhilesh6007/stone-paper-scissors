import random

best_of_rounds = int(input('Enter no.of rounds you want to play: '))

user_score, computer_score = 0, 0

while True:
    user_play = input('Enter your play: ').lower()

    if (random.randint(1, 3) / 3) <= 0.3: computer_play = 'stone'
    elif (random.randint(1, 3) / 3) <= 0.6: computer_play = 'paper'
    else: computer_play = 'scissor'

    if user_play == computer_play:
        print('It is a draw! ☹')
        print('Computer chose', computer_play)
        print('Score:', 'User-', user_score, 'Computer-', computer_score)
    elif user_play == 'paper' and computer_play == 'scissor':
        computer_score += 1
        print('Computer won! 😉')
        print('Computer chose', computer_play)
        print('Score:', 'User-', user_score, 'Computer-', computer_score)


    elif user_play == 'scissor' and computer_play == 'stone':
        computer_score += 1
        print('Computer won! 😉')
        print('Computer chose', computer_play)
        print('Score:', 'User-', user_score, 'Computer-', computer_score)


    elif user_play == 'stone' and computer_play == 'paper':
        computer_score += 1
        print('Computer won! 😉')
        print('Computer chose', computer_play)
        print('Score:', 'User-', user_score, 'Computer-', computer_score)


    elif user_play == 'paper' and computer_play == 'stone':
        user_score += 1
        print('User won! 🙄')
        print('Computer chose', computer_play)
        print('Score:', 'User-', user_score, 'Computer-', computer_score)


    elif user_play == 'scissor' and computer_play == 'paper':
        user_score += 1
        print('User won! 🙄')
        print('Computer chose', computer_play)
        print('Score:', 'User-', user_score, 'Computer-', computer_score)


    elif user_play == 'stone' and computer_play == 'scissor':
        user_score += 1
        print('User won! 🙄')
        print('Computer chose', computer_play)
        print('Score:', 'User-', user_score, 'Computer-', computer_score)
    
    print('*******************************************************************')


    if user_score == best_of_rounds:
        print('Congratulations User won! 🙄')
        print('Score:', 'User-', user_score, 'Computer-', computer_score)
        break
    elif computer_score == best_of_rounds:
        print('Congratulations Computer won! 😉')
        print('Score:', 'User-', user_score, 'Computer-', computer_score)
        break