def main():
    print('Hello from wordle.')

    # The word
    answer = 'thing'

    # Run game for six guesses
    for x in range(6):
        # Get a guess
        guess = input('Guess: ')

        # Check and print result
        print(check_guess(guess, answer))

        # Look for win
        if guess == answer:
            print('Win!')


# Generate the colors for each letter in the guess
def check_guess(guess, answer):
    response = ''

    # Check each letter in the guess and response with 'B', 'Y', 'G'
    for x in range(5):
        letter = guess[x]
        if letter in answer:
            if letter == answer[x]:
                response += 'G'
            else:
                response += 'Y'
        else:
            response += 'B'

    return response


if __name__ == '__main__':
    main()
