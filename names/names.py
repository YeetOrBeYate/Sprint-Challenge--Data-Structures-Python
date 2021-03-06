import time
from binary import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# # Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


first_list = BinarySearchTree('Yeet')

for name in names_1:
    first_list.insert(name)

for name2 in names_2:
    if first_list.contains(name2):
        duplicates.append(name2)



end_time = time.time()

def quick_test(node):
    print(node.value)
    if node.left:
        quick_test(node.left)
    if node.right:
        quick_test(node.right)
# so it appears that all 1000 are in my tree....
# quick_test(first_list)
    
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
