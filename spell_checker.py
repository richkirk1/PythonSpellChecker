import re
from collections import Counter

LETTERS = 'abcdefghijklmnopqrstuvwxyz'
DELIMITERS = '[-!~&()\[\]"”:;,.? _\n\t{}]'

WORDS = list(filter(None, re.split(DELIMITERS, open(
    'C:\\Users\\Rich Kirk\\Documents\\Corpus\\A Tale of Two Cities - Charles Dickens.txt', 'r',
    encoding='utf8').read().lower())))
WORDS.extend(list(filter(None, re.split(DELIMITERS, open(
    'C:\\Users\\Rich Kirk\\Documents\\Corpus\\Alice\'s Adventures in Wonderland - Lewis Carroll.txt', 'r',
    encoding='utf8').read().lower()))))
WORDS.extend(list(filter(None, re.split(DELIMITERS,
                                        open('C:\\Users\\Rich Kirk\\Documents\\Corpus\\Dracula - Bram Stoker.txt', 'r',
                                             encoding='utf8').read().lower()))))
WORDS.extend(list(filter(None, re.split(DELIMITERS,
                                        open('C:\\Users\\Rich Kirk\\Documents\\Corpus\\Frankenstein - Mary Shelley.txt',
                                             'r', encoding='utf8').read().lower()))))
WORDS.extend(list(filter(None, re.split(DELIMITERS, open(
    'C:\\Users\\Rich Kirk\\Documents\\Corpus\\Les Miserables - Victor Hugo.txt', 'r',
    encoding='utf8').read().lower()))))
WORDS.extend(list(filter(None, re.split(DELIMITERS,
                                        open('C:\\Users\\Rich Kirk\\Documents\\Corpus\\Moby Dick - Herman Melville.txt',
                                             'r', encoding='utf8').read().lower()))))
WORDS.extend(list(filter(None, re.split(DELIMITERS, open(
    'C:\\Users\\Rich Kirk\\Documents\\Corpus\\Pride and Prejudice - Jane Austen.txt', 'r',
    encoding='utf8').read().lower()))))
WORDS.extend(list(filter(None, re.split(DELIMITERS, open(
    'C:\\Users\\Rich Kirk\\Documents\\Corpus\\The Adventures of Sherlock Holmes - Conan Doyle.txt', 'r',
    encoding='utf8').read().lower()))))
WORDS.extend(list(filter(None, re.split(DELIMITERS, open(
    'C:\\Users\\Rich Kirk\\Documents\\Corpus\\The Adventures of Tom Sawyer by Mark Twain.txt', 'r',
    encoding='utf8').read().lower()))))
WORDS.extend(list(filter(None, re.split(DELIMITERS,
                                        open('C:\\Users\\Rich Kirk\\Documents\\Corpus\\War and Peace - Leo Tolstoy.txt',
                                             'r', encoding='utf8').read().lower()))))


def is_word(word):
    return word in WORDS


def frequency(word):
    return Counter(WORDS).get(word) / sum(Counter(WORDS).values())


def correct_word(word):
    cnt = Counter(WORDS)
    candidates = candidate_words(word)
    return max(candidates, key=frequency)


def candidate_words(word):
    return one_edit(word) or two_edits(word)


# insertion, deletion, transposition, replacement
def one_edit(word):
    insertions = []
    l = len(word)
    for i in range(l):
        for c in LETTERS:
            w = word[0:i] + c + word[i:]
            if w in WORDS:
                insertions.append(word[0:i] + c + word[i:])

    deletions = []
    for i in range(l):
        w = word[0:i] + word[i + 1:]
        if w in WORDS:
            deletions.append(word[0:i] + word[i + 1:])

    transpositions = []
    for i in range(l - 1):
        w = word[0:i] + word[i + 1] + word[i] + word[i + 2:]
        if w in WORDS:

            transpositions.append(word[0:i] + word[i + 1] + word[i] + word[i + 2:])

    replacements = []
    for i in range(l):
        for c in LETTERS:
            w = word[0:i] + c + word[i + 1:]
            if w in WORDS:
                replacements.append(word[0:i] + c + word[i + 1:])

    return set(insertions + deletions + transpositions + replacements)


def two_edits(word):
    edits = []
    first_edits = one_edit(word)
    for edit1 in first_edits:
        edits.extend(one_edit(edit1))
    return edits


def word_check(word):
    if is_word(word):
        print("Spelled correctly")
    else:
        print(correct_word(word))


if __name__ == '__main__':
    some_word = input("Enter a word: ")
    word_check(some_word)
