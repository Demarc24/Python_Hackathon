"""In many natural languages we can find some pairs of words which could be transformed to each other
by changing the order of letters. I.e. they consist of the same set of letters, for example:
act - cat, ate - eat - tea.Such words are called anagrams and as we see in the third example sometimes
there are more than two words. Your task is to find out the amount of anagrams for given word by
the dictionary."""

"""SAMPLE USAGE
Start the program and prompt the user for a word. You can specify options to extend the funcitonality
of the program, but it's up to you how you'll implement it and what options you'll decide to use.
In general, the program should be able to run with:
[test@test ]$ ./anagrams.py
Provide the word to find anagrams for: slot
The output should be:
There are 2 anagrams we've been able to find for the word slot:
 * lots
 * lost"""

# define a function to load the dictionary to internal structure
# we will load it from external file
# def load_dict():
#     pass

# process the input word we're working with

# logic behind the anagram program
# ideal case - work with the internal structure (array) with all
# words from the dictionary and try to find proper letters in those words
# it is up to you how you'll handle this area, try to figure this out

# print the requested anagrams

word = str(input('Zadej slovo: '))
serazani = sorted(word)
slovo = ''.join(serazani)


soubor = open('dictionary.txt')
soubor1 = soubor.read()
roz_soubor = soubor1.split('\n')
seznam = []
"""
for index, radek in enumerate(roz_soubor):
    radek1 = sorted(radek)
    nove_slovo = ''.join(radek1)
    nove_slovo = nove_slovo.strip()
    if slovo == nove_slovo:
        seznam.append(radek)"""

for radek in roz_soubor:
    radek1 = sorted(radek)
    nove_slovo = ''.join(radek1)
    nove_slovo = nove_slovo.strip()
    if slovo == nove_slovo:
        seznam.append(radek)

if len(seznam) == 0:
    finalni_seznam = 'Zadne mozne kombinace v seznamu.'
else:
    finalni_seznam = ', '.join(seznam)

print('Puvodni slovo:', word)
print('Mozne kombinace:',finalni_seznam)
soubor.close()














#
