"""
------------------------------------------------------------------------
[Array-based list version of the Hasy Set ADT]
------------------------------------------------------------------------
Author: Lovette Oyewole
Email:  lovette.oyewole@icloud.com
__updated__ = "2020-03-23"
------------------------------------------------------------------------
"""

# Imports
from copy import deepcopy
# Use any appropriate data structure here.
from List_array import List
# Define the new_slot slot creation function.
new_slot = List

# Constants
SEP = '-' * 40


class Hash_Set:
    """
    -------------------------------------------------------
    Constants.
    -------------------------------------------------------
    """
    _LOAD_FACTOR = 2

    def __init__(self, slots):
        """
        -------------------------------------------------------
        Initializes an empty Hash_Set of size slots.
        Use: hs = Hash_Set(slots)
        -------------------------------------------------------
        Parameter:
            slots - number of initial slots in Hash Set (int > 0)
        Returns:
            A new Hash_Set object (Hash_Set)
        -------------------------------------------------------
        """
        self._slots = slots
        self._table = []
        self._count = 0

        # Define the empty slots.
        for _ in range(self._slots):
            self._table.append(new_slot())

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the Hash Set.
        Use: n = len(hs)
        -------------------------------------------------------
        Returns:
            the number of values in the Hash Set.
        -------------------------------------------------------
        """
        return self._count

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the Hash Set is empty.
        Use: b = hs.is_empty()
        -------------------------------------------------------
        Returns:
            True if the Hash Set is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def _find_slot(self, key):
        """
        -------------------------------------------------------
        Returns the slot for a key value.
        Use: list = hs._find_slot(key)
        -------------------------------------------------------
        Returns:
            slot - list at the position of hash key in self._table
        -------------------------------------------------------
        """

        # your code here
        hash_key = (hash(key))% self._slots
        
        return self._table[hash_key]


    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the Hash Set contains key.
        Use: b = key in hs
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            True if the Hash Set contains key, False otherwise.
        -------------------------------------------------------
        """

        # your code here
        con = False
            
        for i in self:
            if i == key:
                con = True
                
            else:
                con = False
                    
        return con


    def insert(self, value):
        """
        ---------------------------------------------------------
        Inserts value into the Hash Set, allows only one copy of value.
        Calls _rehash if the Hash Set _LOAD_FACTOR is exceeded.
        Use: inserted = hs.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a comparable data element (?)
        Returns:
            inserted - True if value is inserted, False otherwise.
        -------------------------------------------------------
        """

        # your code here
        
        if self._count >= ( Hash_Set._LOAD_FACTOR * self._slots): #
            self._rehash()  
            inserted = True
            
        else: 
            
            hash_value = (hash(value)) % self._slots
            s = self._find_slot(hash_value)
            p = s._linear_search(value)

            if p == -1:
                inserted = True
              
                
                if self._table[hash_value] is None:
                    s[0]= deepcopy(value)
                    
                else:
                    s.append(deepcopy(value))
                    
                self._count+=1
                        
            else:
                inserted = False
                
            
        return inserted

    def find(self, key):
        """
        ---------------------------------------------------------
        Returns the value identified by key.
        Use: value = hs.find(key)
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            value - if it exists in the Hash Set, None otherwise.
        -------------------------------------------------------
        """

        # your code here

        
    def remove(self, key):
        """
        ---------------------------------------------------------
        Removes the value matching key from the Hash Set, if it exists.
        Use: value = hs.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            value - if it exists in the Hash Set, None otherwise.
        -------------------------------------------------------
        """

        # your code here
        value = None
        if self._count!=0 :
            hash_key = (hash(key))%self._slots
            
            p = self._table[hash_key]._linear_search(key)
           
            if p >-1:
                value = self._table[hash_key].pop(p)
                    
            self._count-=1
       
        return value

    def _rehash(self):
        """
        ---------------------------------------------------------
        Increases the number of slots in the Hash Set and reallocates the
        existing data within the Hash Set to the new table.
        Use: hs._rehash()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """

        # your code here
        self._slots = 2*self._slots+1
        n = []
        
        for i in self._table:
            for j in i:
                n.append(j)
      
        self._table = []
        for _ in range(self._slots):
            self._table.append(new_slot())
        
        for q in n:
            hash_value = (hash(q)) % self._slots
            s = self._find_slot(hash_value)
            p = s._linear_search(q)

            if p == -1:              
                
                if self._table[hash_value] is None:
                    self._table[hash_value]= deepcopy(q)
                    
                else:
                    self._table[hash_value].append(deepcopy(q))
        return
        
    def is_identical(self, target):
        """
        ---------------------------------------------------------
        Determines whether two hash sets are identical.
        Use: b = source.is_identical(target)
        -------------------------------------------------------
        Parameters:
             target - another hash set (Hash_Set)
        Returns:
            identical - True if this hash set contains the same values 
                as other in the same order, otherwise returns False.
        -------------------------------------------------------
        """

        # your code here


    def debug(self):
        """
        USE FOR TESTING ONLY
        ---------------------------------------------------------
        Prints the contents of the Hash Set starting at slot 0,
        showing the slot currently being printed. Used for
        debugging purposes.
        Use: hs.debug()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """

        # your code here 
        print("{} slots".format(self._slots))
        print()
        print("=======================================")
        i = 0
        while i < self._count:
            print("Slot {}".format(i))
            print()
            for j in self._table[i]:
                print(j)
                print()
                
            i+=1

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the hash set
        from first to last slots. Assumes slot has own iterator.
        Use: for v in q:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        for slot in self._table:
            for item in slot:
                yield item