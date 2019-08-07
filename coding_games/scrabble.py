import sys

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

scores = {
    'e': 1,
    'a': 1,
    'i': 1,
    'o': 1,
    'n': 1,
    'r': 1,
    't': 1,
    'l': 1,
    's': 1,
    'u': 1,
    'd': 2,
    'g': 2,
    'b': 3,
    'c': 3,
    'm': 3,
    'p': 3,
    'f': 4,
    'h': 4,
    'v': 4,
    'w': 4,
    'y': 4,
    'k': 5,
    'j': 8,
    'x': 8,
    'q': 10,
    'z': 10
}

word = []

n = int(input())
for i in range(n):
    word.append(input())
letters = input()

best_word = 'invalid word'
best_char = ''
best_score = 0


def calculate_score(word):
    score = 0
    for c in word:
        if c in letters:
            score += scores[c]
        else:
            return -1

    return score


for w in word:
    new = "".join(set(w))

    score = calculate_score(new)

    if score > best_score:
        best_score = score
        best_word = w
        best_char = new
    elif new == best_char:
        best_word = w if len(w) < len(best_word) else best_word


print(best_word)


