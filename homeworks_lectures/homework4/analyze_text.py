import re
import unittest
from collections import Counter

from nltk.tokenize import RegexpTokenizer
import spacy

word = r"[\w\d'\-’]+"


def read_file(path):
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        return None, "Файл не знайдено."
    except UnicodeDecodeError:
        return None, "Файл не в кодуванні UTF-8."
    if not text.strip():
        return None, "Файл порожній."
    
    return text, None


def get_words(text: str, library="nltk") -> list:
    tokens = RegexpTokenizer(word).tokenize(text)
    if library == "spacy":
        tokens = [t.text for t in spacy.blank("xx").make_doc(text)]
    else:
        tokens = RegexpTokenizer(word).tokenize(text)
    return [t.lower() for t in tokens if re.fullmatch(word, t)]


def count_words(words):
    return len(words)


def frequency(words):

    return Counter(words).most_common(20)


class Tests(unittest.TestCase):
    def test_word_count(self):
        self.assertEqual(count_words(get_words("Hello, world! Привіт, світе! 123")), 4)

    def test_frequency(self):
        freq = frequency(get_words("Data data DATA science"))
        self.assertEqual(freq["data"], 3)
        self.assertEqual(list(freq)[0], "data")

    def test_empty_text(self):
        self.assertEqual(get_words("   "), [])
        self.assertEqual(get_words("123 !!!"), [])

    def test_file_errors(self):
        self.assertEqual(read_file("no_such_file.txt")[1], "Файл не знайдено.")

    def test_libraries_agree(self):
        text = "М'яч летить. Привіт, world! Привіт!"
        self.assertEqual(get_words(text, "nltk"), get_words(text, "spacy"))