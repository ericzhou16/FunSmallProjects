import pickle
import random

COUNT = "__count__"  # set string for variable to track count in dictionary
WORDS_ROW = 3  # number of words in a row
GEN_WORDS = 200  # todo: number of words to be generated, change to whatever

with open('Shakespeare.txt', 'r') as f:
    text = f.read()

words = text.replace("\n", " ").lower().split(" ")
words.append(words[0])
mat = {}


def print_mat():
    print("Current \"matrix\": ")
    for k in mat.keys():
        print(f"{k}: ")
        for t in mat[k].keys():
            print(f"\t{t}: {mat[k][t]}")
            pass


def combine_words(start):
    s = ""
    for i in range(WORDS_ROW):
        s += (words[start + i] + " ")
    return s[:-1]


# print(str(words[:-1]))
# print(words[0] + " " + words[1])


for i in range(len(words) - WORDS_ROW):
    cur = combine_words(i)
    next_word = words[i + WORDS_ROW]

    if cur in mat.keys():
        mat[cur][COUNT] += 1
        if next_word in mat[cur].keys():
            mat[cur][next_word] += 1
        else:
            mat[cur][next_word] = 1
    else:
        mat[cur] = {COUNT: 1, next_word: 1}

# print_mat()
# pickle.dump(mat, open("markov_chain.pickle", "wb"))

chain = combine_words(0)
print(chain, end=" ")
for i in range(GEN_WORDS - WORDS_ROW):
    temp = mat[chain]
    r = random.randint(1, temp[COUNT])
    for k in temp.keys():
        if k is not COUNT:
            cur = temp[k]
            if r <= cur:
                ans = k
                break
            else:
                r -= cur
    print(ans, end=" ")
    if WORDS_ROW >= 2:
        chain = chain[chain.find(" ") + 1:] + " " + ans
    else:
        chain = ans
