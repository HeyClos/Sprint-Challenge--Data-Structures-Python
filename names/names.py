import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
'''for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)'''

# the values given are not numbers, but letters have numerical value to them
# so they'll be organized in order


# I need to set up my root node
tree = BSTNode(names_1[0])
# - Feed the rest of names_1 into a BST so we can search its values 
#   and use its "contains" method
# - If I want to use indeces, use range in my for loop
for i in range(len(names_1)):
    if i == 0:
        continue
    tree.insert(names_1[i])

# Im searching for name_2's elements in a BST containin names_1 elements
# - If we want i to hold the value of elements(str, in this case)
#   then we use this for loop
for i in names_2:
    if tree.contains(i) is True:
        duplicates.append(i)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.