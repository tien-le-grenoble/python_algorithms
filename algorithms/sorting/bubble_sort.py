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
Le tri à bulles
---------------
Le tri à bulles ou tri par propagation est un algorithme de tri. Il consiste
à comparer répétitivement les éléments consécutifs d'un tableau, et à
les permuter lorsqu'ils sont mal triés. Il doit son nom au fait qu'il déplace
rapidement les plus grands éléments en fin de tableau, comme des bulles d'air
qui remonteraient rapidement à la surface d'un liquide.

Le tri à bulles est souvent enseigné en tant qu'exemple algorithmique,
car son principe est simple. Mais c'est le plus lent des algorithmes de
tri communément enseignés, et il n'est donc guère utilisé en pratique.

La complexité est alors Θ(n*n).

ref:
https://fr.wikipedia.org/wiki/Tri_%C3%A0_bulles
https://github.com/nryoung/algorithms/blob/master/algorithms/sorting/bubble_sort.py
"""


def sort(liste, ordre_croissant=True):
    u"""
    Trier une liste des nombres dans l' ordre croissant ou décroissant.

    :param liste: une liste des nombres
    :rtype: une liste après trier
    """
    length_liste = len(liste)
    for _ in range(length_liste):
        for n in range(1, length_liste):
            if ordre_croissant:
                if liste[n] < liste[n - 1]:
                    liste[n - 1], liste[n] = liste[n], liste[n - 1]
            else:
                if liste[n] > liste[n - 1]:
                    liste[n - 1], liste[n] = liste[n], liste[n - 1]
    return liste
