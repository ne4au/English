import os
from functools import reduce

voc_directory = os.fsencode('../Vocabulary')


def get_all_vocabulary_files(directory):
    return map(
        filter(
            lambda filename: filename.endswith('.md'),
            [os.fsdecode(file) for file in os.listdir(directory)]))

def replace_to_tags(original_file):

def replace_link_to_tag(directory: bytes, filename: str):
    with (open(directory.decode("utf-8") + '/' + filename, 'r') as f):
        text = (f.read()
                .replace('[[Adj]]', '#Adjective')
                .replace('[[N]]', '#Noun')
                .replace('[[V]]', '#Verb')
                .replace('[[Adv]]', '#Adverb')
                .replace('[[Pronoun]]', '#Pronoun')
                .replace('[[Phrase]]', '#Phrase')
                .replace('[[Phrasal verb]]', '#Phrasal_Verb')
                .replace('[[Idiom]]', '#Idiom')
                .replace('[[Conjunction]]', '#Conjunction')
                .replace('[[UK]]', '#UK')
                .replace('[[US]]', '#US')
                .replace('[[Approving]]', '#Approving')
                .replace())
