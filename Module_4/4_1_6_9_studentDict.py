# 4.1.6.9 Tuples and dictionaries

# you need a program to evaluate the students' average scores;
# the program should ask for the student's name, followed by her/his single score;
# the names may be entered in any order;
# entering an empty name finishes the inputting of the data;
# a list of all names, together with the evaluated average score, should be then emitted.

schoolClass = {}

while True:
    name = input("Enter the student's name (or type 'exit' to stop): ")
    if name == 'exit':
        break
    
    score = int(input("Enter the student's score (0-10): "))
    
    if name in schoolClass:
        schoolClass[name] += (score,)
    else:
        schoolClass[name] = (score,)
        
for name in sorted(schoolClass.keys()):
    sum = 0
    counter = 0
    for score in schoolClass[name]:
        sum += score
        counter += 1
    print(name, ":", sum / counter)