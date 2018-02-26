def start_hangman (word):
    while word != "stop" :
        letters_wrong = list()
        letters_guessed = list()
        stages = [
            "__________          \n         |          \n",
            "         O          \n",
            "        /",
            "|",
            "\         \n",
            "        /",
            " \         \n",
            "                    "]
        letters_in_word = list(word)
        board = ["_"]  * len(word)
        win = False
        print("Got it")
        print("\n" * 50)
        
        message = "guess a letter: "
        char = input(message)
        while len(letters_wrong) < len(stages) -1:
            if char == "stop":
                exit(0)
            while char in letters_guessed:
                print("you guesses that already.")
                char = input(message)
            if char in letters_in_word:
                letters_guessed.append(char)
                while char in letters_in_word:
                    correct_index = letters_in_word.index(char)
                    board[correct_index] = char
                    letters_in_word[letters_in_word.index(char)] = "#"
                print("YUP!")
                
            else :
                print("NOPE!")
                letters_wrong.append(char)
                letters_guessed.append(char)
                
            print("".join(stages[0:len(letters_wrong)+1]))
            print(" ".join(board))
            print("letters you guessed wrong:" + ",".join(letters_wrong))

            if "_" not in board :
                print("you won!")
                print(" ".join(board))
                print("".join(stages[0:len(letters_wrong)+1]))
                win = True
                break
            message = "guess a letter: "
            char = input(message)
        if not win :
            print("".join(stages))
            print("you lose. the word was " +'"' +word+ '".')
        word = input("type the word you want to use for hangman: ")
    

yes_or_no = input("""
      Wlcome to hangman! \n
      Player 1. choose a word with no letter repititions \n
      Player 2. guess letters you think are in the word.\n
      IF you guess enough wrong letters to hang a full man OR woman bc 2018,
      you lose.\n
      IF you guess the word, obviously, you win. \n
      TYPE "stop" to end the game or to not play again. \n
      Do you wanna Play? type "yes" or "no":
      """)
if yes_or_no == "yes" :
    start_hangman(input("type the word you want to use for hangman: "))

