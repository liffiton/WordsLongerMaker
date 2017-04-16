#!/usr/bin/env python3

import re

import nltk
from nltk.corpus import wordnet


# Thanks: http://stackoverflow.com/a/15590384
def get_wordnet_pos(treebank_tag):
    """ Translate treebank parts-of-speech tags into WordNet tags. """
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None


def make_longer_word(word, pos):
    """ Find the longest synonym in WordNet for the given
        word / part-of-speech. """
    synsets = wordnet.synsets(word, pos)
    longest = word
    for synset in synsets:
        for lemma in synset.lemmas():
            new = lemma.name()
            if len(new) > len(longest):
                longest = new
    return longest.replace('_', ' ')


def make_longer_all(text):
    """ Produce a longer version of a given text by applying
        make_longer_word() to every word. """
    tokens = nltk.pos_tag(nltk.word_tokenize(text))

    output = []
    for token in tokens:
        wn_pos = get_wordnet_pos(token[1])
        if wn_pos:
            output.append(make_longer_word(token[0], wn_pos))
        else:
            output.append(token[0])

    outputstr = ' '.join(output)
    # remove spaces before punctuation (overeager; not ideal)
    outputstr = re.sub(r" (\W)", r"\1", outputstr)
    return outputstr


def main():
    """ Simple test. """
    text = "This is a sentence with many words in it, some of which have synonyms, I hope."

    print(text)
    longer = make_longer_all(text)
    print(longer)
    longer_longer = make_longer_all(longer)
    print(longer_longer)
    longer_longer_longer = make_longer_all(longer)
    print(longer_longer_longer)


if __name__ == '__main__':
    main()
