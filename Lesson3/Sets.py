# my_set = {1, 2, 3}
# print(my_set)

# my_set = set([4, 5, 6])
# print(my_set)

# my_set = set()
# print(my_set)

# my_set = {1, 2, 3, 3, 4, 5, 6}
# print(my_set)
#
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
#
# union_result_method = set1.union(set2)
#
# union_result_operator = set1 | set2
#
# print("Union of set1 and set2 using union method:", union_result_method)
# print("Union of set1 and set2 using the | operator:", union_result_operator)
#
# intersection_result_method = set1.intersection(set2)
#
# intersection_result_operator = set1 & set2
#
# print("Intersection of set1 and set2 using intersection method", intersection_result_method)
# print("Intersection of set1 and set2 using the & operator", intersection_result_operator)
#
# difference_result_method = set1.difference(set2)
#
# difference_result_operator = set1 - set2
#
# print("difference of set1 and set2 using difference method", difference_result_method)
# print("difference of set1 and set2 using the - operator", difference_result_method)
#
# difference_result_method = set2.difference(set1)
#
# difference_result_operator = set2 - set1
#
# print("difference of set2 and set1 using difference method", difference_result_method)
# print("difference of set2 and set1 using the - operator", difference_result_operator)
#
# symmetric_difference_result_method = set1.symmetric_difference(set2)
# symmetric_difference_result_operator = set1 ^ set2
#
# print("symmetric difference of set1 and set2 using symmetric difference method", symmetric_difference_result_method)
# print("symmetric difference of set1 and set2 using the & operator", symmetric_difference_result_operator)

my_set = {1, 2, 3}

my_set.add(7)
my_set.remove(3)

my_set.discard(8)

length_set = len(my_set)

my_set.clear()


print(length_set)

my_list = [1, 2, 3, 3, 4, 4, 5, 6 ]

unique_set = set(my_list)

print(unique_set)

unique_list = list(unique_set)
print(unique_list)

user1_interests = {"music", "movies", "travel"}
user2_interests = {"movies", "reading", "cooking"}
common_interests = user1_interests.intersection(user2_interests)
print(common_interests)

colors = {"red", "green", "blue"}
color = "green"

print(color in colors)
print(color not in colors)