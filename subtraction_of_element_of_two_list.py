list1=[99,88,44,33,22,11]
list2=[5,4,3,2,1,7]
print(list1)
print(list2)
op_list=[]
for i in range(len(list1)):
    op_list.append(list1[i]-list2[i])
print("Result list:",op_list)
