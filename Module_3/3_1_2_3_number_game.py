#######################################
# evil number magician game
# while loop
# triple quotes

secretNumber = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

guess = 0
while guess != secretNumber:
    print ("You are stuck! Buahahaha!!!")
    guess = int(input("Number please: "))
    

print("You are free now! Oh n"+"o"*100+"!")
