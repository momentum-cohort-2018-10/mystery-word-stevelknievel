import random


def open_text_file(file):
    """
    Opens text file, makes list and removes extraneous characters
    """
    word_file = open(file, 'r')
    open_file = word_file.readlines()
    open_file = [word.replace('\n', '').lower() for word in open_file]
    # print(open_file)
    return open_file


def difficulty_level_list(word_list, level):
    """
    Iterates words in txt file, pulls words in varying lengths
    """
    difficulty_level_word_list = []

    for word in word_list:
        if level == "easy":
            if len(word) == 3 or len(word) == 4:
                difficulty_level_word_list.append(word)

        if level == "medium":
            if len(word) == 5 or len(word) == 6:
                difficulty_level_word_list.append(word)

        if level == "hard":
            if len(word) > 7:
                difficulty_level_word_list.append(word)

    print(random.choice(difficulty_level_word_list))


def user_level_choice():
    """
    Propts user to type level of difficulty, passes choice into difficulty
    level list fucntion.
    """
    user_input = input("Type easy medium or hard in lowercase ")

    difficulty_level_list(open_text_file("words.txt"), user_input)


user_level_choice()


# Still needed:  
# 1. Word appears as underscores 
# 2. Prompt user to guess letters
# 3. Count guesses that are wrong, up to 8 total
# 4. Ask user if he/she would like to play again