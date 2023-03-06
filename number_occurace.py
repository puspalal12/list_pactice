num_list=[1,2,3,45,12,3,1,2,3,4,1,9,11,12]
print("Original Number List:",num_list)
num_set=set(num_list)
print("Number set is:",num_set)
for num in num_set:
    print("Number is:",num,"count is:",num_list.count(num))
