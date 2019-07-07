# 5.1.10.6 LAB: A LED Display
# LAB 
# Your task is to write a program which is able to simulate the work of a seven-display device,
# although you're going to use single LEDs instead of segments.


disp = {0:["***","* *","* *","* *","***"],
1:["  *","  *","  *","  *","  *"],
2:["***","  *","***","*  ","***"],
3:["***","  *","***","  *","***"],
4:["* *","* *","***","  *","  *"],
5:["***","*  ","***","  *","***"],
6:["***","*  ","***","* *","***"],
7:["***","  *","  *","  *","  *"],
8:["***","* *","***","* *","***"],
9:["***","* *","***","  *","  *"]}

# for j in range(10):
#     for i in range (len(disp[0])):
#         print (disp[j][i])
#     print ()

# for i in range (len(disp[0])): 
#     for j in range(10):
#         print (disp[j][i],end="")

digit = "0123456789"
digit = list (digit)
for l in range(5):
    for d in digit:
        print (disp[int(d)][l],end=" ")
    print()

