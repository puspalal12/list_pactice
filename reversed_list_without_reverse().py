list1=[100,200,100,400,500,300]
print("original list",list1)
op_list=[]
len_list=len(list1)
for i in range(1,len_list+1):
    op_list.append(list1[len_list-i])
print("reversed list is:",op_list)
