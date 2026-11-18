import re
from collections import Counter

from nltk.tokenize import RegexpTokenizer
import spacy

word = r"[A-Za-zА-Яа-яіІїЇєЄґҐ'\-’]+"


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