#Sets

my_set = {1, 2, 3, 4, 5}
print(my_set)
# Output: {1, 2, 3, 4, 5}

my_set.add(6)
print(my_set)   
# Output: {1, 2, 3, 4, 5, 6}

my_set.remove(3)
print(my_set)
# Output: {1, 2, 4, 5, 6}

#Union

set1 = {1, 2, 3}
set2 = {3, 4, 5}    
# The union() method returns a set that contains all items from both sets

set_union = set1.union(set2)
print(set_union)
# Output: {1, 2, 3, 4, 5}

#intersection

inter_set = set1.intersection(set2)
print(inter_set)
# Output: {3}

#Difference
diff_set = set1.difference(set2)
print(diff_set)
# Output: {1, 2}



