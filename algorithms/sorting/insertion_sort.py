# -*- coding: utf-8 -*-
##############################################################################
# Groupe d'Étude pour la Traduction/le Traitement Automatique des Langues
# et de la Parole (GETALP)
#
# Homepage: http://getalp.imag.fr
#
# Author: Tien LE (ngoc-tien.le@imag.fr)
# URL: tienhuong.weebly.com
##############################################################################

u"""
Tri par insertion
-----------------
En informatique, le tri par insertion est un algorithme de tri classique,
que la plupart des personnes utilisent naturellement pour trier des cartes
à jouer : prendre les cartes mélangées une à une sur la table, et former
une main en insérant chaque carte à sa place.

En général, le tri par insertion est beaucoup plus lent que
d'autres algorithmes comme le tri rapide (ou quicksort) et le tri fusion
pour traiter de grandes séquences, car sa complexité asymptotique
est quadratique.

Le tri par insertion est cependant considéré comme le tri le plus efficace
sur des entrées de petite taille. Il est aussi très rapide lorsque
les données sont déjà presque triées. Pour ces raisons, il est utilisé
en pratique en combinaison avec d'autres méthodes comme le tri rapide.

En programmation informatique, on applique le plus souvent ce tri à
des tableaux. La description et l'étude de l'algorithme qui suivent
se restreignent à cette version, tandis que l'adaptation à des listes
est considérée plus loin.

La complexité est alors Θ(n*n).

Ref:
https://fr.wikipedia.org/wiki/Tri_par_insertion
https://github.com/nryoung/algorithms/blob/master/algorithms/sorting/insertion_sort.py
"""


def sort(liste, ordre_croissant=True):
    u"""
    Trier une liste des nombres dans l' ordre croissant ou décroissant.

    :param liste: une liste des nombres
    :rtype: une liste après trier
    """
    for n in range(1, len(liste)):
        item = liste[n]
        hole = n

        if ordre_croissant:
            while hole > 0 and liste[hole - 1] > item:
                liste[hole] = liste[hole - 1]
                hole = hole - 1
        else:
            while hole > 0 and liste[hole - 1] < item:
                liste[hole] = liste[hole - 1]
                hole = hole - 1

        liste[hole] = item
    return liste
