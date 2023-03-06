num_list=list(range(0,111))
even_list=[]
odd_list=[]
for num in num_list:
    if num%2==0:
        even_list.append(num)
    else:
        odd_list.append(num)
    print(f"even number list is {even_list} and odd number list is {odd_list}")
