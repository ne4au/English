import os
from functools import reduce

voc_directory = os.fsencode('../Vocabulary')
phrase_directory = os.fsencode('../Phrases')


def get_all_vocabulary_files(directory):
    return filter(
        lambda filename: filename.endswith('.md'),
        [os.fsdecode(file) for file in os.listdir(directory)])

def replace_to_tags(original_text : str, links_to_change: [(str, str)]):
    result = original_text
    for link in links_to_change:
        result = result.replace(f'[[{link[0]}]]', f'#{link[1]}')
    return result

def replace_link_to_tag(directory: bytes, filename: str):
    with open(directory.decode("utf-8") + '/' + filename, 'r', encoding="utf8") as f:
        text = replace_to_tags(f.read(), [
            ('Adj', 'Adjective'),
            ('N', 'Noun'),
            ('V', 'Verb'),
            ('Adv', 'Adverb'),
            ('Pronoun', 'Pronoun'),
            ('Phrase', 'Phrase'),
            ('Phrasal verb', 'Phrasal_Verb'),
            ('Phrasal verb', 'Phrasal_Verb'),
            ('Idiom', 'Idiom'),
            ('Conjunction', 'Conjunction'),
            ('UK', 'UK'),
            ('US', 'US'),
            ('Approving', 'Approving'),
            ('Architecture', 'Architecture'),
            ('Disapproving', 'Disapproving'),
            ('Formal', 'Formal'),
            ('Humorous', 'Humorous'),
            ('Informal', 'Informal'),
            ('Law', 'Law'),
            ('Literary', 'Literary'),
            ('Medical', 'Medical'),
            ('Offensive', 'Offensive'),
            ('Old use', 'Old_Use'),
            ('Old-fashioned', 'Old_Fashioned'),
        ])

    with open(directory.decode("utf-8") + '/' + filename, 'w', encoding="utf8") as f:
        f.write(text)

for voc_file in get_all_vocabulary_files(voc_directory):
    replace_link_to_tag(voc_directory, voc_file)

for voc_file in get_all_vocabulary_files(phrase_directory):
    replace_link_to_tag(phrase_directory, voc_file)