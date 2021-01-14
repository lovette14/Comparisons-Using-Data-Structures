"""
------------------------------------------------------------------------
Using linked BST Hash Table to count the total comaparisons in 
a .txt file and the word with the maximum comparison
------------------------------------------------------------------------
Author: Lovette Oyewole
Email:  lovette.oyewole@icloud.com
__updated__ = "2020-04-01"
------------------------------------------------------------------------
"""
from Hash_Set_BST import Hash_Set
from functions import insert_words, comparison_total
filename = input("Enter the file name (include .txt): ")
fv = open(filename,"r",encoding = "utf-8")

hs = Hash_Set(20)

(insert_words(fv,hs))

t ,m= comparison_total(hs)
print("Using linked BST Hash_Set")
print()
print("Total comparisons: {:,}".format(t))
print("Word with maximum comparisons '{}': {:,}".format(m.word,m.comparisons))