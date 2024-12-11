"""retourne la liste de tuples encodant une chaîne de caractères passée en argument 
selon des algorithmes itératif et récursif
"""
import sys
sys.setrecursionlimit(2000)

#### Imports et définition des variables globales


#### Fonctions secondaires


def artcode_i(s:tuple)->list:
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument 
    selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """


    if not s:
        return []

    result = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append((s[i - 1], count))
            count = 1
    result.append((s[-1], count))
    return result

def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument 
    selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    if not s:
        return []
    count = 1
    while count < len(s) and s[count] == s[0]:
        count += 1
    return [(s[0], count)] + artcode_r(s[count:])


#### Fonction principale


def main():
    """Fonction principale du code
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
