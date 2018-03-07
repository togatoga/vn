import unicodedata
import nltk
from nltk.corpus import wordnet as wn

def is_japanese(text):
    for ch in text:
        name = unicodedata.name(ch) 
        if "CJK UNIFIED" in name \
        or "HIRAGANA" in name \
        or "KATAKANA" in name:
            return True
    return False

def get_synonyms(word):
    synonyms = []
    values = set()
    for syn in wn.synsets(word):
        for lemma in syn.lemmas():
            if lemma.name() in values:
                continue
            synonyms.append(lemma.name())
            values.add(lemma.name())
    return synonyms