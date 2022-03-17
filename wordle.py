def main():
    print('Hello from wordle.')

    # The word
    answer = 'thing'

    guess = input('Guess: ')

    print(check_guess(guess, answer))


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
