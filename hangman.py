from obrazky import obrazek
import random

def vyber_slova():
    """ Vrati nahodne vybrane slovo z daneho souboru. """
    soubor = open('dictionary.txt')
    soubor1 = soubor.read()
    roz_soubor = soubor1.split('\n')
    slovo = random.choice(roz_soubor)
    slovo = slovo.lower()
    return slovo

def pismeno_in_slovo(pole, slovo, pismeno):
    index = 0
    while pismeno in slovo[index:]:
        pozice = slovo.index(pismeno, index)
        pole = pole[:pozice] + pismeno + pole[pozice + 1:]
        index = pozice + 1
    return pole

def hangman():
    vybrane_slovo = vyber_slova()
    pole = '-' * len(vybrane_slovo)

    print ('Vychozi pole:', pole)
    pocet_neuspechu = 0
    while '-' in pole and pocet_neuspechu < len(obrazek):
        pismeno = str(input('Zvol pismeno:'))
        if len(pismeno) != 1:
            print ('Zadej pouze jedno pismeno!')
            continue
        if pismeno in vybrane_slovo:
            pole = pismeno_in_slovo(pole, vybrane_slovo, pismeno)
            print (pole)
        else:
            print ('Toto pismeno ve slove neni')
            pocet_neuspechu = pocet_neuspechu + 1
            print ('Pocet neuspechu:',pocet_neuspechu)
            zobrazeny_obrazek = obrazek[pocet_neuspechu - 1]
            print (zobrazeny_obrazek)
    if '-' in pole:
        return 'Konec hry, prohrals! Hledane slovo bylo ' + str(vybrane_slovo) + '.'
    else:
        return 'Konec hry, gratuluji k uhadnutemu slovu: ' + str(vybrane_slovo) + '.'

print(hangman())
