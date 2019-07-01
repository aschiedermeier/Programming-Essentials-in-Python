# 4.1.6.5 Tuples and dictionaries

# English-French word dictionary
dict = {"cat" : "chat", "dog" : "chien", "a_horse" : "cheval"}
words = ['cat', 'lion', 'horse']

# print out only if word in dictionary
for word in words:
    if word in dict:
        print(word, "->", dict[word])
    else:
        print(word, "is not in dictionary")

# keys () method
for key in dict.keys():
    print(key, "->", dict[key])
    
# sorted () method
# sorts alpahbetically by key names
for key in sorted(dict.keys()):
    print(key, "->", dict[key])
    
# item () method
for english, french in dict.items():
    print(english, "->", french)
    
# values() method
for french in dict.values():
    print(french)
    
# edit dictionary
# replace value of key 'cat'
dict['cat'] = 'minou'
print(dict)

# add new key-value-pair
dict['swan'] = 'cygne'
print(dict)

# add new key-value-pair using update() method
dict.update({"duck" : "canard"})
print(dict)

# remove key-value-pair
del dict['dog']
print(dict)

# remove last key-value-pair
# before Python 3.6.7 removes random item from dictionary !
dict.popitem()
print(dict) 