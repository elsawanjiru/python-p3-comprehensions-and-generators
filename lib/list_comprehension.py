#!/usr/bin/env python3

def return_evens(sequence):
    even_elements = [num for num in sequence if num % 2 == 0]
    return even_elements if even_elements else []

def make_exclamation(sentence_list):
    if not sentence_list:
        return []
    exclaimed_sentences = [sentence + '!' for sentence in sentence_list]
    return exclaimed_sentences
