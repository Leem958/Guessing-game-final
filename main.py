secret = "chameleon"

Clues = [
    'I am a living organsim.', 'I am a vertabrate', 'I am terrestrial.',
    'I am a reptile.', 'I am a lizard.',
    'I mostly eat insects, but i can also eat smaller lizards and birds.',
    'I am part of the iguana sub order.',
    'I have a tongue twice the length of my body.', 'i can change the color of my skin'
]

print(" Liam's Guessing Game \n")
print('You have ten tries to guess what I am thinking of.')
print('Every time you get a question wrong I will give you a hint.\n')
print(
    'If you lose the game a giant lazer will shoot out of your computer and turn you into a hippo\n'
)
score = 10

guess1 = input('first guess: ')
if guess1 == 'chameleon':
    print("You win!")
    print(score)
else:
    print('That is incorrect \n')
    print("hint: " + Clues[0])
    score = 9
    print('\n')
    guess1 = input('second guess: ')
    if guess1 == 'chameleon':
        print("You win!")
        print(score)
    else:
        print('That is incorrect \n')
        print("hint: " + Clues[1])
        score = 8
        print('\n')
        guess1 = input('third guess: ')
        if guess1 == 'chameleon':
            print('You win!')
            print(score)
        else:
            print('That is incorrect \n')
            print("hint: " + Clues[2])
            score = 7
            print('\n')
            guess1 = input('fourth guess: ')
            if guess1 == 'chameleon':
                print("you win!")
                print(score)
            else:
                print('That is incorrect \n')
                print("hint: " + Clues[3])
                score = 6
                print('\n')
                guess1 = input('fith guess: ')
                if guess1 == 'chameleon':
                    print("You win!")
                    print(score)
                else:
                    print('That is incorrect \n')
                    print("hint: " + Clues[4])
                    score = 5
                    print('\n')
                    guess1 = input('sixth guess: ')
                    if guess1 == 'chameleon':
                        print("You win!")
                        print(score)
                    else:
                        print('That is incorrect \n')
                        print("hint: " + Clues[5])
                        score = 4
                        print('\n')
                        guess1 = input('seventh guess: ')
                        if guess1 == 'chameleon':
                            print("You win!")
                            print(score)
                        else:
                            print('That is incorrect \n')
                            print('hint: ' + Clues[6])
                            score = 3
                            print('\n')
                            guess1 = input('eighth guess: ')
                            if guess1 == 'chameleon':
                                print("You win!")
                            else:
                                print('That is incorrect \n')
                                print("hint: " + Clues[7])
                                score = 2
                                print('\n')
                                guess1 = input('ninth guess: ')
                                if guess1 == 'chameleon':
                                    print("You win!")
                                else:
                                    print('That is incorrect \n')
                                    print("hint: " + Clues[8])
                                    score = 1
                                    print('\n')
                                    guess1 = input('tenth guess: ')
                                    if guess1 == 'chameleon':
                                        print("You win!\n")
                                        print(score)
                                    else:
                                        print('That is incorrect \n')
                                        score = 0
                                        print('\n')
                                        print('You lose the game!')
