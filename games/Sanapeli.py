import random

word_bank = ["kissa", "syke", "meikki", "auto", "kalja", "lentokoneturbiini", "aasi", "sairaala"]

word = random.choice(word_bank)

guessedWord = ['_'] * len(word)

attempts = 10

while attempts > 0:
    print('\nNykyinen sana: ' + ' '.join(guessedWord))

    guess = input('Arvaa sana: ').lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print('Hyvä arvaus!')
    else:
        attempts -= 1
        print('Väärä arvaus, yrityksiä jäljellä: ' + str(attempts))
    if '_' not in guessedWord:
        print('\nOnneksi olkoon! Arvasit sanan: ' + word)
        break

if attempts == 0 and '_' in guessedWord:
    print('\nYritykset loppu, sori! Sana oli: ' + word)
