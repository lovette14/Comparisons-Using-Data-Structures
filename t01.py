"""
------------------------------------------------------------------------
Using array-based list Hash Table to count the total comaparisons in 
a .txt file and the word with the maximum comparison
------------------------------------------------------------------------
Author: Lovette Oyewole
Email:  lovette.oyewole@icloud.com
__updated__ = "2020-04-01"
------------------------------------------------------------------------
"""
from functions import insert_words, comparison_total
from Hash_Set_array import Hash_Set
filename = input("Enter the file name (include .txt): ")
fv = open(filename,"r",encoding = "utf-8")
Hash_Set._LOAD_FACTOR = 20

hs = Hash_Set(20)

(insert_words(fv,hs))


t, m = comparison_total(hs)
print("Using array-based list Hash_Set")
print()
print("Total comparisons: {:,}".format(t))
print("Word with maximum comparisons '{}': {:,}".format(m.word,m.comparisons))