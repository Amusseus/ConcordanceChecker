from hash_quad import *
import string

class Concordance:

    def __init__(self):
        self.stop_table = None          # hash table for stop words
        self.concordance_table = None   # hash table for concordance

    # filename -> none
    # adds all the words from the stop file to the stop table
    def load_stop_table(self, filename):
        try: # try except to avoid filenotfounderror
            stop_file = open(filename,'r')
            stop_hash = HashTable()
            for line in stop_file: # reads line by line and adds the word
                word_lst = line.split()
                for word in word_lst:
                    stop_hash.insert(word)
            self.stop_table = stop_hash    
            stop_file.close()        
        except FileNotFoundError:
            raise FileNotFoundError

    # filename -> none
    # adds all the words from the file given that its not one of the stop words into the concordance table
    def load_concordance_table(self, filename):
        try: # uses try except to avoid filenotfounderror
            load_file = open(filename,'r')
            word_hash = HashTable()
            line_num = 1
            for line in load_file: # reads line by line 
                # removes punctuation from the line
                no_apostro = ""
                for character in line:
                    if not character == "'":
                        no_apostro += character
                no_punctuation = ""
                for character in no_apostro:
                    if character in string.punctuation:
                        no_punctuation += " "
                    else:
                        no_punctuation += character

                word_lst = no_punctuation.split()
                for word in word_lst: # goes through all the words in the list
                    word = word.lower()
                    if not self.is_num(word): # checks if the word is a number 
                        if not self.stop_table.in_table(word):
                            word_hash.insert(word, line_num)
                line_num += 1
            self.concordance_table = word_hash
            load_file.close()            
        except FileNotFoundError:
            raise FileNotFoundError

    # string -> boolean
    # tells if the string is a number or not
    def is_num(self,num_string):
        try:
            float(num_string)
            return True
        except ValueError:
            return False

    # string -> none
    # writes the key - value in the output file
    def write_concordance(self, filename):
        wf = open(filename,'w') # opens the file
        key_lst = self.concordance_table.get_all_keys()  
        key_lst.sort() # sorts the list alaphabetically
        num_words = len(key_lst)
        num_words_done = 0
        for word in key_lst:
            file_string = word + ': '
            line_lst = self.concordance_table.get_value(word)
            num_lines = len(line_lst)
            lines_done = 0
            for num in line_lst:
                if lines_done == num_lines - 1:
                    file_string += str(num)
                else:    
                    file_string += str(num) + ' '
                lines_done += 1
            if num_words_done == num_words - 1:
                wf.write(file_string)
            else:
                wf.write(file_string + "\n")
            num_words_done += 1
        wf.close()