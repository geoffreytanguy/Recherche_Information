import re

def supprime_tout(texte):

    url = re.compile(r'https?:\S*')
    url2 = re.compile(r'www\S*')
    email = re.compile(r'\S*@\S*')
    alpha = re.compile(r'[^a-zA-Z0-9éèêëàâäîïüûöô]')


    texte = url.sub(' ', texte)
    texte = url2.sub(' ', texte)
    texte = email.sub(' ', texte)
    texte = alpha.sub(' ', texte)

    return texte
