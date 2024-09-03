
file_name = '../Texts to learn/Revival Amidst Adversity.md'
with open(file_name, 'r') as f:
    print(f.read().replace('[[', '').replace(']]', ''))