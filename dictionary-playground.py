# A python dictionary is an unordered collection of items.
# It contains data as a set of key: value pairs.
my_dictionary = {1: "L.A. Lakers", 2: "Houston Rockets"}

#_______________________________#
# Dictionary Key-Value Methods  #
#_______________________________#
ex_dict = {"a": "anteater", "b": "bumblebee", "c": "cheetah"}

ex_dict.keys()
# dict_keys(["a","b","c"])

ex_dict.values()
# dict_values(["anteater", "bumblebee", "cheetah"])

ex_dict.items()
# dict_items([("a","anteater"),("b","bumblebee"),("c","cheetah")])

# When trying to look at the information in a Python dictionary,
# there are multiple methods that return objects that contain the dictionary keys and values.

# .keys() returns the keys through a dict_keys object.
# .values() returns the values through a dict_values object.
# .items() returns both the keys and values through a dict_items object.


# Values in a dictionary can be accessed by placing the key within [] next to the dictionary.
# Values can be written by placing key within [] next to the dictionary and using the assignment operator (=).
# If the key already exists, the old value will be overwritten.
# Attempting to access a value with a key that does not exist will cause a KeyError.
my_dictionary = {"song": "Estranged", "artist": "Guns N' Roses"}
print(my_dictionary["song"])
my_dictionary["song"] = "Paradise City"

#____________________________#
#     The .pop() Method      #
#____________________________#
# Python dictionaries can remove key-value pairs with the .pop() method.
# The method takes a key as an argument and removes it from the dictionary.
# At the same time, it also returns the value that it removes from the dictionary.
famous_museums = {
    'Washington': 'Smithsonian Institution',
    'Paris': 'Le Louvre',
    'Athens': 'The Acropolis Museum'}
print(famous_museums)
famous_museums.pop('Athens')
print(famous_museums) # {'Washington': 'Smithsonian Institution', 'Paris': 'Le Louvre'}

#________________________________________________#
# Merging dictionaries with the .update() Method #
#________________________________________________#
##### Merging dictionaries with the .update() Method #####
# Given two dictionaries that need to be combined, Python makes this easy with the .update() function.
# For dict1.update(dict2), the key-value pairs of dict2 will be written into the dict1 dictionary.
# For keys in both dict1 and dict2, the value in dict1 will be overwritten by the corresponding value in dict2.
dict1 = {'color': 'blue', 'shape': 'circle'}
dict2 = {'color': 'red', 'number': 42}

dict1.update(dict2)
# dict1 is now {'color': 'red', 'shape': 'circle', 'number': 42}