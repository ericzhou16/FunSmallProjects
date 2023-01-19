from nltk.corpus import gutenberg
print(gutenberg.fileids())
macbeth_words = gutenberg.words('shakespeare-macbeth.txt')
caesar_words = gutenberg.words('shakespeare-caesar.txt')
hamlet_words = gutenberg.words('shakespeare-hamlet.txt')

s = ''
for word in macbeth_words:
    s += ' ' + word
for word in caesar_words:
    s += ' ' + word
for word in hamlet_words:
    s += ' ' + word
s = s.strip()

symbs = '!,.:;)}]?'
for symb in symbs:
    s = s.replace(' ' + symb, symb)
left_bracs = '{[('
for symb in left_bracs:
    s = s.replace(symb + ' ', symb)
s = s.replace(' \' ', '')
s = s.replace(' " ', '')
print(s.lower().strip())

with open("Shakespeare.txt", "w") as text_file:
    text_file.write(s.lower().strip())
