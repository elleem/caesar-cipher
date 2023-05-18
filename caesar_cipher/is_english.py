import nltk
import re

nltk.download("words", quiet=True)
nltk.download("names", quiet=True)

from nltk.corpus import words, names


word_dict = set(words.words() + [word.lower() for word in words.words()])
name_dict = set(names.words())


def count_words(text):

    plaintext_words = text.split()

    word_count = 0

    for plaintext in plaintext_words:
        plaintext = re.sub(r"[^A-Za-z]+", "", plaintext)
        if plaintext.lower() in word_dict or plaintext in name_dict:
            word_count += 1

    return word_count

