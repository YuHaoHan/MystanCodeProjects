"""
File: anagram.py
Name: David
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
dic = {}                     # dictionary used in has_prefix()


def main():
    """
    This program recursively finds all the anagram(s) for the input word and terminates when the
    input string matches the EXIT constant defined at line 19.
    """
    # open the dictionary
    read_dictionary()
    print('"Welcome to stanCode Anagram Generator" (or -1 to quit)')
    while True:
        target = input("Find anagrams for: ")
        # Exit
        if target == "-1":
            break
        # Run the recursive finding program
        elif target.isalpha():
            start = time.time()
            # Case insensitive
            target = target.lower()
            find_anagrams(target)
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end-start} seconds.')
        # Illegal format
        else:
            print("Illegal format!")


def read_dictionary():
    """
    This function open the dictionary file and categorize words by the first two characters
    of every word.
    """
    global dic
    # a, i, o are words with single character
    dic["a"] = ["a"]
    dic["i"] = ["i"]
    dic["o"] = ["o"]
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
                "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    # Loop over 26 alphabets
    for i in range(len(alphabet)):
        for j in range(len(alphabet)):
            head = alphabet[i] + alphabet[j]
            # Make the keys of the dictionary
            dic[head] = []
    # Put words into the specific list
    with open(FILE, "r") as f:
        for line in f:
            word = line.replace("\n", "")
            if len(word) > 1:
                dic[word[:2]].append(word)


def find_anagrams(s):
    """
    :param s: string, the input word
    This function finds all anagrams of the input word and print them on console.
    """
    print("Searching...")
    ans_lst = []   # The list of answers
    count = [0]    # The list to count the number of recursion
    helper(s, ans_lst, "", [], count)   # Helper function
    print(str(len(ans_lst)), "anagrams:", end="")
    print(ans_lst)
    print(count[0])


def helper(s, ans_lst, current_str, current_lst, count):
    """
    This function help find all anagrams of input word by recursion.
    :param s: string, input word
    :param ans_lst: list, the list of answers
    :param current_str: string, the current string in the process of recursion
    :param current_lst: lst, help record the characters that have been used
    :param count: list, help count the number of recursion
    """
    count[0] += 1
    # if the input word has less than 2 character, it can at most have only one anagram
    if len(s) < 2:
        ans_lst.append(s)
        return
    # For words with over 2 character
    else:
        # Base case(the current string has the same length as the input word and is in the dictionary)
        if len(current_str) == len(s) and current_str in dic[current_str[:2]]:
            # Prevent from double counting
            if current_str not in ans_lst:
                ans_lst.append(current_str)
                print("Found:", current_str)
                print("Searching...")
        # Recursive
        else:
            for i in range(len(s)):
                if i not in current_lst:
                    # Choose
                    current_str += s[i]
                    current_lst.append(i)
                    # Explore
                    if len(current_str) <= len(s):
                        # If there is no word starts with current string, there si no need to keep finding
                        if has_prefix(current_str):
                            helper(s, ans_lst, current_str, current_lst, count)
                    # Unchoose
                    current_str = current_str[:len(current_str)-1]
                    current_lst.pop()


def has_prefix(sub_s):
    """
    :param sub_s: the current string in the recursion
    :return: True when there are words start with sub_s, False when there are not
    """
    if len(sub_s) <= 1:
        return True
    else:
        # Loop over the dictionary
        for word in dic[sub_s[:2]]:
            if word.startswith(sub_s):
                return True
        return False


if __name__ == '__main__':
    main()
