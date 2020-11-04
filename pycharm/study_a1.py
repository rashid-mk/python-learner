#set

s={'rsd','mrc'}
s.add('omr')
s.add('rsd')  #no duplicate
print(s)
for i in  range (3):
    print()


#to make list with no duplicate using set

list_of_num=[1,1,2,4,3,3,4,5,6,1]
no_duplicate_set=set(list_of_num)
print(no_duplicate_set)
no_duplicate_list=list(no_duplicate_set)
list_of_num=no_duplicate_list
print(list_of_num)
for i in range (3):
    print()

library_1={"rsd","mrc","amn"}
library_2={"mrc","jll","skr","rsd"}
combined_of_library=library_1.union(library_2)      # a union b
print(combined_of_library)
for i in range (3):
    print()

both_library=library_1.intersection(library_2)      # a intersection b
print(both_library)
for i in range (3):
    print()

in_library_1_only=library_1.difference(library_2)       # a - b
print(in_library_1_only)
