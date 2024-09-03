import os
from functools import reduce

directory = os.fsencode('../Vocabulary')


def get_all_vocab_words(directory):
    return map(
        lambda filename: filename[:-3],  # removes `.md`
        filter(
            lambda filename: filename.endswith('.md'),
            [os.fsdecode(file) for file in os.listdir(directory)]))

all_words = list(get_all_vocab_words(directory))

words: str = reduce(
    lambda acc, next: acc + ', ' + next,
    all_words)
print(words)

count : int = len(all_words)
print(count)