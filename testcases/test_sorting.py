# -*- coding: utf-8 -*-
"""
Created on 10-05-2016
"""

##############################################################################
# Groupe d'Étude pour la Traduction/le Traitement Automatique des Langues
# et de la Parole (GETALP)
#
# Homepage: http://getalp.imag.fr
#
# Author: Tien LE (ngoc-tien.le@imag.fr)
# URL: tienhuong.weebly.com
##############################################################################

import unittest
import random

from algorithms.sorting import selection_sort


class SortingAlgorithmTestCase(unittest.TestCase):
    """
    Shared code for a sorting unit test.
    """

    def setUp(self):
        self.input = list(range(10))

        # Changé élément dans liste
        random.shuffle(self.input)

        self.correct = list(range(10))


class TestSelectionSort(SortingAlgorithmTestCase):
    """
    Test Selection sort on a small range from 0-9
    """

    def test_selection_sort(self):
        # Default: True-ASC; False-DESC
        self.output = selection_sort.sort(self.input)
        self.assertEqual(self.correct, self.output)

"""
if __name__ == "__main__":
    print("OK")
"""

"""Test - Passed
TestCase:
self.input = list(range(10))
self.correct = list(range(10))

$ python3 run_test_unit.py
========================= test session starts ===============================
platform linux -- Python 3.4.3 -- py-1.4.30 -- pytest-2.7.2
rootdir: /home/lent/Develops/Solution/github/python_algorithms, inifile:
plugins: cov
collected 1 items

testcases/test_sorting.py .

======================== 1 passed in 0.03 seconds ============================
Running flake8 code linting
flake8 passed
"""

"""Test Failures
TestCase:
self.input = list(range(10))
self.correct = list(range(11))

$ python3 run_test_unit.py
==================================== test session starts ====================
platform linux -- Python 3.4.3 -- py-1.4.30 -- pytest-2.7.2
rootdir: /home/lent/Develops/Solution/github/python_algorithms, inifile:
plugins: cov
collected 1 items

testcases/test_sorting.py F

====================================== FAILURES =============================
TestSelectionSort.test_selection_sort

self = <testcases.test_sorting.TestSelectionSort
testMethod=test_selection_sort>

    def test_selection_sort(self):
        self.output = selection_sort.sort(self.input)
>       self.assertEqual(self.correct, self.output)
E       AssertionError: Lists differ: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
!= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
E
E       First list contains 1 additional elements.
E       First extra element 10:
E       10
E
E       - [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
E       ?                              ----
E
E       + [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

testcases/test_sorting.py:43: AssertionError
============================== 1 failed in 0.03 seconds ====================
"""
