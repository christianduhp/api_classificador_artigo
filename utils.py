
import spacy
import numpy as np

nlp = spacy.load("pt_core_news_sm", disable=["parser", "ner", "tagger", "textcat"])

def tokenizer(text):
    doc = nlp(text)
    valid_tokens = []

    for token in doc:
        is_valid = not token.is_stop and token.is_alpha
        if is_valid:
            valid_tokens.append(token.text.lower())

    return valid_tokens

def vector_combination_by_sum(words, model):

    result_vector = np.zeros((1, 300))

    for word in words:
        try:
            result_vector += model.get_vector(word)

        except KeyError:
            pass

    return result_vector

