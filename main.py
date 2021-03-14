# This program takes in a list or dictionary and print the items on a new line.


class Separator: # Class seperates values into each line.

    def __init__(self, collection):
        self.obj = collection  # Storing the collection in a variable
        self.collection_type = type(collection) # Storing the type of collection.
    

    def list_separator(self):
        # Sepreates the list items into strings than prints them.
        #obj_len = len(self.obj)  # Storing the length of the obj.
        pos = range(len(self.obj)) # A ranged list from zero till the objects length.

        current_index, current_item = [], [] # twi Empty lists that will hold appended index and item.

        for item in self.obj:  # For each item in the collection print the item.
            current_item.append(item)

        for index in pos:
            current_index.append(index)
        
        zipped_collection = zip(current_index, current_item) # pairing seperate lists items by their position.
        
        
        for index, item in zipped_collection: 
            phrase = f"Item at index {current_index}, is: {current_item}"
            print(phrase)


        return  print(phrase)# Return a formatted stirng with values and positions.
    

    def dict_separator(self):
        pass


test_list = ["Apple", 75, "Dog", 3.12]
s = Separator(test_list)

s.list_separator()