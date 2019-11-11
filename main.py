import os

chemin_script = os.path.dirname(os.path.realpath(__file__))
fichier_a_traduire = os.path.join(chemin_script,'braille.txt')

mydict = {
    '*-----': 'a',
    '**----': 'b',
    '*--*--': 'c',
    '*--**-': 'd',
    '*---*-': 'e',
    '**-*--': 'f',
    '**-**-': 'g',
    '**--*-': 'h',
    '-*-*--': 'i',
    '-*-**-': 'j',
    '*-*---': 'k',
    '***---': 'l',
    '*-**--': 'm',
    '*-***-': 'n',
    '*-*-*-': 'o',
    '****--': 'p',
    '*****-': 'q',
    '***-*-': 'r',
    '-***--': 's',
    '-****-': 't',
    '*-*--*': 'u',
    '***--*': 'v',
    '-*-***': 'w',
    '*-**-*': 'x',
    '*-****': 'y',
    '*-*-**': 'z',
    '******': 'é',
    '***-**': 'à',
    '-***-*': 'è',
    '-*****': 'ù',
    '*-----': 'â',
    '**---*': 'ê',
    '*--*-*': 'î',
    '*--***': 'ô',
    '*---**': 'û'
}

traduction = []

with open(fichier_a_traduire,'r') as infile:
    phrase = infile.read().splitlines()
    for mot in phrase:
        phrase_len = len(mot)
        nb_lettre = phrase_len/6
        nb_cara_in_mot = 6
        while nb_lettre > 0:
            lettre_en_braille = mot[nb_cara_in_mot-6:nb_cara_in_mot]
            nb_cara_in_mot = nb_cara_in_mot + 6
            nb_lettre = nb_lettre - 1
            traduction.append(mydict.get(lettre_en_braille))
        traduction.append("\n")
print(*traduction)