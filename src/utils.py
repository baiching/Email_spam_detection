import pandas as pd
import re

#data loader of csv file
def load_data(path):
    return pd.read_csv(path)

# data saving
def save_to_csv(data, path):
    data.to_csv(path, index=False)
def remove_special_character(text):
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)

def to_lower(column_name):
    return column_name.str.lower()

def remove_stop_words(sentence):
    stop_words = ["the", "and", "a", "to", "of", "in", "is", "you", "for", "on",
                  "with", "that", "as", "it", "be", "are", "this", "from", "or", "by",
                  "your", "at", "not", "have", "was", "but", "which", "an", "if", "they"]
    # word_list=sentence.split()
    clean_sentence = ' '.join([w for w in sentence if w.lower() not in stop_words])
    return (clean_sentence)
