import string 
class HashTable:

    def __init__(self, table_size = 191) :         # can add additional attributes
        self.table_size = table_size        # initial table size
        self.hash_table = [None]*table_size # hash table
        self.num_items = 0                  # empty hash table

    # key and corresponding value -> None
    # inserts the key-value pair into the hash table / Uses quadratic probing 
    def insert(self, key, value=None):
        horner_val = self.horner_hash(key)
        quad_index = horner_val
        i_index = 0
        if self.hash_table[horner_val] is None: # if index is not occupied
            self.hash_table[horner_val] = [key, [value]]
            self.num_items += 1
        elif self.hash_table[horner_val][0] == key: # index is occupied but with the same key
            if value not in self.hash_table[horner_val][1]:
                self.hash_table[horner_val][1].append(value)
        else:
            none_found = True
            while self.hash_table[quad_index] is not None: # searches for new open spot with quadratic probing
                if self.hash_table[quad_index][0] == key: # non-empty index but index has the same key
                    if value not in self.hash_table[quad_index][1]:
                        self.hash_table[quad_index][1].append(value)
                    none_found = False
                    break
                i_index += 1
                quad_index = (horner_val + (i_index**2)) % self.get_table_size()
            if none_found: # open "None" spot found in hash table
                self.hash_table[quad_index] = [key, [value]]
                self.num_items += 1
        
        if self.get_load_factor() > 0.5: # loadfactor breached -> needs to be rehashed
            temp_item_lst = []
            for item in self.hash_table: # insert all None items into temp_item_lst
                if item is not None:
                    temp_item_lst.append(item)
            self.table_size = (self.table_size *2) + 1 # size = (2* size) +1
            self.num_items = 0
            self.hash_table = [None] * self.table_size
            for value_pair in temp_item_lst: # add all items back to the bigger hash table
                for num in value_pair[1]:
                    self.insert(value_pair[0],num)
        
    # key -> int
    # returns the hash index of the key based on horner's rule
    def horner_hash(self, key):
        loop_num = len(key)
        if loop_num > 8: # only uses the first eight characters of the key
            loop_num = 8
        hash_index = 0
        for i in range(loop_num): # horner's rule
            hash_index += ord(key[i]) * ((31)**(loop_num-1-i))
        hash_index = hash_index % self.table_size
        return hash_index

    # key -> boolean
    # use the get index function to check if item is in the hash table
    def in_table(self, key):
        index = self.get_index(key)
        if index is not None:
            return True
        return False

    # key -> int(index)
    # returns index of the key(if it exists in the hash table) \ uses quadratic proving
    def get_index(self, key):
        horner_val = self.horner_hash(key)
        num_quad = 0
        index = ((horner_val +(num_quad**2)) % self.table_size)
        while self.hash_table[index] is not None: # quadratic probing to traverse through the index where the key could have existed
            if self.hash_table[index][0] == key:
                return index
            else:
                num_quad += 1
                index = ((horner_val +(num_quad**2)) % self.table_size)
        return None
    
    # none -> list
    # returns a list of all keys in the hash table
    def get_all_keys(self):
        key_lst = []
        for i in range(len(self.hash_table)):
           if self.hash_table[i] is not None:
                key_lst.append(self.hash_table[i][0])
        return key_lst

    # key -> value
    # returns the keys corresponding value(s)
    def get_value(self, key):
        index = self.get_index(key)
        if index is not None:
            return self.hash_table[index][1]
        return None

    # returns the number of items in the list
    def get_num_items(self):
        return self.num_items

    # returns the size of the table
    def get_table_size(self):
        return self.table_size

    # returns the load factor of the table
    def get_load_factor(self):
        return self.num_items/self.table_size