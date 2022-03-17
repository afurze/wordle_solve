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
            quit()


# Generate the colors for each letter in the guess
def check_guess(guess, answer):
    response = ''

    # Check each letter in the guess and response with 'B', 'Y', 'G'
    for x in range(5):
        try:
            letter = guess[x]

            # Check if letter has already occurred in guess
            # If so, the answer must contain an additional of that letter as well
            # else 'B' should be returned
            if guess.count(letter) > 1:
                # Always check if this is the correct position first
                if letter == answer[x]:
                    response += 'G'
                # If a future instance of the letter is in the right place, and
                # the answer does not have two of this letter, return 'B'
                elif (x < 5
                      and guess[x:].index(letter) == answer[x:].index(letter)
                      and answer.count(letter) == 1):
                    response += 'B'
                elif guess[:x].count(letter) == 0:
                    response += 'Y'
                elif answer.count(letter) > 1:
                    response += 'Y'
                else:
                    response += 'B'

            # If there is only one of this letter so far, apply normal rules
            elif letter in answer:
                if letter == answer[x]:
                    response += 'G'
                else:
                    response += 'Y'
            else:
                response += 'B'
        except ValueError:
            response += 'B'

        #print(response)

    return response


if __name__ == '__main__':
    main()
