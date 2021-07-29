"""
File: boggle.py
Name: David
----------------------------------------
This file recursively find the answers of the boggle game whose
4x4 letters board will be entered by users.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
    """
    After users enter 4x4 boggle board, this function finds all correct answers
    of it.
    """
    print("Welcome to boggle!")
    print("Please enter 4 letters in one row and every letter should "
          "be separated from each others by a single space. ")
    # Create boggle board
    board = {}
    # Determine if a game should be started
    start = True
    # Enter the letters
    for i in range(4):
        row = input(str(i+1)+" row of letters: ")
        if format_correct(row):
            # Count the number of the letters in the same row
            count = 0
            for ch in row:
                if ch.isalpha():
                    # Case-insensitive
                    ch = ch.lower()
                    index = str(i)+str(count)  # The first digit is its y-index, and the second digit is its x-index
                    board[index] = ch
                    count += 1
        else:
            print("Illegal input")
            start = False
            break
    if start:
        start = time.time()
        # Find answers recursively
        boggle(board)
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your boggle algorithm: {end - start} seconds.')


def format_correct(row):
    """
    This function help determine if users enter the boggle board in a correct format.
    :param row: string, Entered row of letters
    :return: Boolean, return True if the entered row is in correct format
    """
    if len(row) != 7:
        return False
    else:
        for i in range(len(row)):
            if i % 2 == 0:
                if not row[i].isalpha():
                    return False
            elif i % 2 == 1:
                if row[i] != " ":
                    return False
        return True


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python dictionary.
    The dictionary is categorized by the first two letters of a word.
    """
    dic = {}
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
                "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    # Loop over 26 alphabets to create all possibilities of letters combination
    for i in range(len(alphabet)):
        for j in range(len(alphabet)):
            for k in range(len(alphabet)):
                head = alphabet[i] + alphabet[j] + alphabet[k]
                # Make the keys of the dictionary
                dic[head] = []
    # Put words into the specific list
    with open(FILE, "r") as f:
        for line in f:
            word = line.replace("\n", "")
            if len(word) >= 4:
                dic[word[:3]].append(word)
    return dic


def boggle(board):
    """
    This function finds every possible answer of the boggle game.
    :param board: dict, the boggle board including letters (value) and their indexes (key)
    """
    dic = read_dictionary()
    ans_lst = []
    # Loop every letters as the first character of a word
    for key in board:
        current_str = board[key]
        used_letters = [key]
        # Use helper function to find answers recursively
        boggle_helper(dic, board, current_str, ans_lst, used_letters)
    print("There are "+str(len(ans_lst))+" words in total.")


def boggle_helper(dic, board, current_str, ans_lst, used_letters):
    """
    This is the helper function of boggle(board).
    :param dic: dict, the dictionary read from FILE
    :param board: dict, the boggle board including letters (value) and their indexes (key)
    :param current_str: str, current sting
    :param ans_lst: list, list of found answers
    :param used_letters: list, list of the indexes of used letters
    """
    # Current string is a word in the dictionary
    if len(current_str) >= 4:
        if current_str in dic[current_str[:3]]:
            if current_str not in ans_lst:
                ans_lst.append(current_str)
                print('Found "'+current_str+'"')
    # Current string is not a word in the dictionary but there are words start with current string
    if has_prefix(current_str, dic):
        # Find neighbors
        neighbor = find_neighbor(used_letters)
        # Loop over all the found neighbors
        for index in neighbor:
            # choose
            current_str += board[index]
            used_letters.append(index)
            # explore
            boggle_helper(dic, board, current_str, ans_lst, used_letters)
            # un_choose
            current_str = current_str[:len(current_str)-1]
            used_letters.pop()


def find_neighbor(used_letters):
    """
    This function help find the current position's neighbors that have not been used previously.
    :param used_letters: list, list of the indexes of used letters
    :return: list, list of indexes that are current position's neighbors and not have been used
    """
    neighbor = []
    center = used_letters[len(used_letters)-1]   # Current position
    # x-index and y-index of current position
    x = int(center[1])
    y = int(center[0])
    # Find neighbors
    for i in range(x-1, x+2):
        if 0 <= i <= 3:
            for j in range(y-1, y+2):
                if 0 <= j <= 3:
                    index = str(j) + str(i)
                    if index not in used_letters:
                        neighbor.append(index)
    return neighbor


def has_prefix(sub_s, dic):
    """
    :param dic: dict, the dictionary read from FILE
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    if len(sub_s) <= 2:
        return True
    else:
        # Loop over the dictionary
        for word in dic[sub_s[:3]]:
            if word.startswith(sub_s):
                return True
        return False


if __name__ == '__main__':
    main()
