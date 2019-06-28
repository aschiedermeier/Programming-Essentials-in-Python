#######################################
# Pyramid wall out of blocks
# First level 1, then 2, then 3 etc. blocks
# enter blocks amount, return height of pyramid
# while blocks counts down the whole building process
# in every step one block is added to blocksfornextlayer
# newlayerneeded: how many do i need for next layer (increases with each layer)

blocks = int(input("Enter the number of blocks: "))


height = 0
blocksfornextlayer = 0
newlayerneeded = 1
while blocks:
    blocks -= 1
    blocksfornextlayer += 1
    # print ("Blocks left: ", blocks)
    # print ("Blocks for next layer: ", blocksfornextlayer)
    # print("Height: ", height)
    if blocksfornextlayer == newlayerneeded:
        height += 1
        blocksfornextlayer = 0
        newlayerneeded += 1
        


print("The height of the pyramid:", height)