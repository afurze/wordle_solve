def main():
    # Get all the words from the file
    words = {}
    with open('word-frequency.txt') as f:
        line = f.readline()
        while line:
            # words += line.split()
            line = line.split()
            words[line[0]] = int(line[2])
            line = f.readline()

    # Find only five letter words
    five_letter_words = {}
    for key, val in words.items():
        if len(key) == 5 and val != 0:
            five_letter_words[key] = val

    print(five_letter_words)


if __name__ == '__main__':
    main()
