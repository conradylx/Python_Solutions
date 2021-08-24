def is_isogram(string):
    checked_word = string.lower()
    special_characters = '"!@  # $%^&*()-+?_=,<>/"'
    counter = 0
    for index in range(len(checked_word)):
        if checked_word[index] not in special_characters:
            counter = checked_word.count(checked_word[index])
        if counter > 1:
            return False
    return True


if __name__ == '__main__':
    text = "alphAbet"
    print(is_isogram(text))
