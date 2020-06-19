import random

print("H A N G M A N")

words = ('python', 'java', 'kotlin', 'javascript')

while True:
    menu_selection = ""
    while menu_selection not in ["play", "exit"]:
        menu_selection = input('Type "play" to play the game, "exit" to quit: ')
    if menu_selection == "exit":
        break
    win = random.choice(words)
    word = list(win)
    dash = ("-" * (len(win)))
    dash_list = list(dash)
    seperator = ''
    dash_str = seperator.join(dash_list)
    solved = []
    solved_str = seperator.join(solved)

    guesses = 0

    while guesses <= 8:
        print()
        print(dash_str)
        letter = input("Input a letter:")
        if len(letter) != 1:
            print("You should input a single letter")
            continue
        if not (letter.isascii() and letter.islower()):
            print("It is not an ASCII lowercase letter")
            continue
        if letter in solved:
            print("You already typed this letter")
            continue


        if letter not in word:
            guesses += 1
            print("No such letter in the word")
        if letter in word:
            for i in range(len(word)):
                if letter == word[i]:
                    dash_list[i] = word[i]
                    seperator = ''
                    dash_str = seperator.join(dash_list)
            if dash_str == win:
                print("You guessed the word!\nYou survived!")
                break

            if letter in solved:
                print("You already typed this letter")
                guesses += 1

        if letter not in solved:
            solved.append(letter)
        if guesses == 8:
            print("You are hanged!")
            break