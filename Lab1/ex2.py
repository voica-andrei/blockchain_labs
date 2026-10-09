import hashlib

hash = '8ec47631827329eb114714a20d9b3eeb8a9a4293bd5d6823af0632e8d4f30dfa'

with open('rockyou.txt', 'r', encoding='latin-1') as f:
    for line in f:
        word = line.strip()
        if hashlib.sha256(word.encode()).hexdigest() == hash:
            print(f'Found the word: {word}')
            break