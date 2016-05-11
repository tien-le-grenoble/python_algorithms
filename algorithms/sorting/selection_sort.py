# -*- coding: utf-8 -*-
"""
Created on 10-05-2016
"""

#####################################################################################################
# Groupe d'Étude pour la Traduction/le Traitement Automatique des Langues et de la Parole (GETALP)
# Homepage: http://getalp.imag.fr
#
# Author: Tien LE (ngoc-tien.le@imag.fr)
# URL: tienhuong.weebly.com
#####################################################################################################

"""
Le tri par sélection
--------------------

Il consiste à sélectionner dans le tableau la plus petite valeur et la permuter avec le premier élément du tableau, puis la deuxième plus petite valeur (hors premier élément) et à la permuter avec le deuxième élément du tableau, et ainsi de suite, et cela pour tous les éléments du tableau. 

L' algorithme résultant nécessite malheureusement la recherche dans tout ou partie du tableau de la plus petite valeur possible et ce sans grande optimisation possible. On peut par contre éviter de permuter des valeurs si aucune valeur inférieure n'a été trouvée.

À chaque passage dans la boucle, on effectue une comparaison de moins que lors du passage précédent. Le nombre total de passages est donc de (n-1)+(n-2)+(n-3) et ainsi de suite soit une complexité de l'algorithme de n(n-1)/2 ce qui développé donne une complexité d'ordre O(n**2).

ref: 
Algorithmique - Techniques fondamentales de programmation - Exemples en Python (Franck EBEL, Sébastien ROHAUT)
https://fr.wikipedia.org/wiki/Tri_par_s%C3%A9lection
https://github.com/nryoung/algorithms/blob/master/algorithms/sorting/selection_sort.py

"""
#**************************************************************************#
def sort(liste):
    """
    Trier une liste des nombres dans l' ordre croissant.
    
    :param liste: une liste des nombres
    :rtype: une liste après trier
    """
    for i in range(0, len(liste)):
        iMin = i
        for j in range(i+1, len(liste)):
            if liste[iMin] > liste[j]:
                iMin = j
            #end if
        #end for

        if i != iMin:
            liste[i], liste[iMin] = liste[iMin], liste[i]
        #end if

    return liste
#**************************************************************************#
def sort(liste, ordre_croissant = True):
    """
    Trier une liste des nombres dans l' ordre croissant ou décroissant.
    
    :param liste: une liste des nombres
    :rtype: une liste après trier
    """
    for i in range(0, len(liste)):
        iMin = i
        for j in range(i+1, len(liste)):
            if ordre_croissant is True: #Ascendant ordre
                if liste[iMin] > liste[j]:
                    iMin = j
                #end if
            else: #Descendant ordre
                if liste[iMin] < liste[j]:
                    iMin = j
                #end if
            #end if
        #end for

        if i != iMin:
            liste[i], liste[iMin] = liste[iMin], liste[i]
        #end if

    return liste
#**************************************************************************#
"""
if __name__ == "__main__":
    liste = [2,5,-9,4,8]
    print("Entrée:")
    print(liste)

    # Descendant ordre
    print("*" * 10)
    print("Descendant ordre")    
    result = sort(liste, False) # Descendant ordre
    print(liste) # Note: Référence Variable    
    #print(result)

    # Ascendant ordre
    print("*" * 10)
    print("Ascendant ordre")    
    #result = sort(liste) # Descendant ordre, avec défault valeur
    result = sort(liste, True) # Descendant ordre
    #print(liste) # Note: Référence Variable    
    print(result)

    print("OK")
"""