import json
from collections import defaultdict
import suppression_caractere as sc


def main():
    #lecture du fichier d'entrée
    fichier = open("startups", "r")
    texte = fichier.read()

    with open("dictionnaire", "r") as dictionnaire:
        dico = json.loads(dictionnaire.read())

    #suppression des caracteres non alphanumeriques,
    #des emails et des urls
    texte_alpha_num = sc.supprime_tout(texte)

    #Suppression des majuscules dans le dico
    #et dans le texte
    texte_sans_maj = texte_alpha_num.lower()

    dico_sans_maj = dict()

    for mot, words in dico.items():
        mot_sans_maj = mot.lower()
        words_sans_maj = []
        for word in words:
            words_sans_maj.append(word.lower())
        dico_sans_maj[mot_sans_maj] = words_sans_maj

    #Traduction des mots par l'intermédiaire du dictionnaire
    #Stockage dans un dictionnaire: mot/nombre d'occurences
    liste_mots = texte_sans_maj.split()
    dico_traduit = defaultdict(lambda: 0)
    for mot in liste_mots:
        if mot in dico_sans_maj:
            if mot in dico_sans_maj[mot]:
                dico_traduit[mot] += 1
            else:
                dico_traduit[dico_sans_maj[mot][0]] += 1
        else:
            dico_traduit[mot] += 1

    #Filtrage des mots grâce à la stoplist
    stoplist = open("StopList", "r")
    stopstring = stoplist.read()

    stoplist = stopstring.split("\n")

    for word in stoplist:
        if word in dico_traduit:
            del dico_traduit[word]

    #Ordonnancement des mots dans l'ordre decroissant de leur apparition
    #Plotter la frequence en fonction du rang

#Enlever les accents

#7)Constituer le dictionnaire

#8)Calculer le document Frequency df = # de docs qui contiennent le mot


    print(dico_traduit)
    #print(dico_sans_maj)

# 9)Indexation directe des docs suivant les codages:
# -Tf
# (index_du_mot_dans_dico:#apparition i:n i+5:42)  avec i index et n nombre d'apparition)
#
# -Tf-idf
# avec idf = ln(N/df), N le # de docs dans la collection

main()
