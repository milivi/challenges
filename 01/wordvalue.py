from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as dictionary:
        dict_list = dictionary.read().splitlines()
    return dict_list


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    word = word.upper()
    for letter in word:
        my_score = LETTER_SCORES.get(letter) # Handles if there are non alphabetic letters
        if my_score:
            score += my_score
    return score


def max_word_value(my_words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if not my_words:
        my_words = load_words()
    highest_score = 0
    highest_word = ''
    for word in my_words:
        my_score = calc_word_value(word)
        if my_score > highest_score:
            highest_score = my_score
            highest_word = word
    return highest_word


if __name__ == "__main__":
    pass # run unittests to validate
