import os
import re

voc_directory = os.fsencode('../Vocabulary')
texts_directory = os.fsencode('../Texts to learn')


def get_all_md_files_in_directory(directory: str) -> [str]:
    return filter(
        lambda filename: filename.endswith('.md'),
        [os.fsdecode(file) for file in os.listdir(directory)])

def get_all_vocab_words(directory):
    return map(
        lambda filename: filename[:-3],  # removes `.md`
        get_all_md_files_in_directory(directory))

def normalize(word : str) -> str:
    return word[0].upper() + word[1:].lower()

def extract_all_vocabulary_words_from_text(directory: bytes, filename : str) -> set[str]:
    with open(directory.decode("utf-8") + '/' + filename, 'r') as f:
        return set(map(
            normalize,
            re.findall(
                r'\[\[([a-zA-Z]+)]]',
                f.read())))


def get_all_text_words(directory) -> set[str]:
    result : set[str] = set()
    for text_file in get_all_md_files_in_directory(directory):
        result.update(extract_all_vocabulary_words_from_text(directory, text_file))
    return result

all_words = set(get_all_vocab_words(voc_directory))
text_words = get_all_text_words(texts_directory)

words_that_are_not_included_in_texts = all_words.difference(text_words)
print(words_that_are_not_included_in_texts)
print(len(words_that_are_not_included_in_texts))