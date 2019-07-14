# 4.1.6.5 Tuples and dictionaries

# English-French word dictionary
dict = {"cat" : "chat", "dog" : "chien", "a_horse" : "cheval"}
words = ['cat', 'lion', 'horse']

# print out single entry
print(dict["cat"])
print()

# print out only if word in dictionary
for word in words:
    if word in dict:
        print(word, "->", dict[word])
    else:
        print(word, "is not in dictionary")

print()
# keys () method
for key in dict.keys():
    print(key, "-->", dict[key])

print()
# sorted () method
# sorts alpahbetically by key names
for key in sorted(dict.keys()):
    print(key, "--->", dict[key])

print()
# sorted () method
# difference output of print(sorted(dict)) and print (dict): sorted only shows the keys
print("unsorted:")
print (dict)
print("sorted:")
print(sorted(dict))
print("sorted keys:")
print(sorted(dict.keys()))
print("sorted items:")
print(sorted(dict.items()))
print("sorted values:")
print(sorted(dict.values()))

print()
# item () method
for english, french in dict.items():
    print(english, "---->", french)
    
print()
# values() method
for french in dict.values():
    print(french)
    
print()
# edit dictionary
# replace value of key 'cat'
dict['cat'] = 'minou'
print(dict)

print()
# add new key-value-pair
dict['swan'] = 'cygne'
print(dict)

print()
# add new key-value-pair using update() method
dict.update({"duck" : "canard"})
print(dict)

print()
# remove key-value-pair
del dict['dog']
print(dict)

print()
# remove last key-value-pair
# before Python 3.6.7 removes random item from dictionary !
dict.popitem()
print(dict) 