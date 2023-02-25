pyg = 'ay'

original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    print (original)
else:
    print ('empty')
new_word = word + first + pyg
new_word = original[1:len(new_word)] + first + pyg
print ('translates to:')
print (new_word)
