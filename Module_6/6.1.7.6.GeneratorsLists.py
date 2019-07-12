print('''
6.1.7.6 Generators and closures
More about list comprehensions
a simple and very impressive way of creating lists and their contents.
''')

listOne = []

for ex in range(6):
    listOne.append(10 ** ex)


listTwo = [10 ** ex for ex in range(6)]

print(listOne)
print(listTwo)

print('''
6.1.7.7 Generators and closures
More about list comprehensions
conditional expression - a way of selecting one of two different values based on the result of a Boolean expression.
expression_one if condition else expression_two
''')

lst = []

for x in range(10):
    lst.append(1 if x % 2 == 0 else 0)

print(lst)

print('''
6.1.7.8 Generators and closures
More about list comprehensions
Just one change can turn any comprehension into a generator.
It's the parentheses. The brackets make a comprehension, the parentheses make a generator.
''')

lst = [1 if x % 2 == 0 else 0 for x in range(10)]
genr = (1 if x % 2 == 0 else 0 for x in range(10))

for v in lst:
    print(v, end=" ")
print()

for v in genr:
    print(v, end=" ")
print()

print(len(lst)) # 10
# print(len(genr)) # TypeError: object of type 'generator' has no len()

# list: the list is created (and iterated through) as a whole - it actually exists when the loop is being executed.
for v in [1 if x % 2 == 0 else 0 for x in range(10)]:
    print(v, end=" ")
print()

# generator: there is no list at all - there are only subsequent values produced by the generator, one by one.
for v in (1 if x % 2 == 0 else 0 for x in range(10)):
    print(v, end=" ")
print()