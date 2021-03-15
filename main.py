# This program takes in a list or dictionary and print the items on a new line.


class Separator: # Class seperates values into each line.

    def __init__(self, collection):
        self.obj = collection  # Storing the collection in a variable
        self.collection_type = type(collection) # Storing the type of collection.
    

    def separator(self):
     # Sepreates the list items into strings than prints them.
        indexes = range(len(self.obj))
        
        if type(self.obj) == list:
            for index in indexes:
                item = self.obj[index]
                phrase = f"Item at index {index}. is {item}"
                print(phrase)

        elif type(self.obj) == dict: 
            pair = self.obj.items()
            pos = len(self.obj)
            for key, value in pair:
                
                phrase = f"position holds the key-value pair:\nKey: {key}\nValues: {value}"
                print(phrase)
            

test_list = ["Apple", 75, "Dog", 3.12]

test_dic = {"Cats": 99, "Grapes": 3.13}


s = Separator(test_dic)
s.separator()

## MAKE THIS CLASS WORK FOR DICTIONARIES