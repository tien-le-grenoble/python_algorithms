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

import unittest
import random

from algorithms.sorting import (
	selection_sort
	)
#**************************************************************************#
class SortingAlgorithmTestCase(unittest.TestCase):
    """
    Shared code for a sorting unit test.
    """

    def setUp(self):
        self.input = list(range(10))
        random.shuffle(self.input) # Changé élément dans liste
        self.correct = list(range(10))

#**************************************************************************#
class TestSelectionSort(SortingAlgorithmTestCase):
    """
    Test Selection sort on a small range from 0-9
    """

    def test_selection_sort(self):
        self.output = selection_sort.sort(self.input)
        self.assertEqual(self.correct, self.output)
#**************************************************************************#
"""
if __name__ == "__main__":
	print("OK")
"""